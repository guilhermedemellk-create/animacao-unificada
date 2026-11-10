# ETAPA 1 (v3) — Análise profunda do áudio original do narrador

Fontes medidas: `voice/trechos_limpos/` (12 trechos, 50,0s de narração limpa) e o
stem vocal contínuo do vídeo-fonte (`iter_v3/stem_vocal_fonte.wav`, 89,09s,
Demucs htdemucs). Ferramentas: librosa.pyin (F0), whisper-small (ASR dos
trechos), pyloudnorm (LUFS). Dados brutos: `iter_v3/analise.json`.
Scripts: `analise_a_asr.py` + `analise_b_metricas.py`.

## F0 — altura e contorno
- **Global (trechos limpos): mediana 123,5 Hz** · média 116,2 · desvio 38,1 ·
  p10 60,0 (= piso do pyin, artefato de borda) · p90 156,3 · faixa útil
  ~90–160 Hz. Confirma a referência anterior de ≈120 Hz.
- Mediana por trecho varia com a interpretação: 80,6 Hz (trecho curto e
  sussurrado) a 141,9 Hz; nos trechos longos e confiáveis: **114,6–137,0 Hz**
  (centro ~120–130 Hz).
- **Contorno médio da frase (10 fatias temporais):** 124,6 → 127,9 → 123,3 →
  117,8 → 113,2 → 124,2 → 130,3 → 113,1 → 123,5 → **113,0 Hz** — começa
  ~125 Hz e **termina ~113 Hz: queda declarativa típica**, com ondulação no
  meio. Não há subida final sustentada (a narração de referência é quase toda
  declarativa; a frase de pergunta é exceção do nosso teste).

## Ritmo
- Sílabas contadas por heurística de grupos vocálicos sobre o ASR de cada
  trecho (mesma régua usada no clone). Média ponderada pela duração:
  **266 sílabas / 51,1s = 5,20 síl/s**. Nos trechos longos (≥6s), que mandam
  no ritmo percebido: **4,59–4,90 síl/s (média ≈ 4,75)**.
- Comparação direta: as frases v2 saíram a 3,6–3,8 síl/s (frases 1–2) —
  **mais lentas que o original**. Alvo de ritmo da v3: **≈4,8–5,2 síl/s**
  (frase de 16 sílabas ≈ 3,1–3,4s).
- **Pausas entre frases no stem contínuo:** 24 pausas ≥0,15s — **mediana
  0,50s**, média 0,57s (inclui pausas intra-frase). Nossa pausa de montagem
  da v2 (~250ms em ponto) está abaixo da mediana original; a de reticências
  (500ms) está na medida.

## Energia / dinâmica
- **Voz limpa: −25,5 LUFS** · RMS −25,8 dBFS · pico −8,9 dBFS ·
  **crest factor 16,8 dB** → dinâmica ampla, **sem compressão forte nem
  brickwall** (pico longe de 0). Master relativamente baixo (−25,5 LUFS).

## Espectro
- **Centroide espectral mediano: 1.263 Hz** · rolloff 85%: 2.367 Hz → voz
  **escura, agudos contidos** (EQ escura/baixa presença de brilho — seja da
  voz, seja de processamento da fonte).

## Ambiente / reverb
- Piso de ruído do stem: **−49,4 dB** (resíduo conhecido do Demucs ≈ −51 dB).
- Decaimento pós-frase: após o fim de cada segmento o sinal já está no piso
  (janelas de ~21ms em −48,8…−43,6 dB, sem cauda decrescente mensurável) →
  **não há reverb mensurável: voz seca**. Não aplicar reverb no clone.

## Decisão de pós-processamento (Etapa 3)
Cadeia leve, só se as medições dos vencedores desviarem do original:
1. **Lowpass suave** se o centroide do clone ficar muito acima de ~1.600 Hz
   (meta: aproximar de ~1.263 Hz sem abafar).
2. **Sem compressão forte** (original tem crest 16,8 dB); no máximo
   normalização de ganho para a faixa de −25,5 LUFS nas frases isoladas.
3. **Sem reverb** (original seco).
4. Micro-`atempo` (sem mudar pitch) apenas se o ritmo do vencedor ficar
   abaixo de ~4,3 síl/s, mirando 4,8–5,2 síl/s.
