# -*- coding: utf-8 -*-
"""
ETAPA 3 (v3) — Seleção objetiva dos candidatos.
Ordem dos critérios (mandato da tarefa):
  1. PORTÃO ASR (whisper-small): transcrição idêntica ao pretendido
     (normalizada) e ZERO palavras de pontuação — reprovou, descarta.
  2. SIMILARIDADE DE TIMBRE: embedding de locutor (resemblyzer GE2E),
     cosseno vs. embedding médio dos 12 trechos limpos originais.
  3. F0 mediano próximo do alvo por tipo de frase e ritmo (sílabas/s)
     próximo do original (analise.json).
Inclui as frases v2 atuais como LINHA DE BASE no mesmo ranking.
Salva iter_v3/avaliacao_v3.json e copia os vencedores (só os que passarem
no portão e vencerem a v2 no embedding, ou o melhor aprovado) para
voice/teste_fraseN_v3.wav. Rodar com venv_clone.
"""
import os, re, json, glob, shutil, unicodedata
import numpy as np
import soundfile as sf

VOICE = os.path.expanduser('~/workspace/custom-skills/muse-dark-video-production/voice')
WORK = os.path.join(VOICE, 'iter_v3')
CAND = os.path.join(WORK, 'candidatos')

PRETENDIDO = {
    1: "Naquela casa, ninguém atendia depois da meia-noite.",
    2: "Ele ouviu passos no corredor... mas não havia ninguém lá.",
    3: "Você também escutou esse barulho no escuro?",
}
def contar_silabas(texto):
    """Mesma heurística de analise_original.py (grupos vocálicos)."""
    t = unicodedata.normalize('NFD', texto.lower())
    t = ''.join(c for c in t if unicodedata.category(c) != 'Mn')
    total = 0
    for palavra in re.findall(r"[a-z]+", t):
        grupos, ant = 0, False
        for ch in palavra:
            v = ch in 'aeiou'
            if v and not ant:
                grupos += 1
            ant = v
        total += max(grupos, 1)
    return total


SIL_PRET = {n: contar_silabas(t) for n, t in PRETENDIDO.items()}
ALVO_F0 = {1: 120.0, 2: 120.0, 3: 145.0}
PROIBIDAS = ['ponto', 'vírgula', 'virgula', 'interrogação', 'interrogacao',
             'exclamação', 'exclamacao', 'reticências', 'reticencias',
             'dois pontos', 'ponto e vírgula']


def norm(t):
    t = unicodedata.normalize('NFKD', t.lower())
    t = ''.join(c for c in t if not unicodedata.combining(c))
    t = re.sub(r'[^a-z0-9 ]', ' ', t)
    return re.sub(r'\s+', ' ', t).strip()


def f0_mediano(path):
    import librosa
    y, sr = librosa.load(path, sr=24000, mono=True)
    f0, voiced, _ = librosa.pyin(y, fmin=60, fmax=400, sr=sr)
    vals = f0[voiced] if f0 is not None else np.array([])
    vals = vals[~np.isnan(vals)]
    return float(np.median(vals)) if len(vals) else float('nan')


def duracao(path):
    info = sf.info(path)
    return info.frames / info.samplerate


def main():
    # ritmo alvo do original
    sil_alvo = None
    aj = os.path.join(WORK, 'analise.json')
    if os.path.exists(aj):
        with open(aj, encoding='utf-8') as f:
            sil_alvo = json.load(f).get('sil_por_s_media')

    # ---------- embeddings de referência ----------
    from resemblyzer import VoiceEncoder, preprocess_wav
    enc = VoiceEncoder(verbose=False)
    embs = []
    for p in sorted(glob.glob(os.path.join(VOICE, 'trechos_limpos', '*.wav'))):
        embs.append(enc.embed_utterance(preprocess_wav(p)))
    ref_emb = np.mean(embs, axis=0)
    ref_emb = ref_emb / np.linalg.norm(ref_emb)
    # espalhamento interno do original (referência de "quão igual é igual")
    internos = [float(np.dot(e / np.linalg.norm(e), ref_emb)) for e in embs]
    print(f'ref: cosseno interno dos trechos originais: '
          f'media={np.mean(internos):.3f} min={np.min(internos):.3f}', flush=True)

    def embedding(path):
        e = enc.embed_utterance(preprocess_wav(path))
        return float(np.dot(e / np.linalg.norm(e), ref_emb))

    # ---------- ASR + métricas ----------
    from transformers import pipeline
    asr = pipeline('automatic-speech-recognition', model='openai/whisper-small',
                   language='pt', device='cpu')

    def avaliar(path, frase_n, rotulo, meta=None):
        r = asr(path, generate_kwargs={'language': 'pt', 'task': 'transcribe'})
        texto = r['text'].strip()
        achadas = [w for w in PROIBIDAS
                   if re.search(r'\b' + re.escape(w) + r'\b', texto.lower())]
        exata = norm(texto) == norm(PRETENDIDO[frase_n])
        f0 = f0_mediano(path)
        dur = duracao(path)
        emb = embedding(path)
        item = {'rotulo': rotulo, 'arquivo': path, 'asr': texto,
                'exata': exata, 'proibidas': achadas,
                'portao': bool(exata and not achadas),
                'embedding_cos': round(emb, 4),
                'f0': round(f0, 1), 'dur': round(dur, 2),
                'sil_por_s': round(SIL_PRET[frase_n] / dur, 2)}
        if meta:
            item.update(meta)
        print(f"frase{frase_n} {rotulo}: portao={item['portao']} emb={emb:.4f} "
              f"f0={f0:.1f} dur={dur:.2f} sil/s={item['sil_por_s']} :: {texto}",
              flush=True)
        return item

    with open(os.path.join(CAND, 'grade.json')) as f:
        grade = json.load(f)

    resultados = {'referencia': {'cos_interno_media': round(float(np.mean(internos)), 4),
                                 'cos_interno_min': round(float(np.min(internos)), 4),
                                 'sil_por_s_original': sil_alvo},
                  'frases': {}}
    for n in (1, 2, 3):
        itens = []
        # linha de base v2 (e v1 p/ contexto)
        itens.append(avaliar(os.path.join(VOICE, f'teste_frase{n}_v2.wav'), n, 'v2_atual'))
        itens.append(avaliar(os.path.join(VOICE, f'teste_frase{n}.wav'), n, 'v1'))
        for path in sorted(glob.glob(os.path.join(CAND, f'frase{n}_c*.wav'))):
            base = os.path.basename(path)
            itens.append(avaliar(path, n, base.replace('.wav', ''),
                                 grade.get(base)))
        aprovados = [i for i in itens if i['portao'] and i['rotulo'] != 'v1']
        # ranking: embedding desc; desempate: |F0-alvo| e ritmo
        aprovados.sort(key=lambda i: (-i['embedding_cos'],
                                      abs(i['f0'] - ALVO_F0[n]),
                                      abs(i['sil_por_s'] - (sil_alvo or i['sil_por_s']))))
        vencedor = aprovados[0] if aprovados else None
        base_v2 = next(i for i in itens if i['rotulo'] == 'v2_atual')
        resultados['frases'][n] = {'itens': itens,
                                   'vencedor': vencedor,
                                   'v2': base_v2}
        if vencedor and vencedor['rotulo'] != 'v2_atual':
            dest = os.path.join(VOICE, f'teste_frase{n}_v3.wav')
            shutil.copy(vencedor['arquivo'], dest)
            print(f"-> frase{n}: VENCEDOR {vencedor['rotulo']} "
                  f"(emb {vencedor['embedding_cos']} vs v2 {base_v2['embedding_cos']}) "
                  f"-> {dest}", flush=True)
        elif vencedor:
            print(f"-> frase{n}: v2 continua melhor (emb {base_v2['embedding_cos']}); "
                  f"nenhum arquivo v3 copiado", flush=True)
        else:
            print(f"-> frase{n}: NENHUM candidato passou no portão!", flush=True)
    with open(os.path.join(WORK, 'avaliacao_v3.json'), 'w', encoding='utf-8') as f:
        json.dump(resultados, f, indent=1, ensure_ascii=False)
    print('AVALIACAO_V3_DONE', flush=True)


if __name__ == '__main__':
    main()
