# QA — teste_video_voz_v2.mp4 (2026-11-07)

Vídeo de teste da voz clonada v2 (iteração de fluidez) da skill de terror,
para o usuário julgar a voz dentro de um vídeo. Montagem:
`voice/iter_video/montar_video.py`.

## Specs verificadas (ffprobe)
- Duração: **12,767s** (= soma das falas v2 + respiros: trecho 1 = 4,40 + 0,40
  = 4,80s · trecho 2 = 4,17 + 0,40 = 4,57s · trecho 3 = 3,00 + 0,40 = 3,40s;
  383 quadros)
- Vídeo: **1080x1920 (9:16), 30 fps, H.264 yuv420p**, CRF 18
- Áudio: **AAC 48 kHz, estéreo, 192 kbps**, presente e sincronizado
  (vozes em t=0 / 4,800s / 9,367s)
- Pico de áudio medido (astats): **−1,92 dB — sem clipping** (média −15,3 dB).
  Correção aplicada na montagem: a mix bruta batia 0,0 dB (os WAVs do XTTS
  já vêm em 0 dBFS); ganho final fixo de 0,79× após a mix — o `alimiter`
  desta build não conteve o pico, foi removido do caminho final.

## Conteúdo
- Narração: `teste_frase1_v2.wav`, `teste_frase2_v2.wav`,
  `teste_frase3_v2.wav` (validação ASR/F0 em
  `iter_fluidez/validacao_final_v2.json` — as 3 exatas, ZERO pontuação).
- Visuais: 3 imagens NOVAS geradas para este teste (não reutilizadas do
  projeto 'O HOMEM QUE NÃO EXISTIA'), escolhidas pelo encaixe direto com
  cada frase: casa escura com porta vermelha e silhueta na janela (frase 1) ·
  corredor escuro com silhueta ao fundo (frase 2) · escuridão com rosto em
  silhueta de contorno vermelho (frase 3). Arquivos em `voice/iter_video/`.
  Movimento: zoompan lento 1,00→1,10 por trecho.
- Textos: legenda queimada com o texto EXATO de cada frase + texto grande
  (DEPOIS DA MEIA-NOITE. / NÃO HAVIA NINGUÉM LÁ. / VOCÊ ESCUTOU?), fonte
  DejaVu Sans Bold, arquivos-fonte em `iter_video/textos/`.
- Som: drone de suspense (55 Hz + 82,4 Hz, lowpass 220 Hz, bem abaixo da
  voz) + blips de glitch sonoro só nas viradas (4,71s / 9,28s / 12,40s);
  glitch visual (RGB shift + ruído) nas mesmas viradas e reforçado no fim
  (12,35–12,77s). Fade-in/out curtos de vídeo.

## Inspeção de quadros (extraídos do arquivo final)
- `iter_video/qa_t2.4.png` (trecho 1): texto grande e legenda legíveis, na
  área segura; silhueta única na janela; a faixa cromática do rodapé da
  imagem-fonte foi removida no preparo (crop). OK
- `iter_video/qa_t7.0.png` (trecho 2): idem; corredor com uma única silhueta
  ao fundo, sem duplicações. OK
- `iter_video/qa_t11.0.png` (trecho 3): idem; silhueta central não colide com
  os textos. OK
- `iter_video/qa_t12.5.png` (glitch final): RGB shift visível nos contornos
  da silhueta e grão aumentado; textos continuam legíveis (leve escurecimento
  é o fade-out final). OK

## Limitações
- Inspeção por amostragem de quadros (4 quadros + specs + pico de áudio);
  não é revisão quadro a quadro nem audição — a fluidez/timbre da voz só o
  usuário julga assistindo.
- As falas v2 têm ritmos diferentes entre si (4,40 / 4,17 / 3,00s), então os
  trechos do vídeo têm durações diferentes — é proposital (duração real de
  cada fala + respiro fixo de ~0,4s).
