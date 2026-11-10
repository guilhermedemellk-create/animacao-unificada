# -*- coding: utf-8 -*-
"""
Avaliação das tentativas v2: ASR (whisper-small via transformers), F0 mediano
(librosa.pyin) e duração. Critérios, nesta ordem:
  1. ASR sem palavras de pontuação e transcrição igual ao pretendido
     (comparação normalizada: minúsculas, sem pontuação/hífen);
  2. F0 mais próximo do alvo (frases 1–2: 120 Hz; frase 3/pergunta: ~145 Hz);
  3. duração não maior que a v1 (4,41 / 5,42 / 9,18s).
Copia a melhor tentativa de cada frase para voice/teste_fraseN_v2.wav e grava
iter_fluidez/avaliacao.json com tudo.
Rodar com o venv_clone da v3.
"""
import os, re, sys, json, unicodedata
import numpy as np
import soundfile as sf

VOICE = os.path.expanduser('~/workspace/custom-skills/muse-dark-video-production/voice')
WORK = os.path.join(VOICE, 'iter_fluidez', 'tentativas')

PRETENDIDO = {
    1: "Naquela casa, ninguém atendia depois da meia-noite.",
    2: "Ele ouviu passos no corredor... mas não havia ninguém lá.",
    3: "Você também escutou esse barulho no escuro?",
}
ALVO_F0 = {1: 120.0, 2: 120.0, 3: 145.0}
DUR_V1 = {1: 4.41, 2: 5.42, 3: 9.18}
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
    from transformers import pipeline
    asr = pipeline('automatic-speech-recognition', model='openai/whisper-small',
                   language='pt', device='cpu')
    resultados = {}
    for n in (1, 2, 3):
        cands = []
        for tent in (1, 2, 3):
            p = os.path.join(WORK, f'frase{n}_tent{tent}.wav')
            if not os.path.exists(p):
                continue
            r = asr(p, generate_kwargs={'language': 'pt', 'task': 'transcribe'})
            texto = r['text'].strip()
            achadas = [w for w in PROIBIDAS
                       if re.search(r'\b' + re.escape(w) + r'\b', texto.lower())]
            exata = norm(texto) == norm(PRETENDIDO[n])
            f0 = f0_mediano(p)
            dur = duracao(p)
            cands.append({'tent': tent, 'arquivo': p, 'asr': texto,
                          'exata': exata, 'proibidas': achadas,
                          'f0': round(f0, 1), 'dur': round(dur, 2)})
            print(f'frase{n} tent{tent}: f0={f0:.1f} dur={dur:.2f} '
                  f'exata={exata} proibidas={achadas} :: {texto}', flush=True)

        def score(c):
            limpo = 0 if (c['exata'] and not c['proibidas']) else 1
            return (limpo, abs(c['f0'] - ALVO_F0[n]),
                    0 if c['dur'] <= DUR_V1[n] else 1, c['dur'])
        cands.sort(key=score)
        melhor = cands[0]
        resultados[n] = {'candidatos': cands, 'escolhido': melhor}
        if melhor['exata'] and not melhor['proibidas']:
            import shutil
            dest = os.path.join(VOICE, f'teste_frase{n}_v2.wav')
            shutil.copy(melhor['arquivo'], dest)
            print(f'-> frase{n}: escolhido tent{melhor["tent"]} -> {dest}', flush=True)
        else:
            print(f'-> frase{n}: NENHUMA tentativa limpa/exata — ajuste necessário', flush=True)
    with open(os.path.join(VOICE, 'iter_fluidez', 'avaliacao.json'), 'w', encoding='utf-8') as f:
        json.dump(resultados, f, indent=1, ensure_ascii=False)
    print('AVALIACAO_DONE', flush=True)


if __name__ == '__main__':
    main()
