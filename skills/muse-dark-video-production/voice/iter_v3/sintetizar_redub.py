# -*- coding: utf-8 -*-
"""
REDUBLAGEM de 'O HOMEM QUE NÃO EXISTIA' com o clone v3 — síntese na GPU
do PC do usuário (RTX 5060). Textos EXATOS do projeto (só NARRACAO_FALADA).
Segmentação SÓ entre frases (regra v2/v3); vírgula dentro do segmento.
Duas configurações vencedoras da v3 + uma extra p/ n1 (risco de janela):
  A = cond simples (referência 23,6s), temp 0.65, speed 1.00 (vencedor frase1)
  B = cond múltiplo (4 trechos),      temp 0.85, speed 1.00 (vencedor frase2)
  C = cond múltiplo,                  temp 0.85, speed 1.05 (só n1)
Uso: python sintetizar_redub.py A|B   (B inclui o job C da n1)
Saída: ./saida_redub/<linha>_<cfg>.wav + redub_info_<cfg>.json com
durações total e por segmento (p/ sincronizar as legendas n5a/b/c).
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
OUT = os.path.join(BASE, 'saida_redub')
os.makedirs(OUT, exist_ok=True)
SR = 24000

LINHAS = {
 'n1': [("Existe alguém aparecendo em todas as suas fotografias", 500),
        ("mas essa pessoa nunca esteve lá.", 0)],
 'n2': [("Ele percebeu isso por acaso, enquanto olhava uma foto tirada dez anos atrás.", 0)],
 'n3': [("Ele procurou outras fotografias.", 250),
        ("E encontrou a mesma figura em todas elas.", 250),
        ("Sempre mais perto.", 0)],
 'n4': [("Assustado, mostrou as imagens para um amigo.", 250),
        ("Mas o amigo ficou em silêncio.", 0)],
 'd4': [("Você também está vendo isso?", 0)],
 'n5': [("Então o amigo revelou algo impossível.", 250),
        ("Aquela figura não aparecia nas fotografias dele", 500),
        ("aparecia apenas nas fotografias de quem estava prestes a desaparecer.", 0)],
 'n6': [("O homem correu para olhar a última fotografia.", 250),
        ("Mas agora havia algo diferente.", 0)],
 'n7': [("E quando levantou os olhos", 500),
        ("viu a mesma figura parada bem na sua frente.", 0)],
}
CONFIGS = {'A': (REF, 0.65, 1.00), 'B': (MULTI, 0.85, 1.00), 'C': (MULTI, 0.85, 1.05)}


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
    partes, durs = [], []
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
        durs.append(round(len(y) / sr, 3))
        if pausa_ms:
            partes.append(np.zeros(int(sr * pausa_ms / 1000), dtype='float32'))
            durs.append(round(pausa_ms / 1000, 3))
        os.remove(tmp)
    audio = np.concatenate(partes)
    sf.write(out_path, audio, SR)
    return len(audio) / SR, durs


def main():
    cfg = sys.argv[1]
    speaker_wav, temp, speed = CONFIGS[cfg]
    from TTS.api import TTS
    t0 = time.time()
    tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to("cuda")
    print(f"[{cfg}] modelo GPU carregado em {time.time()-t0:.0f}s", flush=True)
    info = {}
    jobs = [(linha, cfg) for linha in LINHAS]
    if cfg == 'B':
        jobs.append(('n1', 'C'))
    for linha, c in jobs:
        sw, tp, sp = CONFIGS[c]
        out = os.path.join(OUT, f'{linha}_{c}.wav')
        t1 = time.time()
        dur, seg_durs = montar(tts, LINHAS[linha], sw, tp, sp, out)
        info[f'{linha}_{c}'] = {'dur': round(dur, 3), 'segmentos': seg_durs,
                                'tempo_s': round(time.time() - t1, 1)}
        print(f"OK {linha}_{c} dur={dur:.2f}s ({time.time()-t1:.0f}s)", flush=True)
        with open(os.path.join(BASE, f'redub_info_{cfg}.json'), 'w') as f:
            json.dump(info, f, indent=1)
    print(f"REDUB_{cfg}_DONE", flush=True)


if __name__ == '__main__':
    main()
