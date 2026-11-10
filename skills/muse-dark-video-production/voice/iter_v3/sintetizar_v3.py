# -*- coding: utf-8 -*-
"""
ETAPA 2 (v3) — Grade de candidatos do clone de voz da skill de terror.
Mesmas 3 frases da v1/v2. Segmentação SOMENTE entre frases (regra da v2:
vírgula dentro do segmento), fades coseno 40ms, pausas reticências 500ms /
ponto-interrogação 250ms, repetition_penalty 2.0, idioma pt.

Grade enxuta (8 candidatos/frase), variando:
  condicionamento: A = só referencia_condicionamento.wav (23,6s)
                   B = múltiplas referências (4 melhores trechos limpos)
  temperature: 0.65 / 0.75 / 0.85
  speed: 0.95 / 1.00 / 1.05
Saída: iter_v3/candidatos/fraseN_cK.wav + grade.json. NÃO sobrescreve v1/v2.
Rodar com venv_clone.
"""
import os, json, time, glob
import numpy as np
import soundfile as sf

os.environ.setdefault('COQUI_TOS_AGREED', '1')
os.environ.setdefault('HF_HUB_DISABLE_XET', '1')

VOICE = os.path.expanduser('~/workspace/custom-skills/muse-dark-video-production/voice')
REF = os.path.join(VOICE, 'referencia_condicionamento.wav')
WORK = os.path.join(VOICE, 'iter_v3', 'candidatos')
os.makedirs(WORK, exist_ok=True)
SR = 24000
FADE_MS = 40

FRASES = {
    1: [("Naquela casa, ninguém atendia depois da meia-noite.", 0)],
    2: [("Ele ouviu passos no corredor", 500),
        ("mas não havia ninguém lá.", 0)],
    3: [("Você também escutou esse barulho no escuro?", 0)],
}


def melhores_trechos(k=4):
    cands = []
    for p in glob.glob(os.path.join(VOICE, 'trechos_limpos', '*.wav')):
        info = sf.info(p)
        cands.append((info.frames / info.samplerate, p))
    cands.sort(reverse=True)
    return [p for _, p in cands[:k]]


MULTI = melhores_trechos(4)
COND = {'A': REF, 'B': MULTI}

GRADE = [
    # (cond, temperature, speed)
    ('A', 0.75, 1.00),
    ('A', 0.85, 1.00),
    ('A', 0.65, 1.00),
    ('B', 0.75, 1.00),
    ('B', 0.85, 1.00),
    ('B', 0.75, 0.95),
    ('B', 0.75, 1.05),
    ('A', 0.85, 1.05),
]


def trim_edges(y, top_db=35):
    import librosa
    yt, _ = librosa.effects.trim(y, top_db=top_db)
    return yt if len(yt) > 0 else y


def apply_fades(y, sr, fade_ms=FADE_MS):
    n = int(sr * fade_ms / 1000)
    if len(y) <= 2 * n:
        return y
    y = y.copy()
    ramp = 0.5 - 0.5 * np.cos(np.linspace(0, np.pi, n))
    y[:n] *= ramp
    y[-n:] *= ramp[::-1]
    return y


def montar(tts, segmentos, speaker_wav, temperature, speed, out_path):
    partes = []
    for texto, pausa_ms in segmentos:
        tmp = out_path + '.seg.wav'
        tts.tts_to_file(text=texto, speaker_wav=speaker_wav, language='pt',
                        file_path=tmp, speed=speed, temperature=temperature,
                        repetition_penalty=2.0)
        y, sr = sf.read(tmp, dtype='float32')
        if y.ndim > 1:
            y = y[:, 0]
        y = trim_edges(y)
        y = apply_fades(y, sr)
        partes.append(y)
        if pausa_ms:
            partes.append(np.zeros(int(sr * pausa_ms / 1000), dtype='float32'))
        os.remove(tmp)
    audio = np.concatenate(partes)
    sf.write(out_path, audio, SR)
    return len(audio) / SR


def main():
    from TTS.api import TTS
    t0 = time.time()
    tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2", gpu=False)
    print(f"modelo carregado em {time.time()-t0:.0f}s", flush=True)
    print('MULTI refs:', [os.path.basename(p) for p in MULTI], flush=True)
    grade_info = {}
    for n, segmentos in FRASES.items():
        for k, (cond, temp, speed) in enumerate(GRADE, start=1):
            out = os.path.join(WORK, f'frase{n}_c{k}.wav')
            key = os.path.basename(out)
            if os.path.exists(out):
                print('já existe, pulando:', key, flush=True)
                continue
            t1 = time.time()
            dur = montar(tts, segmentos, COND[cond], temp, speed, out)
            grade_info[key] = {'cond': cond, 'temperature': temp,
                               'speed': speed, 'dur': round(dur, 2),
                               'tempo_s': round(time.time() - t1, 1)}
            print(f"OK {key} dur={dur:.2f}s ({time.time()-t1:.0f}s)", flush=True)
            with open(os.path.join(WORK, 'grade.json'), 'w') as f:
                json.dump(grade_info, f, indent=1)
    print("SINTESE_V3_DONE", flush=True)


if __name__ == '__main__':
    main()
