# -*- coding: utf-8 -*-
"""
Iteração de FLUIDEZ (v2) do clone de voz da skill de terror — 2026-11-07.

Feedback do usuário sobre a v1: "um pouco robótica e travada; a original é
mais fluida". Hipóteses atacadas:
  1. v1 cortava em TODA pontuação (vírgula incluída) → cada micro-segmento
     sintetizado do zero quebrava a prosódia. v2 segmenta SOMENTE entre
     frases (ponto/reticências/interrogação); a vírgula fica DENTRO do
     segmento e a frase é sintetizada inteira de uma vez.
  2. Junções secas com silêncios rígidos → v2 usa fade coseno de 40ms nas
     bordas dos segmentos + pausas menores (ponto/interrogação ~250ms,
     reticências ~500ms).
  3. Temperature 0.65 monótona → v2 usa 0.75.

Parâmetros fixos: XTTS v2, speed 1.00, repetition_penalty 2.0, idioma pt,
speaker_wav = voice/referencia_condicionamento.wav.
Gera até 3 tentativas por frase em iter_fluidez/tentativas/ para seleção
posterior por ASR + F0 + duração. NÃO sobrescreve os arquivos v1.
"""
import os, sys, json, time
import numpy as np
import soundfile as sf

os.environ.setdefault('COQUI_TOS_AGREED', '1')
os.environ.setdefault('HF_HUB_DISABLE_XET', '1')

VOICE = os.path.expanduser('~/workspace/custom-skills/muse-dark-video-production/voice')
REF = os.path.join(VOICE, 'referencia_condicionamento.wav')
WORK = os.path.join(VOICE, 'iter_fluidez', 'tentativas')
os.makedirs(WORK, exist_ok=True)
SR = 24000  # saída nativa do XTTS

FADE_MS = 40
PAUSE_MS = {'reticencias': 500, 'frase': 250}

# segmentos v2: (texto enviado ao motor, pausa_apos_ms)
FRASES = {
    1: [("Naquela casa, ninguém atendia depois da meia-noite.", 0)],
    2: [("Ele ouviu passos no corredor", PAUSE_MS['reticencias']),
        ("mas não havia ninguém lá.", 0)],
    3: [("Você também escutou esse barulho no escuro?", 0)],
}
TENTATIVAS = 3


def trim_edges(y, sr, top_db=35):
    """Remove silêncio das bordas (o XTTS devolve padding variável)."""
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


def montar(tts, segmentos, out_path):
    partes = []
    for texto, pausa_ms in segmentos:
        tmp = out_path + '.seg.wav'
        tts.tts_to_file(text=texto, speaker_wav=REF, language='pt',
                        file_path=tmp, speed=1.00, temperature=0.75,
                        repetition_penalty=2.0)
        y, sr = sf.read(tmp, dtype='float32')
        if y.ndim > 1:
            y = y[:, 0]
        y = trim_edges(y, sr)
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
    log = {}
    for n, segmentos in FRASES.items():
        for tent in range(1, TENTATIVAS + 1):
            out = os.path.join(WORK, f'frase{n}_tent{tent}.wav')
            if os.path.exists(out):
                print('já existe, pulando:', out, flush=True)
                continue
            t1 = time.time()
            dur = montar(tts, segmentos, out)
            log[os.path.basename(out)] = round(dur, 2)
            print(f"OK {out} dur={dur:.2f}s ({time.time()-t1:.0f}s)", flush=True)
    with open(os.path.join(WORK, 'sintese_log.json'), 'w') as f:
        json.dump(log, f, indent=1)
    print("SINTESE_V2_DONE", flush=True)


if __name__ == '__main__':
    main()
