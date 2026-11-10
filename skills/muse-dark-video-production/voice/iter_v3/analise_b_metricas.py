# -*- coding: utf-8 -*-
"""
ETAPA 1B — Métricas do original a partir de transcricoes.json:
F0 (estatísticas + contorno), ritmo, pausas no stem, energia (LUFS/RMS/crest),
espectro, ambiente (piso + decaimento pós-frase). Salva analise.json.
Rodar com venv_clone.
"""
import os, re, json, glob, unicodedata
import numpy as np
import soundfile as sf
import librosa
import pyloudnorm as pyln

VOICE = os.path.expanduser('~/workspace/custom-skills/muse-dark-video-production/voice')
WORK = os.path.join(VOICE, 'iter_v3')
SR = 24000

def contar_silabas(texto):
    t = ''.join(c for c in unicodedata.normalize('NFD', texto.lower())
                if unicodedata.category(c) != 'Mn')
    total = 0
    for palavra in re.findall(r"[a-z]+", t):
        grupos, ant = 0, False
        for ch in palavra:
            v = ch in 'aeiou'
            if v and not ant:
                grupos += 1
            ant = v
        total += max(grupos, 1)
    return total

def stats_f0(vals):
    if len(vals) == 0:
        return {}
    return {'mediana': round(float(np.median(vals)), 1),
            'media': round(float(np.mean(vals)), 1),
            'desvio': round(float(np.std(vals)), 1),
            'p10': round(float(np.percentile(vals, 10)), 1),
            'p90': round(float(np.percentile(vals, 90)), 1),
            'min': round(float(np.min(vals)), 1),
            'max': round(float(np.max(vals)), 1),
            'n_quadros': int(len(vals))}

def main():
    with open(os.path.join(WORK, 'transcricoes.json'), encoding='utf-8') as f:
        transcricoes = json.load(f)
    trechos = sorted(glob.glob(os.path.join(VOICE, 'trechos_limpos', '*.wav')))

    todos_f0, contornos, ritmo, por_trecho = [], [], [], {}
    espec_c, espec_r = [], []
    for p in trechos:
        nome = os.path.basename(p)
        y, _ = librosa.load(p, sr=SR, mono=True)
        f0, voiced, _ = librosa.pyin(y, fmin=60, fmax=400, sr=SR)
        vals = f0[voiced & ~np.isnan(f0)] if f0 is not None else np.array([])
        todos_f0.append(vals)
        info = sf.info(p)
        dur = info.frames / info.samplerate
        if len(vals) >= 10:
            bins = np.array_split(vals, 10)
            c = [float(np.median(b)) for b in bins if len(b)]
            if len(c) == 10:
                contornos.append(c)
        texto = transcricoes.get(nome, '')
        sil = contar_silabas(texto)
        ritmo.append({'trecho': nome, 'dur': round(dur, 2), 'silabas': sil,
                      'sil_por_s_total': round(sil / dur, 2) if dur else 0})
        cent = librosa.feature.spectral_centroid(y=y, sr=SR)[0]
        roll = librosa.feature.spectral_rolloff(y=y, sr=SR, roll_percent=0.85)[0]
        espec_c.append(float(np.median(cent))); espec_r.append(float(np.median(roll)))
        por_trecho[nome] = {'f0': stats_f0(vals), 'dur': round(dur, 2),
                            'texto_asr': texto, 'silabas': sil}
        print('MET', nome, 'f0med=', por_trecho[nome]['f0'].get('mediana'), flush=True)
    todos_f0 = np.concatenate(todos_f0) if todos_f0 else np.array([])
    contorno_medio = np.mean(np.array(contornos), axis=0) if contornos else []

    # stem contínuo
    stem = os.path.join(WORK, 'stem_vocal_fonte.wav')
    ys, srs = librosa.load(stem, sr=None, mono=True)
    lufs_stem = float(pyln.Meter(srs).integrated_loudness(ys))
    rms_stem = float(20 * np.log10(np.sqrt(np.mean(ys ** 2)) + 1e-12))
    peak_stem = float(20 * np.log10(np.max(np.abs(ys)) + 1e-12))
    yc, src = librosa.load(os.path.join(VOICE, 'trechos_limpos_todos.wav'), sr=None, mono=True)
    lufs_limpo = float(pyln.Meter(src).integrated_loudness(yc))
    rms_limpo = float(20 * np.log10(np.sqrt(np.mean(yc ** 2)) + 1e-12))
    peak_limpo = float(20 * np.log10(np.max(np.abs(yc)) + 1e-12))

    y24, _ = librosa.load(stem, sr=SR, mono=True)
    interv = librosa.effects.split(y24, top_db=30, ref=np.max, frame_length=2048, hop_length=512)
    pausas = []
    for i in range(len(interv) - 1):
        gap = (interv[i + 1][0] - interv[i][1]) / SR
        if gap >= 0.15:
            pausas.append(round(float(gap), 2))
    hop = 512
    frame_rms = librosa.feature.rms(y=y24, frame_length=2048, hop_length=hop)[0]
    tempos = librosa.frames_to_time(np.arange(len(frame_rms)), sr=SR, hop_length=hop)
    decaimentos = []
    for (a, b) in interv:
        idx = np.searchsorted(tempos, b / SR)
        jan = []
        for k in range(8):
            j = idx + k
            if j < len(frame_rms):
                jan.append(float(20 * np.log10(frame_rms[j] + 1e-12)))
        if len(jan) == 8:
            decaimentos.append(jan)
    piso_db = float(np.percentile(20 * np.log10(frame_rms + 1e-12), 10))
    dec_media = np.mean(np.array(decaimentos), axis=0) if decaimentos else []

    resultado = {
        'f0_global_limpos': stats_f0(todos_f0),
        'contorno_medio_10bins_hz': [round(float(x), 1) for x in contorno_medio],
        'ritmo_trechos': ritmo,
        'sil_por_s_media': round(float(np.mean([r['sil_por_s_total'] for r in ritmo])), 2),
        'pausas_entre_frases_stem_s': pausas,
        'pausa_mediana_s': round(float(np.median(pausas)), 2) if pausas else None,
        'pausa_media_s': round(float(np.mean(pausas)), 2) if pausas else None,
        'n_segmentos_stem': int(len(interv)),
        'energia': {'lufs_stem_com_acompanhamento': round(lufs_stem, 1),
                    'lufs_voz_limpa': round(lufs_limpo, 1),
                    'rms_limpa_dbfs': round(rms_limpo, 1),
                    'pico_limpa_dbfs': round(peak_limpo, 1),
                    'crest_limpa_db': round(peak_limpo - rms_limpo, 1),
                    'rms_stem_dbfs': round(rms_stem, 1),
                    'pico_stem_dbfs': round(peak_stem, 1)},
        'espectro': {'centroide_mediano_hz': round(float(np.median(espec_c)), 0),
                     'rolloff85_mediano_hz': round(float(np.median(espec_r)), 0)},
        'ambiente': {'piso_ruido_db': round(piso_db, 1),
                     'decaimento_pos_frase_db_por_janela': [round(float(x), 1) for x in dec_media],
                     'janela_ms_aprox': 21},
        'por_trecho': por_trecho,
        'transcricoes': transcricoes,
    }
    with open(os.path.join(WORK, 'analise.json'), 'w', encoding='utf-8') as f:
        json.dump(resultado, f, indent=1, ensure_ascii=False)
    print('ANALISE_B_DONE', flush=True)

if __name__ == '__main__':
    main()
