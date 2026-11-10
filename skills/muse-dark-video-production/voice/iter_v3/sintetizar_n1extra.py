# -*- coding: utf-8 -*-
"""Candidatos extras da n1 (janela de 5s é a mais apertada do filme):
D = cond simples, temp 0.65, speed 1.10 · E = cond múltiplo, temp 0.85,
speed 1.10. Mesma segmentação da redublagem. Saída em saida_redub/."""
import os, sys, json, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('COQUI_TOS_AGREED', '1')
os.environ.setdefault('HF_HUB_DISABLE_XET', '1')
from sintetizar_redub import LINHAS, montar, OUT, BASE, REF, MULTI

CONFIGS = {'D': (REF, 0.65, 1.10), 'E': (MULTI, 0.85, 1.10)}

from TTS.api import TTS
t0 = time.time()
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to("cuda")
print(f"modelo GPU carregado em {time.time()-t0:.0f}s", flush=True)
info = {}
for cfg, (sw, tp, sp) in CONFIGS.items():
    out = os.path.join(OUT, f'n1_{cfg}.wav')
    t1 = time.time()
    dur, seg_durs = montar(tts, LINHAS['n1'], sw, tp, sp, out)
    info[f'n1_{cfg}'] = {'dur': round(dur, 3), 'segmentos': seg_durs,
                         'tempo_s': round(time.time() - t1, 1)}
    print(f"OK n1_{cfg} dur={dur:.2f}s ({time.time()-t1:.0f}s)", flush=True)
with open(os.path.join(BASE, 'redub_info_extra.json'), 'w') as f:
    json.dump(info, f, indent=1)
print("REDUB_EXTRA_DONE", flush=True)
