# -*- coding: utf-8 -*-
"""
ETAPA 4 (v3) — Vídeo de teste com as melhores frases por comparação objetiva:
  trecho 1: voice/teste_frase1_v3.wav (candidato c3 pós-seleção)
  trecho 2: voice/teste_frase2_v3.wav (candidato c5 + micro-atempo)
  trecho 3: voice/teste_frase3_v2.wav (v2 — nenhum candidato v3 a superou)
Reutiliza visuais/textos de voice/iter_video/ (prep1-3.png, textos/) e a mesma
receita de montagem da v2: segmento = áudio + ~0,4s de respiro, zoompan lento,
drone 55+82,4 Hz baixo, glitch só nas viradas/fim, legenda exata + texto
grande, ganho final 0,79. Saída: voice/teste_video_voz_v3.mp4
1080x1920, 30fps, H.264 + AAC 48kHz.
"""
import os, subprocess, sys
import soundfile as sf

VOICE = os.path.expanduser('~/workspace/custom-skills/muse-dark-video-production/voice')
BASE = os.path.join(VOICE, 'iter_video')
WORK = os.path.join(VOICE, 'iter_v3')
OUT = os.path.join(VOICE, 'teste_video_voz_v3.mp4')
FONT = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
AUDIOS = {1: os.path.join(VOICE, 'teste_frase1_v3.wav'),
          2: os.path.join(VOICE, 'teste_frase2_v3.wav'),
          3: os.path.join(VOICE, 'teste_frase3_v2.wav')}
RESP = 0.4


def run(cmd):
    print('+', ' '.join(cmd[:3]), '...', flush=True)
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        print(r.stderr[-3000:]); sys.exit(1)
    return r


def dur(path):
    i = sf.info(path)
    return i.frames / i.samplerate


def segment(n, frames):
    out = os.path.join(WORK, f'seg{n}_v3.mp4')
    vf = (f"scale=2160:3840,zoompan=z='1+0.10*on/{frames}':d={frames}:"
          f"x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1080x1920:fps=30,"
          f"format=yuv420p")
    run(['ffmpeg', '-y', '-v', 'error', '-loop', '1',
         '-i', os.path.join(BASE, f'prep{n}.png'),
         '-vf', vf, '-frames:v', str(frames), '-c:v', 'libx264',
         '-preset', 'veryfast', '-crf', '17', '-r', '30', out])
    return out


def dt(textfile, size, y, start, end, box=False):
    base = (f"drawtext=fontfile={FONT}:textfile='{os.path.join(BASE, 'textos', textfile)}'"
            f":fontsize={size}:fontcolor=white:borderw=4:bordercolor=black"
            f":x=(w-text_w)/2:y={y}:enable='between(t\\,{start:.4f}\\,{end:.4f})'")
    if box:
        base += ':box=1:boxcolor=black@0.55:boxborderw=14'
    return base


def main():
    durs = {n: dur(AUDIOS[n]) for n in (1, 2, 3)}
    frames, starts, ends = {}, {}, {}
    t = 0.0
    for n in (1, 2, 3):
        seg_dur = durs[n] + RESP
        frames[n] = int(round(seg_dur * 30))
        starts[n] = t
        t += frames[n] / 30.0
        ends[n] = t
    total = t
    print('durs:', durs, 'frames:', frames, 'total:', round(total, 4), flush=True)

    segs = [segment(n, frames[n]) for n in (1, 2, 3)]
    lst = os.path.join(WORK, 'concat_v3.txt')
    with open(lst, 'w') as f:
        for s in segs:
            f.write(f"file '{s}'\n")
    base_vid = os.path.join(WORK, 'base_v3.mp4')
    run(['ffmpeg', '-y', '-v', 'error', '-f', 'concat', '-safe', '0', '-i', lst,
         '-c', 'copy', base_vid])

    vfilters = []
    viradas = [ends[1], ends[2]]
    for v in viradas:
        vfilters.append(f"rgbashift=rh=10:bh=-10:enable='between(t\\,{v-0.08:.4f}\\,{v+0.10:.4f})'")
        vfilters.append(f"noise=alls=22:allf=t:enable='between(t\\,{v-0.08:.4f}\\,{v+0.10:.4f})'")
    vfilters.append(f"rgbashift=rh=10:bh=-10:enable='between(t\\,{total-0.42:.4f}\\,{total:.4f})'")
    vfilters.append(f"noise=alls=22:allf=t:enable='between(t\\,{total-0.42:.4f}\\,{total:.4f})'")
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

    ms = {n: int(round(starts[n] * 1000)) for n in (1, 2, 3)}
    g = [int(round((v - 0.09) * 1000)) for v in viradas]
    achain = (
        f'[1:a]aresample=48000,adelay={ms[1]}|{ms[1]}[v1];'
        f'[2:a]aresample=48000,adelay={ms[2]}|{ms[2]}[v2];'
        f'[3:a]aresample=48000,adelay={ms[3]}|{ms[3]}[v3];'
        '[4:a]volume=0.055[dr1];[5:a]volume=0.028[dr2];'
        '[dr1][dr2]amix=inputs=2:normalize=0,lowpass=f=220,'
        f'afade=t=in:st=0:d=0.4,afade=t=out:st={total-0.4:.4f}:d=0.4[drone];'
        f'[6:a]atrim=end=0.18,bandpass=f=1800:width_type=o:w=1.2,volume=0.10,'
        f'adelay={g[0]}|{g[0]}[g1];'
        f'[6:a]atrim=end=0.18,bandpass=f=1800:width_type=o:w=1.2,volume=0.10,'
        f'adelay={g[1]}|{g[1]}[g2];'
        f'[6:a]atrim=end=0.30,bandpass=f=1400:width_type=o:w=1.2,volume=0.12,'
        f'adelay={int(round((total-0.37)*1000))}|{int(round((total-0.37)*1000))}[g3];'
        '[v1][v2][v3][drone][g1][g2][g3]amix=inputs=7:normalize=0,'
        'volume=0.79,pan=stereo|c0=c0|c1=c0,aresample=48000[aout]'
    )
    fc = vchain + ';' + achain
    cmd = ['ffmpeg', '-y', '-v', 'error', '-i', base_vid,
           '-i', AUDIOS[1], '-i', AUDIOS[2], '-i', AUDIOS[3],
           '-f', 'lavfi', '-i', f'sine=frequency=55:duration={total:.4f}:sample_rate=48000',
           '-f', 'lavfi', '-i', f'sine=frequency=82.4:duration={total:.4f}:sample_rate=48000',
           '-f', 'lavfi', '-i', 'anoisesrc=color=white:duration=13:sample_rate=48000:amplitude=0.6',
           '-filter_complex', fc, '-map', '[vout]', '-map', '[aout]',
           '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '18',
           '-pix_fmt', 'yuv420p', '-r', '30', '-c:a', 'aac', '-b:a', '192k',
           '-ar', '48000', '-movflags', '+faststart', '-t', f'{total:.4f}', OUT]
    run(cmd)
    print('VIDEO_V3_OK', OUT, 'total', round(total, 4), flush=True)


if __name__ == '__main__':
    main()
