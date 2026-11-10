# VOZ_TERROR — Voz clonada do narrador (padrão da skill de terror)

Perfil criado em 2026-11-07. Esta é a voz do **NARRADOR** dos vídeos produzidos
com a skill `muse-dark-video-production`. Arquivos de voz em
`~/workspace/custom-skills/muse-dark-video-production/voice/`.

## Fonte e autorização
- Fonte: vídeo do canal **@estudio.vhs** (referência visual/original da skill),
  arquivo `~/workspace/user/media_library/video/ed/ede90ac89223b88c0bd382fc3567a1f558273de3d6c8df8339d26ebfb80ed31f.mp4`
  — 89,09s, áudio AAC 44,1 kHz estéreo com narração. Usado **somente o áudio**.
- Autorização: o usuário confirmou expressamente em **2026-11-07**:
  **"É minha voz ou tenho autorização do narrador"** — mesmo protocolo já usado
  no clone de voz do projeto dos 10 segundos (Teco Azarado, 2026-11-06).

## Extração e seleção (pipeline reutilizado da clonagem anterior)
- Áudio extraído do vídeo e separado com **Demucs (htdemucs, two-stems)** para
  remover música/efeitos: stem vocal limpo, com acompanhamento residual em
  ≈ −51 dB contra ≈ −25 dB de voz (separação muito boa; vazamento agudo ~0).
- Frases detectadas por silêncio e pontuadas (nível, banda de voz, ausência de
  agudos de SFX, nível do acompanhamento) — método de
  `producao_volta10s_v3/audio_clone/montar_amostra.py`.
- **Conjunto limpo: 12 trechos em nível de frase, 50,0s de narração**
  (`voice/trechos_limpos/trecho_01..12_*.wav`; combinado em
  `voice/trechos_limpos_todos.wav`, 53,7s com respiros de 0,22s).
- **Amostra de condicionamento: `voice/referencia_condicionamento.wav` —
  23,6s de bloco CONTÍNUO real** do stem vocal (6,18s–29,71s do vídeo-fonte),
  sem montagem.

## Motor e parâmetros finais
- Motor: **Coqui XTTS v2 (coqui-tts 0.28.0)**, modelo
  `tts_models/multilingual/multi-dataset/xtts_v2`, rodando no CPU desta VM
  (venv `~/workspace/video_project/producao_volta10s_v3/audio_clone/venv_clone`).
- Idioma: `pt`. `speaker_wav` = `referencia_condicionamento.wav`.
- **speed = 1.00** (escolhido por F0 — ver abaixo). `temperature = 0.65`,
  `repetition_penalty = 2.0`.
- **Síntese segmentada OBRIGATÓRIA** (causa-raiz provada na v4: o XTTS v2
  verbaliza pontuação em pt-BR mesmo com texto limpo). Na **v1** usava-se
  `producao_volta10s_v4/teste_voz/limpeza_texto.py` (`segmentar()`): cada
  segmento sintetizado **sem** vírgula/ponto/reticências no texto; pausas
  como silêncios exatos — **vírgula 150ms · ponto 350ms · reticências 700ms**.
  **ATENÇÃO: essa segmentação foi APOSENTADA para este clone na iteração de
  fluidez — vale a seção "Iteração de fluidez — v2" abaixo (segmentar só
  entre frases, vírgula dentro do segmento).** NUNCA enviar nomes de sinais
  nem marcações ao motor.

## F0 (librosa.pyin, mediano dos quadros vozeados)
- **Narrador original:** 119,3 Hz na amostra de condicionamento ·
  120,7 Hz no conjunto limpo completo → referência ≈ **120 Hz**.
- Busca de speed (mesma frase): speed 1.00 → **120,7 Hz** · 1.15 → 117,3 Hz ·
  1.30 → 130,9 Hz. Escolhido **1.00**.
- **Clone (teste final):** frase 1 → **120,0 Hz** · frase 2 → **120,3 Hz** ·
  frase 3 (pergunta, entonação sobe) → 144,8 Hz.

## Teste de validação (3 frases novas, ASR whisper-small)
Frases de suspense genéricas, criadas para o teste — **sem copiar** o texto do
vídeo de referência. Transcrições ASR idênticas ao texto pretendido e
**ZERO palavras de pontuação faladas** nas três:

| Arquivo | Texto pretendido | ASR | Duração | F0 |
|---|---|---|---|---|
| `voice/teste_frase1.wav` | "Naquela casa, ninguém atendia depois da meia-noite." | exata — LIMPO | 4,41s | 120,0 Hz |
| `voice/teste_frase2.wav` | "Ele ouviu passos no corredor... mas não havia ninguém lá." | exata — LIMPO | 5,42s | 120,3 Hz |
| `voice/teste_frase3.wav` | "Você também escutou esse barulho no escuro?" | exata — LIMPO | 9,18s | 144,8 Hz |

Notas honestas do teste: a frase 3 (pergunta, segmento único com `?`) tende a
sair arrastada (1ª geração: 12,06s; refeita: 9,18s) e a frase 1 precisou de uma
regeneração para o F0 cair no alvo (1ª geração: 140,3 Hz; refeita: 120,0 Hz) —
o XTTS tem variância real entre gerações; conferir duração/F0 por frase nas
produções e regenerar a frase fora do padrão, nunca o vídeo inteiro.

## Iteração de fluidez — v2 (2026-11-07) — PADRÃO VIGENTE

**Feedback do usuário (2026-11-07, após ouvir os testes v1):** "está um pouco
robótica e travada — a voz original é mais fluida".

**Diagnóstico atacado:** (1) a v1 cortava a frase em TODA pontuação — cada
micro-segmento era sintetizado do zero, sem continuidade de entonação;
(2) silêncios rígidos + junção seca entre segmentos; (3) temperature 0.65
deixava a prosódia monótona.

**O que mudou na v2:**
- Segmentação **somente entre frases** (ponto final/reticências/interrogação);
  a **vírgula fica DENTRO do segmento** e a frase é sintetizada inteira de uma
  vez, com a pontuação final enviada ao motor (a prosódia da vírgula e da
  queda final é do próprio modelo).
- `temperature = 0.75` (era 0.65). Speed segue **1.00**, repetition_penalty 2.0.
- Junções entre segmentos com **fade coseno de 40ms** nas bordas (efeito
  crossfade, sem clique) e pausas menores: **reticências 500ms** (era 700) ·
  ponto/interrogação ~250ms (era 350).
- Seleção por frase entre até 3 tentativas, por ASR + F0 + duração (nunca
  mais lenta que a v1), com ajustes localizados quando necessário.

**Resultados da v2 (validação final nos arquivos entregues — ASR
whisper-small, F0 librosa.pyin):**

| Arquivo | ASR | F0 | Duração (v1) |
|---|---|---|---|
| `voice/teste_frase1_v2.wav` | exata — ZERO pontuação | 128,6 Hz | 4,40s (4,41s) |
| `voice/teste_frase2_v2.wav` | exata — ZERO pontuação | 112,0 Hz | 4,17s (5,42s) |
| `voice/teste_frase3_v2.wav` | exata — ZERO pontuação | 136,7 Hz | 3,00s (9,18s) |

Ajustes localizados registrados (scripts e tentativas em `voice/iter_fluidez/`):
- Frase 1: a tentativa escolhida (única limpa com F0 no alvo — outra tentativa
  verbalizou "Ponto." e foi descartada) saiu a 4,57s; micro-correção
  `atempo=1.037` (sem mudar o pitch) → 4,40s. A pausa da vírgula (~0,7s) é
  prosódia do próprio modelo, não corte de montagem.
- Frase 2: tentativa com F0 112,0 Hz escolhida; a de F0 143,1 Hz foi
  descartada (aguda demais vs. narrador ~120 Hz).
- Frase 3: a tentativa escolhida trazia um **artefato audível após ~2,7s de
  silêncio** no fim (fragmento espúrio que o ASR leu como "Obrigado." —
  alucinação típica do XTTS); a frase completa está nos primeiros 3,0s
  (provado por ASR do trecho isolado) e o arquivo foi cortado em 3,0s com
  fade-out de 40ms. Outra tentativa (2,20s, ~7,3 sílabas/s) foi descartada
  por ritmo corrido demais.

**Regra vigente:** daqui em diante, a narração com este clone segue os
parâmetros da **v2** (segmentação entre frases, vírgula dentro do segmento,
temperature 0.75, fades de 40ms, pausas 500/250ms). A segmentação antiga da
v1 (cortar na vírgula) fica **aposentada** para este clone. Os arquivos v1
(`teste_frase1–3.wav`) foram mantidos para comparação. A fluidez percebida
continua dependendo do ouvido do usuário — F0/ASR/duração provam altura,
texto e ritmo, não naturalidade.

## Iteração de similaridade — v3 (2026-11-07) — PADRÃO VIGENTE

**Pedido do usuário (após ouvir a v2):** "tenta melhorar mais ainda, faça o
seu melhor, olha o áudio e reproduza mais igual". Método: analisar o
original a fundo, gerar grade de candidatos e selecionar por critérios
objetivos mensuráveis (ninguém "ouve" nesta etapa). Tudo em
`voice/iter_v3/` (scripts, candidatos, logs, `analise.json`,
`avaliacao_v3.json`, `pos_v3.json`).

### Análise do original (`iter_v3/analise_original.md`)
- **F0:** mediana global 123,5 Hz (trechos longos: 114,6–137,0) — confirma
  ~120 Hz. Contorno médio da frase: começa ~125 Hz e **cai para ~113 Hz**
  (declarativo).
- **Ritmo: 5,20 síl/s ponderado; 4,59–4,90 nos trechos longos.** As frases
  v2 (3,6–3,8 síl/s nas frases 1–2) estavam **mais lentas que o original**.
- **Pausas reais entre frases: mediana 0,50s** (a v2 usava ~250ms em ponto).
- **Energia:** voz limpa −25,5 LUFS, crest 16,8 dB → **sem compressão
  forte**; pico −8,9 dBFS.
- **Espectro escuro:** centroide mediano **1.263 Hz**, rolloff85 2.367 Hz.
- **Ambiente:** piso −49,4 dB e **nenhum reverb mensurável** (voz seca).

### Grade e seleção objetiva
8 candidatos/frase (24 no total), variando condicionamento (A = só a
referência de 23,6s; B = 4 melhores trechos limpos juntos), temperature
(0,65/0,75/0,85) e speed (0,95/1,00/1,05), segmentação da v2 mantida.
Critérios, nesta ordem: **(1) portão ASR** idêntico e zero pontuação
(8/24 candidatos reprovados — o portão trabalha); **(2) faixa de ritmo sã**
3,5–6,0 síl/s (os maiores embeddings crus eram de gerações arrastadas a
2,7–2,9 síl/s — embedding sozinho não mede ritmo); **(3) embedding de
locutor** (resemblyzer GE2E, cosseno vs. média dos 12 trechos originais;
régua: os trechos originais entre si marcam 0,913 de média, mín. 0,845);
**(4) F0**.

| Frase | Melhor v3 | Embedding (v2) | F0 | Ritmo |
|---|---|---|---|---|
| 1 | cond A · temp 0,65 · speed 1,00 (`teste_frase1_v3.wav`) | **0,7604** (0,7523) | 109,7 Hz | **4,83 síl/s** |
| 2 | cond B · temp 0,85 · speed 1,00 (`teste_frase2_v3.wav`) | **0,7795** (0,7642) | 121,4 Hz | 3,66 síl/s |
| 3 | **v2 permanece** — nenhum candidato na faixa de ritmo superou 0,7880 | 0,7880 (v2) | 136,7 Hz | 5,33 síl/s |

- **Pós-processamento:** nenhum aplicado no final. Os centroides dos
  vencedores (1.072 e ~1.011 Hz) já são tão ou mais escuros que o original
  (1.263 Hz) — lowpass desnecessário. **Micro-atempo 1,20 na frase 2 foi
  testado e REVERTIDO:** o ritmo subiu (4,40 síl/s), mas o embedding caiu
  de 0,7795 para 0,7460, abaixo da v2 — timbre medido manda no ritmo.
- Trade-off honesto da frase 2: a v3 ganha em timbre (+0,015) e F0
  (121,4 vs. alvo 120; v2 tinha 112,0), mas é um pouco mais lenta que a
  v2 (4,64s vs. 4,17s).
- Teto atual do método: embeddings ~0,76–0,81 contra 0,913 dos originais
  entre si — o XTTS zero-shot aproxima, não iguala; quem decide se basta
  é o usuário ouvindo o `teste_video_voz_v3.mp4`.

**Regra vigente a partir da v3:** não existe um único conjunto de
parâmetros vencedor — varia por frase. O procedimento padrão passa a ser:
gerar grade enxuta por frase (cond A e B × temperature 0,65–0,85 × speed
0,95–1,05), selecionar por portão ASR → faixa de ritmo → embedding → F0, e
só promover o que superar a versão vigente. Arquivos v1/v2 mantidos;
`teste_frase3_v3.wav` não existe de propósito (a frase 3 vigente é a v2).

## Redublagem de "O HOMEM QUE NÃO EXISTIA" (2026-11-07) + LIÇÃO DO "PONTO"

O usuário ouviu um "ponto" falado no `teste_video_voz_v3.mp4`. Varredura
palavra por palavra localizou a causa: as 3 frases soltas estavam LIMPAS; o
"Ponto." estava aos **7,88s da trilha MONTADA**, na pausa entre as frases 2
e 3 — **a contaminação entrou na montagem/junção da narração**, não nas
frases validadas.

**LIÇÃO PERMANENTE:** validar com ASR por palavra a **trilha MONTADA / o
export final, incluindo as pausas** — nunca só as linhas soltas. Montar
narração EXCLUSIVAMENTE de wavs de linha validados, posicionados com
**silêncio digital puro**; proibido usar narração contínua/intermediária
pré-juntada. Correção do teste: `voice/teste_video_voz_v3_corrigido.mp4`
(mesmos visuais, narração remontada dos 3 wavs limpos; varredura zerada).

**Redublagem entregue:** `~/workspace/homem_que_nao_existia/exports/`
`o_homem_que_nao_existia_voz_clonada.mp4` (67,9s; original gTTS preservado).
Método: segmentação anti-pontuação da v4 (`limpeza_texto.py`) + grade e
seleção objetiva da v3, síntese na GPU do PC dele. Cena 1 estendida +0,9s
(n1 não cabia a atempo ≤1,20). Amigo (d4) = mesmo clone com pitch +3
semitons, duração preservada (F0 141,5 Hz). Portão por palavra zerado em
todas as linhas E na varredura final do export (110 palavras, com pausas).
Relatório completo: `~/workspace/homem_que_nao_existia/qa/QA_voz_clonada.md`.

## Regra de uso
- Esta voz é a do **NARRADOR** em todo vídeo feito com a skill de terror —
  **somente quando a skill for acionada pelo gatilho "use a skill de terror"**.
  Fora desse gatilho, este clone não entra em nenhum outro projeto.
- Outros personagens (diálogos) usam processamento distinto sobre outra base —
  nunca esta voz sem diferenciação (na produção de 'O HOMEM QUE NÃO EXISTIA',
  o amigo teve pitch/ritmo próprios).
- Texto ao motor: somente `NARRACAO_FALADA` limpa e segmentada (ver
  `NARRACAO_TTS.md`); gerar teste curto e validar com ASR antes da narração
  completa de cada vídeo.

## Limitações reais
- **O usuário precisa validar o timbre ouvindo** os `teste_frase*.wav` — o
  agente não ouve o áudio; F0/ASR provam altura e texto, não identidade
  percebida.
- Síntese no CPU é lenta: ~15–45s por segmento curto (frase de teste completa
  ≈ 1–4 min, incluindo ~2 min de carga do modelo por processo).
- Resíduo do Demucs: acompanhamento a ≈ −51 dB pode deixar sopro ambiente
  mínimo na amostra; não foi detectado vazamento de SFX nos trechos escolhidos.
- A amostra de condicionamento tem taxa 44,1 kHz (stem do Demucs); as sínteses
  saem a 24 kHz (nativo do XTTS).
