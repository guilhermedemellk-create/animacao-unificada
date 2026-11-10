# -*- coding: utf-8 -*-
"""
Vídeo de teste v3 CORRIGIDO — voice/teste_video_voz_v3_corrigido.mp4

Causa do erro original: o usuário ouviu um "ponto" falado aos 7,88s da trilha
MONTADA do teste v3, embora as 3 frases soltas estivessem limpas (varredura
por palavra confirmou). A contaminação entrou na MONTAGEM/junção da narração.

Correção aplicada aqui:
- Narração remontada EXCLUSIVAMENTE dos 3 wavs validados palavra por palavra
  (teste_frase1_v3.wav, teste_frase2_v3.wav, teste_frase3_v2.wav), posicionados
  sobre um canvas de SILÊNCIO DIGITAL (zeros) — nenhum intermediário
  pré-juntado, nenhuma junção processada.
- Visuais idênticos ao v3 (mesmos segmentos seg1-3_v3.mp4 e textos).
- Drone/SFX seguem a receita do v3 (são ruído/sintetizados, não voz).
"""
import os, subprocess, sys
import numpy as np
import soundfile as sf

VOICE = os.path.expanduser('~/workspace/custom-skills/muse-dark-video-production/voice')
BASE = os.path.join(VOICE, 'iter_video')
WORK = os.path.join(VOICE, 'iter_v3')
OUT = os.path.join(VOICE, 'teste_video_voz_v3_corrigido.mp4')
FONT = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
AUDIOS = {1: os.path.join(VOICE, 'teste_frase1_v3.wav'),
          2: os.path.join(VOICE, 'teste_frase2_v3.wav'),
          3: os.path.join(VOICE, 'teste_frase3_v2.wav')}
RESP = 0.4
SR = 48000


def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        print(r.stderr[-3000:]); sys.exit(1)
    return r


def dur(path):
    i = sf.info(path)
    return i.frames / i.samplerate


def dt(textfile, size, y, start, end, box=False):
    base = (f"drawtext=fontfile={FONT}:textfile={os.path.join(BASE, 'textos', textfile)}:"
            f"fontsize={size}:fontcolor=white:borderw=4:bordercolor=black:"
            f"x=(w-text_w)/2:y={y}:enable='between(t,{start:.4f},{end:.4f})'")
    if box:
        base += ':box=1:boxcolor=black@0.55:boxborderw=14'
    return base


def main():
    durs = {n: dur(AUDIOS[n]) for n in (1, 2, 3)}
    frames, starts, ends = {}, {}, {}
    t = 0.0
    for n in (1, 2, 3):
        frames[n] = int(round((durs[n] + RESP) * 30))
        starts[n] = t
        t += frames[n] / 30.0
        ends[n] = t
    total = t
    print('durs:', durs, 'starts:', starts, 'total:', round(total, 4), flush=True)

    # --- narração: canvas de silêncio digital + wavs validados ---
    canvas = np.zeros(int(round(total * SR)) + SR, dtype=np.float32)
    for n in (1, 2, 3):
        tmp = os.path.join(WORK, f'frase{n}_48k.wav')
        run(['ffmpeg', '-y', '-v', 'error', '-i', AUDIOS[n], '-ar', '48000',
             '-ac', '1', tmp])
        y, _ = sf.read(tmp, always_2d=False)
        ini = int(round(starts[n] * SR))
        canvas[ini:ini + len(y)] += y.astype(np.float32)
    narr = os.path.join(WORK, 'narrativa_corrigida.wav')
    sf.write(narr, canvas[:int(round(total * SR))], SR, subtype='PCM_16')
    print('narração corrigida:', narr, flush=True)

    base_vid = os.path.join(WORK, 'base_v3.mp4')   # mesmos segmentos do v3
    if not os.path.exists(base_vid):
        lst = os.path.join(WORK, 'concat_v3.txt')
        with open(lst, 'w') as f:
            for n in (1, 2, 3):
                f.write(f"file '{os.path.join(WORK, f'seg{n}_v3.mp4')}'\n")
        run(['ffmpeg', '-y', '-v', 'error', '-f', 'concat', '-safe', '0',
             '-i', lst, '-c', 'copy', base_vid])

    vfilters = []
    viradas = [ends[1], ends[2]]
    for v in viradas:
        vfilters.append(f"rgbashift=rh=10:bh=-10:enable='between(t,{v-0.08:.4f},{v+0.10:.4f})'")
        vfilters.append(f"noise=alls=22:allf=t:enable='between(t,{v-0.08:.4f},{v+0.10:.4f})'")
    vfilters.append(f"rgbashift=rh=10:bh=-10:enable='between(t,{total-0.42:.4f},{total:.4f})'")
    vfilters.append(f"noise=alls=22:allf=t:enable='between(t,{total-0.42:.4f},{total:.4f})'")
    B, S = 92, 46
    for n in (1, 2, 3):
        st, en = starts[n], ends[n]
        if n in (1, 2):
            vfilters.append(dt(f'big{n}a.txt', B, 250, st, en))
            vfilters.append(dt(f'big{n}b.txt', B, 368, st, en))
        else:
            vfilters.append(dt('big3.txt', B, 300, st, en))
        vfilters.append(dt(f'sub{n}a.txt', S, 'h-368', st, en, box=True))
        vfilters.append(dt(f'sub{n}b.txt', S, 'h-300', st, en, box=True))
    vfilters.append('fade=t=in:st=0:d=0.25')
    vfilters.append(f'fade=t=out:st={total-0.3:.4f}:d=0.3')
    vchain = '[0:v]' + ','.join(vfilters) + '[vout]'

    g = [int(round((v - 0.09) * 1000)) for v in viradas]
    achain = (
        '[1:a]aresample=48000,volume=0.79[voz];'
        '[2:a]volume=0.055[dr1];[3:a]volume=0.028[dr2];'
        '[dr1][dr2]amix=inputs=2:normalize=0,lowpass=f=220,'
        f'afade=t=in:st=0:d=0.4,afade=t=out:st={total-0.4:.4f}:d=0.4[drone];'
        f'[4:a]atrim=end=0.18,bandpass=f=1800:width_type=o:w=1.2,volume=0.10,'
        f'adelay={g[0]}|{g[0]}[g1];'
        f'[4:a]atrim=end=0.18,bandpass=f=1800:width_type=o:w=1.2,volume=0.10,'
        f'adelay={g[1]}|{g[1]}[g2];'
        f'[4:a]atrim=end=0.30,bandpass=f=1400:width_type=o:w=1.2,volume=0.12,'
        f'adelay={int(round((total-0.37)*1000))}|{int(round((total-0.37)*1000))}[g3];'
        '[voz][drone][g1][g2][g3]amix=inputs=5:normalize=0,'
        'pan=stereo|c0=c0|c1=c0,aresample=48000[aout]'
    )
    fc = vchain + ';' + achain
    cmd = ['ffmpeg', '-y', '-v', 'error', '-i', base_vid, '-i', narr,
           '-f', 'lavfi', '-i', f'sine=frequency=55:duration={total:.4f}:sample_rate=48000',
           '-f', 'lavfi', '-i', f'sine=frequency=82.4:duration={total:.4f}:sample_rate=48000',
           '-f', 'lavfi', '-i', 'anoisesrc=color=white:duration=13:sample_rate=48000:amplitude=0.6',
           '-filter_complex', fc, '-map', '[vout]', '-map', '[aout]',
           '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '18',
           '-pix_fmt', 'yuv420p', '-r', '30', '-c:a', 'aac', '-b:a', '192k',
           '-ar', '48000', '-movflags', '+faststart', '-t', f'{total:.4f}', OUT]
    run(cmd)
    print('VIDEO_V3_CORRIGIDO_OK', OUT, 'total', round(total, 4), flush=True)


if __name__ == '__main__':
    main()
