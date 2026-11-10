# -*- coding: utf-8 -*-
"""
Avaliação dos candidatos gerados na GPU do PC (lote suplementar v3).
Mesma régua de avaliar_v3.py: portão ASR (whisper-small) -> faixa de ritmo
sã (3,5–6,0 síl/s) -> embedding resemblyzer vs. média dos 12 trechos
originais -> F0. Baselines: frase2 final atual (c5, emb 0,7795);
frase3 vigente = v2 (emb 0,7880). Salva avaliacao_gpu.json.
Rodar com venv_clone.
"""
import os, re, json, glob, unicodedata
import numpy as np
import soundfile as sf

VOICE = os.path.expanduser('~/workspace/custom-skills/muse-dark-video-production/voice')
WORK = os.path.join(VOICE, 'iter_v3')
GPU = os.path.join(WORK, 'candidatos_gpu')
PRETENDIDO = {2: "Ele ouviu passos no corredor... mas não havia ninguém lá.",
              3: "Você também escutou esse barulho no escuro?"}
ALVO_F0 = {2: 120.0, 3: 145.0}
BASELINE = {2: {'rotulo': 'final_v3_c5', 'embedding_cos': 0.7795},
            3: {'rotulo': 'v2_vigente', 'embedding_cos': 0.7880}}
PROIBIDAS = ['ponto', 'vírgula', 'virgula', 'interrogação', 'interrogacao',
             'exclamação', 'exclamacao', 'reticências', 'reticencias',
             'dois pontos', 'ponto e vírgula']


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
    return float(np.median(vals)) if len(vals) else float('nan')


def main():
    from resemblyzer import VoiceEncoder, preprocess_wav
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
    for n in (2, 3):
        itens = []
        for path in sorted(glob.glob(os.path.join(GPU, f'frase{n}_g*.wav'))):
            r = asr(path, generate_kwargs={'language': 'pt', 'task': 'transcribe'})
            texto = r['text'].strip()
            achadas = [w for w in PROIBIDAS
                       if re.search(r'\b' + re.escape(w) + r'\b', texto.lower())]
            info = sf.info(path)
            dur = info.frames / info.samplerate
            item = {'rotulo': os.path.basename(path).replace('.wav', ''),
                    'arquivo': path, 'asr': texto,
                    'portao': bool(norm(texto) == norm(PRETENDIDO[n]) and not achadas),
                    'proibidas': achadas, 'embedding_cos': emb_cos(path),
                    'f0': round(f0_mediano(path), 1), 'dur': round(dur, 2),
                    'sil_por_s': round(contar_silabas(PRETENDIDO[n]) / dur, 2)}
            itens.append(item)
            print(f"frase{n} {item['rotulo']}: portao={item['portao']} "
                  f"emb={item['embedding_cos']} f0={item['f0']} "
                  f"sil/s={item['sil_por_s']} :: {texto}", flush=True)
        validos = [i for i in itens if i['portao'] and 3.5 <= i['sil_por_s'] <= 6.0]
        validos.sort(key=lambda i: (-i['embedding_cos'], abs(i['f0'] - ALVO_F0[n])))
        melhor = validos[0] if validos else None
        promove = bool(melhor and melhor['embedding_cos'] > BASELINE[n]['embedding_cos'])
        resultado[n] = {'itens': itens, 'baseline': BASELINE[n],
                        'melhor_gpu': melhor, 'promove': promove}
        print(f"-> frase{n}: melhor GPU = "
              f"{melhor['rotulo'] if melhor else None} "
              f"(baseline {BASELINE[n]['rotulo']} {BASELINE[n]['embedding_cos']}) "
              f"promove={promove}", flush=True)
    with open(os.path.join(WORK, 'avaliacao_gpu.json'), 'w', encoding='utf-8') as f:
        json.dump(resultado, f, indent=1, ensure_ascii=False)
    print('AVALIACAO_GPU_DONE', flush=True)


if __name__ == '__main__':
    main()
