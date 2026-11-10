# Estilos visuais — realista, Pixar 3D por IA, Blender 3D, infográfico 2D ou imagem estática

O usuário escolhe o estilo na entrevista de abertura. Não produza visual antes dessa escolha. Cada rota tem custo e tempo diferentes e nenhuma serve para tudo.

## 1. Vídeo realista gerado por IA

- Como é: clipes curtos gerados por IA com visual de cinema, pessoas e lugares realistas.
- Ferramenta: geração de vídeo por IA com a ferramenta disponível no momento, depois de ler o documento do conector e verificar o saldo de créditos. O conector Runway não está conectado, então não gere nada com Runway até conectar a conta.
- Custo: cada clipe custa créditos e dura cerca de 10 segundos. Um vídeo de 13 minutos precisaria de dezenas de clipes.
- Quando usar: cenas que não existem em arquivo, como um lugar inacessível ou uma reconstrução.
- Limite: o Lorenzo rejeitou o clipe de teste de IA do Tuto por realista demais. Para canal de animação, esse estilo quebra a identidade visual.
- Risco: declare imagem gerada por IA na thumbnail quando não for foto real do fato.
- Monte o prompt na ordem meio, plano, ângulo, movimento, foco, assunto, luz e cor, com 60 a 140 palavras por clipe. Use I2V motion-first com prompt curto de 25 a 70 palavras quando existir imagem inicial aprovada. Leia a fórmula e o aceite completo em [animação](animacao.md), na seção da trilha realista.
- Aprove o still de cada beat antes de animar e siga a cadeia ficha, image-ref e start-frame. Compare o clipe novo com o anterior lado a lado e aplique a regra das 3 tentativas.

## 2. Animação 3D low-poly por código com Blender e Python

- Como é: cenas 3D low-poly modeladas por código, no estilo do Desconstruindo Universo. O boneco, o cenário e a câmera são todos desenhados por um script Python.
- Ferramenta: Blender 4.5.3 LTS portátil em `~/workspace/tools/blender-4.5.3-linux-x64/`. O `bpy` só funciona dentro do Blender com `blender -b --python cena.py`.
- Pipeline: roteiro, storyboard em texto com 1 cena igual a 1 clipe de cerca de 10 segundos, um script `.py` por cena com primitivas low-poly, boneco com pivôs, keyframes e câmera com TRACK_TO, render Cycles CPU em 480x854 com 6 samples e sem denoise em PNGs, ffmpeg monta o MP4, sobe para 720x1280 e junta com a narração.
- Custo real medido: cerca de 5 segundos por frame, cerca de 20 minutos por clipe de 10 segundos, cerca de 2 horas por Short de 60 segundos, em lote e sem supervisão.
- Limite: o Eevee não funciona nesta máquina porque falta libEGL. Não prometa render rápido por Eevee. Não renderize em paralelo, a RAM livre é de cerca de 480 MB. Renderize sempre em PNGs e nunca em MP4 direto do Blender, para retomar do frame onde parou.
- Quando usar: quando o usuário quer o vídeo todo animado, com identidade visual própria e sem depender de crédito de IA.
- Use para explicar construção e engenharia passo a passo, com a montagem peça por peça da seção de montagem passo a passo em [animação](animacao.md).
- Monte cada cena com 1 script por cena, rig de pivôs, keyframes nas poses extremas e câmera com TRACK_TO. Confira a ação pronta da biblioteca no frame de teste antes do render.
- Aplique o checklist de aceite da trilha em [animação](animacao.md), na seção da trilha 3D por código, antes do render completo de cada cena.
- Use as animações prontas da biblioteca quando o gesto já existir. Os 5 personagens KayKit Adventurers trazem 76 animações cada e os 4 esqueletos KayKit trazem 95 animações cada, medidas na importação de teste em 06/11/2026 no Blender 4.5.3. Leia como aplicar as ações no Blender em [animação](animacao.md).
- Guia completo: `~/workspace/research_notes/animacao-codigo-blender-2026-11-05.md` e a seção de animação por código em `~/workspace/custom-skills/videos_animados_como_funciona/SKILL.md`.
- Cena real de exemplo: `~/workspace/your_files/tuto-lowpoly-codigo/render_blender.py`. Template de exemplo: `~/workspace/tools/blender-exemplo/cena_peixe_10s.py`.

## 3. Infográfico 2D por código com Python e PIL

- Como é: motion graphics 2D infográfico desenhado por código, no estilo do vídeo 1 do O Laboratório Curioso. Diagramas, mapas, números grandes animados, carimbos de VERDADE e MENTIRA, painéis e grades. Sem apresentador, sem boneco e sem caixa 3D.
- Ferramenta: Python com PIL 10.2.0 e numpy, e ffmpeg. Um script `render_cenaNN.py` por cena, com biblioteca partilhada `lib_info.py`.
- Pipeline: roteiro, storyboard em texto com 1 cena igual a 1 diagrama, um script por cena que desenha os frames em PNG a 60 fps, com 40 fps como mínimo aceitável, ffmpeg monta o MP4 de cada cena, concatena todas as cenas, queima a legenda com o filtro `subtitles` e junta a narração.
- Custo real medido: a cena 1 de teste rendeu 240 frames em 10,4 segundos. As 72 cenas do vídeo 1 levaram de 20 a 30 minutos no total. É cerca de 50 vezes mais rápido que o Blender.
- Paleta do exemplo: fundo #1A305A, painel #264476, linhas #8FB4E3, texto branco, laranja #FF8C1A, azul-aço #6EA8DC. Cores proibidas no exemplo: vermelho, amarelo e verde.
- Limite: não serve para mostrar pessoas de verdade nem para um mascote apresentador. Texto e números saem exatos, porque são desenhados por código, e não gerados por IA.
- Quando usar: quando o usuário quer o vídeo todo animado com diagramas, mapas e números grandes, sem depender de crédito de IA e sem esperar horas de render. Quando o tema é ciência, história ou espaço.
- Estudo de caso completo: [estudo de caso do Laboratório Curioso](estudo-caso-laboratorio-curioso.md).
- Anime cada diagrama com as receitas de [animação](animacao.md), na seção da trilha 2D por código, com o número contando com easing e o carimbo caindo no segundo da palavra.
- Aplique o checklist de aceite da trilha em [animação](animacao.md) antes do render completo de cada cena.
- Exemplo real: `~/workspace/your_files/video-1-laboratorio-curioso/video-1-final.mp4`, 11 minutos e 20 segundos, 72 cenas, 1280x720.

### 3b. Histórias 2D por código com renderFrame(n) e render.mjs

- Como é: a variante de histórias da trilha 2D. A cena é uma página HTML com uma função `renderFrame(n)` que desenha o quadro n, e o `render.mjs` fotografa cada quadro num Chromium sem tela. Protagonista fixo, 4 estilos de quadros de movimento, formato mãe vertical 1080x1920 e as regras do movimento profissional.
- Ferramenta: `~/workspace/tools/renderizador-cdp/render.mjs`, sem pacote npm, com Node 22 ou mais novo e o Chromium da imagem da máquina. O guia completo, com os 4 estilos, as regras do movimento, o formato interativo e o pipeline, está em [quadros de movimento](quadros-movimento.md).
- Custo real medido em 06/11/2026: 11,20 quadros por segundo em 1280x720 em JPEG e 9,82 quadros por segundo em 1080x1920 vertical em JPEG. Um Short vertical de 60 segundos em JPEG leva cerca de 6,1 minutos de render a 60 fps e cerca de 4,1 minutos a 40 fps. O padrão é 60 fps, com 40 fps como mínimo aceitável.
- Quando usar: quando o vídeo é uma história animada narrada, uma história interativa com escolha no final ou um vídeo vertical curto, com protagonista fixo e texto grande na tela.
- Limite: o render é mais lento que o PIL e o HTML não desenha diagrama com geometria exata por coordenadas. Para diagrama e mapa, use a opção A, o PIL. Nunca misture as duas opções no mesmo vídeo.
- Aplique as receitas GSAP e o portão de vídeo estático de [quadros de movimento](quadros-movimento.md), com micro-evento a cada 0,5 a 1,5 segundo e 3 segundos sem mudança reprovando a cena.
- Confira o checklist da cena de história em [quadros de movimento](quadros-movimento.md) antes de renderizar a cena completa.

## 4. Animação 3D estilo Pixar por IA

- Como é: clipes curtos gerados por IA com animação 3D estilo Pixar, personagens estilizados de olhos grandes, luz de cinema e cenários detalhados. O modelo é o Crânio Era, @cranioera no TikTok, com a série História do Tomate em 12 episódios, protagonista fixo e cliffhanger por parte.
- Ferramenta: geração de vídeo por IA, com o mesmo método da trilha realista e o visual Pixar no prompt, com a ficha do personagem e o bloco de estilo copiados em todos os prompts.
- Pipeline: bíblia da série, roteiro por parte com o cliffhanger já no fim, narração antes dos clipes, storyboard com 1 cena igual a 1 clipe de cerca de 10 segundos, 6 clipes por parte de 60 segundos, montagem com os tempos reais da narração, áudio completo a -14 LUFS e legenda karaokê queimada.
- Custo: cada clipe custa créditos e dura cerca de 10 segundos. Uma parte de 60 segundos precisa de cerca de 6 clipes. Duas partes por dia precisam de cerca de 12 clipes por dia. Some os créditos antes de prometer a frequência.
- Quando usar: história seriada com protagonista fixo, drama em partes com cliffhanger, terror e histórias em capítulos, como o Terror da Meia-Noite.
- Limite: a continuidade é o maior desafio. O personagem muda de rosto e de roupa se a ficha não for copiada em todos os prompts. Nunca misture clipe realista com clipe Pixar no mesmo vídeo. Não serve para diagramas e números exatos, porque a IA não acerta texto e números.
- Exemplo real: o clipe de teste do Terror da Meia-Noite, 10 segundos em 720x1280, relógio marcando meia-noite e porta se abrindo sozinha, aprovado pelo Lorenzo em 06/11/2026.
- Planeje cada beat com cerca de 8 segundos e 1 ação clara por beat. Aprove o still antes de animar e siga a cadeia ficha, image-ref e start-frame.
- Aplique o checklist de aceite da trilha em [animação](animacao.md), na seção da trilha Pixar, antes de montar cada parte.
- Risco: declare imagem gerada por IA na thumbnail quando não for foto real do fato.

## 5. Imagem estática com zoom

- Como é: uma imagem por capítulo com zoom lento de entrada e saída, sem animação de verdade.
- Esta é a quinta opção da entrevista. Ela não é uma trilha de animação.
- Custo: quase zero. É o mais rápido de produzir.
- Quando usar: só quando o prazo é curto ou como rascunho para aprovar o roteiro.
- Limite: derruba a retenção. O vídeo 1 do canal sofreu com isso, com o Mundinho parado por 13 minutos. Em vídeo sem rosto, troque o visual a cada 5 a 10 segundos.
- Regra: nunca entregue um vídeo inteiro assim como versão final sem avisar o usuário do problema de retenção.
- Reprove o vídeo final inteiro em imagem estática quando o usuário não pediu rascunho e não registrou o aviso de retenção.
- Meça a retenção do rascunho e troque para uma trilha animada antes de publicar como final.

## Como decidir

- O usuário quer o vídeo todo animado e tem tempo: Blender e Python.
- O usuário quer o vídeo todo animado com diagramas e números, rápido e sem crédito de IA: infográfico 2D com Python e PIL.
- O usuário quer uma história animada, interativa ou vertical curta, com protagonista fixo: histórias 2D com renderFrame(n) e render.mjs, com os 4 estilos de quadros de movimento.
- O usuário quer história seriada com protagonista fixo em animação 3D estilo Pixar: vídeo 3D estilo Pixar por IA, com a ficha do personagem e o bloco de estilo copiados em todos os prompts.
- O usuário quer rápido e aceita perder retenção: imagem estática, com o aviso.
- O usuário quer o vídeo realista: IA em todos os clipes, com a ficha do personagem copiada em cada prompt para manter a continuidade.
- Quando o usuário não souber, mostre as cinco opções com custo e tempo e deixe ele escolher. Não escolha por ele.
- A plataforma não muda a trilha, mas muda o quadro: TikTok e Short usam 1080x1920 vertical, vídeo longo do YouTube usa 1920x1080 horizontal.

## O que os canais novos ensinam para cada trilha

Pesquisa de 06/11/2026, com 13 canais novos na biblioteca. Cada trilha tem um modelo de ambição e um limite de custo.

- Trilha 2D por código: Kurzgesagt, 25,6 a 25,8 milhões de inscritos, é o teto de ambição. Pergunta gigante como título, animação flat vetorial com paleta própria, narração calma e 1 a 2 vídeos por mês de altíssima qualidade. Copie a ambição da pergunta e a paleta própria, não o custo. O Kurzgesagt é um estúdio com dezenas de pessoas. OverSimplified, cerca de 9,5 milhões de inscritos com 33 vídeos, prova o mesmo ponto com animação 2D simples e engraçada: história complexa comprimida em narrativa com piadas visuais.
- Trilha 2D por código, documentário: LEMMiNO, 5,93 milhões de inscritos, é o modelo de documentário longo sem rosto com infográficos próprios, trilha original e 1 a 4 vídeos por ano. Copie a paciência de publicar pouco e bem, com pesquisa profunda.
- Trilha realista: BBC Earth, 14,6 milhões de inscritos, é o modelo de clipe curto recortado de documentário longo, com um conflito animal por vídeo. Copie a estrutura de um conflito por vídeo, não o material, que é da BBC. Astrum, 2,9 milhões de inscritos, é o modelo de série por corpo celeste com imagens reais de sondas da NASA e da ESA. Copie a série por tema fixo e cite a fonte de cada imagem.
- Trilha 3D por código: What If, 8,99 milhões de inscritos, é o modelo de "E se...?" com animação 3D e cenário impossível. Copie a estrutura de pergunta, cenário, mecanismo passo a passo e exceção. A animação 3D dele é de estúdio, adapte para low-poly por código.
- Trilha 3D por código, construção passo a passo: Mano Curioso, @curiosidades-3d-yt, é o modelo de engenharia explicada em 3D low-poly, com problema, tentativa que falha, solução passo a passo e prova final. Copie a montagem peça por peça e a palavra-chave na tela. Inscritos não verificados em 07/11/2026.
- Trilha Pixar por IA: Crânio Era, cerca de 1,6 milhão de seguidores no TikTok, é o modelo de história seriada com protagonista fixo. A série História do Tomate tem 12 episódios, cada um com 8,5 a 18,3 milhões de views, com cerca de 142 milhões de views no total, segundo vídeos que explicam os ganhos do criador em outubro de 2026, não verificado na conta oficial. Copie o protagonista simples e marcante, o arco dramático e o cliffhanger por parte, não os números de views.
- Qualquer trilha: Half as Interesting, 2,94 milhões de inscritos, prova que mapa com motion graphics simples é identidade visual barata e eficaz. Fireship, 4,3 milhões de inscritos, prova que densidade é identidade: um conceito inteiro em 100 segundos.

## Bibliotecas 3D na trilha 3D por código

- Use modelos prontos de biblioteca CC0 para cenário e objetos e reserve a modelagem própria para o herói. O guia completo com licenças, downloads e importação está em [bibliotecas 3D](bibliotecas-3d.md).
- Comece pelo conjunto já baixado em `~/workspace/tools/bibliotecas-3d/`: 936 MB, 20.567 arquivos, 4.700 GLB, 5.809 FBX, 993 GLTF, 147 blend e 13 HDR, medido em 07/11/2026 depois da limpeza. O conjunto inicial tinha 130 MB e 1.059 GLB.
- Monte histórias de terror e de Halloween com os 4 esqueletos rigados, com o cemitério, com as peças de Halloween e com o fantasma. Monte histórias de cidade com os prédios de bairro, com as ruas, com os carros, com os trens e com as multidões de personagens de blocos. Monte histórias de espaço com os 8 modelos reais da NASA, com o astronauta real, com a estação espacial e com a base espacial low-poly.
- Monte histórias de como funciona uma fábrica, um trem, um barco e um restaurante com as peças de fábrica, de trem, de barco e de cozinha. Monte histórias de comida com os 200 alimentos low-poly e com os modelos realistas de maçã, croissant e bolo para o close do objeto herói. Monte histórias de idade média com o castelo, com o mapa hexagonal de reino, com o pirata e com o canhão.
- Monte histórias de fundo do mar de superfície com os barcos, com a boia, com a concha e com o caranguejo de cubo. Monte histórias com animais de estimação e de fazenda com os 24 animais de cubo. Monte histórias de mistério e de detetive com a lupa, com o relógio de bolso, com o baú do tesouro e com a katana antiga.
- Monte o cenário com peças modulares da biblioteca e anime o mecanismo por código. O cenário pronto economiza o tempo de modelagem e o código guarda o controle do movimento.
- Adapte cada modelo à paleta do canal antes de animar. Recoloque a cor base para azul-marinho com laranja, aplique a escala real em metros e marque o shading plano. O modelo sem adaptação quebra a identidade visual.
- Mantenha o herói no mesmo arquivo em todas as cenas e use a biblioteca só para cenário, objetos e personagens secundários. A continuidade do herói é regra da skill.
- Prefira o modelo low-poly original a um modelo realista decimado. O modelo realista decimado continua com cara de realista e quebra o estilo da série.
- Confira a licença de cada modelo antes de publicar. Use só CC0 ou CC BY com crédito registrado. Rejeite CC BY-NC, CC BY-ND e Editorial. Dê crédito à NASA na descrição de todo vídeo que usar um modelo dela e nunca use a insígnia da NASA.
- Ilumine cada cena com um dos 5 HDRIs do acervo: campo, pôr do sol, noite, interior de casa e floresta. O HDRI de noite já foi validado como luz do mundo no Blender 4.5.3.
- Não baixe bibliotecas gigantes sem necessidade. O conjunto atual cobre casa, rua, floresta, espaço, masmorra, cidade, castelo, fábrica, cemitério e fundo do mar de superfície. Peixes animados continuam pendentes de download manual no Quaternius, porque não existe URL de download direto. Baixe um pacote novo só quando a história pedir um lugar que nenhum pacote cobre.

## Sub-estilos novos dentro da trilha 2D por código

Estes 5 sub-estilos vivem dentro da trilha 2D por código. Eles não são trilhas novas e não mudam a entrevista. Escolha um sub-estilo por vídeo quando a trilha 2D já estiver escolhida e siga só ele do começo ao fim. Todos usam o renderizador CDP com renderFrame(n) e o formato mãe vertical 1080x1920 a 60 fps.

### Isométrico 2.5D, construção e diagramas explodidos

Origem: isometric-animation em https://github.com/iart-ai/explainer-video-skills

- Escolha uma projeção e nunca misture as duas no mesmo vídeo. A iso verdadeira usa os eixos a mais e menos 30 graus da horizontal e a dimétrica 2 para 1 usa cerca de 26,57 graus.
- Monte a iso verdadeira com rotateX de 60 graus e rotateZ de 45 graus sobre o plano. A dimétrica 2 para 1 é o padrão de pixel-art e jogos.
- Sombreie por face para criar profundidade. Topo mais claro, lado esquerdo médio e lado direito mais escuro, com uma só direção de luz fixa em toda a cena.
- Construa pilhas de baixo para cima. O stagger segue a posição física das camadas e não a ordem do DOM.
- Abra diagramas explodidos com um único gap compartilhado. Todas as camadas se afastam juntas e voltam juntas ao montar.
- Anime a revelação por camada com back.out e a explosão e montagem com power3.inOut em 0,7 a 1 segundo.
- Use câmera com drift minúsculo e lento, de 6 a 12 segundos com yoyo, e parallax por profundidade.
- Use Three.js com OrthographicCamera quando precisar de oclusão real, sombras ou rotação 3D. Mantenha a projeção paralela sem encolhimento de perspectiva.
- Use este sub-estilo para explicar mecanismos, pilhas de camadas e diagramas explodidos. É o sub-estilo de como funciona em 2.5D.

### Whiteboard draw-on, a mão desenha enquanto a narração explica

Origem: whiteboard-animation em https://github.com/iart-ai/explainer-video-skills

- Desenhe cada traço com SVG stroke-dashoffset do comprimento total até 0. Normalize qualquer path com pathLength 1 e anime um só valor de 0 a 1.
- Use ease linear ou quase linear nos traços longos. O ease-in-out no traço longo faz o marcador dar solavancos.
- Siga a ponta do traço com a mão do marcador a cada quadro. Use getPointAtLength no mesmo progresso do dashoffset e alinhe a ponta da caneta com o ponto, com o offset de nib calibrado.
- Levante a mão entre os traços. A mão some ou pula para o começo do próximo traço e nunca desliza sobre o quadro vazio.
- Desenhe a arte em paths abertos de traço único e na ordem de desenho. Preenchimentos de cor entram depois do contorno, com fade ou clip-reveal.
- Escreva à mão na ordem de leitura, glifo por glifo. A escrita segue a narração e o rótulo termina de ser desenhado quando a palavra é dita.
- Guie o ritmo pela narração a cerca de 2,3 palavras por segundo. A duração de cada desenho é a duração da frase que ele ilustra, mais uma pausa curta.
- Apague com uma gramática única e consistente. O wipe vai sempre na mesma direção ou o draw reverso, para o quadro não acumular poluição visual.
- Use este sub-estilo para explainers de como funciona e curiosidades. É o sub-estilo de scribe para vídeo curto.

### Pintado aquarela e tinta, o visual artesanal

Origem: painted-animation em https://github.com/tuzhechen2005/opus-video-skills

- Pinte cada quadro como função pura de t com p5.brush. Use só paint e inkLine e nunca formas planas de p5.
- Mantenha o visual em 2D plano. Viradas passam por vistas chave desenhadas e nunca por projeção 3D.
- Faça a luz com glow aditivo. A mistura de pigmento estraga amarelo sobre azul e vira verde.
- Ferva as linhas de tinta. O boil dá vida ao traço parado e é a assinatura do estilo.
- Escreva o storyboard antes do código com reads por shot. O read é a lista cronometrada do que o espectador precisa entender e os reads definem a duração do shot.
- Mostre um read por vez. Ações rápidas e significados segurados, com o personagem grande no quadro em plano médio ou close.
- Bloqueie as poses chave como stills antes de animar entre elas. Atue com a biblioteca de emoções e poses do estilo.
- Coloque uma transição em cada costura. Brush wipe, íris, match cut ou corte na ação, sempre.
- Revise com contact sheet por shot, tira quadro a quadro dos movimentos chave e crop nos rostos. Olhe cada imagem de verdade antes de renderizar o vídeo.
- Use este sub-estilo para séries de terror ou histórias com visual artesanal. É o sub-estilo mais distinto da trilha 2D e o mais caro por quadro, então meça o custo antes de prometer prazo.

### Stickman minimalista, boneco de palito de alto contraste

Origem: stickman-animation em https://github.com/advibly/skills

- Trave o STYLE LOCK em todo prompt. Figura de cabeça circular oca, sem rosto e sem roupa, traço único uniforme, emoção só por pose e timing, sem sombreamento e sem volume 3D.
- Estruture cada clipe de 10 segundos em 3 beats. Estabelecer, transformar e entregar o clímax, com 4 ou mais dispositivos visuais por clipe.
- Use canvas monocromático claro ou escuro com até 3 cores de destaque. Cada cor tem um significado fixo, como problema, insight e desfecho.
- Proíba texto em todas as gerações de vídeo. O texto vira overlay nítido só na composição final.
- Escreva cores por nome comum e nunca por hex. Modelos renderizam códigos hex como texto visível na tela.
- Narre a 2,3 a 2,5 palavras por segundo. São 20 a 25 palavras por clipe e 130 a 150 por Short de 60 segundos.
- Costure os clipes por interfaces nomeadas. O still de abertura do clipe seguinte é o quadro final do clipe anterior, então a costura acontece em câmera.
- Aprove a proposta do diretor e os stills antes de animar. A proposta traz a tabela de clipes, beats, SFX e transições.
- Avise que a skill de origem usa o Advibly MCP, que é pago. Importe a direção e os gates e nunca prometa a ferramenta como se fosse gratuita.
- Use este sub-estilo para explainers baratos e muito legíveis no celular. É o sub-estilo de menor custo de produção da trilha 2D.

### Tipografia cinética, o tipo é o protagonista

Origem: kinetic-reel em https://github.com/tuzhechen2005/opus-video-skills

- Use Anton para headlines condensadas, Archivo Black para slams largos, Instrument Serif itálico para a frase de voz e JetBrains Mono para micro-texto e HUD.
- Adapte as fontes ao acervo local antes de prometer. O template desta skill só tem as 8 fontes woff2 em ~/workspace/tools/renderizador-cdp/fonts/ e o render abre a página por file sem rede, então fonte externa não carrega. Use Archivo Black do acervo para slams quando Anton não estiver no acervo e adicione fonte nova só com licença OFL e aprovação.
- Trave o ritmo em 120 BPM. Cortes caem nos beats e mudanças de capítulo caem nos compassos.
- Faça letras, chips e contadores entrarem rápido com expo-out, segurarem e passarem. O ritmo travado no beat é a gramática do sub-estilo.
- Dê a cada shot um mecanismo e não só palavras. A grade roteia, a matriz escaneia e os pacotes passam por portões. O headline nomeia o mecanismo e a animação prova ele.
- Transicione por continuidade de forma. O zoom atravessa o elemento que o olho segue e a íris nasce do que acendeu.
- Marque dados ilustrativos com o selo ILUSTRATIVO no HUD. Use só números da fonte com escopo e nunca desenhe dado por dimensão que você não tem. Visualize o processo e não o número inventado.
- Use este sub-estilo para reels, promos e vídeos de fato com texto gigante. É a versão de tipografia pura do estilo 4 de quadros de movimento.

## Regra de amostragem de estilo

Origem: style-sampling em https://github.com/heygen-com/hyperframes

- Amostre a gramática do estilo e nunca a identidade do criador. Estrutura, ritmo, visual, gráficos e som de uma série existente aplicados a um tema novo.
- Nunca use rosto, voz, footage, logo ou nome do criador original. Só a gramática do estilo viaja para o vídeo novo.
- Mantenha por canal um template de estilo documentado. Estrutura, ritmo, paleta, gráficos e som ficam escritos e o episódio novo reutiliza o template em vez de reinventar o visual.
- Apresente os estilos candidatos em lista curta e recomende o que cabe no tema. Espere a escolha antes de produzir.
- Pare em 2 pontos obrigatórios. Storyboard aprovado e draft aprovado, sem produção completa antes deles.
- Avise que os templates prontos do HyperFrames Pro são pagos. Sem a assinatura, a skill de origem só orienta a assinar e proíbe reconstruir o template de memória ou da web. Importe o método de amostragem e nunca prometa os templates como se fossem gratuitos.

## Modelo kit travado por canal

Origem: theme-factory e brand-guidelines em https://github.com/anthropics/skills

- Trave um kit por canal com paleta, fontes, gramática de movimento e SFX. O kit é o tema do canal e vale para todos os vídeos dele.
- Mostre o tema e espere confirmação antes de aplicar. Aplique cores e fontes consistentemente em todo o vídeo depois da confirmação.
- Derive thumbnails, legendas, cards e banners do kit. Nada escolhe cor na hora por vídeo.
- Escreva o kit no mesmo formato enxuto. Cores principais com hex, cores de destaque com hex, tipografia por função com título acima de certo tamanho e corpo para o resto.
- Reserve as cores de destaque para formas e acentos. Cicle entre elas para manter interesse sem quebrar a marca.
- Cheque contraste e legibilidade em cada aplicação. A escolha de cor muda conforme o fundo e a legenda queimada tem que ler no celular.
- Dê nome descritivo ao kit do canal. Terror ganha paleta escura com acento vermelho e curiosidades ganham azul-marinho com laranja, por exemplo.

## Reestilização vídeo para vídeo como ferramenta de $corrigir

Origem: video-restyle em https://github.com/advibly/skills

- Use a reestilização vídeo para vídeo para corrigir o estilo de um vídeo pronto sem refazer o roteiro. É uma ferramenta de $corrigir e não uma trilha nova.
- Preserve identidade, expressões, lip-sync e áudio original. A reestilização muda o visual e mantém o resto.
- Empacote o vídeo em segmentos de 8 a 10 segundos. Corte nas fronteiras de frase e junte frases adjacentes para encher o segmento em vez de enviar muitos segmentos curtos.
- Escreva cada segmento como timeline beat por beat sobre a transcrição dele. O evento cai exatamente na palavra que o ancora.
- Trave um bloco de estilo que viaja verbatim em todos os prompts de segmento. O bloco fixo mais os eixos de variação por segmento é o que faz os segmentos parecerem um só vídeo.
- Trate o áudio original como verdade de base. A composição final usa o áudio do vídeo original e nunca o áudio do segmento reestilizado.
- Conforme cada segmento reestilizado ao comprimento exato do segmento fonte. O movimento pesado pode mudar a duração em fração de segundo e a conformação corrige isso.
- Avise que a skill de origem usa o Advibly MCP, que é pago. Importe o método de segmentação e conformação e nunca prometa a ferramenta como se fosse gratuita.
