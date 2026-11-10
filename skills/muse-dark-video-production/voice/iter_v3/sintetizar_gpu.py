# -*- coding: utf-8 -*-
"""
Lote SUPLEMENTAR v3 na GPU do PC do usuário (RTX 5060) — 2026-11-07.
Mesma receita da v2/v3 (segmentação só entre frases, fades 40ms, pausas
reticências 500ms / ponto 250ms, repetition_penalty 2.0, idioma pt).
Amostras NOVAS (o XTTS é estocástico) das configurações mais promissoras
das frases 2 e 3, para tentar superar os vencedores do CPU.
Uso: python sintetizar_gpu.py g1,g2,...  (nomes dos jobs)
Saída: ./saida/<job>.wav + tempos no stdout.
"""
import os, sys, json, time
import numpy as np
import soundfile as sf

os.environ.setdefault('COQUI_TOS_AGREED', '1')
os.environ.setdefault('HF_HUB_DISABLE_XET', '1')

BASE = os.path.dirname(os.path.abspath(__file__))
REF = os.path.join(BASE, 'refs', 'referencia_condicionamento.wav')
MULTI = [os.path.join(BASE, 'refs', 'trechos', n) for n in
         ('trecho_10_60.0s.wav', 'trecho_12_81.4s.wav',
          'trecho_06_22.6s.wav', 'trecho_07_30.2s.wav')]
COND = {'A': REF, 'B': MULTI}
OUT = os.path.join(BASE, 'saida')
os.makedirs(OUT, exist_ok=True)
SR = 24000

FRASES = {
    2: [("Ele ouviu passos no corredor", 500),
        ("mas não havia ninguém lá.", 0)],
    3: [("Você também escutou esse barulho no escuro?", 0)],
}
# job: (frase, cond, temperature, speed)
JOBS = {
    'frase2_g1': (2, 'B', 0.85, 1.00),
    'frase2_g2': (2, 'B', 0.85, 1.00),
    'frase2_g3': (2, 'B', 0.75, 1.05),
    'frase3_g1': (3, 'A', 0.75, 1.00),
    'frase3_g2': (3, 'A', 0.85, 1.00),
    'frase3_g3': (3, 'B', 0.75, 1.05),
}


def trim_edges(y, top_db=35):
    import librosa
    yt, _ = librosa.effects.trim(y, top_db=top_db)
    return yt if len(yt) > 0 else y


def apply_fades(y, sr, fade_ms=40):
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
    nomes = sys.argv[1].split(',') if len(sys.argv) > 1 else list(JOBS)
    from TTS.api import TTS
    t0 = time.time()
    tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to("cuda")
    print(f"modelo GPU carregado em {time.time()-t0:.0f}s", flush=True)
    tempos = {}
    for nome in nomes:
        frase, cond, temp, speed = JOBS[nome]
        out = os.path.join(OUT, nome + '.wav')
        t1 = time.time()
        dur = montar(tts, FRASES[frase], COND[cond], temp, speed, out)
        tempos[nome] = {'dur_audio': round(dur, 2),
                        'tempo_sintese_s': round(time.time() - t1, 1)}
        print(f"OK {nome} dur={dur:.2f}s ({time.time()-t1:.0f}s)", flush=True)
    print(json.dumps(tempos), flush=True)
    print("SINTESE_GPU_DONE", flush=True)


if __name__ == '__main__':
    main()
