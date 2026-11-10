# -*- coding: utf-8 -*-
"""ETAPA 1A — ASR dos 12 trechos limpos -> transcricoes.json (processo leve)."""
import os, json, glob, gc
VOICE = os.path.expanduser('~/workspace/custom-skills/muse-dark-video-production/voice')
WORK = os.path.join(VOICE, 'iter_v3')

from transformers import pipeline
asr = pipeline('automatic-speech-recognition', model='openai/whisper-small',
               language='pt', device='cpu')
out = {}
for p in sorted(glob.glob(os.path.join(VOICE, 'trechos_limpos', '*.wav'))):
    r = asr(p, generate_kwargs={'language': 'pt', 'task': 'transcribe'})
    out[os.path.basename(p)] = r['text'].strip()
    print('ASR', os.path.basename(p), '::', out[os.path.basename(p)], flush=True)
    del r
    gc.collect()
with open(os.path.join(WORK, 'transcricoes.json'), 'w', encoding='utf-8') as f:
    json.dump(out, f, indent=1, ensure_ascii=False)
print('ASR_DONE', flush=True)
