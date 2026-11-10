# -*- coding: utf-8 -*-
"""
Avaliação dos candidatos v4-seg da REDUBLAGEM — PORTÃO ENDURECIDO:
ASR faster-whisper com timestamps POR PALAVRA + busca explícita dos tokens
de pontuação (ponto, vírgula/virgula, dois-pontos, reticências/reticencias).
Depois: ritmo são (3,5–6,0 síl/s) -> embedding resemblyzer -> F0 (librosa).
Salva avaliacao_v4.json. Rodar com venv_clone.
"""
import os, re, json, glob, unicodedata
import numpy as np
import soundfile as sf

VOICE = os.path.expanduser('~/workspace/custom-skills/muse-dark-video-production/voice')
WORK = os.path.join(VOICE, 'iter_v3')
CAND = os.path.join(WORK, 'saida_v4_dl')

PRETENDIDO = {
 'n1': "Existe alguém aparecendo em todas as suas fotografias... mas essa pessoa nunca esteve lá.",
 'n2': "Ele percebeu isso por acaso, enquanto olhava uma foto tirada dez anos atrás.",
 'n3': "Ele procurou outras fotografias. E encontrou a mesma figura em todas elas. Sempre mais perto.",
 'n4': "Assustado, mostrou as imagens para um amigo. Mas o amigo ficou em silêncio.",
 'd4': "Você também está vendo isso?",
 'n5': "Então o amigo revelou algo impossível. Aquela figura não aparecia nas fotografias dele... aparecia apenas nas fotografias de quem estava prestes a desaparecer.",
 'n6': "O homem correu para olhar a última fotografia. Mas agora havia algo diferente.",
 'n7': "E quando levantou os olhos... viu a mesma figura parada bem na sua frente.",
}
JANELA = {'n1': 4.97, 'n2': 8.40, 'n3': 10.65, 'n4': 5.90, 'd4': 3.70,
          'n5': 12.55, 'n6': 10.60, 'n7': 5.55}
TOKENS = ['ponto', 'vírgula', 'virgula', 'reticências', 'reticencias',
          'dois-pontos', 'exclamação', 'exclamacao', 'interrogação',
          'interrogacao']

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

def f0_mediano(path):
    import librosa
    y, sr = librosa.load(path, sr=24000, mono=True)
    f0, voiced, _ = librosa.pyin(y, fmin=60, fmax=400, sr=sr)
    vals = f0[voiced & ~np.isnan(f0)] if f0 is not None else np.array([])
    return round(float(np.median(vals)), 1) if len(vals) else float('nan')

def main():
    from faster_whisper import WhisperModel
    modelo = WhisperModel('small', device='cpu', compute_type='int8')
    from resemblyzer import VoiceEncoder, preprocess_wav
    enc = VoiceEncoder(verbose=False)
    embs = [enc.embed_utterance(preprocess_wav(p))
            for p in sorted(glob.glob(os.path.join(VOICE, 'trechos_limpos', '*.wav')))]
    ref = np.mean(embs, axis=0); ref = ref / np.linalg.norm(ref)

    def emb_cos(path):
        e = enc.embed_utterance(preprocess_wav(path))
        return round(float(np.dot(e / np.linalg.norm(e), ref)), 4)

    import sys as _s
    so = _s.argv[1].split(',') if len(_s.argv) > 1 else list(PRETENDIDO)
    resultado = {}
    for linha, texto in PRETENDIDO.items():
        if linha not in so:
            continue
        itens = []
        for path in sorted(glob.glob(os.path.join(CAND, f'{linha}_*.wav'))):
            import librosa
            y16, _ = librosa.load(path, sr=16000, mono=True)
            segs, _info = modelo.transcribe(y16, language='pt',
                                            word_timestamps=True,
                                            vad_filter=False)
            palavras, texto_asr = [], []
            for s in segs:
                texto_asr.append(s.text)
                for w in (s.words or []):
                    palavras.append({'w': w.word.strip(),
                                     'ini': round(w.start, 2),
                                     'fim': round(w.end, 2)})
            t_asr = ' '.join(texto_asr).strip()
            toks_norm = [norm(p['w']) for p in palavras]
            achados = []
            for tok in TOKENS:
                tn = norm(tok)
                for p, wn in zip(palavras, toks_norm):
                    if wn == tn:
                        achados.append({'token': tok, 'em_s': p['ini']})
            info = sf.info(path)
            dur = info.frames / info.samplerate
            sil = contar_silabas(texto)
            item = {'rotulo': os.path.basename(path).replace('.wav', ''),
                    'arquivo': path, 'asr': t_asr, 'palavras': palavras,
                    'tokens_pontuacao': achados,
                    'portao_palavra': bool(not achados),
                    'portao_texto': bool(norm(t_asr) == norm(texto)),
                    'dur': round(dur, 3),
                    'sil_por_s': round(sil / dur, 2),
                    'atempo_necessario': round(max(1.0, dur / JANELA[linha]), 3),
                    'embedding_cos': emb_cos(path)}
            item['f0'] = f0_mediano(path) if (item['portao_palavra'] and item['portao_texto']) else None
            itens.append(item)
            print(f"{linha} {item['rotulo']}: palavra_ok={item['portao_palavra']} "
                  f"texto_ok={item['portao_texto']} emb={item['embedding_cos']} "
                  f"f0={item['f0']} dur={item['dur']} sil/s={item['sil_por_s']} "
                  f"atempo={item['atempo_necessario']} achados={achados} :: {t_asr}",
                  flush=True)
        validos = [i for i in itens if i['portao_palavra'] and i['portao_texto']
                   and 3.5 <= i['sil_por_s'] <= 6.0]
        validos.sort(key=lambda i: (-i['embedding_cos'],
                                    abs((i['f0'] or 120) - 120.0)))
        escolhido = validos[0] if validos else None
        resultado[linha] = {'itens': itens, 'janela_util': JANELA[linha],
                            'escolhido': escolhido}
        print(f"-> {linha}: escolhido = {escolhido['rotulo'] if escolhido else None}",
              flush=True)
    with open(os.path.join(WORK, 'avaliacao_v4_' + '_'.join(so) + '.json'), 'w', encoding='utf-8') as f:
        json.dump(resultado, f, indent=1, ensure_ascii=False)
    print('AVALIACAO_V4_DONE', flush=True)

if __name__ == '__main__':
    main()
