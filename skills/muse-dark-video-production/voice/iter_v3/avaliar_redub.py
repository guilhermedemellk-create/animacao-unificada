# -*- coding: utf-8 -*-
"""
Avaliação dos candidatos da REDUBLAGEM (GPU do PC) — mesma régua da v3:
portão ASR (whisper-small) -> encaixe na janela da cena (atempo necessário
<= 1,20) -> embedding resemblyzer vs. média dos 12 trechos -> F0.
Salva avaliacao_redub.json com a escolha por linha. Rodar com venv_clone.
"""
import os, re, json, glob, unicodedata
import numpy as np
import soundfile as sf

VOICE = os.path.expanduser('~/workspace/custom-skills/muse-dark-video-production/voice')
WORK = os.path.join(VOICE, 'iter_v3')
CAND = os.path.join(WORK, 'redub_candidatos')

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
# janela útil de fala (s) na montagem original: do início da voz ao fim útil
JANELA = {'n1': 4.97, 'n2': 8.40, 'n3': 10.65, 'n4': 5.90, 'd4': 3.70,
          'n5': 12.55, 'n6': 10.60, 'n7': 5.55}
ALVO_F0 = {'n1': 120.0, 'n2': 120.0, 'n3': 120.0, 'n4': 120.0, 'd4': 145.0,
           'n5': 120.0, 'n6': 120.0, 'n7': 125.0}
PROIBIDAS = ['ponto', 'vírgula', 'virgula', 'interrogação', 'interrogacao',
             'exclamação', 'exclamacao', 'reticências', 'reticencias',
             'dois pontos', 'ponto e vírgula']


def norm(t):
    t = unicodedata.normalize('NFKD', t.lower())
    t = ''.join(c for c in t if not unicodedata.combining(c))
    t = re.sub(r'[^a-z0-9 ]', ' ', t)
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
    return float(np.median(vals)) if len(vals) else float('nan')


def main():
    from resemblyzer import VoiceEncoder, preprocess_wav
    enc = VoiceEncoder(verbose=False)
    embs = [enc.embed_utterance(preprocess_wav(p))
            for p in sorted(glob.glob(os.path.join(VOICE, 'trechos_limpos', '*.wav')))]
    ref = np.mean(embs, axis=0); ref = ref / np.linalg.norm(ref)

    def emb_cos(path):
        e = enc.embed_utterance(preprocess_wav(path))
        return round(float(np.dot(e / np.linalg.norm(e), ref)), 4)

    from transformers import pipeline
    asr = pipeline('automatic-speech-recognition', model='openai/whisper-small',
                   language='pt', device='cpu')
    resultado = {}
    for linha, texto in PRETENDIDO.items():
        itens = []
        for path in sorted(glob.glob(os.path.join(CAND, f'{linha}_*.wav'))):
            r = asr(path, generate_kwargs={'language': 'pt', 'task': 'transcribe'})
            t_asr = r['text'].strip()
            achadas = [w for w in PROIBIDAS
                       if re.search(r'\b' + re.escape(w) + r'\b', t_asr.lower())]
            info = sf.info(path)
            dur = info.frames / info.samplerate
            atempo_necessario = round(max(1.0, dur / JANELA[linha]), 3)
            item = {'rotulo': os.path.basename(path).replace('.wav', ''),
                    'arquivo': path, 'asr': t_asr,
                    'portao': bool(norm(t_asr) == norm(texto) and not achadas),
                    'proibidas': achadas, 'embedding_cos': emb_cos(path),
                    'f0': round(f0_mediano(path), 1), 'dur': round(dur, 2),
                    'sil_por_s': round(contar_silabas(texto) / dur, 2),
                    'atempo_necessario': atempo_necessario}
            itens.append(item)
            print(f"{linha} {item['rotulo']}: portao={item['portao']} "
                  f"emb={item['embedding_cos']} f0={item['f0']} "
                  f"dur={item['dur']} atempo={atempo_necessario} "
                  f"sil/s={item['sil_por_s']} :: {t_asr}", flush=True)
        validos = [i for i in itens if i['portao'] and i['atempo_necessario'] <= 1.20]
        # preferência: menor atempo necessário, depois maior embedding
        validos.sort(key=lambda i: (round(i['atempo_necessario'], 2),
                                    -i['embedding_cos'],
                                    abs(i['f0'] - ALVO_F0[linha])))
        escolhido = validos[0] if validos else None
        resultado[linha] = {'itens': itens, 'janela_util': JANELA[linha],
                            'escolhido': escolhido}
        print(f"-> {linha}: escolhido = "
              f"{escolhido['rotulo'] if escolhido else None}", flush=True)
    with open(os.path.join(WORK, 'avaliacao_redub.json'), 'w', encoding='utf-8') as f:
        json.dump(resultado, f, indent=1, ensure_ascii=False)
    print('AVALIACAO_REDUB_DONE', flush=True)


if __name__ == '__main__':
    main()
