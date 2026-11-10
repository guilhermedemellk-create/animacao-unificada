# -*- coding: utf-8 -*-
"""
Vídeo de teste da voz v2 (skill de terror) — 2026-11-07.
3 trechos (um por frase v2), cada um = duração real do áudio + ~0,4s de respiro:
  seg1: áudio 4,40s -> 4,80s (144 quadros)   voz em t=0
  seg2: áudio 4,17s -> 4,57s (137 quadros)   voz em t=4,800s
  seg3: áudio 3,00s -> 3,40s (102 quadros)   voz em t=9,367s
Total: 383 quadros = 12,767s @30fps. 1080x1920, H.264 + AAC 48kHz.
Visuais: 3 imagens geradas (casa/corredor/escuridão) + zoompan lento.
Edição: drone de suspense baixo, glitch sonoro+visual só nas viradas e no fim,
legenda queimada exata + texto grande por frase (drawtext com textfile).
"""
import os, subprocess, sys

BASE = os.path.dirname(os.path.abspath(__file__))
VOICE = os.path.dirname(BASE)
OUT = os.path.join(VOICE, 'teste_video_voz_v2.mp4')
FONT = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
IMG = {
    1: os.path.join(BASE, 'media-generation-cena1-casa-0-73ea53c0-fbbf-43ec-9bad-1cc9a7cbc121.webp'),
    2: os.path.join(BASE, 'media-generation-cena2-corredor-0-ee4a7730-6c51-4567-8e8d-51095c3fe599.webp'),
    3: os.path.join(BASE, 'media-generation-cena3-escuridao-0-3b1c6d55-811e-4202-a8f5-c7c4fdc6cb02.webp'),
}
FRAMES = {1: 144, 2: 137, 3: 102}          # 4,80s / 4,567s / 3,40s
T_START = {1: '0', 2: '4.80', 3: '9.3667'}
T_END = {1: '4.80', 2: '9.3667', 3: '12.7667'}


def run(cmd, **kw):
    print('+', ' '.join(cmd[:3]), '...', flush=True)
    r = subprocess.run(cmd, capture_output=True, text=True, **kw)
    if r.returncode != 0:
        print(r.stderr[-3000:]); sys.exit(1)
    return r


def prep(n):
    """Limpa a imagem para 1080x1920 (a cena1 perde a faixa cromática do rodapé)."""
    out = os.path.join(BASE, f'prep{n}.png')
    if n == 1:
        vf = 'crop=1152:1960:0:0,scale=-2:1920,crop=1080:1920:24:0'
    else:
        vf = 'scale=1080:1920'
    run(['ffmpeg', '-y', '-v', 'error', '-i', IMG[n], '-vf', vf, out])
    return out


def segment(n, img):
    out = os.path.join(BASE, f'seg{n}.mp4')
    f = FRAMES[n]
    vf = (f"scale=2160:3840,zoompan=z='1+0.10*on/{f}':d={f}:"
          f"x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1080x1920:fps=30,"
          f"format=yuv420p")
    run(['ffmpeg', '-y', '-v', 'error', '-loop', '1', '-i', img,
         '-vf', vf, '-frames:v', str(f), '-c:v', 'libx264', '-preset', 'veryfast',
         '-crf', '17', '-r', '30', out])
    return out


def dt(textfile, size, y, start, end, box=False):
    base = (f"drawtext=fontfile={FONT}:textfile='{os.path.join(BASE, 'textos', textfile)}'"
            f":fontsize={size}:fontcolor=white:borderw=4:bordercolor=black"
            f":x=(w-text_w)/2:y={y}:enable='between(t\\,{start}\\,{end})'")
    if box:
        base += ':box=1:boxcolor=black@0.55:boxborderw=14'
    return base


def main():
    segs = [segment(n, prep(n)) for n in (1, 2, 3)]
    lst = os.path.join(BASE, 'concat.txt')
    with open(lst, 'w') as f:
        for s in segs:
            f.write(f"file '{s}'\n")
    base_vid = os.path.join(BASE, 'base.mp4')
    run(['ffmpeg', '-y', '-v', 'error', '-f', 'concat', '-safe', '0', '-i', lst,
         '-c', 'copy', base_vid])

    vfilters = []
    # glitch visual só nas viradas (4,72-4,90 / 9,29-9,47) e no fim (12,35-12,767)
    for a, b in (('4.72', '4.90'), ('9.29', '9.47'), ('12.35', '12.7667')):
        vfilters.append(f"rgbashift=rh=10:bh=-10:enable='between(t\\,{a}\\,{b})'")
        vfilters.append(f"noise=alls=22:allf=t:enable='between(t\\,{a}\\,{b})'")
    B = 92   # texto grande
    S = 46   # legenda
    for n in (1, 2, 3):
        st, en = T_START[n], T_END[n]
        if n in (1, 2):
            vfilters.append(dt(f'big{n}a.txt', B, 250, st, en))
            vfilters.append(dt(f'big{n}b.txt', B, 368, st, en))
        else:
            vfilters.append(dt('big3.txt', B, 300, st, en))
        vfilters.append(dt(f'sub{n}a.txt', S, 'h-368', st, en, box=True))
        vfilters.append(dt(f'sub{n}b.txt', S, 'h-300', st, en, box=True))
    vfilters.append('fade=t=in:st=0:d=0.25')
    vfilters.append('fade=t=out:st=12.467:d=0.3')
    vchain = '[0:v]' + ','.join(vfilters) + '[vout]'

    achain = (
        '[1:a]aresample=48000,adelay=0|0[v1];'
        '[2:a]aresample=48000,adelay=4800|4800[v2];'
        '[3:a]aresample=48000,adelay=9367|9367[v3];'
        '[4:a]volume=0.055[dr1];[5:a]volume=0.028[dr2];'
        '[dr1][dr2]amix=inputs=2:normalize=0,lowpass=f=220,'
        'afade=t=in:st=0:d=0.4,afade=t=out:st=12.367:d=0.4[drone];'
        '[6:a]atrim=end=0.18,bandpass=f=1800:width_type=o:w=1.2,volume=0.10,'
        'adelay=4710|4710[g1];'
        '[6:a]atrim=end=0.18,bandpass=f=1800:width_type=o:w=1.2,volume=0.10,'
        'adelay=9277|9277[g2];'
        '[6:a]atrim=end=0.30,bandpass=f=1400:width_type=o:w=1.2,volume=0.12,'
        'adelay=12400|12400[g3];'
        '[v1][v2][v3][drone][g1][g2][g3]amix=inputs=7:normalize=0,'
        'volume=0.79,pan=stereo|c0=c0|c1=c0,aresample=48000[aout]'
    )
    fc = vchain + ';' + achain
    cmd = ['ffmpeg', '-y', '-v', 'error', '-i', base_vid,
           '-i', os.path.join(VOICE, 'teste_frase1_v2.wav'),
           '-i', os.path.join(VOICE, 'teste_frase2_v2.wav'),
           '-i', os.path.join(VOICE, 'teste_frase3_v2.wav'),
           '-f', 'lavfi', '-i', 'sine=frequency=55:duration=12.7667:sample_rate=48000',
           '-f', 'lavfi', '-i', 'sine=frequency=82.4:duration=12.7667:sample_rate=48000',
           '-f', 'lavfi', '-i', 'anoisesrc=color=white:duration=13:sample_rate=48000:amplitude=0.6',
           '-filter_complex', fc, '-map', '[vout]', '-map', '[aout]',
           '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '18', '-pix_fmt', 'yuv420p',
           '-r', '30', '-c:a', 'aac', '-b:a', '192k', '-ar', '48000',
           '-movflags', '+faststart', '-t', '12.7667', OUT]
    run(cmd)
    print('VIDEO_OK', OUT, flush=True)


if __name__ == '__main__':
    main()
