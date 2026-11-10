# canal-dark-youtube

Skill para criar e operar um canal dark de curiosidades no YouTube, no padrão das skills do GitHub (SKILL.md + skill.yaml + referências).

## O que ela faz

- Pergunta antes de tudo se você já tem nome para o canal: se não tiver, mostra os estilos e cria 5 nomes novos verificados no YouTube de acordo com o estilo escolhido, sem repetir nomes de outros chats. O estilo escolhido decide o formato, a voz, a thumbnail e os títulos. Depois entrevista sobre plataforma (TikTok, YouTube longo ou YouTube Shorts), duração, promessa, formato, a decisão entre vídeo realista, 3D estilo Pixar por IA, 3D por código ou infográfico 2D por código que muda o rumo da animação, voz (1 dos 26 estilos, com a opção "Não entendi"), origem da voz com o gerador de voz da skill, legenda karaokê automática e frequência. Gera vídeos realistas como padrão.
- Estuda os concorrentes do nicho, com uma biblioteca de 52 canais dark: 16 brasileiros e 36 do mundo, cada um com ficha completa.
- Escreve roteiro com hook de 30 segundos, capítulos, fontes e tela final, e quebra o roteiro em storyboard cena a cena.
- Anima de verdade nas quatro trilhas, realista por IA, 3D estilo Pixar por IA, 3D por código com Blender e Python, ou infográfico 2D por código com Python e PIL, com os 12 princípios da animação, a doutrina de movimento profissional, gestos, ritmo de 4 tempos por clipe, receitas de cena e o teste do mudo. O estudo de caso da trilha 2D é o vídeo 1 do O Laboratório Curioso.
- Produz narração e visual na rota escolhida, monta o vídeo final com ffmpeg, sincronia de áudio por cena e legenda automática queimada, cria título e thumbnail com 23 fórmulas, e publica com descrição, tags e Short, ou no TikTok com capa e hashtags.
- Traz 300 ideias de vídeo prontas e 5 formatos além da lista de 10.

## Como usar

Chame a skill só de um jeito: com $ na frente. Sem o $ é só uma mensagem normal e a skill não ativa.

- `$canal-dark` — o comando principal, com cifrão.

Digite o comando seguido do que você quer:

- `$canal-dark` — mostra os canais criados para escolher qual continuar, ou começa a entrevista do zero para criar um canal novo.
- `$canal-dark quero um vídeo novo` — começa a entrevista com o pedido já dado.
- `$canal-dark cria um vídeo sobre mistérios` — começa com o tema já escolhido.

A skill pergunta o que falta e salva suas respostas num perfil do canal. Para instalar, copie a pasta `canal_dark_youtube` para o diretório de skills do seu agente (por exemplo `~/workspace/custom-skills/`).

## Comandos

Use um comando para ir direto ao trabalho, sem refazer a entrevista:

- `$canal-dark` — começa a skill e mostra os canais criados para escolher qual continuar, ou começa a entrevista de abertura para um canal novo. Exemplo: `$canal-dark quero um vídeo novo`.
- `$canais` — mostra os canais criados na máquina, com nome, @, nicho e plataforma de cada um e qual é o ativo, e deixa trocar o perfil ativo. Exemplo: `$canais` quando você quer continuar outro canal.
- `$help` — mostra a lista de todos os comandos com uma explicação curta de cada um. Funciona a qualquer momento, sem começar a entrevista e sem apagar o que já foi feito. Exemplo: `$help` no meio de um roteiro.
- `$ideias` — mostra ideias de vídeo para o canal, sem começar tudo de novo. Usa o perfil salvo e o nicho do canal. Quando você pedir mais ideias aqui, ela gera 5 ideias novas sem repetir as já mostradas. Exemplo: `$ideias` depois de terminar um vídeo.
- `$nomes` — mostra 5 nomes novos de canal, sem repetir os já sugeridos. Usa as fórmulas de `references/nomes.md` e o registro em `~/workspace/your_files/canal-dark-nomes-usados.md`. Exemplo: `$nomes` quando você não gostou dos 5 nomes mostrados.
- `$roteiro` — escreve o roteiro do próximo vídeo do canal que já existe, usando o perfil salvo. Se não houver perfil salvo, a skill diz que falta a entrevista e oferece começar com `$canal-dark`. Exemplo: `$roteiro sobre mistérios do Brasil`.
- `$revisar` — diagnostica o roteiro aprovado antes de produzir. Exemplo: `$revisar` depois de aprovar o roteiro.
- `$storyboard` — monta o storyboard do roteiro aprovado, com 1 cena por clipe de cerca de 10 segundos, antes de qualquer render ou geração. Exemplo: `$storyboard` depois de aprovar o roteiro.
- `$personagem` — cria a ficha do personagem ou mascote para manter ele igual em todos os clipes. Exemplo: `$personagem` antes de gerar o primeiro clipe.
- `$teste` — produz 1 clipe de teste com 1 cena do storyboard para aprovar visual, movimento e voz antes do vídeo inteiro. Exemplo: `$teste` depois de aprovar o storyboard.
- `$thumbnail` — cria título e thumbnail de um vídeo, ou capa no TikTok, seguindo `references/titulo-thumbnail.md`. Exemplo: `$thumbnail` depois de aprovar o roteiro.
- `$publicar` — guia a publicação e a medição do vídeo: título, descrição, tags, visibilidade, tela final e o que medir depois. Exemplo: `$publicar` quando o vídeo final está pronto.
- `$status` — mostra o perfil do canal salvo e o que já foi feito: vídeos prontos, roteiros escritos e ideias usadas. Exemplo: `$status` quando você volta depois de dias sem abrir o chat.
- `$voz` — escolhe e testa a voz da narração, com os 26 estilos, os áudios de amostra de cada voz e a opção "Não entendi". Exemplo: `$voz` antes de gerar a narração.
- `$legenda` — escolhe o estilo da legenda karaokê e confere a legenda queimada no vídeo. Exemplo: `$legenda` quando a legenda ficou pequena no Short.
- `$capa` — cria a capa do vídeo vertical para TikTok e Shorts. Exemplo: `$capa` depois de aprovar o vídeo vertical.
- `$musica` — escolhe a música do vídeo. Os efeitos sonoros ficam com `$efeitos`. Exemplo: `$musica` quando o vídeo é de terror.
- `$plano` — mostra o plano dos 10 primeiros vídeos e onde o canal está. Exemplo: `$plano` no começo da semana.
- `$concorrentes` — estuda os concorrentes do nicho antes do roteiro. Exemplo: `$concorrentes` antes do vídeo 1.
- `$referencia` — disseca um vídeo de referência quadro a quadro antes de produzir. Exemplo: `$referencia` com o link do vídeo de referência.
- `$titulo` — gera 5 opções de título para um vídeo, com a melhor aposta marcada. Exemplo: `$titulo` quando o roteiro está pronto.
- `$short` — adapta um vídeo longo do YouTube para Short. Exemplo: `$short` depois de publicar o vídeo longo.
- `$stats` — mede o resultado dos vídeos publicados e diz o que mudar no próximo. Exemplo: `$stats` depois de uma semana no ar.
- `$monetizar` — confere se o canal já pode monetizar no YouTube e o que falta para liberar. Exemplo: `$monetizar` depois dos 10 primeiros vídeos publicados.
- `$logo` — cria a logo do canal a partir do perfil salvo. Exemplo: `$logo` depois da entrevista.
- `$banner` — cria a arte do banner 2560x1440 do canal no YouTube. Exemplo: `$banner` antes de publicar o primeiro vídeo.
- `$descricao` — escreve ou reescreve a descrição do canal. Exemplo: `$descricao` quando o nicho muda.
- `$gancho` — gera 5 opções de gancho para um vídeo, no tamanho da plataforma. Exemplo: `$gancho` antes de escrever o roteiro.
- `$agenda` — monta o calendário de postagens com data e prazo de cada entrega. Exemplo: `$agenda` no começo da semana.
- `$nicho` — troca o nicho do canal sem trocar o nome. Exemplo: `$nicho` quando o canal muda de tema.
- `$serie` — planeja uma série de vídeos sobre um tema, com arco e ordem dos episódios. Exemplo: `$serie` para um tema grande.
- `$audio` — revisa o áudio de um vídeo pronto. Exemplo: `$audio` antes de publicar.
- `$efeitos` — monta o banco de efeitos sonoros do vídeo. Exemplo: `$efeitos` quando o roteiro está pronto.
- `$intro` — cria a intro e o outro do canal. Exemplo: `$intro` quando o canal ainda não tem abertura.
- `$checklist` — roda o checklist de pré-publicação do vídeo. Exemplo: `$checklist` antes de subir o vídeo.
- `$corrigir` — corrige um problema específico do vídeo pronto sem refazer o vídeo inteiro. Exemplo: `$corrigir` quando o áudio ficou fora de sincronia.
- `$tema` — pesquisa um tema a fundo antes do roteiro. Exemplo: `$tema` quando o tema é novo para o canal.
- `$fontes` — verifica as fontes dos fatos do roteiro. Exemplo: `$fontes` quando o roteiro está pronto.
- `$template` — cria o template fixo do vídeo do canal. Exemplo: `$template` quando o canal vai gravar o vídeo 1.
- `$backup` — faz o backup dos arquivos do canal. Exemplo: `$backup` no fim da semana.
- `$automatizar` — liga a automação de conteúdo do canal e produz e posta os vídeos da fila no calendário, com a fila, a agenda, o pipeline e as regras de falha em `references/automacao.md`. Exemplo: `$automatizar` na manhã do dia da postagem.
- `$portoes` — roda todos os portões de qualidade de uma vez no vídeo final e devolve aprovados e reprovados com o número de cada um. Exemplo: `$portoes` com o vídeo final pronto, antes de entregar.
- `$varredura` — roda o blackdetect e o freezedetect no vídeo final e devolve os trechos com problema e o LUFS medido. Exemplo: `$varredura` com o vídeo final pronto, antes de entregar.

A lista completa de comandos, com quando usar cada um, exemplo e quando ele não serve, está em `references/comandos.md`.

## Estrutura

- `SKILL.md` — as instruções da skill.
- `skill.yaml` — nome, título e descrição.
- `references/perguntas-iniciais.md` — a entrevista de abertura.
- `references/comandos.md` — a lista completa de comandos da skill, com o que cada um faz, quando usar, exemplo e quando ele não serve.
- `references/perfis.md` — vários perfis de canal na mesma skill, com o diretório de perfis, o perfil ativo, o apontador e o comando `$canais`.
- `references/automacao.md` — o guia geral de automação de conteúdo para qualquer canal, com configuração guiada, modelos de agenda, postagem por plataforma, checklist antes de postar, teste de postagem e solução de problemas.
- `references/nomes.md` — do estilo ao nome do canal, com 21 estilos e fórmulas para criar 5 nomes novos verificados no YouTube a cada chat.
- `references/vozes.md` — os 26 estilos de voz, com nicho e canal modelo de cada um, a explicação do "Não entendi" e a origem da voz.
- `references/gerador-voz.md` — o gerador de voz da skill, com uma passada suave, voz fixa, escolha da voz por estilo e o guia do ElevenLabs.
- `references/series.md` — séries com voz por personagem, com a parte de 60 segundos, a bíblia da série, o elenco de vozes, diálogo contra narração e o roteiro com falas marcadas.
- `references/logo.md` — a logo do canal, com estilo por nicho, paleta e foto de perfil.
- `references/legendas.md` — legenda karaokê automática queimada no vídeo, com estilo, tempo por palavra e ffmpeg.
- `references/canais-dark-brasil.md` — 17 canais dark brasileiros com ficha completa e correções de premissa.
- `references/canais-dark-mundo.md` — 36 canais dark do mundo, em inglês e espanhol, com ficha completa.
- `references/estilos-visuais.md` — realista, Pixar 3D por IA, Blender 3D, infográfico 2D por código, ou imagem estática.
- `references/animacao.md` — animação de verdade, com as quatro trilhas, os 12 princípios da animação, ritmo do clipe, receitas de cena, o teste do mudo e o checklist por clipe.
- `references/movimento-profissional.md` — a doutrina de movimento profissional, com lei do vetor, carriers, arquétipos com números, os 12 princípios como lente de revisão e receitas GSAP.
- `references/revisar-roteiro.md` — o diagnóstico de roteiro antes de produzir, com as 4 assinaturas de falha, cut points e orçamento de palavras.
- `references/referencia.md` — o método para dissecar um vídeo de referência quadro a quadro, com probe, cortes, frames consecutivos, camadas e diff.
- `references/estudo-caso-laboratorio-curioso.md` — estudo de caso do vídeo 1 do O Laboratório Curioso, a trilha do infográfico 2D por código, com paleta, pipeline, números medidos e as lições da sincronia.
- `references/storyboard.md` — do roteiro à animação cena a cena, com exemplo e template.
- `references/ambientacao.md` — um ambiente por capítulo, com a regra das 3 camadas.
- `references/audio.md` — narração, efeitos, música, mixagem e volume.
- `references/montagem.md` — do clipe solto ao vídeo final, com ffmpeg, a regra de sincronia de áudio por cena, volume e upload no YouTube e no TikTok.
- `references/portoes-qualidade.md` — os portões de qualidade e o checklist de entrega por etapa.
- `references/titulo-thumbnail.md` — 23 fórmulas de título, regras de thumbnail e Test & Compare, e capa do TikTok e do Short.
- `references/erros-comuns.md` — 89 lições aprendidas com erros que já aconteceram.
- `references/ideias.md` — 300 ideias de vídeo, 5 formatos e retenção 2026.
- `references/livros.md` — 68 livros verificados com ano, fonte e aplicação prática, mais retenção e algoritmo 2026, design de som e teoria das cores.
- `references/plano-10-videos.md` — o plano dos 10 primeiros vídeos.
- `references/bibliotecas-3d.md` — bibliotecas 3D gratuitas baixadas, com licenças e importação no Blender.
- `references/videos-referencia.md` — vídeos de referência para estudar, um por nicho.
- `amostras-voz/` — áudios de amostra das 26 vozes, nas duas frases padrão, "Você sabia que a Lua está fugindo da Terra?" e "Melhor desenvolvedor é o Brigueli", gerados localmente. Os áudios não vão para o GitHub: a skill gera as amostras de novo com o comando documentado em `references/gerador-voz.md` quando elas faltam.
