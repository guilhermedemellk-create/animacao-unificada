---
name: fabrica-videos
description: Fluxo "fábrica de vídeos" do canal do ENZO (adotado em 2026-11-06 a partir do vídeo "Criei uma fábrica de vídeos com IA em 10 minutos"). Pipeline repetível tema→vídeo publicado: referência visual, roteiro de retenção, narração will por registros, cenas aiTrends 2D/2.5D com regras de POV, legendas palavra por palavra, QC de quadros, render no Mac e pacote de publicação (título + hashtags). Usar sempre que o ENZO pedir um vídeo novo do canal.
---

# Fábrica de Vídeos — fluxo padrão do canal

Um tema entra, um vídeo pronto pra postar sai. Não reinventar o formato a cada vídeo: este fluxo É o formato. Desvios só por ordem explícita do ENZO.

## Etapas

1. **Tema e referência** — o ENZO dá o tema (ou aprova sugestão). Se ele mandar referência visual (vídeo, quadro, folha de modelo), a referência manda: adotar verbatim e mostrar no próximo output.
2. **Roteiro de retenção** — curto, episódio independente, segunda pessoa, 40–70 s de narração (~110–175 palavras). Usar um dos DOIS MODELOS do vídeo-fonte:
   - **Modelo história**: uma pergunta muito impactante que martela na mente do espectador e **só é respondida no final**.
   - **Modelo por etapas**: premissa forte + etapas em sequência, cada uma puxando a próxima, pra viciar até o fim.
   Sem ideia? Escolher o modelo e pedir ideias de histórias ("E se...?") antes de escrever. Ação concreta, sem final filosófico/moral em roteiro de luta. Números por extenso, anos em dígitos, só reticências e pontos como pausa. Marcar os registros de voz no roteiro: [CONVERSA] abertura/fecho, [NARRADOR] desenvolvimento, [SUSSURRO] batida de perigo/suspense.
3. **Narração** — voz will clonada, VoiceStudio no MacBook (perfil `afe1dbfa`, OmniVoice), gerada em blocos por registro. Sussurro: 3 tomadas, entra a mais baixa, tratamento −5,5 dB + EQ próximo (método aprovado no teste D. B. Cooper). Alinhamento palavra por palavra pras legendas. **Pilotos e conceitos novos: montar primeiro com voz de MARCAÇÃO local (Piper) pra aprovar o visual; a voz will final só é gerada depois do conceito aprovado** (economia de geração no Mac — é a ordem do vídeo-fonte: marcação → aprova a cena → voz profissional → sincroniza).
4. **Cenas (aiTrends 2D Studio)** — vertical 1080×1920, estilo golden (luz dourada, poeira, vinheta). Maioria 2D com fatia generosa de 2.5D (camadas com parallax + push-in). Herói = família visual do Caio. Regras de cena do ENZO:
   - **Painel do sistema e lutas = visão do herói (POV)**, não do narrador: painel flutua na altura dos olhos dele; luta em primeira pessoa com o slime/monstro vindo pra câmera.
   - **Braço em POV é cadeia ancorada**: ombro fixo fora de quadro, dois ossos com cotovelo (IK), sem teleporte de mão — interpolação contínua, objeto pego sobe grudado na mão.
   - **Gosma/sangue de verdade**: corpo gelatinoso com wobble e squash de impacto; estouro com fios, gotas, poça persistente. Quem se suja fica sujo: manchas desenhadas na roupa e no corpo, persistentes até o fim do vídeo (nada de bolinha simbólica). Em luta com corte, os dois lados sangram e a marca continua.
   - Nada de elemento aleatório fora do roteiro.
5. **Legendas** — palavra por palavra, maiúsculas, fonte pesada sem serifa, branco com contorno preto, palavras-chave em amarelo.
6. **QC antes de entregar** — ffprobe (duração/resolução) + quadros extraídos do MP4 final conferidos nos momentos críticos (painel, luta, sujeira, POV). Nunca entregar sem conferir os quadros.
7. **Render** — no MacBook (caffeinate ligado, não atrapalhar outras produções), master 1080×1920 + cópia leve 720×1280 pra tocar no chat.
8. **Pacote de publicação** — entregar junto: título pronto pra colar + hashtags. (Postagem no TikTok/YouTube é manual pelo ENZO ou via navegador com login dele — não há conector nativo de TikTok.)

## Formatos derivados
- **Documentário dossiê** (Guerra Fria, JFK, PGM): mesmo fluxo, cenas estilo dossiê (documentos, mapas, foto cards de arquivo com licença conferida), duração livre conforme o pedido.
- **Série em partes** (isekai Leo & Aria): manter personagens e ganchos de continuação entre episódios.
- Formato novo que se repetir vira **skill própria** (uma por formato), como no vídeo-fonte.

## REGRA DE OURO (do vídeo-fonte)
**Toda correção do ENZO — e todo acerto confirmado — é anotada nesta skill (ou na skill do formato) na mesma hora.** A skill é o manual que impede o erro de se repetir: braço em POV que descola, bolinha no lugar de mancha, painel fora da visão dele — corrigiu uma vez, entra na regra e nunca mais volta. Sem essa anotação, a entrega não está completa.
