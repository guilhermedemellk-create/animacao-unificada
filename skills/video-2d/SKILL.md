---
name: video-2d
description: >
  Skill 2D unificada (gatilho do usuário: "use a skill 2d"). Faz o vídeo 2D INTEIRO, do nicho à entrega:
  (1) ScriptForge (2D_Niche_Prompt_for_Claude.pdf) — seleção de nicho, 10 ideias e roteiro completo de
  narração 3–4 min com estrutura, estilo por nicho, títulos, thumbnail e tags; (2) GrowKaz Stickman Studio
  (GrowKaz_Stickman.plugin) — transforma a narração em vídeo animado stick-figure cinematográfico desenhado
  100% por código (Canvas + Three.js, frame a frame no Chromium headless, sem IA de imagem/vídeo):
  timestamps com Whisper, breakdown da história, 5 estilos visuais, construção de cenas, música e SFX
  gerados, mix a -14 LUFS e MP4 final em 16:9 ou 9:16, de 720p a 4K. SÓ usar quando o usuário mandar algo
  relacionado a "use a skill 2d"; nunca aplicar por padrão a outros vídeos ou projetos.
metadata:
  version: "1.0.0"
  trigger: "use a skill 2d"
---

# Skill 2D — do nicho ao vídeo inteiro (ScriptForge + GrowKaz Stickman)

## Gatilho e escopo (regra do usuário, 2026-11-07)
- Esta skill fica **apenas armazenada** e só é usada quando o usuário mandar algo relacionado a **"use a skill 2d"** (variações: "use skill 2d", "skill 2d"). Mesmo padrão das outras skills dele. **Não aplicar por padrão** a outros vídeos e projetos.
- Quando acionada, ela faz o **vídeo inteiro do jeito que ele pedir**: o pedido dele (tema, duração, formato, idioma, estilo) manda sobre qualquer padrão das fontes. Defaults servem só para o que ele não definir.

## As duas fontes (integrais, dentro desta pasta)
1. **ScriptForge** — `sources/2D_Niche_Prompt_for_Claude.pdf` (+ `.txt` extraído) e versão formatada em `references/scriptforge-niche-roteiro.md`. Cuida de: nicho → ideias → roteiro de narração.
2. **GrowKaz Stickman Studio** — plugin original em `sources/GrowKaz_Stickman.plugin` e extraído intacto em `growkaz-plugin/`:
   - `growkaz-plugin/skills/make-2d-video/SKILL.md` — pipeline completo (ler integralmente ao acionar)
   - `growkaz-plugin/skills/make-2d-video/references/` — `style-bible.md` (a bíblia do visual, ler inteira antes de desenhar qualquer cena), `story-breakdown.md`, `engine-api.md`, `sound-design.md`, `render-qc.md`, `install.md`
   - `growkaz-plugin/skills/make-2d-video/kit/` — o estúdio: renderer (`render.mjs`), engine (core/rig2d/fx2d/ui2d/styles/three-kit/player), tools (new_project, transcribe, parse_script, beats, doctor, verify_kit), áudio (music/sfx/mix/dsp) e o projeto-exemplo `examples/reaction-time`
   - Subcomandos do plugin (etapas isoladas, dentro de `growkaz-plugin/skills/`): `new-video` (etapas 1–4), `video-styles` (5), `render-video` (6 e 8), `video-sound` (7)

## O visual (GrowKaz, resumo — o detalhe obrigatório está no style-bible)
Stick figures pretos com **rim light** fina do lado da luz, em cenários vetoriais cinematográficos 2.5D de baixo contraste luminoso (sombras roxas/marinho, destaques âmbar, 1 fonte de luz forte por cena, poeira/chuva, profundidade com camadas borradas), closes gigantes de rosto (`bigFace`), momentos freeze-frame "tempo parado", números/gráficos animados sincronizados à fala, diagramas blueprint azul-marinho, e tomadas 3D low-poly em órbita (Three.js). Cada quadro é código — personagens consistentes e texto sempre nítido. Estilos prontos: **emerald** (padrão GrowKaz), **ember**, **arctic**, **sakura**, **retro** (+ customizados via `engine/styles.js`).

## Fluxo completo (quando ele pede o vídeo inteiro)

### Fase A — Nicho, ideia e roteiro (ScriptForge)
- Se ele **já trouxer tema/roteiro/narração prontos**, pular esta fase e ir direto à Fase C/D com o material dele.
- Se ele quiser escolher: Passo 1 (menu de 5 nichos × 5 subnichos, ou subnicho próprio) → Passo 2 (exatamente 10 ideias, título <60 caracteres + hook de 1 linha) → Passo 3 (roteiro 450–600 palavras, 3–4 min, no estilo de narração do nicho; estrutura HOOK 0:00–0:15 / SETUP 0:15–0:40 / CORPO 0:40–3:00 com 3–5 beats escalando / PAYOFF 3:00–3:30 / OUTRO 3:30–4:00; formato com timestamps, [NARRATION] e [VISUAL]; fechar com 3 títulos alternativos, texto de thumbnail de 2–4 palavras, 5 tags, contagem de palavras e duração estimada).
- Regras ScriptForge: fatos precisos, nunca inventar estatística/citação/estudo; escrever para o ouvido; psicologia/manipulação sempre como consciência/autoproteção.
- Duração/formato diferentes do padrão 3–4 min (ex.: Shorts de 60s) seguem o pedido dele, mantendo a estrutura proporcional.

### Fase B — Narração (áudio)
- O pipeline GrowKaz parte de um **arquivo de narração (voiceover)**. Se ele enviar o áudio, usar como está: **nunca reescrever, adicionar, cortar ou reordenar palavra falada** (regra de ouro 1 do GrowKaz).
- Se só houver roteiro, gerar a narração com o TTS disponível no ambiente (texto falado limpo, sem pronunciar pontuação; testar trecho curto antes da narração completa) ou pedir o áudio a ele se nenhuma voz servir. Voz clonada só com autorização registrada, como nas outras produções dele.

### Fase C — Instalação do estúdio (uma vez por máquina/workspace)
Seguir `growkaz-plugin/skills/make-2d-video/references/install.md`:
- Copiar `growkaz-plugin/skills/make-2d-video/kit/` para `growkaz-stickman-studio/` no workspace do projeto (nesta VM: `~/workspace/growkaz-stickman-studio/`; no PC dele: dentro de `E:\muse ia\`). Nunca sobrescrever `projects/` existente.
- `python tools/verify_kit.py` tem que dar **29/29**. Depois instalar: ffmpeg, pacotes Node (`npm install`: renderer, Three.js, fontes), Chromium headless (`npx playwright install chromium`) e Python `numpy scipy faster-whisper`; rodar `python tools/doctor.py` até tudo OK e o autoteste do exemplo (`node render.mjs --project examples/reaction-time --sheet --scale 0.3` → 14 quadros, sem erros).
- Estado verificado nesta VM em 2026-11-07: Node 24, Python 3.12, ffmpeg 8.1.2, numpy/scipy presentes; **faltam** faster-whisper, `node_modules` e o Chromium do Playwright (instalam na primeira produção, ~1 GB no total).

### Fase D — Projeto e timeline
- `python tools/new_project.py --name <slug> --voice "<narração>" [--script "<roteiro>"] --aspect <16:9|9:16> --resolution <720p|1080p|1440p|2160p> --title "<título>" [--captions]`
- Roteiro com timestamps → `parse_script.py`; roteiro puro → `transcribe.py --script` (exige match ≥90%); sem roteiro → `transcribe.py` (Whisper; modelo baixa na 1ª vez). Conferir `timeline/transcript.txt` e rodar `beats.py` (gera o rascunho de `story/shots.json`).
- Defaults GrowKaz: 1080p, 24 fps, música gerada + SFX, estilo emerald, legendas queimadas ligadas no 9:16 e desligadas no 16:9 — tudo cede ao pedido dele (o padrão dele em Shorts é 9:16 1080x1920).

### Fase E — Breakdown da história
Ler `style-bible.md` + `story-breakdown.md` inteiros. Escrever `story/bible.md` (logline/tom, elenco com **uma cor-assinatura saturada por personagem**, locações com mood/luz/props, motivos, plano de música), `scenes/cast.js` e reescrever `story/shots.json`: tomadas contíguas, corte 0,1–0,2s antes da frase, mediana de 2–3,5s, **15–25 tomadas/min**, shot de abertura para cada locação nova, descrição concreta de cena por tomada. Resumo de 5–10 linhas para ele e seguir (autonomia dele: não travar esperando aprovação do que já foi pedido).

### Fase F — Estilo
Montar os 1–2 cenários mais usados + 3 tomadas representativas (plano aberto com ≥2 personagens, close `bigFace`, tomada de dados/blueprint ou 3D) e renderizar a grade:
`node render.mjs --project projects/<slug> --styles emerald,ember,arctic,sakura,retro --at <t1>,<t2>,<t3> --scale 0.5`
Mostrar a grade (`build/styles/style_grid.png`) com 1 linha por estilo e gravar a escolha em `config.json`. Se ele não estiver presente/respondendo, usar o padrão (emerald ou o que combina com o tema) declarando o assumido e continuar.

### Fase G — Construção das cenas (lotes de 8–12 tomadas)
Ler `engine-api.md` e os exemplos em `examples/reaction-time/scenes/`. Para cada lote: escrever `scenes/sets/<locação>.js` e `scenes/shots/NN_<nome>.js` (`registerShot`), rodar `node render.mjs --project projects/<slug> --sheet --scale 0.5`, **abrir todas as folhas de contato** e corrigir contra o checklist de QC (`render-qc.md`) — nada de render completo com tomada MISSING/ERROR. Checar movimento com `--stills` ou preview parcial.
Innegociáveis do style-bible: rim light em toda figura iluminada; cores só de `mood()`/`S()` (nada hard-coded); **câmera se move em toda tomada**; atmosfera (poeira/chuva/brilhos); estrutura de valores moody (60–75% tons escuros, 1–3 acentos brilhantes); gráficos sincronizados à palavra com `wordTime()`; `V()` em todo valor dependente do formato; **proibido `Math.random`/`Date.now`** (usar `rng(seed)` e `t`); figura sempre no chão com sombra de contato; no máximo ~4 personagens em foco; no 9:16, rostos/textos na área segura central e legendas a ~79% da altura.

### Fase H — Som
Ler `sound-design.md`. Preencher `music` em `shots.json` (seções contíguas por mood — mystery, tension, action, wonder, hopeful, sad, triumph, playful, calm, dark, epic — trocando nas viradas da história, a cada 30–90s) e os cues de SFX/ambiência por tomada (biblioteca de 36 efeitos em `audio/sfx.py`; convenções: whoosh em movimento rápido, pop/blip quando gráfico entra, riser→impact/stinger na revelação, freeze no tempo parado; no máx. ~2 cues no mesmo instante). Trilha própria dele entra via `config.music.file`; sem música, `enabled: false`.

### Fase I — Render, mix e entrega
Ler `render-qc.md`.
1. Preview: `node render.mjs --project projects/<slug> --from 0 --to 30 --scale 0.5` → mostrar preview/folha de contato antes do render longo, com a estimativa de tempo (guia: ~2 fps em 720p numa CPU fraca de 2 núcleos; 1080p ≈2×, 4K ≈8×; desktop moderno 3–5× mais rápido).
2. Render final: `node render.mjs --project projects/<slug>` (em segundo plano se for longo, acompanhando o log com fps/ETA). Sai `build/video_silent.mp4`, sem erros de tomada.
3. Mix: `python audio/mix.py --project projects/<slug>` — gera música/SFX, ducking (−9 dB música, −5 dB ambiência sob a voz), normaliza a **−14 LUFS** e muxa `out/<título>.mp4`.
4. **QA obrigatório antes de declarar pronto** (padrão dele): ffprobe (duração ≈ shots.json, áudio presente) + folha de contato do arquivo final (1 quadro a cada 10s) inspecionada + checklist de QC inteiro. Entregar o MP4 anexado, com specs e ressalvas honestas — só o que foi realmente testado.

## Regras permanentes dele que valem nesta skill
- **Caminho mais rápido:** render frame a frame é pesado — preferir o PC dele (SSH/Tailscale, pasta `E:\muse ia`) quando ele estiver acessível e for mais rápido; **avisar sempre** quando estiver usando o PC dele ou quando não conseguir conectar.
- **Autonomia:** executar o que ele pediu sem pedir aprovação a cada etapa; falar com resultado ou problema real. Os "checkpoints" do GrowKaz (setup, estilo, preview) viram entregas mostradas a ele, não bloqueios — sem resposta, valem os defaults declarados.
- Conversa em **pt-BR**; o idioma do roteiro/narração segue o pedido dele para cada vídeo.
- Correção localizada: corrigir só a tomada/trecho com problema e re-renderizar o menor intervalo possível, sem recomeçar o vídeo inteiro.
