# -*- coding: utf-8 -*-
"""Avaliação enxuta v4-seg — portão por PALAVRA (faster-whisper, timestamps),
ritmo, embedding; F0 só do vencedor de cada linha. Uso: avaliar_v5.py n1,n2,..."""
import os, re, sys, json, glob, unicodedata, time
import numpy as np
import soundfile as sf

VOICE = os.path.expanduser('~/workspace/custom-skills/muse-dark-video-production/voice')
WORK = os.path.join(VOICE, 'iter_v3')
CAND = os.path.join(WORK, 'saida_v4_dl')
PRETENDIDO = {
 'n1': "Existe alguém aparecendo em todas as suas fotografias... mas essa pessoa nunca esteve lá.",
 'n2': "Ele percebeu isso por acaso, enquanto olhava uma foto tirada dez anos atrás.",
 'n3': "Ele procurou outras fotografias. E encontrou a mesma figura em todas elas. Sempre mais perto.",
 'n4': "Assustado, mostrou as imagens para um amigo. Mas o amigo ficou em silêncio.",
 'd4': "Você também está vendo isso?",
 'n5': "Então o amigo revelou algo impossível. Aquela figura não aparecia nas fotografias dele... aparecia apenas nas fotografias de quem estava prestes a desaparecer.",
 'n6': "O homem correu para olhar a última fotografia. Mas agora havia algo diferente.",
 'n7': "E quando levantou os olhos... viu a mesma figura parada bem na sua frente.",
}
JANELA = {'n1': 4.97, 'n2': 8.40, 'n3': 10.65, 'n4': 5.90, 'd4': 3.70,
          'n5': 12.55, 'n6': 10.60, 'n7': 5.55}
TOKENS = {'ponto', 'virgula', 'reticencias', 'exclamacao', 'interrogacao'}

NUM = {'10': 'dez', '1': 'um'}
def norm(t):
    t = unicodedata.normalize('NFKD', t.lower())
    t = ''.join(c for c in t if not unicodedata.combining(c))
    t = re.sub(r'[^a-z0-9 ]', ' ', t)
    t = ' '.join(NUM.get(w, w) for w in t.split())
    return re.sub(r'\s+', ' ', t).strip()

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

def f0_mediano(path):
    import librosa
    y, sr = librosa.load(path, sr=24000, mono=True)
    f0, voiced, _ = librosa.pyin(y, fmin=60, fmax=400, sr=sr)
    vals = f0[voiced & ~np.isnan(f0)] if f0 is not None else np.array([])
    return round(float(np.median(vals)), 1) if len(vals) else None

def main():
    linhas = sys.argv[1].split(',')
    from faster_whisper import WhisperModel
    import librosa
    t0 = time.time()
    modelo = WhisperModel('small', device='cpu', compute_type='int8',
                          cpu_threads=4)
    print(f'modelo ok {time.time()-t0:.0f}s', flush=True)
    from resemblyzer import VoiceEncoder, preprocess_wav
    enc = VoiceEncoder(verbose=False)
    embs = [enc.embed_utterance(preprocess_wav(p))
            for p in sorted(glob.glob(os.path.join(VOICE, 'trechos_limpos', '*.wav')))]
    ref = np.mean(embs, axis=0); ref = ref / np.linalg.norm(ref)
    print(f'embedding ref ok {time.time()-t0:.0f}s', flush=True)

    def emb_cos(path):
        e = enc.embed_utterance(preprocess_wav(path))
        return round(float(np.dot(e / np.linalg.norm(e), ref)), 4)

    resultado = {}
    for linha in linhas:
        texto = PRETENDIDO[linha]
        itens = []
        for path in sorted(glob.glob(os.path.join(CAND, f'{linha}_*.wav'))):
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
            info = sf.info(path)
            dur = info.frames / info.samplerate
            item = {'rotulo': os.path.basename(path).replace('.wav', ''),
                    'arquivo': path, 'asr': t_asr, 'palavras': palavras,
                    'tokens_pontuacao': achados,
                    'portao_palavra': not achados,
                    'portao_texto': norm(t_asr) == norm(texto),
                    'dur': round(dur, 3),
                    'sil_por_s': round(contar_silabas(texto) / dur, 2),
                    'atempo_necessario': round(max(1.0, dur / JANELA[linha]), 3),
                    'embedding_cos': emb_cos(path), 'f0': None}
            itens.append(item)
            print(f"{linha} {item['rotulo']}: palavra={item['portao_palavra']} "
                  f"texto={item['portao_texto']} emb={item['embedding_cos']} "
                  f"dur={item['dur']} sil/s={item['sil_por_s']} "
                  f"atempo={item['atempo_necessario']} ach={achados}", flush=True)
        validos = [i for i in itens if i['portao_palavra'] and i['portao_texto']
                   and 3.5 <= i['sil_por_s'] <= 6.0]
        validos.sort(key=lambda i: -i['embedding_cos'])
        esc = validos[0] if validos else None
        if esc:
            esc['f0'] = f0_mediano(esc['arquivo'])
        resultado[linha] = {'itens': itens, 'janela_util': JANELA[linha],
                            'escolhido': esc}
        print(f"-> {linha}: {esc['rotulo'] if esc else None} f0={esc['f0'] if esc else None}",
              flush=True)
    out = os.path.join(WORK, 'avaliacao_v5_' + '_'.join(linhas) + '.json')
    with open(out, 'w', encoding='utf-8') as f:
        json.dump(resultado, f, indent=1, ensure_ascii=False)
    print('AV5_DONE', out, flush=True)

if __name__ == '__main__':
    main()
