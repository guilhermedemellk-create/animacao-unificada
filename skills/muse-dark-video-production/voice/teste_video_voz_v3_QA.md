# QA — teste_video_voz_v3.mp4 (2026-11-07)

Montagem idêntica à da v2 (mesmos visuais, textos, drone e receita),
trocando SÓ a narração pelas melhores frases da comparação objetiva v3:
- Trecho 1: `teste_frase1_v3.wav` (candidato c3) — 3,31s
- Trecho 2: `teste_frase2_v3.wav` (candidato c5 bruto) — 4,64s
- Trecho 3: `teste_frase3_v2.wav` (v2 — nenhum candidato v3 a superou) — 3,00s

## Specs (ffprobe)
- Duração: **12,133s** (falas 10,95s + ~0,4s de respiro por trecho; 364 quadros)
- Vídeo: H.264 yuv420p, **1080x1920 (9:16), 30 fps**
- Áudio: AAC **48 kHz** estéreo, presente e sincronizado
- Pico: **−1,97 dB** (sem clipping) · RMS −17,96 dB
- Tamanho: 10.316.181 bytes

## Inspeção visual (amostragem)
Quadros extraídos do arquivo final (`iter_v3/qa_v3_t*.png`): t=1,85s (casa —
texto "DEPOIS DA MEIA-NOITE." + legenda exata da frase 1), t=6,2s (corredor —
"NÃO HAVIA NINGUÉM LÁ." + legenda da frase 2), t=10,4s (escuridão —
"VOCÊ ESCUTOU?" + legenda da frase 3). Textos legíveis e dentro da área
segura; silhueta única por cena, sem duplicações. Inspeção por amostragem,
não quadro a quadro.

## Limitação
A fluidez/timbre percebidos só o usuário julga assistindo — ASR/F0/embedding
provam texto, altura, ritmo e proximidade espectral de locutor, não
naturalidade percebida.
