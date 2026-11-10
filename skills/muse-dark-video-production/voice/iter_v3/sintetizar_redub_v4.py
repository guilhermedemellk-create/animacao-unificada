# -*- coding: utf-8 -*-
"""
REDUBLAGEM 'O HOMEM QUE NÃO EXISTIA' — síntese na GPU do PC (RTX 5060).
PORTÃO ENDURECIDO (pedido do usuário, 2026-11-07): prioridade absoluta =
ZERO pontuação falada. Método de segmentação = o PROVADO da v4
(producao_volta10s_v4/teste_voz/limpeza_texto.py): split em TODA fronteira
de pausa; segmento ao motor SEM vírgula/ponto/reticências ('?' mantido no
segmento, carrega a entonação); pausas viram silêncios controlados na
montagem — vírgula 150ms · ponto 350ms · reticências 700ms. Junções com
fade coseno de 40ms nas bordas (fluidez sem clique).
Condicionamento/parâmetros = vencedores da v3:
  A = cond simples (referência 23,6s), temp 0.65, speed 1.00
  B = cond múltiplo (4 trechos),      temp 0.85, speed 1.00
  A108/B108 = idem com speed 1.08 (só n1, risco de janela)
Uso: python sintetizar_redub_v4.py A|B|N1X|R2
Saída: ./saida_v4/<linha>_<cfg>.wav + redub_v4_info_<cfg>.json
"""
import os, sys, json, time, re
import numpy as np
import soundfile as sf

os.environ.setdefault('COQUI_TOS_AGREED', '1')
os.environ.setdefault('HF_HUB_DISABLE_XET', '1')

BASE = os.path.dirname(os.path.abspath(__file__))
REF = os.path.join(BASE, 'refs', 'referencia_condicionamento.wav')
MULTI = [os.path.join(BASE, 'refs', 'trechos', n) for n in
         ('trecho_10_60.0s.wav', 'trecho_12_81.4s.wav',
          'trecho_06_22.6s.wav', 'trecho_07_30.2s.wav')]
OUT = os.path.join(BASE, 'saida_v4')
os.makedirs(OUT, exist_ok=True)
SR = 24000

SIL_CURTO, SIL_LONGO, SIL_DRAM = 150, 350, 700

def limpar(t):
    t = t.replace('—', ', ').replace('–', ', ')
    t = re.sub(r'["“”\'‘’«»`]', '', t)
    t = t.replace('…', '...')
    t = re.sub(r'\s+', ' ', t).strip()
    return t

def segmentar(texto):
    """Idêntico ao segmentar() da v4: retorna [(segmento, silencio_apos_ms)]."""
    t = limpar(texto)
    partes = re.split(r'(\.\.\.|[.,;:!?])', t)
    segmentos, atual = [], ''
    for pedaco in partes:
        if pedaco == '...':
            if atual.strip():
                segmentos.append((atual.strip(), SIL_DRAM))
            atual = ''
        elif pedaco in '.,;:':
            if atual.strip():
                sil = SIL_LONGO if pedaco == '.' else SIL_CURTO
                segmentos.append((atual.strip(), sil))
            atual = ''
        elif pedaco in '!?':
            atual += pedaco
            segmentos.append((atual.strip(), SIL_LONGO))
            atual = ''
        else:
            atual += pedaco
    if atual.strip():
        segmentos.append((atual.strip(), 0))
    return segmentos

LINHAS = {
 'n1': "Existe alguém aparecendo em todas as suas fotografias... mas essa pessoa nunca esteve lá.",
 'n2': "Ele percebeu isso por acaso, enquanto olhava uma foto tirada dez anos atrás.",
 'n3': "Ele procurou outras fotografias. E encontrou a mesma figura em todas elas. Sempre mais perto.",
 'n4': "Assustado, mostrou as imagens para um amigo. Mas o amigo ficou em silêncio.",
 'd4': "Você também está vendo isso?",
 'n5': "Então o amigo revelou algo impossível. Aquela figura não aparecia nas fotografias dele... aparecia apenas nas fotografias de quem estava prestes a desaparecer.",
 'n6': "O homem correu para olhar a última fotografia. Mas agora havia algo diferente.",
 'n7': "E quando levantou os olhos... viu a mesma figura parada bem na sua frente.",
}
CONFIGS = {'A': (REF, 0.65, 1.00), 'B': (MULTI, 0.85, 1.00),
           'A108': (REF, 0.65, 1.08), 'B108': (MULTI, 0.85, 1.08),
           'A090': (REF, 0.65, 0.90), 'B090': (MULTI, 0.85, 0.90),
           'A095': (REF, 0.65, 0.95), 'B112': (MULTI, 0.85, 1.12)}

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

def montar(tts, texto, speaker_wav, temperature, speed, out_path):
    segs = segmentar(texto)
    partes, durs = [], []
    for i, (seg, sil_ms) in enumerate(segs):
        tmp = out_path + '.seg.wav'
        tts.tts_to_file(text=seg, speaker_wav=speaker_wav, language='pt',
                        file_path=tmp, speed=speed, temperature=temperature,
                        repetition_penalty=2.0)
        y, sr = sf.read(tmp, dtype='float32')
        if y.ndim > 1:
            y = y[:, 0]
        y = trim_edges(y)
        y = apply_fades(y, sr)
        partes.append(y)
        durs.append(round(len(y) / sr, 3))
        if i < len(segs) - 1 and sil_ms:
            partes.append(np.zeros(int(sr * sil_ms / 1000), dtype='float32'))
            durs.append(sil_ms / 1000.0)
        os.remove(tmp)
    audio = np.concatenate(partes)
    sf.write(out_path, audio, SR)
    return round(len(audio) / SR, 3), durs, [s for s, _ in segs]

def main():
    cfg = sys.argv[1]
    from TTS.api import TTS
    tts = TTS('tts_models/multilingual/multi-dataset/xtts_v2', gpu=True)
    info = {}
    if cfg in ('A', 'B'):
        jobs = [(linha, cfg) for linha in LINHAS]
    elif cfg == 'N1X':
        jobs = [('n1', 'A108'), ('n1', 'B108')]
    elif cfg == 'R2':
        jobs = [('n2', 'A090'), ('n2', 'B090'), ('n2', 'A095'), ('n1', 'B112')]
    else:
        raise SystemExit('cfg inválida: ' + cfg)
    for linha, c in jobs:
        sw, tp, sp = CONFIGS[c]
        out = os.path.join(OUT, f'{linha}_{c}.wav')
        t0 = time.time()
        dur, durs, segs_txt = montar(tts, LINHAS[linha], sw, tp, sp, out)
        info[f'{linha}_{c}'] = {'dur': dur, 'partes': durs,
                                'segmentos_motor': segs_txt,
                                'tempo_s': round(time.time() - t0, 1)}
        print(f'{linha}_{c}: dur={dur} tempo={info[f"{linha}_{c}"]["tempo_s"]}s', flush=True)
    tag = 'N1X' if cfg == 'N1X' else cfg
    with open(os.path.join(BASE, f'redub_v4_info_{tag}.json'), 'w', encoding='utf-8') as f:
        json.dump(info, f, indent=1, ensure_ascii=False)
    print('SINT_REDUB_V4_DONE', cfg, flush=True)

if __name__ == '__main__':
    main()
