# Animação — o manual completo

## A regra de ouro

Um vídeo só é animado quando alguma coisa se move ou a câmera corta a cada 2 a 4 segundos. Em vídeo longo, troque o visual a cada 5 a 10 segundos no mínimo. Zoom lento sobre imagem parada não é animação.

## Os livros que fundamentam esta skill

A animação desta skill não é palpite. Ela segue livros de animação de verdade. Leia esta seção antes de animar qualquer clipe.

- The Animator's Survival Kit, de Richard Williams, primeira edição em 2001. O manual de métodos, princípios e fórmulas para animação clássica, por computador, jogos, stop motion e internet. Ensina timing e spacing, aceleração e desaceleração, antecipação, arcos, extremos e poses de passagem, caminhadas com peso, flexibilidade e ação sobreposta, peso e esforço, diálogo e atuação.
- The Illusion of Life, de Frank Thomas e Ollie Johnston, primeira edição em 1981. Dois dos Nove Anciões da Disney codificaram os 12 princípios da animação, praticados no estúdio desde os anos 1930. Os 12 princípios estão na seção abaixo.
- Cartoon Animation, de Preston Blair, primeira edição em 1994. Manual prático de desenho animado: construção de personagens, linhas de ação, diálogo sincronizado com a ação e timing. Base de poses para o trilho 3D por código.
- Timing for Animation, de Harold Whitaker e John Halas, original de 1981 e segunda edição revisada em 2009. O livro mais focado em timing: tabelas de timing, quanto espaçamento usar, quanto tempo cada pose dura e como o timing comunica peso, emoção e intenção.
- Drawn to Life, de Walt Stanchfield, primeiro volume em 2009. Aulas de desenho da Disney: gesto, observação da vida real, silhueta, peso e simplificação. Ensina a enxergar o movimento antes de animá-lo.
- Elemental Magic, de Joseph Gilland, volume 1 em 2009. Guia de efeitos desenhado à mão: líquidos, fogo, fumaça, explosões, magia e transformações, com a física de cada elemento antes do desenho. Serve para animar água, fogo e fumaça no trilho por código e para escrever prompts de efeitos com comportamento físico correto no trilho realista.
- Creating Motion Graphics with After Effects, de Trish Meyer e Chris Meyer, quinta edição em 2010. Referência de motion graphics: keyframes, editor de gráfico, caminhos de movimento em curva de Bezier, tipografia cinética, infográficos animados e expressões. Os conceitos de easing, hierarquia e ritmo valem direto para o trilho 2D por código.
- Motion Graphic Design, de Jon Krasner, segunda edição em 2008. História e estética do motion design: composição, tipografia em movimento e ritmo visual. Base das decisões de estilo do trilho 2D.
- Character Animation Crash Course!, de Eric Goldberg, 2008, Silman-James Press, com prefácio de Brad Bird. Como conceber personagens e dar-lhes performance, com os princípios da animação clássica explicados com exemplos da Era de Ouro. Goldberg animou o Gênio de Aladdin. Para canal dark: mesmo sem apresentador, personagens, mascotes e figuras históricas precisam de intenção, gesto e timing. Fonte: Archive.org e AWN, pesquisa de 06/11/2026.
- Animation: From Script to Screen, de Shamus Culhane, 1988, St. Martin's Press. Cobre todo o processo, do roteiro à produção: escrita, gravação, atuação, diálogo e gestão de estúdio. Culhane animou os anões de Branca de Neve. Para canal dark: é o manual de pipeline completo, roteiro, storyboard, voz, animação e montagem. Fonte: Open Library, pesquisa de 06/11/2026.
- Directing the Story, de Francis Glebas, 2008, Focal Press, 346 páginas. Abordagem estrutural para apresentar histórias visualmente: transmitir significado com imagens e dirigir o olhar do espectador. Glebas foi story artist da Disney em Aladdin, O Rei Leão, Pocahontas e Hércules. Para canal dark: é o livro-ponte entre roteiro e storyboard. Cada cena precisa de uma imagem que carrega o sentido, não só de uma narração por cima de B-roll. Fonte: Goodreads e Biblio, pesquisa de 06/11/2026.
- The Art of Pixar, de Amid Amidi, 2011, Chronicle Books. A coleção completa dos colorscripts dos filmes da Pixar, com a arte de desenvolvimento visual de 25 anos de animação. A lição prática para o canal dark é o colorscript: cada capítulo ganha uma cor dominante que marca o clima da cena antes de qualquer detalhe. A paleta fixa do canal com uma cor de destaque por capítulo, que a skill já usa em [ambientação](ambientacao.md), é a versão simples do colorscript da Pixar. Antes de animar um capítulo, desenhe a sequência de cores dele em miniatura e confira se o clima muda de um capítulo para o outro. Fonte: Archive.org, copyright 2011, consulta em 06/11/2026.

Não existe livro dedicado a animação por código com Python e PIL ou com Blender e Python. Os livros acima cobrem os princípios. A parte de código vem da documentação do Blender e do Pillow e dos conceitos de keyframe e easing dos livros de motion graphics.

## O que os livros novos acrescentam

Os três livros novos da pesquisa de 06/11/2026 viram regras práticas. Aplique uma por cena, junto com os 12 princípios.

### Dirija o olhar, não só a câmera (Glebas, 2008)

- Cada cena tem uma imagem que carrega o sentido da ideia. Se a imagem não conta nada sozinha, a cena é só narração com B-roll.
- Pergunte antes de animar: o que o espectador precisa entender só com os olhos nesta cena? A resposta é o enquadramento.
- O olhar vai para o contraste, para o movimento e para o rosto. Coloque o elemento chave no ponto de maior contraste do quadro.
- Na trilha 2D, a imagem que carrega o sentido é o diagrama. Um diagrama por cena, com o número ou o carimbo no centro, sem elemento competindo.
- Na trilha realista, dirija o olhar com o prompt: sujeito central, fundo limpo, uma ação só por clipe.

### O gesto nasce de uma intenção (Goldberg, 2008)

- Todo gesto precisa de um pensamento antes dele. O personagem aponta porque acabou de perceber algo. Ele recua porque ficou com medo. Gesto sem intenção é boneco mexendo o braço.
- Escreva a intenção no storyboard, junto com o gesto: "ele aponta porque acabou de ver a porta abrir".
- A performance é o que separa animação de movimento. Dois gestos com intenção valem mais que dez gestos aleatórios.
- Na trilha 2D, a intenção vira o comportamento do diagrama: o número conta devagar porque o fato é pesado, o carimbo cai com força porque o veredito é chocante.
- Varie a intenção por capítulo. Se o personagem reage do mesmo jeito em todos os capítulos, a performance some.

### Grave a voz antes de animar o gesto (Culhane, 1988)

- O pipeline completo é roteiro, storyboard, voz, animação e montagem, nesta ordem. A voz vem antes da animação porque o timing da fala manda no timing do movimento.
- O gesto acontece no mesmo segundo da palavra que ele ilustra. Sem a narração pronta, o animador adivinha o timing e erra.
- Na prática da skill, isso já é regra: a narração é gerada antes dos clipes, e a duração real de cada cena vem da transcrição da narração. Leia a regra de sincronia em [montagem](montagem.md).
- Na trilha 3D por código, planeje os keyframes com o tempo real da fala em mãos. Na trilha 2D, a contagem do número e a queda do carimbo seguem a fala, não a estimativa do storyboard.
- Diálogo e atuação andam juntos: a ênfase da voz pede um gesto maior, a pausa da voz pede o personagem parado em tensão, não parado sem motivo.

## Os 12 princípios da animação

Os 12 princípios vêm de The Illusion of Life, de Frank Thomas e Ollie Johnston. Aplique um princípio por vez em cada cena. Uma cena que usa 3 princípios bem aplicados já parece animada de verdade. As aplicações abaixo cobrem as 4 trilhas animadas: realista por IA, 3D estilo Pixar por IA, 3D por código com Blender e 2D infográfico por código com Python e PIL ou com o renderizador CDP em HTML e CSS. A imagem estática com zoom é a quinta opção e não tem animação para aplicar princípio nenhum. No trilho Pixar por IA valem as aplicações do trilho realista, porque o método é o mesmo, vídeo gerado por IA em clipes de cerca de 10 segundos, e as diferenças estão na seção da trilha D.

### 1. Squash and stretch, comprimir e esticar

Comprima e estique o objeto mantendo o volume, para dar peso, elasticidade e sensação de impacto e gravidade.

- No trilho realista: peça no prompt o objeto ou o personagem achatando ao pousar e esticando ao saltar. Sem isso o movimento sai rígido.
- No trilho 3D por código: escale o objeto nos keyframes, achatando no eixo vertical no impacto e esticando no salto, mantendo o volume aproximado.
- No trilho 2D por código: aplique a formas planas. Um círculo que cai achata ao tocar o chão e estica ao subir. Uma barra de gráfico achata ao bater no valor final.

### 2. Antecipação

Uma pequena ação preparatória avisa o público do que vem: agachar antes de pular, puxar o braço antes do soco.

- No trilho realista: inclua a preparação no prompt, como "ele agacha e então pula". Sem ela a ação parece surgir do nada.
- No trilho 3D por código: faça o keyframe de antecipação 3 a 6 frames antes da ação principal, em direção oposta.
- No trilho 2D por código: antes de um número saltar ou de um diagrama mudar, faça um pequeno recuo ou pulso do elemento.

### 3. Encenação, staging

Apresente cada ideia de forma completamente clara. Enquadramento, posição dos elementos e câmera guiam o olhar para o que importa.

- No trilho realista: um clipe é uma ideia. Prompt com sujeito central, fundo limpo e ação única, sem elementos competindo.
- No trilho 3D por código: câmera com TRACK_TO no alvo, objeto principal isolado no centro, sem obstrução no enquadramento.
- No trilho 2D por código: um diagrama por cena, hierarquia clara de título, número grande e detalhe, nada sobrepondo o elemento chave.

### 4. Animação direta e pose a pose

Animação direta anima quadro a quadro do início ao fim e é boa para fluidos. Pose a pose define as poses chave e depois preenche os intervalos e é boa para ações com timing preciso.

- No trilho realista: não se aplica direto, porque não há desenho quadro a quadro. O equivalente é gerar o clipe em sequência ou gerar imagens chave e interpolar entre elas.
- No trilho 3D por código: pose a pose é o método natural. Keyframes nas poses extremas e nas poses de passagem, e o Blender interpola. Use animação direta, com keyframes em todos os frames, só para fluidos como água e fumaça.
- No trilho 2D por código: pose a pose por código. Defina estados chave de posição e valor e interpole entre eles por função. Animação direta é recalcular a forma a cada frame, como uma onda ou uma fumaça.

### 5. Follow-through e ação sobreposta

Partes secundárias continuam se movendo depois que a ação principal para, e se movem com atraso em relação ao corpo.

- No trilho realista: peça no prompt que o casaco continua balançando depois que ele para. A IA tende a parar tudo junto se não for instruída.
- No trilho 3D por código: anime partes secundárias, como braços, capa e antena, com keyframes atrasados 2 a 4 frames em relação ao corpo, e com assentamento depois da parada.
- No trilho 2D por código: elementos secundários, como linhas, partículas e sombras, chegam ao destino alguns frames depois do elemento principal e oscilam antes de assentar.

### 6. Aceleração e desaceleração, easing

Objetos aceleram e freiam gradualmente. Reproduza com mais desenhos juntos no início e no fim e mais espaçados no meio.

- No trilho realista: peça no prompt que o movimento começa devagar, acelera e freia suavemente. Clipes sem easing parecem mecânicos e com parada brusca.
- No trilho 3D por código: use interpolação Bezier nos keyframes, com ease-in e ease-out, em vez de interpolação linear. Nunca deixe um movimento começar ou parar em velocidade máxima.
- No trilho 2D por código: use funções de easing, como ease-out cúbico, em toda interpolação de posição, escala e contagem de números. É o que tira o aspecto robótico do motion graphics por código.

### 7. Arcos

Quase todo movimento natural segue trajetória curva, porque os membros giram a partir de pivôs. Trajetórias retas parecem mecânicas.

- No trilho realista: peça trajetórias curvas no prompt, como o braço descrevendo um arco ao apontar. Trajetória reta é um defeito típico de clipe de IA.
- No trilho 3D por código: rotacione a partir dos pivôs das articulações em vez de transladar em linha reta. Desenhe o arco do movimento ao planejar os keyframes.
- No trilho 2D por código: movimente elementos ao longo de arcos, como uma seta que sobe em curva ou um número que entra por arco, em vez de deslocamentos retos em X ou Y.

### 8. Ação secundária

Movimento adicional que apoia a ação principal, como braços balançando ao andar ou cabelo ao vento, sem roubar a atenção dela.

- No trilho realista: inclua uma ação secundária no prompt, como "enquanto explica, ele gesticula com a mão livre", para o clipe não parecer parado.
- No trilho 3D por código: acrescente balanço de braços, inclinação de cabeça ou balanço de capa sincronizados ao movimento principal.
- No trilho 2D por código: enquanto o número principal conta, um gráfico de fundo ou uma linha secundária se move em apoio. Nunca dois elementos competindo pelo foco.

### 9. Timing

A duração e a velocidade de uma ação definem peso, humor e intenção. Timing errado destrói a credibilidade.

- No trilho realista: defina a duração da ação no prompt, como "em 2 segundos ele levanta o braço devagar". Em 10 segundos, cada ação precisa de tempo contado.
- No trilho 3D por código: conte os frames. Ação pesada usa mais frames, ação leve e rápida usa menos frames. Sincronize a duração da cena com a narração real, não com estimativa.
- No trilho 2D por código: a duração de cada cena é a duração real da fala correspondente. Números contam em ritmo legível, nem instantâneo, nem arrastado.

### 10. Exagero

Empurre a ação além do realismo, em pose, expressão e velocidade, para comunicar emoção e intenção com mais força, sem perder a credibilidade.

- No trilho realista: peça exagero moderado no prompt, como "gesto amplo e expressivo". A IA realista tende ao contido demais.
- No trilho 3D por código: exagere poses e amplitudes, com o braço mais alto e a inclinação maior, e depois reduza se ficar caricato.
- No trilho 2D por código: exagere a escala do número chave, o salto de um gráfico ou o destaque da palavra-chave. No infográfico, exagero é hierarquia visual.

### 11. Desenho sólido

Domínio de forma, volume, peso e perspectiva 3D no espaço 2D. O personagem precisa manter estrutura e proporção consistentes.

- No trilho realista: é o ponto fraco da IA. Use referência fixa do personagem e prompt com descrição de proporções em todos os clipes para manter a continuidade.
- No trilho 3D por código: modelos low-poly com proporções fixas e pivôs bem posicionados já garantem a solidez. Evite deformar a malha fora do planejado.
- No trilho 2D por código: formas planas com proporções e espessuras consistentes em todas as cenas, mesma espessura de linha, mesmos raios e mesma grade.

### 12. Apelo

Carisma e clareza visual que prendem o olhar. Vale para heróis e vilões. Apelo não é ser fofo, é ser interessante e legível.

- No trilho realista: personagem com traços distintos e legíveis no prompt. Rostos genéricos perdem apelo e continuidade.
- No trilho 3D por código: silhueta legível do boneco, cores e proporções marcantes, poses claras.
- No trilho 2D por código: design limpo e carismático. Paleta fixa, tipografia forte, números grandes. O apelo aqui é legibilidade e identidade visual.

## O que a pesquisa de 2026 acrescenta

- Easing acima de tudo: movimento em velocidade constante é o sinal mais claro de trabalho amador. Elementos aceleram ao sair do repouso e desaceleram ao chegar. Sobreponha entradas com offset de poucos frames em vez de disparar tudo junto. Fonte: pexo.ai, atualizado em 06/08/2026.
- A IA não aplica os princípios sozinha: bibliotecas de movimento de IA dão uma base realista, mas não exageram, não encenam e não temporizam a ação para a história. O fluxo é levar o movimento gerado por IA para o Blender ou para o código e aplicar os princípios ajustando poses, easing e keys. Fonte: meshy.ai, atualizado em 22/09/2026.
- Timing contra spacing: timing é quantos frames uma ação leva. Spacing é quanto o objeto se move entre frames. Timing curto é movimento leve e rápido. Timing longo é movimento pesado e deliberado. Fonte: meshy.ai, 22/09/2026.
- Ordem de prioridade quando os princípios conflitam: primeiro intenção e legibilidade, depois identidade e continuidade, depois timing e peso, depois staging e silhueta, depois arcos, easing e overlap. Fonte: awful-motion-skills no GitHub, consulta em 06/11/2026.
- Tempo de leitura: um espectador de primeira viagem precisa de cerca de 2 segundos para uma linha curta de texto. Fonte: pexo.ai, 06/08/2026.
- Pattern interrupt: em formato curto, mude o visual a cada 2 a 4 segundos e coloque uma interrupção deliberada a cada 10 a 15 segundos em vídeos com mais de 30 segundos. Fonte: shortzly.com, atualizado há 48 dias em 06/11/2026.

## A decisão que muda tudo: cinco opções

A escolha é feita na entrevista, antes de qualquer produção, e muda o rumo inteiro da animação. Não dá para trocar de rumo no meio do vídeo sem refazer tudo. São quatro trilhas de animação e uma quinta opção sem animação, a imagem estática com zoom.

- Trilha realista: visual de cinema, pessoas e lugares de verdade, clipes de cerca de 10 segundos gerados por IA. O desafio é a continuidade, manter o mesmo personagem igual em todos os clipes. O custo é por crédito e a produção é rápida. A animação vem do prompt de ação.
- Trilha Pixar por IA: animação 3D estilo Pixar gerada por IA, com personagens estilizados de olhos grandes, luz de cinema e clipes de cerca de 10 segundos. O desafio é a continuidade, manter o mesmo personagem igual em todos os clipes. O custo é por crédito e a produção é rápida. A animação vem do prompt de ação, com a ficha do personagem e o bloco de estilo copiados em todos os prompts. É a trilha do Crânio Era.
- Trilha 3D por código: animação 3D low-poly desenhada por script em Blender e Python, no estilo do Desconstruindo Universo. O desafio é o tempo de render, cerca de 20 minutos por clipe de 10 segundos. O ganho é controle total de cada movimento e identidade visual própria, sem depender de crédito de IA.
- Trilha 2D por código: motion graphics 2D infográfico desenhado por script em Python e PIL ou por página HTML com o renderizador CDP, no estilo do vídeo 1 do O Laboratório Curioso. O desafio é desenhar cada diagrama por código. O ganho é render em segundos por cena, texto e números exatos, e identidade visual própria, sem depender de crédito de IA. A opção B do trilho, o renderizador CDP, está em [renderizador CDP](renderizador-cdp.md). A variante de histórias 2D usa a opção B com os 4 estilos de quadros de movimento, protagonista fixo e formato mãe vertical 1080x1920, e está em [quadros de movimento](quadros-movimento.md).
- A imagem estática com zoom é a quinta opção e não é uma trilha de animação. É só rascunho para aprovar roteiro ou quebra-galho de prazo curto, com o aviso de que derruba a retenção.

Quando o usuário não souber, mostre as cinco opções com custo e tempo e deixe ele escolher. Depois que ele escolher, siga só aquela opção no vídeo inteiro. O estudo de caso da trilha 2D está em [estudo de caso do Laboratório Curioso](estudo-caso-laboratorio-curioso.md).

- A plataforma muda o quadro e não a trilha. TikTok e Short usam 1080x1920 vertical e o vídeo longo do YouTube usa 1920x1080 horizontal. A trilha escolhida vale nas duas proporções, com o enquadramento fechado e o assunto grande no quadro nas duas.

## Trilha A — Animação realista com vídeo gerado por IA

### Como funciona

- Um clipe é uma cena de cerca de 10 segundos, gerada por IA com a ferramenta de geração de vídeo por IA disponível no momento. O conector Runway não está conectado, então não gere nada com Runway até conectar a conta. Um vídeo de 13 minutos precisa de dezenas de clipes.
- Cada clipe nasce de um prompt com 4 partes: quem está na cena, o que ele faz, o que acontece no ambiente e como a câmera se move.
- Verifique o saldo de créditos antes de gerar. Gere em lote por capítulo, para não parar no meio.

### Continuidade do personagem, o maior desafio desta trilha

- Escreva a ficha do personagem uma vez, com descrição fixa: idade, cabelo, rosto, roupa, calçado e objeto que ele carrega. Copie essa ficha em todos os prompts, sem mudar uma palavra.
- Gere a primeira imagem do personagem e use ela como referência de imagem para os próximos clipes, quando a ferramenta permitir.
- Use a mesma semente quando a ferramenta permitir.
- Confira o rosto e a roupa em cada clipe gerado. Se o personagem mudou de rosto, de roupa ou de idade, gere de novo.
- O mesmo menino em todos os clipes é uma exigência do Lorenzo para o Short da geladeira. Vale para qualquer série: o personagem não muda no meio.

### Prompt de ação, como escrever

- Comece o prompt com o verbo da ação, não com a descrição do lugar. A ação é o que anima.
- Prompt fraco: "um menino em um lago". Prompt forte: "um menino pescando em um lago, ele puxa a vara, o peixe pula na água, a água ondula, close-up no menino surpreso".
- Coloque o movimento do assunto no prompt: o peixe nada e boqueja, a porta abre, a pedra rola, o mecanismo gira.
- Coloque o movimento do ambiente no prompt: a água se mexe, as árvores balançam, a poeira cai, a fumaça sobe.
- Coloque a câmera no prompt: close-up, zoom lento, travelling, câmera parada, plano aberto.
- Um prompt bom tem pelo menos 1 verbo de ação do personagem, 1 movimento do assunto e 1 movimento de câmera.
- Escreva o prompt com os princípios da seção acima: antecipação antes da ação, easing no movimento, arco na trajetória, ação secundária de apoio e exagero moderado no gesto.
- Escolha o modo antes de escrever o prompt. Texto para vídeo nasce só da ideia, imagem para vídeo nasce de uma imagem de partida e vídeo para vídeo transforma um clipe que já existe. Fonte: ai-video, sintetizado com palavras próprias, em https://github.com/jordangaston/claude-plugins
- Monte o prompt de texto para vídeo em 8 partes e nesta ordem fixa: meio, plano, ângulo, movimento, foco, assunto, luz e cor. Não empilhe adjetivos soltos fora da ordem.
- Faça o assunto ser o coração do clipe. Escreva quem é, o que ele faz ao longo do tempo, a idade, a roupa e a expressão, com uma ação dinâmica clara, como desembainha e vira ou desliza o copo enquanto a fumaça sobe.
- No modo imagem para vídeo, use a estrutura curta e primeiro o movimento. A imagem trava o visual e o texto só descreve o movimento.
- No modo vídeo para vídeo, descreva só a transformação alvo, com novo meio, estilo, paleta, luz ou época, e preserve o movimento e a composição do original.

### Linguagem de câmera nesta trilha

- Close-up no rosto: para reação e surpresa.
- Close-up no mecanismo: para mostrar a peça funcionando.
- Zoom lento: para revelar o lugar, no máximo 2 segundos.
- Travelling: para acompanhar o personagem andando.
- Plano aberto: só para estabelecer o lugar, no máximo 2 segundos, e nunca com o personagem pequeno no meio da paisagem vazia.

### O que a IA faz bem e o que faz mal

- Faz bem: expressões faciais, água, fogo, fumaça, multidão, luz.
- Faz mal: mãos, texto na tela, física de objetos, continuidade de roupa e cenário, contar dedos e letras.
- Nunca peça texto na tela para a IA gerar. Texto na tela é feito na edição, depois.
- Nunca peça uma ação física complicada, como pegar um objeto pequeno e abrir ele. Divida em 2 clipes.

### Quando rejeitar um clipe

- Rejeite quando nada se move nele.
- Rejeite quando o personagem mudou de rosto, de roupa ou de idade.
- Rejeite quando a física quebra: objeto atravessando parede, mão com 6 dedos, água subindo.
- Gere de novo com a ação mais forte no prompt. Se falhar 3 vezes, mude a ação para uma mais simples.

### Fórmula de prompt e aceite na trilha realista

- Monte o prompt de texto para vídeo na ordem meio, plano, ângulo, movimento, foco, assunto, luz e cor, com 60 a 140 palavras por clipe. Leia a fórmula completa na seção Fórmula de prompt de vídeo por IA em 8 partes deste guia.
- Use o modo I2V motion-first quando existir uma imagem inicial aprovada. Escreva um prompt curto de 25 a 70 palavras com só o que muda ao longo do tempo e um só movimento de câmera. Leia a regra completa na seção Modo I2V motion-first deste guia.
- Aprove o still de cada beat antes de animar e siga a cadeia ficha, image-ref e start-frame. Guarde o texto no still aprovado e repita a string curta no prompt de movimento como texto estático e legível. Leia a regra completa na seção Regra still-first e cadeia de consistência deste guia.
- Estruture cada clipe de 10 segundos em 3 beats com estabelecer, transformar e entregar o clímax, e exija 4 ou mais dispositivos visuais por clipe. Leia a regra completa na seção Densidade de 3 beats por clipe de 10 segundos deste guia.
- Compare o frame do clipe novo com o frame do clipe anterior lado a lado antes de montar. A comparação mostra a troca de rosto que o olho sozinho não percebe.
- Aplique a regra das 3 tentativas. Se o clipe falhar 3 vezes, simplifique a ação ou o enquadramento. Nunca aceite o personagem errado para fechar o capítulo.
- Aplique o checklist de aceite abaixo em cada clipe antes de montar. Clipe que falha em 1 item volta para regeneração.
- Aprove quando o personagem faz pelo menos 1 gesto com intenção e o assunto se move em caminho curvo no mesmo segundo da narração.
- Aprove quando o ambiente se move o tempo todo e a câmera corta ou se move a cada 2 a 4 segundos.
- Aprove quando o rosto, a roupa, a idade e o objeto do personagem batem com o clipe anterior na comparação lado a lado.
- Aprove quando a ação narrada aparece visível na tela no mesmo segundo da fala, com desvio máximo de 0,5 segundo.
- Rejeite quando nada se move, quando o personagem mudou, quando a física quebra, quando o texto na tela saiu com letra falsa e quando o gesto cai depois da palavra que ele ilustra.
- Rejeite quando o clipe tem mais de 3 segundos sem mudança visível. Meça com o portão de vídeo estático em [quadros de movimento](quadros-movimento.md).

## Trilha B — Animação por código com Blender e Python

### Como funciona

- Um script `.py` por cena de cerca de 10 segundos, com primitivas low-poly, boneco com pivôs, keyframes e câmera com TRACK_TO.
- Pipeline completo: roteiro, storyboard em texto com 1 cena igual a 1 clipe de cerca de 10 segundos, um script por cena, render Cycles CPU em 480x854 com 6 samples e sem denoise em PNGs, ffmpeg monta o MP4, sobe para 720x1280 e junta com a narração.
- Ferramenta: Blender 4.5.3 LTS portátil em `~/workspace/tools/blender-4.5.3-linux-x64/`. O `bpy` só funciona dentro do Blender com `blender -b --python cena.py`.
- Bibliotecas prontas: use personagens, objetos e cenários CC0 já baixados em `~/workspace/tools/bibliotecas-3d/` e siga o guia de importação e adaptação em [bibliotecas 3D](bibliotecas-3d.md).
- Guia completo com comandos exatos: `~/workspace/research_notes/animacao-codigo-blender-2026-11-05.md`.
- Cena real de exemplo: `~/workspace/your_files/tuto-lowpoly-codigo/render_blender.py`. Template de exemplo: `~/workspace/tools/blender-exemplo/cena_peixe_10s.py`.

### Animações prontas da biblioteca, use antes de keyframar

- Use a ação pronta da biblioteca quando o gesto já existir. Keyframar uma caminhada do zero quando a biblioteca já tem a caminhada pronta é retrabalho.
- Use os 5 personagens KayKit Adventurers com 76 animações cada no arquivo GLB. O Knight foi validado na importação de teste em 06/11/2026 no Blender 4.5.3 com 1 armature, 76 actions e 17 objetos.
- Use os 4 esqueletos KayKit Skeletons com 95 animações cada no arquivo GLB. O Skeleton Mage foi validado com 95 actions e 4.098 vértices e o Skeleton Warrior com 95 actions e 6.159 vértices. Use os esqueletos para terror e Halloween com movimento pronto.
- Use os personagens Kenney Animated Characters Protagonists e Survivors com as animações idle, jump e run em arquivos FBX separados. Apague o objeto Icosphere oculto de 1,90 m depois de importar, porque ele sobrevive ao select all e delete.
- Use os 18 personagens Kenney Blocky Characters para figurantes e multidões de cidade e de fantasia. Use os 24 animais Kenney Cube Pets para bicho de estimação, animal de fazenda e animal da história. O gato foi validado com 1.246 vértices.
- Importe o GLB e abra o Action Editor para ver as ações que vieram no arquivo. Atribua a ação ao armature com animation_data.action e empurre a ação para o NLA quando precisar misturar duas ações ou repetir a ação em loop.
- Ajuste a escala de tempo da faixa do NLA para casar a ação com a duração real da fala, medida da transcrição. Nunca estique a ação com escala uniforme no vídeo inteiro. Leia a regra de sincronia em [montagem](montagem.md).
- Combine a ação pronta com keyframes próprios nos pivôs quando o gesto precisar de intenção. A ação pronta é a base e o gesto com intenção vem por cima. A ação pronta sem intenção vira boneco andando sem motivo.
- Confira a ação pronta no frame de teste antes do render. A ação errada no personagem certo quebra a cena do mesmo jeito que o personagem errado.

### O rig do personagem

- Modele o boneco com um pivô vazio por parte do corpo: cabeça, braço direito, braço esquerdo, tronco, perna direita e perna esquerda.
- Anime cada pivô com keyframes a cada 12 a 24 frames. A 24 frames por segundo, 12 frames é meio segundo.
- Nunca anime o boneco inteiro como um bloco só. O movimento nasce das partes.

### Receitas de gestos

Copie estas receitas. Cada gesto tem 3 tempos: preparar, fazer e voltar. O tempo de preparar é a antecipação do princípio 2. O tempo de fazer usa easing do princípio 6. O tempo de voltar usa follow-through do princípio 5.

- Apontar: frame 0, braço direito abaixado. Frame 12, braço levanta e aponta. Frame 36, braço segura apontando. Frame 48, braço desce.
- Virar a cabeça: frame 0, cabeça de frente. Frame 12, cabeça vira para o assunto. Frame 36, cabeça segura. Frame 48, cabeça volta.
- Surpresa: frame 0, posição neutra. Frame 8, braços abrem rápido e cabeça vai para trás. Frame 24, segura. Frame 40, volta devagar.
- Andar: pernas alternadas a cada 12 frames, braços balançando em oposição, tronco inclinado para frente. O personagem anda no lugar e o cenário passa, ou anda em caminho reto curto.
- Pegar e segurar: frame 0, braço estende em 12 frames. Frame 12, mão fecha. Frame 24 em diante, o objeto segue a mão, preso ao pivô dela.
- Reagir com o corpo inteiro: cabeça, braços e tronco se movem juntos no mesmo gesto. Um gesto só de cabeça é pouco.

### Movimento do assunto

- O assunto se move no próprio caminho curvo, nunca em linha reta. Use curva Bezier para o caminho. O caminho curvo é o princípio 7, arcos.
- Um peixe nada em S, com a cauda balançando de um lado para o outro a cada 6 frames.
- Uma porta abre em arco, com o pivô na dobradiça.
- Uma pedra rola e quica, com rotação e pequenos saltos. O quique usa squash and stretch do princípio 1.
- Um mecanismo gira peça por peça: cada peça entra em cena e gira no seu tempo, nunca todas ao mesmo tempo.
- O assunto nunca desliza no ar sem vida. Se ele flutua, está errado.

### Montagem passo a passo em 3D low-poly

- Monte a obra na ordem física, de baixo para cima: fundação, pilar, viga, tabuleiro e acabamento. Cada peça entra em cena no seu tempo, com stagger seguindo a posição física da camada, nunca todas ao mesmo tempo.
- Mostre a tentativa errada antes da certa. A tábua enverga e quebra com o carro, a viga cede no meio do vão, e só então entra o pilar que resolve. O erro visível é o que faz o espectador ficar para ver a solução.
- Abra a vista em corte quando a peça fica enterrada. Corte o solo ou o rio para mostrar a estaca cravada até a rocha, com a água e a terra em camadas planas ao redor.
- Acenda a palavra-chave na tela no segundo em que a peça pousa. Uma palavra por passo, como pilar, estaca e junta de dilatação, em texto grande no centro da zona segura.
- Marque cada passo com certo ou errado no mesmo segundo da fala. Acerto ganha marca verde e erro ganha marca vermelha, sem texto longo.
- Feche com a prova de carga. O carro atravessa a ponte pronta, a porta abre, o elevador sobe com peso, e a obra aguenta. Sem prova final, a montagem parece desenho e não construção.
- Separe as peças em vista explodida quando o mecanismo tem mais de 3 partes. Afaste as peças com um só gap compartilhado e remonte na ordem inversa, com power3.inOut em 0,7 a 1 segundo.
- Anime cada peça com antecipação, easing e assentamento. A peça entra de cima com ease-out, achata levemente ao pousar e assenta com follow-through de 2 a 4 frames.
- Rejeite a cena quando as peças entram todas juntas, quando a ordem física está invertida, quando a tentativa errada não aparece e quando a prova final falta.

### Movimento do ambiente

- Água com ondas: desloque os vértices da superfície com uma função de seno no tempo, ou anime a textura.
- Árvores balançando: rotação leve no pivô do tronco, de 2 a 3 graus para cada lado.
- Poeira e partículas: objetos pequenos caindo ou subindo com velocidade constante.
- Luz piscando: energia da luz variando em keyframes.
- O ambiente se mexe o tempo todo, mesmo quando o personagem está parado falando.

### Linguagem de câmera nesta trilha

- Corte a cada 2 a 4 segundos: vários ângulos na mesma cena, com marcadores de câmera na linha do tempo.
- Zoom com TRACK_TO no mecanismo: a câmera aponta para o assunto e se aproxima.
- Close-up no rosto: para reação e surpresa, com o personagem grande no quadro.
- Plano aberto: só para estabelecer o lugar, no máximo 2 segundos.
- A câmera fica na altura do personagem, olhando de frente ou em três quartos. Nunca de longe e de cima com o personagem pequeno no meio da paisagem vazia.
- Amorteça a câmera com lerp exponencial em vez de pulo seco. A câmera persegue o alvo com 1 menos exponencial de menos lambda vezes delta, com lambda de 3 a 8. Fonte: threejs-animation, sintetizado com palavras próprias, em https://github.com/iart-ai/webgl-animation-skills

### Render

- Render em Cycles CPU, 480x854, 6 samples, sem denoise, em PNGs. Custo real medido: cerca de 5 segundos por frame, cerca de 20 minutos por clipe de 10 segundos, cerca de 2 horas por Short de 60 segundos, em lote e sem supervisão.
- O Eevee não funciona nesta máquina porque falta libEGL. Não prometa render rápido por Eevee.
- Não renderize em paralelo. A RAM livre é de cerca de 480 MB.
- Renderize sempre em PNGs e nunca em MP4 direto do Blender, para retomar do frame onde parou.
- Antes do render completo, renderize 1 frame de teste e confira: o frame não está preto, o personagem está grande no quadro e o mecanismo está no centro.

### Fórmula de cena e aceite na trilha 3D por código

- Monte cada cena com 1 script por cena, com o rig de pivôs, os keyframes nas poses extremas e nas poses de passagem, a câmera com TRACK_TO no assunto e 1 frame de teste aprovado antes do render completo.
- Use a ação pronta da biblioteca quando o gesto já existir e confira a ação no frame de teste antes do render. Combine a ação pronta com keyframes próprios quando o gesto precisar de intenção.
- Escreva cada gesto com 3 tempos, preparar, fazer e voltar, com antecipação de 3 a 6 frames antes da ação e follow-through de 2 a 4 frames depois da parada.
- Anime o assunto no próprio caminho curvo com curva Bezier e nunca em linha reta. Anime o ambiente o tempo todo, mesmo quando o personagem está parado falando.
- Corte a câmera a cada 2 a 4 segundos com marcadores na linha do tempo e sincronize cada corte com a palavra que ele ilustra. Amorteça a câmera com lerp exponencial e nunca com pulo seco.
- Sincronize os keyframes com o tempo real da fala, medido da transcrição, e nunca com a estimativa do storyboard. Ajuste a escala de tempo da faixa do NLA para casar a ação pronta com a duração real da fala.
- Aplique o checklist de aceite abaixo em cada cena antes do render completo. Cena que falha em 1 item volta para o script.
- Aprove quando o personagem faz pelo menos 2 gestos diferentes com intenção e o assunto se move em caminho curvo.
- Aprove quando a água, as árvores, a poeira ou a luz se movem no fundo e a câmera corta a cada 2 a 4 segundos.
- Aprove quando o frame de teste mostra o personagem grande no quadro e o mecanismo no centro, com a ficha do personagem idêntica à cena anterior.
- Aprove quando cada ação narrada aparece visível na tela no mesmo segundo da fala, com desvio máximo de 0,5 segundo.
- Rejeite quando o personagem desliza sem andar, quando o assunto flutua sem vida, quando a câmera só faz zoom lento e quando a cena é paisagem aberta e vazia com o personagem pequeno no meio.
- Rejeite quando o render de teste sai preto, quando a ação pronta está errada para a cena e quando o movimento usa interpolação linear sem easing.

## Trilha C — Infográfico 2D por código com Python e PIL

### Como funciona

- Um script `render_cenaNN.py` por cena, numa pasta `scripts2d`, com uma biblioteca partilhada `lib_info.py` que guarda a paleta, o tamanho do quadro, o fps e as funções de desenho.
- Cada script desenha os frames da cena em PNG a 60 fps com PIL, com 40 fps como mínimo aceitável. O ffmpeg monta o MP4 de cada cena e depois concatena todas as cenas.
- A legenda é queimada com o filtro `subtitles` do ffmpeg, a partir do arquivo `.ass` da transcrição real da narração.
- Ferramentas: Python com PIL 10.2.0 e numpy 1.26.4, e ffmpeg. Sem geração de vídeo por IA, porque a IA não acerta texto e números exatos.
- O estudo de caso completo, com paleta, pipeline e números medidos, está em [estudo de caso do Laboratório Curioso](estudo-caso-laboratorio-curioso.md).
- Velocidade medida: a cena 1 de teste do vídeo 1 rendeu 240 frames em 10,4 segundos, ou cerca de 23 quadros por segundo. As 72 cenas levaram de 20 a 30 minutos no total. É cerca de 50 vezes mais rápido que o Blender. Um Short de 60 segundos a 60 fps, com 3.600 quadros, levaria cerca de 2,6 minutos em 720p pelo PIL. O PIL em vertical não foi medido, então não prometa número nenhum para ele em vertical sem medir.

### Opção B: renderizador CDP com HTML e CSS

- A opção B do trilho 2D é o renderizador CDP, um script `render.mjs` sem dependências npm que abre uma página HTML num Chromium sem tela, chama `renderFrame(n)` para cada quadro e fotografa com o Chrome DevTools Protocol. A documentação completa, com requisitos, uso e o teste medido, está em [renderizador CDP](renderizador-cdp.md).
- Use a opção B quando a cena tem muito texto, com títulos longos, parágrafos, listas e números grandes com tipografia cuidada. O HTML e o CSS resolvem quebra de linha, alinhamento e fontes do sistema sem desenhar letra por letra.
- Use a opção A, o PIL, quando a cena é um diagrama com geometria exata, com formas, linhas e setas desenhadas por coordenadas. O PIL é o caminho provado em produção, com as 72 cenas do vídeo 1 do O Laboratório Curioso.
- Nunca misture as duas opções no mesmo vídeo. Escolha uma na entrevista e siga só ela até o fim.
- Velocidade medida da opção B no teste de 2026-11-06, em sequência: 48 quadros em 4,28 segundos de parede em JPEG, 11,20 fps (interno 13,01), e em 4,58 segundos em PNG, 10,48 fps (interno 12,11), em 1280x720. Em vertical 1080x1920, 120 quadros em 12,22 segundos em JPEG, 9,82 fps, e em 75,40 segundos em PNG, 1,59 fps. É mais lenta que o PIL, então some o tempo antes de prometer prazo.
- As receitas de cena e os 12 princípios desta trilha valem iguais nas duas opções. A contagem do número, o easing e o carimbo seguem as mesmas regras abaixo.

### Histórias 2D com renderFrame(n)

- A variante de histórias usa a opção B, o renderizador CDP, com uma página HTML por cena e a função `renderFrame(n)` desenhando o quadro n. O protagonista é fixo, com a ficha de `$personagem`, e o formato mãe é o vídeo vertical 1080x1920.
- Use esta variante quando o vídeo é uma história animada narrada, uma história interativa com escolha no final ou um vídeo vertical curto para TikTok, Reels e Shorts.
- Os 4 estilos de história são cinema e morph, promo premium, cena interativa sem cortes e tipografia clara. Cada estilo tem formato, duração, voz e momento certo de uso em [quadros de movimento](quadros-movimento.md).
- Aplique as 5 regras do movimento profissional em cada cena: tipografia protagonista, micro-evento a cada 0,5 a 1,5 segundo, morphs, fundo vivo com profundidade e som em cada animação. As regras completas estão em [quadros de movimento](quadros-movimento.md).
- A história interativa usa um nível por vídeo, com o protagonista ganhando um poder por nível e uma escolha com 2 opções nos últimos 5 segundos. O próximo vídeo continua a opção mais votada nos comentários.
- A sincronia é palavra por palavra: o gesto e a palavra-chave acendem no quadro exato em que a palavra começa na narração, com os tempos de palavra da transcrição real. Nunca use uma escala uniforme no vídeo inteiro. Leia a regra em [montagem](montagem.md).
- O padrão é 60 fps, com 40 fps como mínimo aceitável. Nunca entregue abaixo de 40 fps. Some o tempo de render antes de prometer prazo. As velocidades medidas estão em [quadros de movimento](quadros-movimento.md).

### Como animar neste estilo

- Cada cena tem 1 diagrama e 1 ideia. O diagrama entra peça por peça, nunca inteiro e parado. Isso é encenação, o princípio 3.
- O número grande conta de zero até o valor final com easing, nunca aparece pronto de uma vez. Use ease-out cúbico na contagem.
- O carimbo de VERDADE ou MENTIRA cai no painel com antecipação e exagero, no mesmo segundo da palavra na narração. O carimbo achata um pouco ao bater, que é squash and stretch.
- Linhas e setas crescem na direção do movimento, seguindo arcos, não retas.
- Gráficos de barra sobem com aceleração e desaceleração. Uma barra que sobe em velocidade constante parece robótica.
- Elementos secundários, como partículas e linhas de fundo, chegam alguns frames depois do elemento principal e oscilam antes de assentar. Isso é follow-through.
- A câmera neste estilo não existe como objeto 3D. O movimento vem de zoom no diagrama, de corte entre diagramas e de deslocamento dos elementos no quadro.
- A duração de cada cena é a duração real da fala correspondente, medida da transcrição. Nunca use a duração estimada do storyboard. A regra completa está em [montagem](montagem.md).
- Antes do render completo de cada cena, renderize 1 frame de teste e confira: o frame não está preto, o diagrama está no centro e a legenda cabe no quadro.

### Receitas de cena neste estilo

- Número grande: o número começa em zero, conta com ease-out até o valor final, dá um pequeno pulso de exagero ao chegar e fica parado por 1 segundo para o espectador ler.
- Diagrama que se monta: cada peça do diagrama entra em cena no seu tempo, uma por vez, com uma linha ligando a peça anterior. Nada entra tudo ao mesmo tempo.
- Comparação lado a lado: os dois lados entram por arcos opostos, o número de cada lado conta ao mesmo tempo e o vencedor ganha um destaque em laranja.
- Linha do tempo: a linha cresce da esquerda para a direita, cada evento surge na linha com um pulso quando a narração chega nele.
- Carimbo de veredito: o painel fica vazio por 1 segundo, o carimbo cai com antecipação, achata ao bater e o texto da palavra-chave acende em laranja.

### Checklist de aceite na trilha 2D por código

- Aplique as receitas de cena e os 12 princípios iguais nas duas opções, PIL e CDP, e nunca misture as duas no mesmo vídeo.
- Use as receitas GSAP de [quadros de movimento](quadros-movimento.md) para os easings, com power2.out nas entradas, power3.inOut nos morphs, back.out(1.7) nos títulos e stagger de 6 a 10 quadros nas entradas em cascata.
- Amarre cada movimento ao tempo real da palavra na transcrição, com o gesto e a palavra-chave acendendo no quadro exato em que a palavra começa.
- Aplique o checklist de aceite abaixo em cada cena antes do render completo. Cena que falha em 1 item volta para o script.
- Aprove quando o diagrama muda pelo menos 2 vezes na cena e o número conta de zero até o valor final com easing, sem aparecer pronto de uma vez.
- Aprove quando o carimbo cai no mesmo segundo da palavra na narração, com antecipação, squash no impacto e texto da palavra-chave acendendo em laranja.
- Aprove quando o fundo tem 3 camadas com parallax e se move o tempo todo, e quando há um micro-evento visível a cada 0,5 a 1,5 segundo.
- Aprove quando o frame de teste mostra o diagrama no centro, a legenda cabendo no quadro e o título medido com o helper medeTexto sem estourar 1000 px de largura.
- Aprove quando cada ação narrada tem o diagrama correspondente na tela no mesmo segundo da fala, com desvio máximo de 0,5 segundo.
- Rejeite quando o diagrama entra inteiro e parado, quando o número aparece pronto, quando o texto estoura a borda e quando a cena passa 3 segundos sem mudança visível.
- Rejeite quando o morph liga ideias sem relação, quando o sub-estilo muda no meio do vídeo e quando o movimento usa easing linear.

## Trilha D — Animação 3D estilo Pixar por IA

### Como funciona

- Um clipe é uma cena de cerca de 10 segundos, gerada por IA com o mesmo método da trilha realista, com o visual 3D estilo Pixar no prompt em vez do visual realista. Um Short de 60 segundos precisa de cerca de 6 clipes. Duas partes por dia, como o Terror da Meia-Noite, precisam de cerca de 12 clipes por dia.
- Cada clipe nasce de um prompt com 5 partes: o bloco de estilo Pixar travado, a ficha do personagem, o que ele faz, o que acontece no ambiente e como a câmera se move.
- O modelo é o Crânio Era, @cranioera no TikTok: a série História do Tomate tem 12 episódios, com um protagonista fixo, um tomate, e um arco dramático com cliffhanger por parte. A pesquisa de 06/11/2026 registrou cerca de 1,6 milhão de seguidores na página do TikTok e cada episódio com 8,5 a 18,3 milhões de views, com cerca de 142 milhões de views no total da série, segundo vídeos que explicam os ganhos do criador em outubro de 2026. Os números por episódio não foram verificados na conta oficial, então cite como relatado por terceiros, nunca como número oficial.
- A produção é rápida e o custo é por crédito, igual à trilha realista. Verifique o saldo de créditos antes de gerar e some os créditos da frequência prometida antes de fechar a agenda. Gere em lote por parte, na ordem do storyboard, para não parar no meio.

### Por que o estilo funciona

- O protagonista é simples e marcante. O tomate é uma forma só, com uma cor só, e reconhecível de longe. A simplicidade é o que segura a continuidade, porque a IA reproduz uma forma simples com muito menos erro que um rosto humano detalhado.
- A história é um drama seriado, uma novela em partes. Cada parte é um capítulo com arco, reviravolta e cliffhanger. O espectador volta pela história, não pelo fato.
- O protagonista narra a própria história em primeira pessoa. A voz é a do personagem, não a de um narrador externo. O narrador é o herói.
- A luz é de cinema com duas cores, uma quente e uma fria. O contraste de luz marca o clima antes de qualquer detalhe. No clipe de teste do Terror da Meia-Noite, a lamparina laranja contra a luz azul da lua faz o terror sem nenhum objeto de terror na tela.
- Os personagens secundários seguem a mesma lógica do protagonista. Cada um é uma forma só com uma cor só, como a abóbora musculosa, a melancia de terno e o limão de terno. Forma simples com cor só é o que a IA consegue repetir.

### A ficha do personagem e o bloco de estilo travado

- Escreva a ficha do personagem uma vez, com $personagem, e copie em todos os prompts sem mudar uma palavra: idade, forma da cabeça, cabelo, olhos, boca, roupa, calçado, objeto que ele carrega e altura.
- Escreva o bloco de estilo uma vez e copie em todos os prompts, sem mudar uma palavra: animação 3D estilo Pixar, personagens estilizados com olhos grandes e expressivos, proporções de desenho animado, superfícies lisas, luz de cinema, profundidade de campo suave e cores saturadas.
- Trave a paleta do canal e uma cor de destaque por capítulo, como manda [ambientação](ambientacao.md). A roupa do personagem tem uma cor fixa e o destaque tem uma cor fixa. Não troque a cor da roupa para combinar com o capítulo.
- Trave a luz: luz quente de um lado e luz fria do outro, em todos os clipes. A luz que muda de cor de um clipe para o outro quebra a continuidade do mundo.
- Gere a primeira imagem do personagem e use ela como referência de imagem para os próximos clipes, quando a ferramenta permitir.
- Use a mesma semente quando a ferramenta permitir.
- Dê ao protagonista 2 traços marcantes e simples, como uma forma só, uma cor só e um objeto fixo. Sem traço marcante, a IA não tem o que repetir e cada clipe gera um rosto diferente.

### Fórmula de prompt

- A ordem do prompt é bloco de estilo, ficha do personagem, ação, ambiente e câmera.
- Prompt fraco: "um menino numa casa escura". Prompt forte: "animação 3D estilo Pixar, menino de 12 anos com cabelo preto bagunçado, olhos grandes, moletom azul-marinho, relógio de parede marcando meia-noite, a porta do corredor se abre sozinha rangendo, luz fria da lua entrando pela janela, close-up no rosto assustado do menino".
- Um prompt bom tem pelo menos 1 verbo de ação do personagem, 1 movimento do assunto, 1 movimento do ambiente e 1 movimento de câmera.
- Coloque a expressão no prompt, porque o rosto estilizado carrega a emoção: olhos arregalados de medo, boca entreaberta, sobrancelha levantada.
- Coloque o movimento do assunto no prompt: a porta abre, o relógio marca meia-noite, o objeto cai, a sombra se move.
- Coloque o movimento do ambiente no prompt: a poeira cai, a cortina balança, a luz pisca, a névoa entra pela janela.
- Coloque a câmera no prompt: close-up no rosto, zoom lento, travelling, câmera parada, plano médio.
- Nunca peça texto na tela para a IA gerar. Texto na tela é feito na edição, depois.
- Nunca peça uma ação física complicada, como pegar um objeto pequeno e abrir ele. Divida em 2 clipes.
- Nunca misture realista com Pixar no mesmo prompt. A palavra realista não entra em nenhum prompt desta trilha. Um prompt com pessoa de verdade e estilo Pixar juntos dá um meio-termo que não é nenhum dos dois.

### Reação cai antes da palavra

Fonte: cartoon-3d-short, sintetizado com palavras próprias, em https://github.com/mromidev/claude-animated-shorts

- Faça cada reação visual cair de 0 a 3 quadros antes da palavra correspondente. Reação que cai depois da palavra lê como atraso.
- Empurre o hold em 0,15 a 0,35 por cento por quadro e em 0,6 por cento por quadro nas palavras de impacto. O push lento segura o quadro sem congelar ele.
- Trave as constantes de tempo da imagem antes de fazer o som. Qualquer mudança de timing depois obriga refazer o áudio inteiro.
- Monte o Short de 55 a 70 segundos com este mapa de beats. Gancho, cenário, escalada em 3 a 4 beats, snap que quebra tudo, dupla sorte e azar, explicação por analogia do dia a dia, consequência e callback no final.
- Nunca descreva na tela o que o espectador já vê. A narração soma e a imagem mostra.

### Continuidade entre clipes, o maior desafio desta trilha

- Confira rosto, roupa, objeto e altura em cada clipe gerado. Se o personagem mudou de rosto, de roupa ou de idade, gere de novo.
- Compare o frame do clipe novo com o frame do clipe anterior lado a lado antes de montar. A comparação lado a lado mostra a troca de rosto que o olho sozinho não percebe.
- Regra das 3 tentativas: se o clipe falhar 3 vezes, simplifique a ação ou o enquadramento. Nunca aceite o personagem errado para fechar a parte.
- O personagem secundário segue a mesma regra: ficha fixa, forma simples e cor só, copiadas em todos os prompts em que ele aparece.
- O cenário segue a mesma regra: a mesma descrição de lugar, a mesma paleta e a mesma luz em todos os clipes da mesma parte.
- A continuidade é o que separa uma série de um monte de clipes soltos. O Crânio Era segura o tomate igual em 12 episódios porque o tomate é uma forma simples com ficha fixa. O rosto estilizado erra menos que o rosto realista, porque o exagero esconde o erro pequeno, mas mesmo assim confira cada rosto.

### Pipeline de produção

- Crie a bíblia da série antes do roteiro da parte 1, com premissa, arco completo, regras do mundo e o bloco de cada personagem, e atualize a bíblia ao fim de cada parte. Leia o guia em [séries](series.md).
- Escreva o roteiro da parte com o cliffhanger já no fim, antes de gerar o primeiro clipe. Uma parte sem cliffhanger não traz o espectador de volta.
- Gere a narração antes dos clipes, em uma só passada suave, com a voz fixa do canal. A narração em pedaços com pausas bruscas denuncia a voz sintética.
- Transcreva a narração com tempos de palavra e meça a duração real de cada cena. A montagem usa os tempos reais, nunca uma escala uniforme. Leia a regra em [montagem](montagem.md).
- Monte o storyboard com 1 cena igual a 1 clipe de cerca de 10 segundos, com 6 clipes por parte de 60 segundos, e gere os clipes em lote por parte, na ordem do storyboard.
- Produza 1 clipe de teste com $teste e mostre ao usuário antes de produzir a parte inteira. O teste aprovado do Terror da Meia-Noite, em 06/11/2026, tem 10 segundos em 720x1280: relógio marcando meia-noite e porta se abrindo sozinha no corredor, com o menino de moletom escuro reagindo. O menino do clipe é só teste de estilo, não é o protagonista aprovado.
- Monte o áudio completo a -14 LUFS, com narração, efeitos e música, e queime a legenda karaokê, com a palavra falada em amarelo e o resto em branco.
- Verifique a sincronia em pelo menos 6 inícios de cena e faça o teste do mudo antes de entregar. Menos de 3 movimentos visíveis em 10 segundos sem som é clipe parado.

### Linguagem de câmera nesta trilha

- Close-up no rosto: para reação e surpresa, com os olhos grandes carregando a emoção.
- Close-up no assunto: para mostrar a porta abrindo, o objeto caindo ou a sombra se movendo.
- Zoom lento: para revelar o lugar, no máximo 2 segundos.
- Travelling: para acompanhar o personagem andando pelo corredor.
- Plano médio: o plano padrão da história, com o personagem da cintura para cima e o assunto ao lado.
- Plano aberto: só para estabelecer o lugar, no máximo 2 segundos, e nunca com o personagem pequeno no meio da paisagem vazia.
- Corte a cada 2 a 4 segundos, com o corte no mesmo segundo da palavra que ele ilustra.

### O que a IA faz bem e o que faz mal

- Faz bem: expressões faciais exageradas, luz de cinema, ambientes detalhados, movimento de tecido e cabelo, reações de medo e surpresa.
- Faz mal: mãos, texto na tela, física de objetos, continuidade de roupa e cenário, contar dedos e letras.
- O rosto estilizado erra menos que o rosto realista, mas confira cada rosto mesmo assim, porque um olho torto num rosto de desenho animado aparece mais que num rosto realista.

### Quando rejeitar um clipe

- Rejeite quando nada se move nele.
- Rejeite quando o personagem mudou de rosto, de roupa ou de idade.
- Rejeite quando o estilo saiu do Pixar para o realista no meio da parte.
- Rejeite quando a luz mudou de cor de um clipe para o outro.
- Rejeite quando a física quebra: objeto atravessando parede, mão com 6 dedos, porta abrindo para o lado errado.
- Gere de novo com a ação mais forte no prompt. Se falhar 3 vezes, mude a ação para uma mais simples.

### Checklist de aceite na trilha Pixar

- Planeje cada beat com cerca de 8 segundos e 1 ação clara por beat. Corte a cauda do clipe de 10 segundos na montagem. Leia a regra completa na seção Clipes Pixar de 8 segundos por padrão deste guia.
- Estruture cada beat em 3 tempos com estabelecer, transformar e entregar o clímax, e exija 4 ou mais dispositivos visuais por clipe.
- Faça cada reação visual cair de 0 a 3 quadros antes da palavra correspondente. Reação que cai depois da palavra lê como atraso.
- Gere uma só narração para a parte inteira, com a voz fixa do canal, e nunca gere narração por beat.
- Compare o frame do clipe novo com o frame do clipe anterior lado a lado antes de montar e confira rosto, roupa, objeto, altura, paleta e luz.
- Aplique a regra das 3 tentativas. Se o clipe falhar 3 vezes, simplifique a ação ou o enquadramento. Nunca aceite o personagem errado para fechar a parte.
- Aplique o checklist de aceite abaixo em cada clipe antes de montar. Clipe que falha em 1 item volta para regeneração.
- Aprove quando o personagem faz 1 gesto com intenção e o assunto se move no mesmo segundo da narração, com a reação caindo antes da palavra.
- Aprove quando o ambiente se move o tempo todo, a câmera corta a cada 2 a 4 segundos e a luz quente de um lado e fria do outro se mantém.
- Aprove quando o rosto, a roupa, o objeto e a altura batem com o clipe anterior na comparação lado a lado e o estilo continua Pixar do começo ao fim.
- Aprove quando a ação narrada aparece visível na tela no mesmo segundo da fala, com desvio máximo de 0,5 segundo.
- Rejeite quando nada se move, quando o personagem mudou, quando o estilo saiu do Pixar para o realista, quando a luz mudou de cor, quando a física quebra e quando o beat carrega 2 ações ao mesmo tempo.
- Rejeite quando o clipe de 10 segundos morph no fim. Planeje o beat com 8 segundos e corte a cauda na montagem.

## Ritmo dentro de um clipe de 10 segundos

Um clipe de 10 segundos tem 4 tempos. Cada tempo tem uma função. Se um tempo não tem movimento, o clipe fica parado naquele trecho.

- 0 a 2 segundos, estabelecer: plano aberto por no máximo 2 segundos, assunto grande no quadro, o espectador entende onde está e o que vai ver.
- 2 a 6 segundos, ação principal: o gesto do personagem e o movimento do assunto acontecem juntos, no mesmo segundo da narração. Este é o coração do clipe.
- 6 a 9 segundos, reação e pagamento: close-up no rosto reagindo ou close-up no mecanismo funcionando. O espectador vê o resultado da ação.
- 9 a 10 segundos, transição: o personagem olha para o próximo assunto ou a câmera corta para o próximo clipe. Nunca termine o clipe parado.

No trilho 2D, o ritmo é o mesmo, com diagrama no lugar do personagem: estabelecer o diagrama, montar as peças, revelar o número ou o carimbo, e cortar para o próximo diagrama. No trilho Pixar por IA, o ritmo é o mesmo do trilho realista, com o rosto estilizado carregando a reação: estabelecer a cena, fazer a ação, fechar no rosto reagindo e cortar para o próximo clipe.

Nunca passe mais de 4 segundos sem uma mudança: um gesto novo, um corte de câmera, o assunto se movendo ou o ambiente mudando. O ritmo do clipe é o que segura o espectador entre um fato e o próximo.

## Receitas de cena

Copie estas receitas quando o roteiro pedir um destes momentos. Cada receita diz o que o personagem faz, o que o assunto faz, o que o ambiente faz e como a câmera se move.

### Revelação, o assunto aparece

- Personagem: aponta para o lugar e abre os braços, surpreso.
- Assunto: surge de trás de uma rocha, de baixo da água ou de dentro da escuridão.
- Ambiente: a luz acende no assunto, poeira ou bolhas marcam a aparição.
- Câmera: zoom no assunto em 2 segundos, depois close-up no rosto surpreso.

### Mecanismo funcionando

- Personagem: acompanha cada peça com a cabeça e aponta para a peça que está girando.
- Assunto: cada peça entra em cena e gira no seu tempo, nunca todas ao mesmo tempo.
- Ambiente: luz no mecanismo, peças de fundo paradas para não distrair.
- Câmera: close-up no mecanismo, com TRACK_TO seguindo a peça que se move.

### Comparação lado a lado

- Personagem: fica no meio dos dois assuntos, olhando de um para o outro.
- Assunto: os dois assuntos no quadro ao mesmo tempo, um de cada lado.
- Ambiente: fundo simples, para a comparação ser o foco.
- Câmera: plano médio com os dois no quadro, depois close-up em cada um, alternando.

### Escala, o quanto é grande ou fundo

- Personagem: fica pequeno de propósito por 2 segundos, só para dar a escala.
- Assunto: o lugar enorme ao redor, como a lagoa, a montanha ou a caverna.
- Ambiente: neblina ou profundidade para marcar a distância.
- Câmera: plano aberto por 2 segundos, depois close-up no detalhe com o número na tela.

### Mistério, o que não dá para ver

- Personagem: segura a lanterna, olha para a escuridão, com expressão de tensão.
- Assunto: aparece só em parte, com a luz da lanterna revelando um pedaço por vez.
- Ambiente: escuridão, som abafado, partículas flutuando.
- Câmera: close-up no rosto tenso, depois close-up no pedaço revelado, sem mostrar tudo.

### Descoberta guiada pelo olhar

- Personagem: olha para o assunto primeiro, depois aponta, depois reage. O olhar guia o espectador antes do gesto.
- Assunto: aparece em parte, revelado aos poucos, com a luz acendendo nele quando o personagem olha.
- Ambiente: luz e contraste marcando o assunto, fundo simples para não disputar o olhar.
- Câmera: close-up no rosto olhando, depois close-up no assunto revelado. É a receita da direção do olhar de Glebas, 2008.

### Terror, o susto com o esqueleto

- Personagem: o esqueleto anda com a ação pronta de caminhada e para de repente quando vê o fantasma.
- Assunto: o fantasma surge de trás da lápide e flutua em direção à câmera.
- Ambiente: cemitério com névoa, tochas acesas e luz de noite do HDRI de noite.
- Câmera: close-up no rosto do esqueleto, depois corte para o fantasma surgindo.

### Cidade viva, multidão e trânsito

- Personagem: a multidão de personagens de blocos anda pela calçada e olha para o trem passando.
- Assunto: o trem passa pela rua e o carro freia no cruzamento.
- Ambiente: rua de bairro com prédios, semáforo e carros estacionados.
- Câmera: plano médio na rua com a multidão e o trem, depois close-up no mecanismo do trem.

### Espaço real, a missão da NASA

- Personagem: o astronauta real da NASA flutua e aponta para o telescópio.
- Assunto: o telescópio Hubble gira devagar e o painel solar abre peça por peça.
- Ambiente: base espacial low-poly com estrelas e luz forte de sol.
- Câmera: plano aberto na estação, depois close-up no telescópio girando. Dê crédito à NASA na descrição do vídeo.

## Checklist de animação por clipe de 10 segundos

Antes de entregar qualquer clipe, confira estes 8 itens. Se algum faltar, refaça o clipe.

1. Personagem: pelo menos 2 gestos diferentes. No trilho 2D, o diagrama muda pelo menos 2 vezes.
2. Assunto: movimento próprio em caminho curvo, não em linha reta.
3. Ambiente: algo se move no fundo o tempo todo.
4. Câmera: corte ou zoom a cada 2 a 4 segundos.
5. Expressão: o rosto reage à ideia, não fica neutro. No trilho 2D, o número ou o carimbo reage com exagero.
6. Sincronia: o gesto acontece no mesmo segundo da narração.
7. Continuidade: mesmo personagem, mesma roupa, mesmo cenário do clipe anterior.
8. Teste do mudo: 3 ou mais movimentos visíveis em 10 segundos sem som.
- Confira o checklist de aceite da trilha do vídeo, na seção da trilha acima, antes de aprovar o clipe. O checklist genérico não substitui o checklist da trilha.

## Teste do mudo

Assista ao clipe sem som e conte os movimentos visíveis em 10 segundos. Menos de 3 movimentos é clipe parado. Refaça antes de mostrar ao usuário.

## Mascote do canal

O Mundinho é o apresentador do canal e nunca pode ficar parado um capítulo inteiro:

- Ele pisca, olha para os lados, aponta para o assunto e reage a cada fato.
- Use as 3 expressões da ficha do personagem: surpreso, pensando e animado.
- Em cada capítulo ele aparece pelo menos uma vez fazendo um gesto novo.
- Quando o capítulo for só paisagem, coloque o Mundinho no canto reagindo.
- Na trilha por código, o Mundinho usa o mesmo rig de pivôs do resto dos personagens.
- Na trilha realista, a ficha do Mundinho vai em todos os prompts, com a mesma descrição.
- Na trilha Pixar por IA, a ficha do mascote vai em todos os prompts, igual à trilha realista, com o bloco de estilo Pixar travado.
- Na trilha 2D, não há mascote. O diagrama é o apresentador. Se o canal usa o estilo 2D, não invente um boneco para ele. Na variante de histórias 2D, o protagonista é o apresentador e a ficha dele vem de `$personagem`, com as mesmas 5 poses fixas em todas as cenas.

## O que deu errado e não pode se repetir

Em 06/11/2026 o Lorenzo rejeitou um clipe de 10 segundos feito por código com a frase "0 animações". O que estava errado, verificado frame a frame:

- O personagem só inclinava a cabeça um pouco. Não gesticulava, não apontava, não virava a cabeça.
- O peixe deslizava no ar em vez de nadar. Ele não boquejava, não mexia a cauda, não seguia um caminho de nado.
- A água e as árvores não se mexiam. Nada no ambiente tinha movimento.
- A câmera só fazia um zoom lento. Não cortava, não fechava no assunto, não mudava de ângulo.
- A cena era uma paisagem aberta e vazia com o personagem pequeno no meio. O certo é cena fechada, com o personagem grande e o mecanismo no centro.

Nunca apresente uma cena de zoom lento como animada. Se o usuário disser que está parado, ele está certo. Refaça.

## Modelagem 3D para contar histórias

Esta seção aprofunda a trilha 3D por código com modelagem, rigging, composição, câmera e continuidade. Use as bibliotecas prontas em [bibliotecas 3D](bibliotecas-3d.md) para cenário e objetos e reserve a modelagem própria para o herói. Os livros da seção de abertura continuam valendo aqui. As regras novas abaixo vêm da documentação do Blender e de tutoriais de modelagem low-poly.

### Crie o personagem low-poly com formas simples

- Comece pelo bloco de formas antes de qualquer detalhe. Use um cubo para o tronco, uma esfera para a cabeça e cilindros para braços e pernas. Posicione e escale as formas até a silhueta ficar legível sem detalhe nenhum. Fonte: tutorial QuickPoly de modelagem low-poly, lido em 06/11/2026.
- Confira a silhueta em preto antes de colorir. Se o personagem não é reconhecível só pela sombra, volte ao bloco de formas.
- Faça a cabeça grande em relação ao corpo quando o personagem precisa ser lido em close no vídeo vertical. A cabeça grande carrega a expressão e o olhar.
- Faça o rosto com poucos elementos e cada um com uma função. Use dois olhos grandes e uma boca simples. O olho conta a emoção e a boca conta a reação. Não modele nariz, orelha e sobrancelha em personagem low-poly de vídeo curto.
- Dê uma cor de destaque para a roupa do personagem. O destaque é o que o espectador usa para achar o herói no meio da cena. No canal, o destaque é laranja sobre azul-marinho.
- Coloque um objeto fixo na mão ou no peito do personagem, como uma lupa ou uma engrenagem. O objeto vira assinatura visual e ajuda a reconhecer o personagem de costas ou de longe.
- Guarde polígonos para o rosto, as mãos e as juntas. O resto do corpo fica simples. Fonte: guia de design low-poly em my3dmodels.com, lido em 06/11/2026.
- Use o modificador Mirror no eixo X para modelar um lado só e garantir simetria perfeita. Fonte: tutorial QuickPoly de modelagem low-poly, lido em 06/11/2026.
- Mantenha quads nas zonas que dobram, como ombros, cotovelos e joelhos. Triângulos valem em áreas planas que nunca deformam. Fonte: tutorial QuickPoly de modelagem low-poly, lido em 06/11/2026.

### Faça o rigging básico para gestos

- Monte o rig com armature e ossos antes de animar qualquer gesto. O rig é o esqueleto que move a malha. Fonte: manual do Blender sobre armatures.
- Use poucos ossos e cada um com um nome claro. Use espinha, pescoço, cabeça, braço esquerdo, braço direito, perna esquerda e perna direita. Nomeie os ossos dos lados com `.L` e `.R` no fim para o Blender espelhar poses.
- Posicione as juntas dos ossos no meio das articulações do corpo. O osso do cotovelo fica no cotovelo e o osso do joelho fica no joelho. Junta fora do lugar dobra a malha no lugar errado.
- Ligue a malha ao armature com pesos automáticos e depois confira cada junta. Pinte os pesos à mão quando o braço puxar o peito junto ou a perna puxar a barriga.
- Anime os ossos em Pose Mode com keyframes de rotação. Rotacione a partir do pivô da junta para o braço descrever um arco, que é o princípio 7.
- Reuse o rig de pivôs vazios da skill quando o personagem for montado por código. O rig de pivôs já existe no exemplo e basta para apontar, virar a cabeça, andar e reagir.
- Suba para um rig com armature de verdade quando o personagem precisar de gestos novos em toda cena. O rig de pivôs serve para o herói fixo e o armature serve para personagens com mais movimento.
- Gere o rig humano com o complemento Rigify quando o personagem for humanoide e precisar de controles prontos. O Rigify cria um meta-rig, posiciona os ossos no corpo e gera os controles com um botão. Fonte: documentação do Rigify no manual do Blender.
- Aplique animações prontas de biblioteca no armature quando o gesto já existir. O pacote KayKit Adventurers traz 76 animações por personagem e o pacote KayKit Skeletons traz 95 animações por esqueleto, medidas na importação de teste em 06/11/2026 no Blender 4.5.3. O Mixamo riga humanoides e aplica milhares de clipes. Leia as licenças em [bibliotecas 3D](bibliotecas-3d.md).
- Grave as poses fixas do personagem antes de animar a cena. Use 5 poses fixas no máximo: neutro, curioso, surpreso, explicando e pensando. Toda cena usa uma dessas poses como base e varia só o gesto.

### Componha a cena em 3 camadas para contar a história

- Monte a cena em primeiro plano, plano do meio e fundo, como manda o guia de ambientação. O assunto fica no plano do meio e o mecanismo fica no centro do quadro.
- Coloque um elemento no primeiro plano em toda cena fechada. Uma folha, uma pedra ou a borda de uma mesa no canto do quadro dá profundidade imediata.
- Deixe o fundo simples e com menos contraste que o assunto. O olhar vai para o contraste, para o movimento e para o rosto. Fonte: Glebas 2008, seção de direção do olhar.
- Enquadre o assunto grande no quadro e o mecanismo no centro. Nunca use paisagem aberta e vazia com personagem pequeno no meio.
- Use a regra dos terços na câmera. Coloque o rosto do personagem ou o mecanismo em um dos cruzamentos dos terços e não no centro exato quando a cena tiver dois elementos.
- Dê uma entrada e uma saída visual para o olhar em cada cena. O olhar entra pelo elemento de maior contraste, percorre o mecanismo e sai pelo gesto do personagem.
- Mude a composição quando a ideia mudar. Revelação pede o assunto entrando de trás de um objeto. Mecanismo pede o close no centro. Comparação pede os dois lados no quadro. Escala pede o personagem pequeno por 2 segundos e depois o close no detalhe.

### Dirija a câmera 3D com linguagem de cinema

- Use o plano geral só para estabelecer o lugar, por no máximo 2 segundos, e nunca com o personagem pequeno no meio da paisagem vazia.
- Use o plano médio para mostrar o personagem da cintura para cima com o assunto ao lado. O plano médio é o plano padrão da história.
- Use o close-up no rosto para reação e surpresa e o close-up no mecanismo para mostrar a peça funcionando.
- Use o contra-plano quando dois personagens conversam ou quando o personagem olha para o assunto. Mostre o rosto de um lado e o assunto do outro, alternando a cada corte.
- Use o travelling para acompanhar o personagem andando. Mova a câmera junto com o personagem em vez de deixar ele atravessar o quadro parado.
- Use o corte a cada 2 a 4 segundos como regra da skill. Marque os cortes com câmeras diferentes na linha do tempo e troque a câmera ativa no marcador.
- Use o TRACK_TO na câmera com o alvo no assunto. A câmera aponta para o mecanismo o tempo todo e o zoom vira dolly-in sem perder o alvo.
- Mantenha a câmera na altura do personagem, olhando de frente ou em três quartos. Nunca filme de longe e de cima com o personagem pequeno no meio da paisagem vazia.
- Sincronize cada corte com a narração. O corte acontece no mesmo segundo da palavra que ele ilustra. Leia a regra de sincronia em [montagem](montagem.md).

### Modele um cenário que sirva para vários capítulos

- Monte o cenário em módulos que se repetem. Use paredes, pisos, pilares e portas como peças separadas e recombine as peças em cada capítulo.
- Use os pacotes modulares da biblioteca para isso. O KayKit Medieval Hexagon Pack tem 442 peças, o KayKit Dungeon Remastered tem 203 peças, o Kenney Factory Kit tem 143 peças, o KayKit Halloween Bits tem 126 peças, o KayKit Space Base Bits tem 114 peças, o Kenney Graveyard Kit tem 91 peças, o KayKit City Builder Bits tem 82 peças, o Kenney Building Kit tem 79 peças, o Kenney Castle Kit tem 76 peças, o Kenney Modular Space Kit tem 40 peças e o Kenney City Kit Suburban tem 40 peças. Leia o inventário em [bibliotecas 3D](bibliotecas-3d.md).
- Fixe o chão, a luz e a paleta do cenário no vídeo inteiro e troque só os objetos do capítulo. O espectador reconhece o lugar e entende que mudou o assunto, não o mundo.
- Modele cada capítulo como uma variação do mesmo lugar. A cozinha vira laboratório quando troca a mesa pelo balcão e a geladeira pelo fogão. A floresta vira caverna quando fecha a luz e troca as árvores por pedras.
- Guarde o cenário base em um arquivo blend separado e importe ele em cada cena com `libraries.load`. Não reconstrua o cenário em cada script.
- Desenhe o cenário para a câmera, não para o mundo inteiro. Modele só o que a câmera vê nos ângulos do storyboard. Parede de fundo que nunca aparece é polígono perdido no render.

### Mantenha o mesmo personagem igual em todas as cenas

- Congele a ficha do personagem antes do vídeo 1. Anote idade, cabelo, rosto, roupa, calçado, objeto e altura em metros. Copie a ficha em cada cena sem mudar uma palavra.
- Use o mesmo arquivo de personagem em todas as cenas. Importe o mesmo GLB ou o mesmo blend de base e não remodele o personagem por cena.
- Trave a paleta do personagem. A roupa tem uma cor fixa e o destaque tem uma cor fixa. Não troque a cor da roupa para combinar com o capítulo.
- Trave as proporções do personagem. A cabeça tem o mesmo tamanho em todas as cenas e o corpo tem a mesma altura. Meça com `objeto.dimensions` depois de importar.
- Trave as 5 poses fixas do personagem. Toda reação usa uma dessas poses como base. Pose nova em cada cena vira outro personagem.
- Confira a continuidade no checklist final. Compare o frame da cena 1 com o frame da última cena e confira rosto, roupa, objeto e altura. Se algo mudou, refaça a cena.
- Lembre que a continuidade é o maior desafio da trilha realista e o maior ganho da trilha 3D por código. No código, o mesmo arquivo garante o mesmo personagem. Não desperdice esse ganho remodelando o herói.

## Fórmula de prompt de vídeo por IA em 8 partes

Origem: ai-video em https://github.com/jordangaston/claude-plugins

- Monte o prompt de vídeo por IA nesta ordem. Meio, plano, ângulo, movimento, foco, assunto, luz e cor.
- Escreva o prompt como descrição cinematográfica fluida e não como rótulos literais. Mire 60 a 140 palavras por clipe.
- Trate movimento e assunto como obrigatórios. Sem os dois, o modelo devolve um JPEG que se mexe.
- Descreva o assunto como quem ou o quê mais o que faz ao longo do tempo. Um samurai sozinho desembainha e vira, um barista desliza a xícara enquanto o vapor sobe, um carro derrapa na curva com os pneus soltando fumaça.
- Mova a câmera quando o assunto estiver parado. Mova o assunto quando a câmera estiver parada. Um dos dois tem que se mover sempre.
- Nomeie o movimento de câmera com precisão. Push-in é diferente de zoom, travelling acompanha de lado e órbita circula o assunto.
- Use o foco para dirigir o olhar. Rack focus troca o foco entre assuntos, shallow focus isola o rosto e deep focus deixa tudo nítido.
- Diagnostique o clipe parado pelo prompt. Falta de movimento ou de ação do assunto é a causa quase sempre. Some movimento em vez de empilhar adjetivos.
- Aplique a fórmula nas trilhas realista e Pixar por IA. A ficha do personagem e o bloco de estilo continuam copiados em todos os prompts, como manda a trilha D.

## Modo I2V motion-first, quando já existe uma imagem inicial

Origem: ai-video em https://github.com/jordangaston/claude-plugins

- Use o modo I2V quando existir uma imagem inicial aprovada. O quadro inicial já carrega 70 a 80 por cento do visual.
- Descreva só o que muda ao longo do tempo. Ação e sequência, mudanças do assunto e do ambiente, um movimento de câmera, mudanças de luz e especificações técnicas.
- Mantenha o prompt I2V curto, com 25 a 70 palavras. Descrever demais a cena briga com a imagem inicial e causa deriva.
- Peça uma ação clara por clipe. Ele sorri devagar, acena e sai andando, ou acelera no túnel e depois derrapa.
- Escolha um só movimento de câmera por clipe. Órbita lenta de 360 graus, pull-out suave revelando a paisagem ou câmera parada com push-in sutil.
- Corte a descrição quando o vídeo sair brigado ou deformado. O excesso de detalhe sobre a cena pronta é a causa mais comum.

## Clipes Pixar de 8 segundos por padrão

Origem: pixar-style-ad em https://github.com/advibly/skills

- Planeje os beats da trilha Pixar com 8 segundos por padrão e corte a cauda do clipe de 10 segundos na montagem. Um beat de 10 segundos fica parado demais e começa a morph.
- Use a duração de 8 segundos em todos os clipes da parte. Mude a duração só quando a narração do beat pedir e registre a exceção no storyboard.
- Escreva uma ação clara por clipe. Um beat carrega uma ação e nunca duas.
- Calibre a narração do beat em 2,2 a 2,6 palavras por segundo. São cerca de 18 a 20 palavras por beat de 8 segundos, para nenhum clipe rodar em silêncio.
- Avise que a skill de origem usa o Advibly MCP, que é pago. Importe o método de direção e nunca prometa a ferramenta como se fosse gratuita.
- Mantenha a regra das 3 tentativas da trilha D. Se o clipe falhar 3 vezes, simplifique a ação ou o enquadramento.

## Uma única renderização de VO para todos os beats

Origem: pixar-style-ad em https://github.com/advibly/skills

- Gere uma só narração para a parte inteira, com a voz fixa do canal. Nunca gere VO por beat.
- Evite a VO por beat porque ela força compromisso de lip-sync e dá uma voz diferente a cada beat. Uma renderização é uma voz consistente em todos os beats.
- Alinhe esta regra com a regra da skill de gerar a narração em uma só passada suave. As duas dizem a mesma coisa e valem para todas as trilhas.
- Gere a música em uma só passada também. Uma trilha por parte, com arco narrativo, e nunca uma música por beat.
- Regenere a VO inteira quando o roteiro mudar. Remendo de frase solta denuncia a voz sintética.

## Regra still-first e cadeia de consistência

Origem: claymation-ad em https://github.com/brycefinnerty/ray-3.2-ad-generator

- Aprove o still antes de animar. Corrija look, texto e casting no still barato e só re-renderize os beats com falha.
- Siga a cadeia ficha, image-ref e start-frame. A ficha do personagem alimenta o image-ref de cada still e o still aprovado alimenta o start-frame de cada clipe. O modelo nunca improvisa o personagem só a partir de texto.
- Copie a ficha e o bloco de estilo em todos os prompts sem mudar uma palavra. A cadeia vale para as trilhas realista e Pixar e para qualquer protagonista fixo, como Cadu e Tuto.
- Guarde o texto no still e não no prompt de movimento. O modelo de vídeo segura texto já embutido e não cria texto limpo. Repita cada string curta e grande no prompt de movimento como texto que fica estático e legível.
- Trave os tokens de material e estilo em todos os prompts. Os tokens repetidos verbatim evitam a deriva para o realista.
- Aprove o mapa de beats antes de gerar qualquer coisa. O mapa aprovado trava custo e direção antes do primeiro render.

## Densidade de 3 beats por clipe de 10 segundos

Origem: stickman-animation em https://github.com/advibly/skills

- Estruture cada clipe de 10 segundos em 3 beats. O primeiro estabelece, o segundo transforma e o terceiro entrega o clímax.
- Exija 4 ou mais dispositivos visuais por clipe. Metáfora literal, transformação de ambiente, revelação, contraste e reação contam como dispositivos.
- Rejeite o clipe com um boneco parado num quadro vazio por 10 segundos. Essa é a falha que a regra existe para evitar e é a mesma régua do erro 3 desta skill.
- Comprima os 3 beats para 8 segundos na trilha Pixar. Estabelecer, transformar e entregar continuam existindo, só mais curtos.
- Trave o estilo em todos os prompts com um STYLE LOCK repetido. Figura, traço, paleta e negativos travados, sem rosto onde o estilo não tem rosto, sem sombreamento e sem volume 3D onde o estilo é plano.
- Proíba texto nas gerações de vídeo. O texto vira overlay nítido só na composição final.
- Narre a 2,3 a 2,5 palavras por segundo neste estilo minimalista. São 20 a 25 palavras por clipe e 130 a 150 por Short de 60 segundos.
- Avise que a skill de origem usa o Advibly MCP, que é pago. Importe a direção e os gates e nunca prometa a ferramenta como se fosse gratuita.

## A voz é o relógio

Origem: animate em https://github.com/cth9191/animate

- Trate a voz como o relógio do vídeo. Cada beat começa cerca de 0,3 segundo após o fim da frase anterior.
- Coloque os grandes momentos sobre as palavras faladas. O payoff cai na palavra que o nomeia e nunca no silêncio depois dela.
- Escreva o roteiro como uma linha por beat. Uma linha é um beat e o beat é uma linha.
- Dê a cada linha um tempo de respiro depois dela quando a imagem precisar de tempo para pousar. Contagem, legenda e silêncio antes do payoff pedem respiro maior.
- Mantenha o ritmo em até 3,5 palavras por segundo. Acima disso a narração atropela a imagem.
- Construa e revise com uma voz provisória antes da voz final quando precisar. A voz provisória nunca vai para o vídeo entregue.
- Alinhe esta regra com a sincronia por tempos reais da narração. Os tempos de palavra do faster-whisper são o relógio e os beats se movem com ele.

## Fórmula de beats de Short de 55 a 70 segundos

Origem: cartoon-3d-short em https://github.com/mromidev/claude-animated-shorts

- Abra com o gancho em uma linha. O fato absurdo dito de uma vez, sem rodeio.
- Escale a ação em 3 ou 4 beats. Cada beat fica um pouco maior que o anterior.
- Insira a dupla Luckily e Unluckily no meio. A sorte vira e o azar responde, em duas linhas secas.
- Explique com uma analogia cotidiana. Uma ideia de física cabe numa criança no balanço.
- Feche com um callback. O fim responde o começo e dá a volta na história.
- Antecipe cada reação visual 0 a 3 quadros antes da palavra dela. A reação chega antes da palavra e nunca depois.
- Marque um flash branco depois do gancho quando o estilo pedir. O flash separa o gancho do resto.
- Mire 3,7 palavras por segundo no roteiro deste formato acelerado de desenho. São cerca de 200 a 260 palavras num Short de 55 a 70 segundos. No Short narrado normal do canal, mantenha 2,3 a 2,6 palavras por segundo.
- Adapte a fórmula ao nicho do canal. A estrutura é gancho, escalada, sorte e azar, analogia e callback, e o assunto muda por canal.
