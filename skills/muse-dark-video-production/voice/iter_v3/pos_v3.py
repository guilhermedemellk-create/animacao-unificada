# -*- coding: utf-8 -*-
"""
ETAPA 3b (v3) — Pós-processamento e versão final das frases v3.
Seleção equilibrada a partir de avaliacao_v3.json (ver decisão no cabeçalho
do relatório): portão ASR -> faixa de ritmo sã (3,5–6,0 síl/s; original
4,75–5,20) -> maior embedding -> F0.
  frase1: candidatos/frase1_c3.wav (emb 0,7604, 4,84 síl/s, F0 109,7)
  frase2: candidatos/frase2_c5.wav (emb 0,7795, 3,66 síl/s, F0 121,4)
          + micro-atempo 1.20 (ritmo -> ~4,4 síl/s, sem mudar pitch)
  frase3: NENHUM candidato na faixa de ritmo bateu a v2 (0,7880) ->
          v2 permanece; teste_frase3_v3.wav (cópia bruta) é removido.
Pós espectral condicional: se centroide do final > 1600 Hz (original:
1263 Hz), lowpass suave 6500 Hz e re-medição; mantém só se o embedding
não cair mais de 0,005. Re-mede TUDO nos arquivos finais (ASR, embedding,
F0, duração, síl/s, centroide) e salva pos_v3.json.
Rodar com venv_clone.
"""
import os, re, json, shutil, subprocess, unicodedata
import numpy as np
import soundfile as sf

VOICE = os.path.expanduser('~/workspace/custom-skills/muse-dark-video-production/voice')
WORK = os.path.join(VOICE, 'iter_v3')
FIN = os.path.join(WORK, 'finais')
os.makedirs(FIN, exist_ok=True)

PRETENDIDO = {
    1: "Naquela casa, ninguém atendia depois da meia-noite.",
    2: "Ele ouviu passos no corredor... mas não havia ninguém lá.",
    3: "Você também escutou esse barulho no escuro?",
}
PROIBIDAS = ['ponto', 'vírgula', 'virgula', 'interrogação', 'interrogacao',
             'exclamação', 'exclamacao', 'reticências', 'reticencias',
             'dois pontos', 'ponto e vírgula']
FONTES = {1: ('candidatos/frase1_c3.wav', None),
          2: ('candidatos/frase2_c5.wav', 1.20)}


def norm(t):
    t = unicodedata.normalize('NFKD', t.lower())
    t = ''.join(c for c in t if not unicodedata.combining(c))
    t = re.sub(r'[^a-z0-9 ]', ' ', t)
    return re.sub(r'\s+', ' ', t).strip()


def contar_silabas(texto):
    t = ''.join(c for c in unicodedata.normalize('NFD', texto.lower())
                if unicodedata.category(c) != 'Mn')
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


def ffmpeg_af(src, dst, af):
    subprocess.run(['ffmpeg', '-y', '-v', 'error', '-i', src, '-af', af,
                    '-ar', '24000', dst], check=True)


def metricas(path):
    import librosa
    y, sr = librosa.load(path, sr=24000, mono=True)
    f0, voiced, _ = librosa.pyin(y, fmin=60, fmax=400, sr=sr)
    vals = f0[voiced & ~np.isnan(f0)] if f0 is not None else np.array([])
    cent = librosa.feature.spectral_centroid(y=y, sr=sr)[0]
    info = sf.info(path)
    return {'f0': round(float(np.median(vals)), 1) if len(vals) else None,
            'centroide': round(float(np.median(cent)), 0),
            'dur': round(info.frames / info.samplerate, 2)}


def main():
    from resemblyzer import VoiceEncoder, preprocess_wav
    import glob
    enc = VoiceEncoder(verbose=False)
    embs = [enc.embed_utterance(preprocess_wav(p))
            for p in sorted(glob.glob(os.path.join(VOICE, 'trechos_limpos', '*.wav')))]
    ref = np.mean(embs, axis=0); ref = ref / np.linalg.norm(ref)

    def emb_cos(path):
        e = enc.embed_utterance(preprocess_wav(path))
        return round(float(np.dot(e / np.linalg.norm(e), ref)), 4)

    from transformers import pipeline
    asr = pipeline('automatic-speech-recognition', model='openai/whisper-small',
                   language='pt', device='cpu')

    resultado = {}
    for n, (src_rel, atempo) in FONTES.items():
        src = os.path.join(WORK, src_rel)
        bruto = os.path.join(FIN, f'frase{n}_final_bruto.wav')
        shutil.copy(src, bruto)
        atual = bruto
        cadeia = []
        if atempo:
            tmp = os.path.join(FIN, f'frase{n}_atempo.wav')
            ffmpeg_af(atual, tmp, f'atempo={atempo}')
            atual = tmp; cadeia.append(f'atempo={atempo}')
        m = metricas(atual)
        emb_antes = emb_cos(atual)
        if m['centroide'] and m['centroide'] > 1600:
            tmp = os.path.join(FIN, f'frase{n}_lp.wav')
            ffmpeg_af(atual, tmp, 'lowpass=f=6500')
            emb_lp = emb_cos(tmp)
            m_lp = metricas(tmp)
            if emb_lp >= emb_antes - 0.005:
                atual = tmp; cadeia.append('lowpass=f=6500')
                m, emb_antes = m_lp, emb_lp
            else:
                os.remove(tmp)
        final = os.path.join(VOICE, f'teste_frase{n}_v3.wav')
        shutil.copy(atual, final)
        r = asr(final, generate_kwargs={'language': 'pt', 'task': 'transcribe'})
        texto = r['text'].strip()
        achadas = [w for w in PROIBIDAS
                   if re.search(r'\b' + re.escape(w) + r'\b', texto.lower())]
        m = metricas(final)
        resultado[n] = {'fonte': src_rel, 'cadeia_pos': cadeia,
                        'arquivo_final': final, 'asr': texto,
                        'portao': bool(norm(texto) == norm(PRETENDIDO[n]) and not achadas),
                        'proibidas': achadas, 'embedding_cos': emb_cos(final),
                        'f0': m['f0'], 'dur': m['dur'], 'centroide': m['centroide'],
                        'sil_por_s': round(contar_silabas(PRETENDIDO[n]) / m['dur'], 2)}
        print(f"frase{n} final: {resultado[n]}", flush=True)
    # frase 3: v2 permanece -> remove cópia bruta do ranking puro
    f3 = os.path.join(VOICE, 'teste_frase3_v3.wav')
    if os.path.exists(f3):
        os.remove(f3)
        resultado[3] = {'decisao': 'v2 permanece (nenhum candidato na faixa de '
                                   'ritmo superou emb 0,7880 da v2)',
                        'arquivo_removido': f3}
        print('frase3: teste_frase3_v3.wav removido; v2 vigente', flush=True)
    with open(os.path.join(WORK, 'pos_v3.json'), 'w', encoding='utf-8') as f:
        json.dump(resultado, f, indent=1, ensure_ascii=False)
    print('POS_V3_DONE', flush=True)


if __name__ == '__main__':
    main()
