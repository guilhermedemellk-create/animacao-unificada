# -*- coding: utf-8 -*-
"""VARREDURA palavra-por-palavra (portão endurecido): faster-whisper com
timestamps por palavra; busca tokens de pontuação falada em TODO o áudio
(inclusive pausas). Uso: varredura.py <audio> [texto_esperado_opcional]
Imprime JSON com veredito."""
import sys, re, json, unicodedata
import librosa
from faster_whisper import WhisperModel

TOKENS = {'ponto', 'virgula', 'reticencias', 'exclamacao', 'interrogacao'}
NUM = {'10': 'dez', '1': 'um'}

def norm(t):
    t = unicodedata.normalize('NFKD', t.lower())
    t = ''.join(c for c in t if not unicodedata.combining(c))
    t = re.sub(r'[^a-z0-9 ]', ' ', t)
    t = ' '.join(NUM.get(w, w) for w in t.split())
    return re.sub(r'\s+', ' ', t).strip()

def varrer(path, esperado=None):
    modelo = WhisperModel('small', device='cpu', compute_type='int8', cpu_threads=4)
    y16, _ = librosa.load(path, sr=16000, mono=True)
    segs, _ = modelo.transcribe(y16, language='pt', word_timestamps=True,
                                vad_filter=False, beam_size=1,
                                condition_on_previous_text=False)
    palavras, partes = [], []
    for s in segs:
        partes.append(s.text)
        for w in (s.words or []):
            palavras.append({'w': w.word.strip(), 'ini': round(w.start, 2),
                             'fim': round(w.end, 2)})
    t_asr = ' '.join(partes).strip()
    achados = [{'token': p['w'], 'em_s': p['ini']} for p in palavras
               if norm(p['w']) in TOKENS]
    return {'arquivo': path, 'asr': t_asr, 'palavras': palavras,
            'tokens_pontuacao': achados, 'zerado': not achados,
            'texto_confere': (norm(t_asr) == norm(esperado)) if esperado else None}

if __name__ == '__main__':
    esp = None
    if len(sys.argv) > 2:
        esp = open(sys.argv[2], encoding='utf-8').read().strip()
    print(json.dumps(varrer(sys.argv[1], esp), ensure_ascii=False, indent=1))
