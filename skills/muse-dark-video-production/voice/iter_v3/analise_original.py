# -*- coding: utf-8 -*-
"""
ETAPA 1 (v3) — Análise profunda do áudio ORIGINAL do narrador.
Fontes: voice/trechos_limpos/*.wav (12 trechos, 50s) + stem vocal contínuo
do vídeo-fonte (iter_v3/stem_vocal_fonte.wav, 89,09s, Demucs htdemucs).
Mede: F0 (estatísticas + contorno), ritmo (sílabas/s via ASR + contagem
heurística de sílabas do pt), pausas entre frases no stem contínuo, energia
(LUFS/RMS/crest), espectro (centroide/rolloff), ambiente (piso de ruído e
decaimento pós-frase = resíduo de reverb). Salva analise.json + dados p/ o .md.
Rodar com venv_clone.
"""
import os, re, json, glob, unicodedata
import numpy as np
import soundfile as sf
import librosa

VOICE = os.path.expanduser('~/workspace/custom-skills/muse-dark-video-production/voice')
WORK = os.path.join(VOICE, 'iter_v3')
SR = 24000

VOGAIS = 'aeiouáéíóúâêôãõàü'

def contar_silabas(texto):
    """Heurística pt-BR: grupos vocálicos (ditongos contam 1)."""
    t = texto.lower()
    t = ''.join(c for c in unicodedata.normalize('NFD', t)
                if unicodedata.category(c) != 'Mn')
    total = 0
    for palavra in re.findall(r"[a-z]+", t):
        grupos = 0
        anterior_vogal = False
        for ch in palavra:
            v = ch in 'aeiou'
            if v and not anterior_vogal:
                grupos += 1
            anterior_vogal = v
        total += max(grupos, 1)
    return total

def f0_track(path, sr=SR):
    y, _ = librosa.load(path, sr=sr, mono=True)
    f0, voiced, _ = librosa.pyin(y, fmin=60, fmax=400, sr=sr)
    if f0 is None:
        return y, np.array([]), np.array([])
    mask = voiced & ~np.isnan(f0)
    return y, f0[mask], mask

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
    from transformers import pipeline
    import pyloudnorm as pyln

    trechos = sorted(glob.glob(os.path.join(VOICE, 'trechos_limpos', '*.wav')))
    print('trechos:', len(trechos), flush=True)

    # ---------- ASR dos trechos (ritmo) ----------
    asr = pipeline('automatic-speech-recognition', model='openai/whisper-small',
                   language='pt', device='cpu')
    transcricoes = {}
    for p in trechos:
        r = asr(p, generate_kwargs={'language': 'pt', 'task': 'transcribe'})
        transcricoes[os.path.basename(p)] = r['text'].strip()
        print('ASR', os.path.basename(p), '::', r['text'].strip(), flush=True)
    del asr

    # ---------- F0 global + contorno + ritmo ----------
    todos_f0 = []
    contornos = []
    ritmo = []
    espec_c, espec_r = [], []
    por_trecho = {}
    for p in trechos:
        nome = os.path.basename(p)
        y, vals, mask = f0_track(p)
        todos_f0.append(vals)
        info = sf.info(p)
        dur = info.frames / info.samplerate
        # contorno normalizado em 10 bins (só quadros vozeados, ordem temporal)
        if len(vals) >= 10:
            bins = np.array_split(vals, 10)
            contornos.append([float(np.median(b)) for b in bins if len(b)])
        texto = transcricoes.get(nome, '')
        sil = contar_silabas(texto)
        # duração vozeada aproximada: fração de quadros vozeados * dur
        dur_voz = dur * (len(vals) / max(1, int(dur * SR / 512))) if dur else 0
        ritmo.append({'trecho': nome, 'dur': round(dur, 2),
                      'silabas': sil, 'sil_por_s_total': round(sil / dur, 2) if dur else 0})
        # espectro
        y44, sr44 = librosa.load(p, sr=None, mono=True)
        cent = librosa.feature.spectral_centroid(y=y44, sr=sr44)[0]
        roll = librosa.feature.spectral_rolloff(y=y44, sr=sr44, roll_percent=0.85)[0]
        espec_c.append(float(np.median(cent))); espec_r.append(float(np.median(roll)))
        por_trecho[nome] = {'f0': stats_f0(vals), 'dur': round(dur, 2),
                            'texto_asr': texto, 'silabas': sil}
    todos_f0 = np.concatenate(todos_f0) if todos_f0 else np.array([])
    contorno_medio = np.mean(np.array([c for c in contornos if len(c) == 10]), axis=0) \
        if any(len(c) == 10 for c in contornos) else []

    # ---------- Stem contínuo: pausas, energia, ambiente ----------
    stem = os.path.join(WORK, 'stem_vocal_fonte.wav')
    ys, srs = librosa.load(stem, sr=None, mono=True)
    meter = pyln.Meter(srs)
    lufs_stem = float(meter.integrated_loudness(ys))
    rms_db = float(20 * np.log10(np.sqrt(np.mean(ys ** 2)) + 1e-12))
    peak_db = float(20 * np.log10(np.max(np.abs(ys)) + 1e-12))

    # trechos limpos combinados: LUFS da voz limpa
    yc, src = librosa.load(os.path.join(VOICE, 'trechos_limpos_todos.wav'), sr=None, mono=True)
    lufs_limpo = float(pyln.Meter(src).integrated_loudness(yc))
    rms_limpo = float(20 * np.log10(np.sqrt(np.mean(yc ** 2)) + 1e-12))
    peak_limpo = float(20 * np.log10(np.max(np.abs(yc)) + 1e-12))

    # segmentação do stem por energia (frases e pausas reais do original)
    y24, _ = librosa.load(stem, sr=SR, mono=True)
    interv = librosa.effects.split(y24, top_db=30, ref=np.max, frame_length=2048, hop_length=512)
    pausas = []
    fins = []
    for i in range(len(interv) - 1):
        gap = (interv[i + 1][0] - interv[i][1]) / SR
        if gap >= 0.15:
            pausas.append(round(float(gap), 2))
    # decaimento pós-frase: RMS em janelas de 50ms após o fim de cada segmento
    decaimentos = []
    piso_amostras = []
    hop = 512
    frame_rms = librosa.feature.rms(y=y24, frame_length=2048, hop_length=hop)[0]
    tempos = librosa.frames_to_time(np.arange(len(frame_rms)), sr=SR, hop_length=hop)
    for (a, b) in interv:
        t_fim = b / SR
        idx = np.searchsorted(tempos, t_fim)
        janelas = []
        for k in range(8):  # 8 janelas ~ 170ms.. (frame hop 512/24000=21ms, rms frame ~85ms)
            j = idx + k
            if j < len(frame_rms):
                janelas.append(float(20 * np.log10(frame_rms[j] + 1e-12)))
        if len(janelas) >= 4:
            decaimentos.append(janelas)
        # piso: trecho de silêncio antes do próximo segmento
    # piso de ruído: quadros RMS abaixo do percentil 10
    piso_db = float(np.percentile(20 * np.log10(frame_rms + 1e-12), 10))
    dec_media = np.mean(np.array([d for d in decaimentos if len(d) == 8]), axis=0) \
        if any(len(d) == 8 for d in decaimentos) else []

    resultado = {
        'f0_global_limpos': stats_f0(todos_f0),
        'contorno_medio_10bins_hz': [round(float(x), 1) for x in contorno_medio],
        'ritmo_trechos': ritmo,
        'sil_por_s_media': round(float(np.mean([r['sil_por_s_total'] for r in ritmo])), 2),
        'pausas_entre_frases_stem_s': pausas,
        'pausa_mediana_s': round(float(np.median(pausas)), 2) if pausas else None,
        'pausa_media_s': round(float(np.mean(pausas)), 2) if pausas else None,
        'energia': {'lufs_stem_com_acompanhamento': round(lufs_stem, 1),
                    'lufs_voz_limpa': round(lufs_limpo, 1),
                    'rms_limpa_dbfs': round(rms_limpo, 1),
                    'pico_limpa_dbfs': round(peak_limpo, 1),
                    'crest_limpa_db': round(peak_limpo - rms_limpo, 1),
                    'rms_stem_dbfs': round(rms_db, 1), 'pico_stem_dbfs': round(peak_db, 1)},
        'espectro': {'centroide_mediano_hz': round(float(np.median(espec_c)), 0),
                     'rolloff85_mediano_hz': round(float(np.median(espec_r)), 0)},
        'ambiente': {'piso_ruido_db': round(piso_db, 1),
                     'decaimento_pos_frase_db_por_janela': [round(float(x), 1) for x in dec_media]},
        'por_trecho': por_trecho,
        'transcricoes': transcricoes,
    }
    with open(os.path.join(WORK, 'analise.json'), 'w', encoding='utf-8') as f:
        json.dump(resultado, f, indent=1, ensure_ascii=False)
    print(json.dumps({k: resultado[k] for k in
                      ('f0_global_limpos', 'sil_por_s_media', 'pausa_mediana_s',
                       'energia', 'espectro', 'ambiente')}, indent=1), flush=True)
    print('ANALISE_DONE', flush=True)


if __name__ == '__main__':
    main()
