# Quadros de movimento — histórias 2D por código

Motion design por código, quadro a quadro, para vídeos 2D de histórias. A cena é uma página HTML com uma função `renderFrame(n)` que desenha o quadro n. O `render.mjs` fotografa cada quadro num Chromium sem tela e o ffmpeg monta o MP4. O mesmo input dá os mesmos pixels sempre, então a cena é determinística e pode ser refeita quadro a quadro sem variação.

Use este guia quando o vídeo for uma história 2D: história animada narrada, história interativa com escolha no final ou vídeo vertical curto para TikTok, Reels e Shorts. O formato mãe é o vídeo vertical 1080x1920. A trilha é a trilha 2D por código da skill, na variante de histórias. Não misture esta variante com o infográfico 2D de diagramas nem com as outras trilhas no mesmo vídeo. Leia as regras das trilhas em [animação](animacao.md) e os custos em [estilos visuais](estilos-visuais.md).

## De onde vêm estas receitas

- Leia o estudo quadro a quadro em `~/workspace/research_notes/estudo-motion-frames-referencias.md` antes de inventar uma cena nova. O estudo analisou 7 vídeos com contact sheets em `~/workspace/research_notes/motion-frames-sheets/` e confirmou 10 regras: micro-evento a cada 0,5 a 1,5 segundo, transição como evento e nunca corte seco, uma cor de destaque com glow, números que contam, UI com conteúdo real, tipografia protagonista, rabisco desenhado como assinatura, câmera que nunca para, logo reveal com desenho e SFX em cada micro-evento.
- Siga as seções 4 a 7 do SKILL.md do Motion Frames (IuryDevz/Motion-Frames-Skill-Muse-AI, https://raw.githubusercontent.com/IuryDevz/Motion-Frames-Skill-Muse-AI/main/SKILL.md): linguagem de movimento, fundos vivos, 3D em CSS e as 4 gramáticas. As receitas abaixo são a adaptação dessas seções para a paleta do canal e para o `template.html` desta skill.
- Corrija duas citações do SKILL.md de origem quando for citá-lo, porque o estudo provou que as duas estão erradas. Primeiro, "Opal/Qwix" mistura duas referências diferentes: Opal é a referência de promo premium (gramática B), um anúncio conceito de Olaf Klimasz, e Qwix é um plugin de After Effects para animação de texto, cuja promo é kinetic type com captura de tela (gramática D). Segundo, o vídeo original "Built with Claude" não foi localizado como vídeo público baixável: a referência analisável da gramática C é o exemplo "Feito com Muse" do próprio autor da skill, não o original. Leia o erro 35 e o erro 36 em [erros comuns](erros-comuns.md).
- Fundamente cada receita nos livros da biblioteca em [livros](livros.md). As citações abaixo trazem o livro e o ano, e a seção de cada livro em livros.md traz a fonte e a aplicação.

## As fontes locais: o que usar e como carregar

- Use só as 8 fontes `.woff2` em `~/workspace/tools/renderizador-cdp/fonts/`, todas sob SIL Open Font License 1.1 (OFL). O registro completo, com origem e licença de cada família, está em `~/workspace/tools/renderizador-cdp/fonts/FONTS.md`.
- Use Archivo Black (declarada como peso 900) para títulos e números gigantes, Inter 400 para subtítulos e texto corrido, Inter 700 para rótulos, ênfases e botões, e Caveat 700 para anotações manuscritas e rabiscos. Essa é a divisão do template: display, texto e manuscrita, uma família por função, sem trocar de fonte no meio do vídeo.
- Carregue as fontes com `@font-face` por caminho relativo, como o `template.html` já faz. Copie o bloco `@font-face` inteiro quando copiar o template, porque ele declara os subsets `latin` e `latin-ext` que cobrem o pt-BR. Nunca aponte para uma fonte da rede: o render abre a página por `file://` e não tem rede em tempo de render, então fonte externa não carrega e o Chromium cai para Arial ou Helvetica sem avisar.
- Copie a pasta `fonts/` junto com o `template.html` sempre que mover a cena para outro lugar. Template sem a pasta ao lado perde as 3 famílias e o vídeo inteiro muda de cara.
- Espere as fontes carregarem antes do quadro 0: o `render.mjs` já espera `document.fonts.ready` antes do primeiro quadro, então não invente outra espera. Se o primeiro quadro sair com a fonte do sistema, confira se a pasta `fonts/` está ao lado do HTML e se o `@font-face` não foi apagado na cópia.
- Meça a largura real antes de aprovar um título, porque Archivo Black é ultra-pesada e estoura a largura sem avisar. Use o helper `medeTexto` do template: `medeTexto("FUGINDO DA TERRA", "900 88px 'Archivo Black'")` devolve a largura em px. Medido em 06/11/2026, "FUGINDO DA TERRA" a 88 px tem 978,8 px de largura e cabe nos 1080 px, e a 96 px tinha 1.067,8 px, com margem de só 6 px de cada lado. Se passar de 1000 px, diminua a fonte ou quebre a linha. Leia o erro 32 em [erros comuns](erros-comuns.md).

## Os 4 estilos adaptados para histórias 2D

Escolha um estilo por vídeo e siga só ele do começo ao fim. Cada estilo tem formato, duração, voz e momento certo de uso.

### 1. Cinema e morph — a história narrada com cara de cinema

- Como é: a história é narrada em 3 batidas, mundo normal, mundo estranho e volta transformada, e as cenas se transformam uma na outra com morphs em vez de cortes secos. O número vira o objeto, o objeto vira o lugar, o lugar vira o desfecho.
- Formato: história animada narrada, com protagonista fixo e um conflito por vídeo.
- Duração: 30 a 90 segundos no vertical, 10 a 12 minutos no longo quando a história pedir.
- Voz: calma e didática para ciência e como funciona, voz de documentário para história e mistério. Leia os 26 estilos em [vozes](vozes.md).
- Quando usar: quando a história tem uma virada clara e o morph ajuda a contar a virada. Não use morph em história de lista, porque não há o que transformar.

### 2. Promo premium — a história de um produto ou de uma marca

- Como é: a história mostra o produto como herói, com visual premium, luz limpa, tipografia grande e o resultado primeiro. O gancho mostra o resultado, o meio mostra o mecanismo e o fim mostra o produto em uso.
- Formato: vídeo vertical curto de produto, app, loja ou marca.
- Duração: 15 a 30 segundos no vertical.
- Voz: locutor de rádio para ritmo rápido e marcante, jovem e animada para produto leve.
- Quando usar: quando o vídeo vende ou apresenta um produto real, com a identidade da marca. Nunca invente um produto que não existe nem prometa o que o produto não entrega. Leia a regra de identidade da marca abaixo.

### 3. Cena interativa sem cortes — a história que o espectador decide

- Como é: a história acontece numa cena contínua, sem cortes, com o protagonista em situação de escolha. No final, duas opções aparecem na tela e o espectador comenta a escolha dele. O próximo vídeo continua a opção mais votada.
- Formato: história interativa, um nível por vídeo. Cada vídeo é um nível e o protagonista ganha um poder ou um item por nível.
- Duração: 45 a 90 segundos no vertical. A escolha precisa de tempo para ser entendida.
- Voz: mascote e personagem quando o protagonista é criança, desafiadora quando a escolha provoca o espectador, jovem e animada para o resto. Leia os 26 estilos em [vozes](vozes.md).
- Quando usar: quando a história tem um dilema de verdade, com custo dos dois lados. Nunca use escolha óbvia, porque ninguém comenta o óbvio. Leia o formato interativo completo abaixo.

### 4. Tipografia clara — o texto é o protagonista

- Como é: o texto carrega a história. Cada batida da narração vira uma palavra gigante na tela, com o resto do texto em apoio. O fundo é simples, com profundidade e movimento lento, para o texto ser o foco.
- Formato: vídeo vertical curto de fato, frase, citação ou pergunta.
- Duração: 15 a 60 segundos no vertical.
- Voz: calma e didática para fato e explicação, locutor de rádio para ritmo rápido.
- Quando usar: quando a ideia é uma frase, um número ou uma pergunta que precisa ser lida. Não use quando a história precisa de personagem e lugar, porque o texto sozinho não conta a cena.

## As regras do movimento profissional

Aplique estas 5 regras em cada cena de história. Uma cena que quebra uma regra parece amadora mesmo com desenho bonito.

### Tipografia protagonista

- Faça a palavra da ideia ser o maior elemento do quadro. O texto não decora a cena, ele é a cena.
- Escreva no máximo uma ideia por quadro de texto. Duas ideias no mesmo quadro dividem o olhar e nenhuma fica.
- Deixe o espectador ler a palavra antes de ela sumir. Uma linha curta precisa de cerca de 2 segundos na tela.
- Use a fonte da marca ou a fonte do canal em todos os quadros. Fonte diferente em cada cena quebra a identidade.

### Micro-evento a cada 0,5 a 1,5 segundo

- Coloque alguma mudança visível a cada 0,5 a 1,5 segundo: uma palavra acende, um elemento entra, um número conta, a câmera corta, o fundo respira.
- Nunca deixe mais de 1,5 segundo sem mudança visível. O silêncio visual é o que faz o espectador rolar para o próximo vídeo.
- Conte os micro-eventos no teste do mudo. Assista sem som e marque cada mudança. Menos de 3 movimentos em 10 segundos é cena parada. Refaça.

### Morphs

- Transforme um elemento no outro quando a ideia continua. O número vira o objeto, a cena vira a próxima cena, o problema vira a solução.
- Use o morph para a virada da história. O corte seco é para a mudança de ideia e o morph é para a continuação da ideia.
- Faça o morph durar de 0,5 a 1 segundo. Morph rápido demais some e morph lento demais arrasta.
- Nunca use morph entre ideias sem relação. Morph sem sentido confunde mais que corte seco.

### Fundo vivo com profundidade

- Monte o fundo em 3 camadas: primeiro plano, plano do meio e fundo. As camadas se movem em velocidades diferentes, que é o parallax.
- Coloque movimento no fundo o tempo todo, mesmo quando o protagonista está parado falando: partículas flutuando, luz respirando, poeira caindo, água ondulando.
- Deixe o fundo com menos contraste que o assunto. O olhar vai para o contraste, para o movimento e para o rosto. Fundo com mais contraste que o assunto rouba o olhar.
- Use um elemento no primeiro plano em toda cena fechada. Uma folha, uma pedra ou a borda de uma mesa no canto do quadro dá profundidade imediata.

### Som em cada animação

- Coloque um efeito sonoro em cada movimento: um whoosh no morph, um pop na entrada do elemento, um blip na palavra que acende, um impacto na queda do carimbo.
- Coloque o efeito no mesmo segundo da ação na tela. Efeito 1 segundo depois da ação parece dublagem errada.
- Deixe a música baixa sob a narração e os efeitos na frente da música. Efeito e música nunca cobrem a voz.
- Nunca entregue uma cena de história sem áudio, a não ser que o usuário tenha pedido um teste só visual e saiba disso. Leia o guia de áudio em [áudio](audio.md).

## Receitas prontas para copiar e colar

Cada receita abaixo é uma função `renderFrame(n)` que roda numa cópia do `template.html` atual, com os helpers novos que já vivem nele: `CORES`, `lissajous`, `corLerp`, `contar`, `poeira`, `gradePontos`, `fundoEstudio`, `fundoAurora`, `fundoGelo`, `cuboHTML`, `orbita`, `rabiscoSVG`, `cursorHTML`, `palavraNoBeat` e `medeTexto`. Copie o `template.html` e a pasta `fonts/` juntos, cole a receita no lugar da cena de exemplo e ajuste só os valores marcados com `AJUSTE`. Duração em quadros a 60 fps: 30 quadros são 0,5 segundo, 60 quadros são 1 segundo, 90 quadros são 1,5 segundo. Base teórica: Design for Motion, de Austin Shaw, 2016 (2ª edição, 2020), e Motion Graphic Design, de Jon Krasner, 2013, em [livros](livros.md).

### Receita 1: estúdio vivo (fundo para promo, gramática B)

- Copie esta cena para o fundo de qualquer vídeo de produto ou marca, no estilo do Kalo do estudo (exemplo 1, 15 segundos, telefone em perspectiva sobre estúdio escuro com blobs verdes e poeira).
- Cole no lugar da cena de exemplo do template e troque só a cor de destaque no `AJUSTE`: use a cor da marca quando ela existir, ou `CORES.laranja` na paleta do canal.
- Ajuste a duração com o `seg` do drift: os blobs derivam devagar o vídeo inteiro, sem janela de fim, então a cena pode durar o que a narração pedir.

```js
function renderFrame(n) {
  // AJUSTE: cor de destaque, uma só, com glow. No canal: CORES.laranja.
  const destaque = CORES.laranja;
  const t = T(n);
  // Drift lento da câmera: escala 1 -> 1,05 em 3 segundos (quadros 0 a 180).
  const zoom = 1 + 0.05 * easeOutCubic(seg(n, 0, 180));
  stage.innerHTML = `
    <div style="position:absolute;inset:0;transform:scale(${zoom.toFixed(3)});transform-origin:50% 40%">
      ${fundoEstudio(n, destaque)}
      <!-- AJUSTE: o herói no meio, com tilt. Troque pelo produto ou card. -->
      <div style="position:absolute;left:50%;top:38%;width:560px;height:760px;transform:translateX(-50%) perspective(1200px) rotateY(-14deg);
                  background:linear-gradient(160deg, #2E6DB4, #1A305A);border-radius:48px;
                  box-shadow:0 40px 90px rgba(0,0,0,0.55), 0 0 60px ${destaque}55"></div>
    </div>`;
}
```

- Confira no preview em tamanho real se o fundo tem menos contraste que o herói: se o blob brilhar mais que o produto, baixe a opacidade dele no `fundoEstudio` de 0,28 para 0,18. O olhar vai para o contraste, e o fundo nunca pode ganhar do assunto.
- Meça o custo antes de prometer prazo: blur grande em tela cheia é o que mais pesa no render. Uma cena com aurora de 6 fitas com blur rendeu 2,76 fps em 06/11/2026 nesta máquina, contra 6,41 fps do template de exemplo na mesma rodada. Se o render ficar lento demais, diminua o blur de 110 px para 70 px, corte uma fita e reduza a poeira de 24 para 12 pontos, e meça de novo.

### Receita 2: aurora líquida (fundo para cena contínua, gramática C)

- Copie esta cena para a história interativa sem cortes, no estilo do "Feito com Muse" do estudo (exemplo 2, 14 segundos, aurora laranja sobre preto com poeira).
- Cole no lugar da cena de exemplo e ajuste o `troca` com os quadros do segundo comando da narração: a aurora faz crossfade da cor A para a cor B no momento em que o comando muda o mundo.
- Ajuste as cores com `corA` e `corB`: no canal, laranja `#FF8C1A` para a cor A e azul `#3B82F6` para a cor B, como no exemplo 2, ou duas cores do nicho (azul-profundo para espaço, verde para natureza).

```js
function renderFrame(n) {
  // AJUSTE: quadros do segundo comando, medidos da transcrição real.
  // Aqui o comando chega no quadro 300 e a troca dura 30 quadros (0,5 s).
  const troca = easeInOutCubic(seg(n, 300, 330));
  stage.innerHTML = `
    ${fundoAurora(n, CORES.laranja, "#3B82F6", troca)}
    <!-- AJUSTE: o objeto da cena fica por cima da aurora, nunca por baixo. -->
    <div style="position:absolute;left:50%;top:42%;transform:translate(-50%,-50%);text-align:center;
                font-family:'Archivo Black',sans-serif;font-size:110px;font-weight:900;color:#FFFFFF">
      O MUNDO MUDA
    </div>`;
}
```

- Use o `troca` como beat de inversão sem corte: a paleta inteira muda e o espectador sente a virada sem nenhuma fronteira dura. É a tradução do segundo comando do exemplo 2 ("agora com o fundo azul") para a história: a virada do roteiro ("mas tem um detalhe...") ganha uma virada visual.
- Nunca deixe a aurora parar: as fitas derivam em Lissajous pelo `lissajous(t)` dentro do helper, então mesmo sem nenhum outro evento a cena respira. Se a aurora parecer parada no preview, confira se você passou `n` e não um número fixo para o `fundoAurora`.

### Receita 3: gelo da marca (fundo claro para tipografia, gramática D)

- Copie esta cena para o vídeo de tipografia clara, no estilo do iPhone SE do estudo (campo branco que inverte para preto) e do kinetic type da London Northwestern Railway (fundo chapado da marca que funciona porque a vida está 100% na tipografia).
- Cole no lugar da cena de exemplo e ajuste `corMarca` com a cor clara da marca, ou deixe o padrão `#DCE8F5` na paleta do canal.
- Ajuste o texto para escuro por cima do gelo: o fundo claro pede texto em `#1A305A`, e a palavra-chave leva a cor de destaque.

```js
function renderFrame(n) {
  stage.innerHTML = `
    ${fundoGelo(n)}
    <!-- AJUSTE: texto escuro sobre o gelo, palavra-chave em laranja. -->
    <div style="position:absolute;left:0;top:40%;width:100%;text-align:center;
                font-family:'Archivo Black',sans-serif;font-size:120px;font-weight:900;color:#1A305A">
      A PALAVRA É <span style="color:${CORES.laranja}">O VÍDEO</span>
    </div>`;
}
```

- Lembre a exceção que o estudo confirmou: fundo chapado só funciona no kinetic type puro, onde a tipografia carrega todo o movimento. No promo de produto, fundo chapado é proibido, porque o produto precisa de profundidade. Não use o gelo no estilo promo premium.

### Receita 4: 3D em CSS, tilt, parallax real e cubo

- Copie este bloco para dar profundidade a qualquer cena que hoje é "texto mais retângulo plano". Base: The Visual Story, de Bruce Block, 2021, em [livros](livros.md), para compor o quadro vertical com espaço, linha e profundidade.
- Cole o tilt no herói, o parallax nas camadas e o cubo onde a cena pedir um objeto com volume. Ajuste os ângulos com o tempo: o tilt reage ao `t` e a sombra reage ao tilt, então o objeto parece fotografado, não desenhado.

```js
function renderFrame(n) {
  const t = T(n);
  // AJUSTE: tilt que respira, de -14 a -8 graus em 2 segundos, e volta.
  const tilt = -11 + Math.sin(t * 1.1) * 3;
  // AJUSTE: parallax real, fundo devagar, meio no meio, frente rápido.
  const panFundo = Math.sin(t * 0.5) * 12;   // fundo: 12 px
  const panMeio = Math.sin(t * 0.5) * 30;    // meio: 30 px
  const panFrente = Math.sin(t * 0.5) * 55;  // frente: 55 px
  // AJUSTE: cubo de 260 px girando de -30 a 30 graus em 2 segundos.
  const rotY = lerp(-30, 30, easeInOutCubic(seg(n, 0, 120)));
  stage.innerHTML = `
    ${fundoEstudio(n, CORES.laranja)}
    <div style="position:absolute;inset:0;transform:translateX(${panFundo.toFixed(1)}px)">
      <div style="position:absolute;left:120px;top:200px;font-family:'Archivo Black',sans-serif;font-size:60px;color:#FFFFFF;opacity:0.5">FUNDO</div>
    </div>
    <div style="position:absolute;inset:0;transform:translateX(${panMeio.toFixed(1)}px)">
      ${cuboHTML(260, [CORES.laranja, "#CC6F00", CORES.amarelo, "#B25E00", "#FFA94D", "#8A4D00"], 12, rotY)}
    </div>
    <div style="position:absolute;inset:0;transform:translateX(${panFrente.toFixed(1)}px)">
      <div style="position:absolute;left:60px;bottom:120px;font-family:'Caveat',cursive;font-size:64px;font-weight:700;color:${CORES.amarelo};transform:rotate(-3deg)">olha o volume!</div>
    </div>`;
}
```

- Respeite a regra do cubo: cada face usa `translateZ` igual à metade da dimensão, e o helper `cuboHTML` já faz isso (para 260 px, 130 px por face). Se abrir fresta na aresta, confira se alguma face foi escrita à mão com `translateZ` diferente da metade. Leia o erro 30 em [erros comuns](erros-comuns.md).
- Faça o teste da seção 6 do Motion Frames: se a cena pode ser descrita como "texto mais retângulo plano", falta 3D. Adicione tilt, camada ou profundidade até ela parecer fotografada.

### Receita 5: morph, um objeto virando outro

- Copie esta receita para a virada da história, no estilo do Kalo do estudo (a pílula de kcal vira o telefone, o telefone vira o scan) e do "Feito com Muse" (a pílula vira a barra de prompt, a barra vira o card).
- Cole no lugar da cena de exemplo e ajuste as janelas em quadros: o morph dura de 0,5 a 1 segundo (30 a 60 quadros), com `easeInOutCubic`, nunca linear. Base de timing: Timing for Animation, de Harold Whitaker e John Halas, 2009, e The Animator's Survival Kit, de Richard Williams, 2001, em [livros](livros.md).
- Interpole a geometria compartilhada com as fórmulas abaixo: posição, largura, altura e raio de borda vão de um estado ao outro com `lerp`, e a cor vai com `corLerp`. O objeto nunca some: ele muda de forma no mesmo lugar.

```js
function renderFrame(n) {
  // AJUSTE: o morph acontece nos quadros 120 a 168 (0,8 segundo).
  const u = easeInOutCubic(seg(n, 120, 168));
  // Estado A: pílula pequena no centro. Estado B: barra larga embaixo.
  const x = lerp(340, 90, u), y = lerp(860, 1450, u);
  const w = lerp(400, 900, u), h = lerp(120, 150, u);
  const raio = lerp(60, 28, u);
  const cor = corLerp("#FF8C1A", "#264476", u);
  // O texto troca no meio do morph, com crossfade de 12 quadros.
  const textoA = 1 - easeOutCubic(seg(n, 138, 150));
  const textoB = easeOutCubic(seg(n, 138, 150));
  stage.innerHTML = `
    ${fundoEstudio(n, CORES.laranja)}
    <div style="position:absolute;left:${x.toFixed(0)}px;top:${y.toFixed(0)}px;width:${w.toFixed(0)}px;height:${h.toFixed(0)}px;
                border-radius:${raio.toFixed(0)}px;background:${cor};border:3px solid rgba(255,255,255,0.4);
                display:flex;align-items:center;justify-content:center">
      <span style="font-family:'Inter',sans-serif;font-size:44px;font-weight:700;color:#FFFFFF;opacity:${textoA.toFixed(2)}">1.240 kcal</span>
      <span style="position:absolute;left:0;width:100%;text-align:center;font-family:'Inter',sans-serif;font-size:44px;font-weight:700;color:#FFFFFF;opacity:${textoB.toFixed(2)}">digite o que comeu...</span>
    </div>`;
}
```

- Use o morph só quando a ideia continua: o número vira o objeto, o objeto vira o lugar, o problema vira a solução. Morph entre ideias sem relação confunde mais que corte seco.
- Coloque um `whoosh` do `sfx_kit.py` no quadro em que o morph começa e um `pop` no quadro em que ele assenta. O som marca a fronteira que o corte seco marcaria.

### Receita 6: sistemas orbitais, nós em volta da logo

- Copie esta receita para o elemento assinatura da gramática D do Motion Frames: nós orbitando a logo, como no sistema orbital de nós em volta da logo do turtle pags.
- Cole no lugar da cena de exemplo e ajuste o centro `(cx, cy)`, os raios e a velocidade: o raio vertical menor achata a elipse e dá perspectiva, e a escala cresce quando o nó vem para a frente.
- Ajuste o raio para o nó nunca cobrir o objeto central: no teste de receitas, o raio horizontal de 330 px cruzou o cubo de 260 px e os nós passaram por cima dele. Suba o raio ou desça o `z-index` do nó quando ele estiver atrás.

```js
function renderFrame(n) {
  // AJUSTE: centro da logo, raios e velocidade (0,6 radiano por segundo).
  const cx = 540, cy = 960, rx = 380, ry = 150;
  const rotulos = ["FATO", "PROVA", "VIRADA"];
  let nos = "";
  for (let i = 0; i < 3; i++) {
    const o = orbita(n, cx, cy, rx, ry, i * 2.094, 0.6);
    nos += `<div style="position:absolute;left:${(o.x - 70 * o.escala).toFixed(0)}px;top:${(o.y - 34 * o.escala).toFixed(0)}px;
      width:${(140 * o.escala).toFixed(0)}px;height:${(68 * o.escala).toFixed(0)}px;border-radius:34px;
      background:${CORES.marinhoClaro};border:3px solid ${CORES.laranja};display:flex;align-items:center;justify-content:center;
      font-family:'Inter',sans-serif;font-size:30px;font-weight:700;color:#FFFFFF;z-index:${o.frente ? 30 : 10}">
      ${rotulos[i]}</div>`;
  }
  stage.innerHTML = `
    ${fundoEstudio(n, CORES.laranja)}
    <svg style="position:absolute;left:50%;top:50%;transform:translate(-50%,-50%)" width="820" height="340" viewBox="0 0 820 340" fill="none">
      <ellipse cx="410" cy="170" rx="380" ry="150" stroke="rgba(255,255,255,0.25)" stroke-width="3" stroke-dasharray="12 14"/>
    </svg>
    <div style="position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);text-align:center;
                font-family:'Archivo Black',sans-serif;font-size:90px;font-weight:900;color:#FFFFFF">LOGO</div>
    ${nos}`;
}
```

- Use a órbita como assinatura, não como decoração solta: os 3 nós são os 3 beats da história (fato, prova, virada), e cada nó pode acender no quadro em que a narração chega naquele beat. Nó parado sem relação com a fala é enfeite.

## A identidade real da marca

- Leia o site do produto antes de desenhar qualquer cena. Anote o logotipo, a paleta com os códigos hex exatos e as fontes usadas no site.
- Use o arquivo do logotipo dentro da página, como imagem, e as cores e as fontes exatas do site. Nunca invente uma paleta quando a marca já tem uma.
- Se a marca não tem site, use a paleta do canal, azul-marinho com laranja, e a logo do canal.
- Mostre a logo no carimbo de marca de 1 segundo depois do gancho e no outro. Nunca mostre a logo antes do gancho, porque o espectador sai antes da história começar.
- Confira a legibilidade no celular. Texto e logo que somem em tela pequena não servem para vídeo vertical.

## O formato interativo

A história interativa é um formato próprio, com regras próprias. Siga todas as regras abaixo quando o vídeo for interativo.

### Protagonista fixo

- Crie a ficha do protagonista com `$personagem` antes do primeiro vídeo da série e copie a mesma ficha em todas as cenas, sem mudar uma palavra. O protagonista não muda de rosto, de roupa nem de idade no meio da série.
- Dê ao protagonista um objeto fixo na mão ou no peito, como uma lupa ou uma engrenagem. O objeto vira assinatura visual e ajuda a reconhecer o protagonista de costas ou de longe.
- Trave as 5 poses fixas do protagonista: neutro, curioso, surpreso, explicando e pensando. Toda reação usa uma dessas poses como base.

### Níveis e poderes

- Cada vídeo é um nível: Nível 1, Nível 2, Nível 3, e assim por diante. O número do nível aparece na tela no começo do vídeo.
- O protagonista ganha um poder ou um item por nível. O poder do nível anterior aparece no nível seguinte, então a série tem progressão.
- O nível termina na escolha. O vídeo não fecha a história, ele abre a próxima.

### A escolha no final

- Mostre a escolha nos últimos 5 segundos, com 2 opções na tela, A e B, legíveis no celular. A narração lê as duas opções em voz alta.
- Faça a escolha ser um dilema de verdade, com custo dos dois lados. Escolha óbvia não gera comentário e comentário é o motor do formato.
- Nunca mostre mais de 2 opções. Três opções dividem os votos e matam os comentários.
- Peça o voto no comentário com uma frase só: "Comenta A ou B, o que você faria?". O CTA é a escolha, não o pedido de inscrição.
- O próximo vídeo continua a opção mais votada. Leia os comentários antes de escrever o próximo nível e diga no começo do vídeo qual opção venceu.

## Receitas de tipografia cinética, interação e contadores

### Receita 7: tipografia cinética, palavra por palavra no beat da fala

- Copie esta receita para o estilo tipografia clara, no estilo do kinetic type da London Northwestern Railway do estudo (20 segundos, palavra por palavra no beat da narração, palavras de ligação pequenas e palavras-conceito gigantes) e do iPhone SE (inversão claro e escuro como batida).
- Cole no lugar da cena de exemplo e ajuste os `inicios` com os tempos reais de cada palavra, medidos da transcrição do faster-whisper: quadro é tempo da palavra vezes fps. Nunca invente os inícios.
- Ajuste o contraste de escala: palavras de ligação em 64 px, palavras-conceito em 170 px ou mais, e a palavra-chave em laranja com rabisco. Base: Type in Motion, de Jeff Bellantoni e Matt Woolman, 1999, e Thinking with Type, de Ellen Lupton, 2004 (2ª edição, 2010), em [livros](livros.md).

```js
function renderFrame(n) {
  // AJUSTE: palavras e quadros de início, medidos da transcrição real.
  const palavras = [
    { t: "A LUA", inicio: 0, grande: true },
    { t: "ESTÁ", inicio: 24, grande: false },
    { t: "FUGINDO", inicio: 48, grande: true, chave: true },
    { t: "DA TERRA", inicio: 78, grande: true },
  ];
  const ativa = palavraNoBeat(n, palavras.map(p => p.inicio));
  let html = "";
  palavras.forEach((p, i) => {
    if (i > ativa) return;
    const u = spring(T(n) - T(p.inicio), 5.2, 0.55);
    const tamanho = p.grande ? 150 : 64;
    const cor = p.chave ? CORES.laranja : "#1A305A";
    const y = 700 + i * 170;
    html += `<div style="position:absolute;left:0;top:${y}px;width:100%;text-align:center;
      font-family:'Archivo Black',sans-serif;font-size:${tamanho}px;font-weight:900;color:${cor};
      transform:translateY(${(1 - u) * 90}px) scale(${(0.7 + 0.3 * u).toFixed(2)});opacity:${clamp(u * 1.6).toFixed(2)}">
      ${p.t}</div>`;
    if (p.chave && i === ativa) {
      const r = easeOutCubic(seg(n, p.inicio + 12, p.inicio + 36));
      html += `<div style="position:absolute;left:50%;top:${y + 150}px;transform:translateX(-50%)">${rabiscoSVG("sublinhado", r, CORES.laranja, 560, 60)}</div>`;
    }
  });
  // Caret piscando: o traço some e volta a cada 15 quadros (0,25 s).
  const caret = (n % 30 < 15) ? "opacity:1" : "opacity:0";
  stage.innerHTML = `
    ${fundoGelo(n)}
    ${html}
    <div style="position:absolute;left:50%;top:1500px;width:6px;height:90px;background:${CORES.laranja};${caret}"></div>`;
}
```

- Faça a palavra virar o conceito quando der: "MILHARES" se multiplica e enche o quadro, "LONGO" se estica na horizontal, o número chove ao redor de "DINHEIRO". O estudo provou que esse é o truque mais forte da tipografia cinética: o significado é encenado, não só escrito.
- Use o rabisco como segunda voz: sublinhado, círculo, seta ou explosão de tracinhos, sempre na cor de destaque, sempre em SVG com `stroke-dasharray` se desenhando, sempre no beat da palavra. O helper `rabiscoSVG` já faz o traço se desenhar de 0 a 1.
- Use a inversão claro e escuro como batida, não como acidente: troque o `fundoGelo` pelo `fundoEstudio` no meio da frase ("E não para por aí!") e volte no fecho. Cada inversão marca uma ideia nova, e o estudo contou 3 inversões em 14 segundos no iPhone SE.

### Receita 8: cursor, prompt digitado e comando que muda o mundo

- Copie esta receita para a cena interativa sem cortes, no estilo do "Feito com Muse" do estudo: o cursor viaja, clica, a pílula vira barra, o prompt é digitado palavra por palavra e o segundo comando muda a cor do fundo inteiro.
- Cole no lugar da cena de exemplo e ajuste os quadros com os landmarks da fala: o clique cai no quadro em que a narração diz a ação, e cada palavra digitada cai no quadro em que a narração diz a palavra.
- Ajuste o caminho do cursor com dois `lerp`: ele viaja do ponto de partida ao alvo com `easeInOutCubic`, nunca salta, e o clique dura 12 quadros (o anel de pulso do `cursorHTML`).

```js
function renderFrame(n) {
  // AJUSTE: quadros do clique e das palavras, medidos da transcrição real.
  const cliqueQuadro = 90;
  const cx = lerp(200, 540, easeInOutCubic(seg(n, 60, cliqueQuadro)));
  const cy = lerp(1700, 1000, easeInOutCubic(seg(n, 60, cliqueQuadro)));
  const clicando = n >= cliqueQuadro && n < cliqueQuadro + 12;
  // A pílula vira barra de prompt no clique (morph da receita 5).
  const u = easeInOutCubic(seg(n, cliqueQuadro, cliqueQuadro + 36));
  const w = lerp(420, 900, u);
  // AJUSTE: palavras do prompt e quadros de início, medidos da transcrição.
  const prompt = ["quero", "um", "vídeo", "sobre", "a", "LUA"];
  const inicios = [132, 144, 156, 172, 188, 200];
  const ativa = palavraNoBeat(n, inicios);
  let digitado = prompt.slice(0, ativa + 1).join(" ");
  if (ativa === prompt.length - 1) digitado = digitado.replace("LUA", `<span style="color:${CORES.laranja}">LUA</span>`);
  const caret = (n % 30 < 15) ? "opacity:1" : "opacity:0";
  stage.innerHTML = `
    ${fundoAurora(n, CORES.laranja, "#3B82F6", easeInOutCubic(seg(n, 300, 330)))}
    <div style="position:absolute;left:${((1080 - w) / 2).toFixed(0)}px;top:960px;width:${w.toFixed(0)}px;height:130px;
                border-radius:65px;background:rgba(255,255,255,0.12);border:3px solid rgba(255,255,255,0.35);
                display:flex;align-items:center;padding:0 50px">
      <span style="font-family:'Inter',sans-serif;font-size:46px;color:#FFFFFF">${digitado}</span>
      <span style="display:inline-block;width:5px;height:56px;background:${CORES.laranja};margin-left:12px;${caret}"></span>
    </div>
    ${cursorHTML(cx, cy, clicando)}`;
}
```

- Conte a história como "alguém usando", não como "produto sendo mostrado": cursor que viaja, clica, digita, pede e muda de ideia. O espectador assiste a um uso, não a um catálogo.
- Coloque um `tick` do `sfx_kit.py` em cada palavra digitada, um `pop` no clique e um `whoosh` na troca de cor do fundo. O som usa os mesmos números de quadro da animação.

### Receita 9: contador que conta e card que se constrói por dentro

- Copie esta receita para qualquer número do fato (anos, km, porcentagem), no estilo do Kalo do estudo (4 contadores animados: kcal do dia, kcal do prato, 3 macros e porcentagem da meta) e do Opal (arco de score contando 30, 50, 69 e 88 com sub-métricas contando junto).
- Cole no lugar da cena de exemplo e ajuste `de`, `para` e a janela em quadros: o contador usa `easeOutCubic` dentro do `contar`, então passe o progresso linear do `seg` e receba o número contando. O número do fato precisa de fonte real, como manda a seção 10 do Motion Frames: número que vira promessa não se inventa.
- Ajuste a construção em camadas com `stagger` de 12 quadros por camada: anel, título, barras e progresso entram um depois do outro, e nunca tudo junto. Cada camada é um micro-evento.

```js
function renderFrame(n) {
  // AJUSTE: o contador vai de 0 a 3.800 nos quadros 30 a 120.
  const num = contar(seg(n, 30, 120), 0, 3800);
  // AJUSTE: cada camada entra 12 quadros depois da anterior.
  const anel = easeOutCubic(seg(n, 30, 54));
  const titulo = easeOutCubic(seg(n, 42, 66));
  const barra = easeOutCubic(seg(n, 54, 90));
  const progresso = easeOutCubic(seg(n, 66, 120));
  // Arco de progresso: o círculo usa pathLength 100, e o dashoffset
  // vai de 100 a 0 com o progresso (anel).
  stage.innerHTML = `
    ${fundoEstudio(n, CORES.laranja)}
    <svg style="position:absolute;left:50%;top:34%;transform:translate(-50%,-50%) rotate(-90deg)" width="300" height="300" viewBox="0 0 300 300" fill="none">
      <circle cx="150" cy="150" r="110" stroke="rgba(255,255,255,0.2)" stroke-width="18"/>
      <circle cx="150" cy="150" r="110" stroke="${CORES.laranja}" stroke-width="18" stroke-linecap="round"
              pathLength="100" stroke-dasharray="100" stroke-dashoffset="${((1 - anel) * 100).toFixed(1)}"/>
    </svg>
    <div style="position:absolute;left:0;top:30%;width:100%;text-align:center;font-family:'Archivo Black',sans-serif;font-size:110px;font-weight:900;color:#FFFFFF;opacity:${titulo.toFixed(2)}">${num}</div>
    <div style="position:absolute;left:140px;top:52%;width:800px;height:48px;background:#264476;border-radius:24px;overflow:hidden;opacity:${barra.toFixed(2)}">
      <div style="height:100%;width:${(progresso * 100).toFixed(1)}%;background:${CORES.laranja};border-radius:24px"></div>
    </div>
    <div style="position:absolute;left:0;top:58%;width:100%;text-align:center;font-family:'Inter',sans-serif;font-size:44px;font-weight:700;color:#FFFFFF;opacity:${progresso.toFixed(2)}">gerando quadro a quadro... ${(progresso * 100).toFixed(0)}%</div>`;
}
```

- Lembre a regra do estudo: número parado é rótulo, número contando é evento. Se o número ficar parado na tela, ele não conta como micro-evento.

### Receita 10: beat de inversão no meio do vídeo

- Copie este bloco para marcar a virada do roteiro sem cortar a cena: o fundo inteiro cruza de escuro para claro, ou de uma paleta para outra, em 30 quadros (0,5 segundo).
- Cole a troca no ponto da narração em que a frase vira ("mas tem um detalhe...", "e não para por aí!") e ajuste os quadros com o landmark da fala.
- Ajuste as duas paletas com `corLerp`: o fundo, o texto e o destaque cruzam juntos, porque a inversão é do mundo, não de um elemento.

```js
function renderFrame(n) {
  // AJUSTE: a virada acontece nos quadros 240 a 270.
  const u = easeInOutCubic(seg(n, 240, 270));
  const fundo = corLerp("#1A305A", "#F7FAFD", u);
  const texto = corLerp("#FFFFFF", "#1A305A", u);
  const detalhe = corLerp("#FF8C1A", "#FF8C1A", u);
  stage.innerHTML = `
    <div style="position:absolute;inset:0;background:${fundo}"></div>
    ${poeira(n, 16, u < 0.5 ? "#FFFFFF" : "#1A305A")}
    <div style="position:absolute;left:0;top:44%;width:100%;text-align:center;
                font-family:'Archivo Black',sans-serif;font-size:120px;font-weight:900;color:${texto}">
      E NÃO PARA <span style="color:${detalhe}">POR AÍ!</span>
    </div>`;
}
```

## Modelos de cena completa por estilo

Cada modelo abaixo é uma cena inteira de 6 segundos (360 quadros a 60 fps) que usa as receitas juntas, na ordem da gramática de cada estilo. Copie o modelo do estilo do vídeo, cole no lugar da cena de exemplo e ajuste os textos, as cores e os quadros com os landmarks da narração real. Os 4 modelos foram conferidos contra as gramáticas A, B, C e D do Motion Frames e contra os 7 vídeos do estudo.

### Modelo A: cinema e morph, 6 segundos, 360 quadros

- Use para a história narrada com virada: título cinematográfico, objeto com squash e stretch, morph para o próximo plano e fecho voltando ao ponto inicial.
- Siga a ordem: quadros 0 a 60, título gigante entrando com spring sobre o estúdio vivo (receita 1), com drift de câmera; quadros 60 a 150, o objeto (a Lua) viaja com squash e stretch na queda; quadros 150 a 210, morph do objeto para o lugar da virada (receita 5), com `whoosh` no quadro 150; quadros 210 a 300, tipografia cinética com círculo desenhado à mão na palavra-chave (receita 7); quadros 300 a 360, fecho retornando ao título, com o logo se desenhando em SVG dash.
- Ajuste o squash na queda com `easeOutBack` na escala vertical e `easeOutCubic` na horizontal: o objeto achata 20 por cento no impacto e volta com overshoot. Base: Disney Animation: The Illusion of Life, de Frank Thomas e Ollie Johnston, 1981, em [livros](livros.md), a fonte original dos 12 princípios.
- Confira o loop: o quadro 360 tem que ser igual ao quadro 0 em posição de câmera e fundo, para o vídeo poder repetir sem salto.

### Modelo B: promo premium, 6 segundos, 360 quadros

- Use para o vídeo de produto ou marca: resultado primeiro, mecanismo no meio, produto em uso no fim.
- Siga a ordem: quadros 0 a 60, abertura com o produto em perspectiva 3D flutuando sobre o estúdio vivo (receitas 1 e 4), com pull focus, começando desfocado e focando; quadros 60 a 150, mergulho da câmera num detalhe que vira o próximo plano, com zoom-punch; quadros 150 a 240, pílulas de vidro com número contando (receita 9), com linhas-suporte se desenhando e convergindo num número gigante; quadros 240 a 300, botão-pílula gigante de CTA com varredura de luz atravessando o botão; quadros 300 a 360, logo reveal com o símbolo se desenhando em SVG dash e a URL pequena.
- Ajuste a varredura de luz do CTA com um gradiente linear branco que atravessa o botão da esquerda para a direita em 30 quadros, com `lerp` na posição. É o evento que o estudo contou no Kalo aos 10 a 12 segundos.
- Confira a identidade real da marca antes de desenhar: leia o site, anote o logotipo, a paleta com os hex exatos e as fontes, e use o arquivo do logotipo como imagem com preload. Leia o erro 31 em [erros comuns](erros-comuns.md).

### Modelo C: cena interativa sem cortes, 6 segundos, 360 quadros

- Use para a história interativa de um nível: uma cena só, sem cortes, sobre a aurora líquida, com o protagonista em situação de escolha.
- Siga a ordem: quadros 0 a 60, símbolo se desenhando traço por traço sobre a aurora (receita 2), com o número do nível na tela; quadros 60 a 120, pílulas de comando entrando uma a uma com spring e stagger de 12 quadros; quadros 120 a 180, cursor viaja e clica numa pílula (receita 8), com `pop` no clique; quadros 180 a 270, a pílula faz morph para a barra de prompt e o prompt é digitado palavra por palavra, com caret piscando; quadros 270 a 330, a barra faz morph para o card do resultado, que se constrói por dentro (receita 9); quadros 330 a 360, as 2 opções A e B entram na tela, legíveis no celular, com a narração lendo as duas.
- Ajuste o segundo comando para a virada: num vídeo de 6 segundos ele cabe nos quadros 270 a 300, e a aurora faz o crossfade de paleta nesse momento. Num vídeo de 60 a 90 segundos, o segundo comando é a escolha do final, e o crossfade marca a decisão.
- Confira o teste do mudo: a escolha precisa ser legível em 5 segundos sem som, e o cursor precisa ser visível o tempo todo, porque ele é o "alguém usando" da cena.

### Modelo D: tipografia clara, 6 segundos, 360 quadros

- Use para o vídeo de fato, frase ou pergunta: o texto é o protagonista e o fundo é o gelo da marca.
- Siga a ordem: quadros 0 a 90, palavras entrando uma por uma no beat da fala (receita 7), com contraste de escala entre ligação e conceito; quadros 90 a 180, a palavra-chave gigante com sombra-fantasma colorida e rabisco desenhado; quadros 180 a 240, beat de inversão escura no meio (receita 10); quadros 240 a 300, sistema orbital de nós em volta da logo (receita 6) ou contador gigante (receita 9); quadros 300 a 360, slogan em 3 golpes com ícone e fecho com logo e CTA clicado pelo cursor.
- Ajuste a sombra-fantasma com o texto repetido em cinza-claro acima e abaixo da palavra-chave, desvanecendo: é o truque do iPhone SE do estudo para dar profundidade a um campo chapado.
- Confira cada palavra em tamanho real antes de aprovar: a contact sheet engana e esconde estouro de largura. Leia o erro 28 em [erros comuns](erros-comuns.md).

## As estruturas da história curta

- História narrada: gancho de 1 a 3 segundos, mundo normal, mundo estranho, virada, volta transformada e CTA nos últimos 5 segundos. É a jornada do herói comprimida em 3 batidas. Leia as estruturas no SKILL.md, na seção "Escreve o roteiro".
- História interativa: gancho de 1 a 3 segundos, situação do nível, complicação, escolha com 2 opções e CTA de voto nos últimos 5 segundos. O clímax fica na escolha, não antes dela.
- Vídeo vertical curto de fato: gancho de 1 a 2 segundos, setup de 3 a 15 segundos, valor até 5 segundos antes do fim e CTA nos últimos 5 segundos, com um reset de retenção aos 25 a 30 segundos no vídeo de 60 segundos.
- Coloque o melhor momento aos dois terços do vídeo, não no final. No vídeo curto, o melhor momento é a virada ou a escolha, e ela não pode escorregar para o fim.

## O pipeline completo até o MP4

Siga nesta ordem e não pule etapas. Cada etapa tem um arquivo de saída que a próxima etapa usa.

1. Escreva o roteiro com `$roteiro`, com o hook no tamanho da plataforma e uma ideia por vídeo.
2. Monte o storyboard com `$storyboard`, com 1 cena a cada 10 segundos, e mostre ao usuário antes de qualquer render. Os tempos do storyboard são estimativas.
3. Grave a narração antes de animar, em uma só passada suave, com a voz fixa do canal. A narração não muda mais depois deste passo.
4. Transcreva a narração real com o faster-whisper e gere o arquivo `.ass` com o tempo de cada palavra. A transcrição real dá os tempos verdadeiros de cada cena e de cada palavra.
5. Escreva uma página HTML por cena, com a função `renderFrame(n)` desenhando o quadro n. A função recebe o número do quadro e desenha tudo a partir dele: posição, escala, opacidade e texto. Nada de animação em tempo real, porque o tempo real não é determinístico.
6. Renderize cada cena com o `render.mjs`, em `~/workspace/tools/renderizador-cdp/render.mjs`, com o número de quadros da duração real da cena. Leia a seção do motor abaixo.
7. Monte cada cena com o ffmpeg, a partir dos JPGs, a 60 fps. Junte as cenas na ordem do storyboard.
8. Junte a narração intocada, os efeitos no mesmo segundo da ação e a música baixa sob a narração. O vídeo segue a narração, nunca o contrário. Leia a regra de sincronia em [montagem](montagem.md).
9. Queime a legenda karaokê no vídeo, com a palavra falada em amarelo e o resto em branco, a partir do mesmo arquivo `.ass`. Leia o guia em [legendas](legendas.md).
10. Confira o volume final no alvo de menos 14 LUFS e exporte o MP4 final em 1080x1920 para vertical ou 1920x1080 para longo.

## O motor: renderFrame(n) e render.mjs

### Como funciona

- A página HTML define `window.renderFrame(n)`. O `render.mjs` abre a página num Chromium sem tela, chama `renderFrame(n)` para cada quadro e fotografa com captura de tela, salvando `frame-0000.jpg`, `frame-0001.jpg` e assim por diante, porque o padrão agora é JPEG. Use PNG só para preview, com `FMT=png`.
- Uso: `node render.mjs <pagina.html> <dir_frames> <num_frames> [largura] [altura]`. A largura e a altura padrão são 1280x720. Para o vertical, passe 1080 e 1920.
- Requisitos: Node 22 ou mais novo, com o WebSocket global, e o Chromium em `/opt/meta-chromium/chrome`, que é o navegador da imagem da máquina. O script não precisa de pacote npm nenhum.
- O script falha com mensagem clara quando a página não define `renderFrame`, quando o Chromium não é encontrado ou quando o quadro vem vazio. Não ignore a mensagem de erro e renderize de novo.

### Velocidade medida

Números medidos em 06/11/2026, em sequência, com o `render.mjs` cujo padrão agora é JPEG. O fps de parede é o que manda no prazo, porque inclui a subida do Chromium. O fps interno é o do loop de render.

- 1280x720, cena de teste, 48 quadros: PNG 4,58 s de parede, 10,48 fps (interno 12,11), 1.781.460 bytes no total. JPEG 4,28 s de parede, 11,20 fps (interno 13,01), 2.235.372 bytes no total.
- 1080x1920 vertical, `template.html`, 120 quadros: JPEG 12,22 s de parede, 9,82 fps (interno 10,32), 10.514.122 bytes no total. PNG 75,40 s de parede, 1,59 fps (interno 1,60), 82.577.477 bytes no total.
- Um Short vertical de 60 segundos em JPEG leva cerca de 6,1 minutos de render a 60 fps (3.600 quadros), cerca de 4,1 minutos a 40 fps (2.400 quadros) e cerca de 2,4 minutos a 24 fps (1.440 quadros).
- A montagem a 60 fps foi verificada: 120 quadros JPEG viraram MP4 1080x1920 a 60 fps com 2,000 s, conferido com `ffprobe`.
- Correção honesta sobre o JPEG: a afirmação de que o JPEG é cerca de 2 vezes mais rápido que o PNG não se confirmou em 720p, onde o JPEG foi só cerca de 7 por cento mais rápido que o PNG. Em vertical, o JPEG é 6,2 vezes mais rápido que o PNG. O JPEG continua o padrão porque o vertical é o formato mãe e o PNG em vertical é inviável, com 1,59 fps. Em cena de cores chapadas o JPEG sai maior em bytes que o PNG, porque o PNG comprime melhor áreas lisas. O ganho do JPEG é tempo, não tamanho.
- O padrão desta skill é 60 fps, com 40 fps como mínimo aceitável. Nunca entregue abaixo de 40 fps. O custo de 60 fps é 2,5 vezes o de 24 fps em número de quadros, então some o tempo de render antes de prometer prazo.
- Ressalva de carga da máquina, medida em 06/11/2026: uma medição recente com a máquina carregada (load cerca de 1,6) rendeu 6,94 fps em 24 quadros verticais, contra 9,82 fps na medição limpa de 120 quadros, e a cena-controle em 720p também caiu (9,04 fps contra 11,20 fps), então a queda é carga da máquina, não as fontes. Em 06/11/2026, na mesma rodada, o template com os helpers novos rendeu 6,41 fps em 24 quadros verticais, e uma cena de teste com aurora de 6 fitas com blur rendeu 2,76 fps em 120 quadros. Um Short de 60 s a 60 fps continua na casa dos 6 minutos de render em JPEG, mas re-medir numa janela quieta antes de prometer prazo, porque blur pesado e carga da máquina derrubam o fps.
- Para comparação, o PIL rendeu cerca de 23 fps em 1280x720, com 240 quadros em 10,4 s. Um Short de 60 segundos a 60 fps, com 3.600 quadros, levaria cerca de 2,6 minutos em 720p pelo PIL. O PIL em vertical não foi medido, então não prometa número nenhum para ele em vertical sem medir.

### As 3 peças novas do renderizador

Use estas 3 peças junto com o `render.mjs`. Todas as 3 ficam em `~/workspace/tools/renderizador-cdp/` e foram testadas em 06/11/2026. A origem das 3 é o repositório IuryDevz/Motion-Frames-Skill-Muse-AI, que não tem arquivo LICENSE. Mantenha a atribuição à origem quando copiar ou adaptar qualquer uma delas.

- `template.html`: página base 1080x1920 para começar uma cena nova. Traz os helpers `spring`, `seg` e `hash` e a estrutura `renderFrame(n)`. O `spring` é um spring analítico subamortecido, que parte de 0 e assenta em 1, puro em tempo. O `seg` dá o progresso de 0 a 1 de uma janela de tempo entre os quadros a e b. O `hash` dá um número determinístico para um aleatório reprodutível. Expansão 2026-11-06: helpers novos de receitas, `CORES`, `lissajous`, `corLerp`, `contar`, `poeira`, `gradePontos`, `fundoEstudio`, `fundoAurora`, `fundoGelo`, `cuboHTML`, `orbita`, `rabiscoSVG`, `cursorHTML`, `palavraNoBeat` e `medeTexto`, com as receitas completas nas seções de receitas deste guia e a cena de teste em `~/workspace/tools/renderizador-cdp/teste-receitas.html`. A cena de exemplo é a Lua fugindo da Terra, no estilo do canal. Teste feito: 24 de 24 quadros verticais renderizados, todos diferentes. Copie o arquivo e reescreva a cena, sem mudar os helpers.
- `preview.mjs`: renderiza só os quadros listados, para conferir a cena sem renderizar tudo. Uso: `node preview.mjs <pagina.html> <dir_frames> <quadros_csv> <total_quadros> [largura] [altura]`. Exemplo: `node preview.mjs cena.html prev "0,60,160,300" 840 1080 1920`. A saída é `f0000.png`, `f0060.png` e assim por diante, com o FMT padrão `png`. Teste feito com os quadros 0, 12 e 24, com a correção do FMT verificada com JPGs de verdade. Use o preview antes do render completo, para aprovar visual e movimento com `$teste`.
- `sfx_kit.py`: kit de efeitos sonoros sintetizados com numpy e scipy, com os 6 sons amarrados ao número do quadro: `pop` para clique e palavra-chave, `tick` para digitação e contador, `whoosh` para transição e morph, `shimmer` para confirmação, `tone` para nota e `pad` para cama harmônica. Uso: crie um `Track(dur_s, seed, fps=60)` e chame um som com o número do quadro, como `tr.pop(158)`. O quadro N corresponde ao instante N dividido por 60 segundos do vídeo, que é o mesmo fps do render. Rode com o python3 do sistema, porque o scipy 1.11.4 já está nele e nenhuma adaptação foi necessária. O venv `~/.venv-whisper` tem numpy mas não tem scipy, então não rode o kit nele. Teste feito: wav de 5,000 s, 48000 Hz, 1 canal, com um evento de cada som. Mixe a trilha de efeitos a cerca de 0,5 para ela ficar sob a narração.

### Como escrever renderFrame(n)

- Faça `renderFrame(n)` ser uma função pura do número do quadro: o mesmo n desenha sempre o mesmo quadro. Não use relógio, não use número aleatório sem semente e não use animação CSS em tempo real, porque nada disso é determinístico.
- Converta o quadro em tempo com `tempo = n / fps` e dirija a animação pelo tempo. O easing vem de função, como ease-out cúbico, e não de transição CSS.
- Desenhe em camadas: fundo, plano do meio, protagonista, texto e primeiro plano. Cada camada é um elemento da página com posição absoluta.
- Teste a página no navegador antes de renderizar. Abra a página, chame `renderFrame(0)` e `renderFrame(24)` no console e confira se o quadro muda. Página que não muda no console não muda no render.
- Use os helpers de receitas do `template.html` em vez de reescrever cada efeito do zero: `fundoEstudio`, `fundoAurora` e `fundoGelo` para os fundos, `cuboHTML` para o cubo 3D, `orbita` para os nós, `rabiscoSVG` para os rabiscos, `cursorHTML` para o cursor, `contar` para os contadores e `medeTexto` para conferir a largura do título. As receitas completas, com o que copiar e onde colar, estão nas seções de receitas deste guia.

### Como montar os JPGs em vídeo

- Monte cada cena com `ffmpeg -y -framerate 60 -i frame-%04d.jpg -c:v libx264 -pix_fmt yuv420p cena.mp4`, com o framerate igual ao fps do vídeo, que é 60 por padrão e nunca abaixo de 40. Para montar um preview em PNG, use `frame-%04d.png` com o framerate do preview.
- Junte as cenas na ordem do storyboard com a lista de concat do ffmpeg. Todos os clipes precisam ter a mesma resolução, o mesmo fps e o mesmo codec. Leia o procedimento em [montagem](montagem.md).
- Confira a cena montada antes de juntar com a narração. Se a cena entrar fora de ordem, o erro aparece aqui.

## A sincronia palavra por palavra

- A narração manda no movimento. O gesto acontece no mesmo segundo da palavra que ele ilustra, a palavra-chave acende no quadro exato em que a palavra começa na narração e o morph acontece no segundo da virada.
- Use os tempos de palavra do faster-whisper, com `word_timestamps`, para ligar cada palavra ao quadro dela. O quadro da palavra é `quadro = tempo_da_palavra x fps`.
- A duração de cada cena é a duração real da fala dela, medida da transcrição. Nunca use a duração estimada do storyboard e nunca use uma escala uniforme no vídeo inteiro. A escala uniforme desalinha cena por cena. Leia a regra completa em [montagem](montagem.md) e o erro 12 em [erros comuns](erros-comuns.md).
- No trilho de histórias, ajuste os movimentos dentro da cena para a nova duração: use o fator de escala de tempo da cena para manter a posição relativa de cada evento, como a contagem do número e a queda do carimbo.
- Verifique a sincronia antes de entregar: extraia o frame no início de pelo menos 6 cenas espalhadas pelo vídeo e confira se o visual e a legenda batem com a fala daquele segundo.

## Checklist da cena de história

Antes de entregar qualquer cena, confira estes 8 itens. Se algum faltar, refaça a cena.

1. Protagonista: visível, grande no quadro e com pelo menos 1 gesto com intenção. No estilo de tipografia, a palavra protagonista muda pelo menos 2 vezes.
2. Micro-evento: alguma mudança visível a cada 0,5 a 1,5 segundo, sem trecho parado.
3. Fundo: vivo o tempo todo, com 3 camadas e parallax.
4. Texto: legível no celular, com uma ideia por quadro e tempo de leitura de cerca de 2 segundos por linha curta. Confira 2 a 3 quadros-chave em tamanho real, porque a contact sheet engana e esconde colisão de texto e estouro de largura. Leia o erro 28 em [erros comuns](erros-comuns.md).
5. Som: cada movimento tem o efeito dele no mesmo segundo.
6. Sincronia: o gesto e a palavra acendem no mesmo segundo da narração real.
7. Continuidade: mesmo protagonista, mesma roupa, mesmo cenário e mesma voz da cena anterior.
8. Teste do mudo: 3 ou mais movimentos visíveis em 10 segundos sem som. Na história interativa, a escolha é legível em 5 segundos sem som.

## Aceite por estilo de história

Use o checklist da cena de história acima e some o critério do estilo do vídeo. Cena que falha no critério do estilo volta para o script, mesmo passando no checklist genérico.

- Aprove o estilo cinema e morph quando cada morph liga ideias com relação direta e dura de 0,5 a 1 segundo. Rejeite quando o morph liga ideias sem relação, quando o morph usa easing linear e quando a cena volta ao ponto inicial com salto no loop.
- Aprove o estilo promo premium quando o produto fica no centro com o fundo em menos contraste que o herói e o resultado aparece no gancho. Rejeite quando o fundo brilha mais que o produto, quando o logo aparece sem preload no quadro 0 e quando a marca usa paleta inventada em vez da paleta real do site.
- Aprove o estilo cena interativa quando a cena corre sem cortes, o cursor fica visível o tempo todo e as 2 opções entram legíveis nos últimos 5 segundos. Rejeite quando a escolha é óbvia, quando há mais de 2 opções e quando o cursor some ou salta em vez de viajar com easing.
- Aprove o estilo tipografia clara quando cada palavra entra no quadro exato da fala, com contraste de escala entre ligação e conceito, e a palavra-chave leva o rabisco no beat. Rejeite quando o título estoura 1000 px de largura, quando duas ideias dividem o mesmo quadro de texto e quando a palavra fica menos de 2 segundos na tela.

## O que não pode se repetir

- Nunca apresente uma cena de zoom lento como animada. Se o usuário disser que está parado, ele está certo. Refaça. Leia o erro 3 em [erros comuns](erros-comuns.md).
- Nunca produza o vídeo inteiro sem aprovar 1 cena de teste com `$teste`. A cena de teste aprova visual, movimento e voz com 1 cena em vez de refazer o vídeo todo.
- Nunca monte o vídeo com os tempos estimados do storyboard. Os tempos reais vêm da transcrição da narração pronta.
- Nunca prometa fps ou tempo de render sem medir. O número medido está na seção do motor acima. Se a máquina mudar, meça de novo.

## Receitas GSAP para renderFrame(n)

Origem: gsap-core e gsap-timeline em https://github.com/greensock/gsap-skills

- Porte os easings do GSAP como funções puras de quadro. O GSAP não roda dentro do renderFrame determinístico, então o que viaja é a curva e não a biblioteca.
- Use power2.out para contadores, barras e entradas padrão. A contagem usa ease-out cúbico dentro do helper contar e o número assenta sem solavanco.
- Use back.out(1.7) para entradas de título e palavra-chave. O overshoot dá o soco do título e assenta em seguida.
- Use power3.inOut para morphs e transições de paleta. O morph dura 0,5 a 1 segundo e nunca usa easing linear.
- Use power2.in para saídas. A saída dura cerca de 75 por cento da entrada e acelera para fora do quadro.
- Aplique stagger nas palavras do karaokê com 6 a 10 quadros entre palavras a 60 fps. Cada palavra acende no quadro em que ela começa na narração, com os tempos reais do faster-whisper.
- Aplique stagger de 12 quadros por camada na construção de cards. Anel, título, barras e progresso entram um depois do outro e nunca tudo junto.
- Nomeie os beats da narração com labels na cena. Gancho, revelação, virada e CTA viram marcos de quadro e a revisão busca direto pelo marco.
- Fixe os defaults do canal em cada cena. Duração de 0,5 segundo e ease power2.out para todos os movimentos, salvo exceção nomeada no plano da cena.
- Anime só transforms com posição, escala e rotação. Nunca anime largura, altura, topo ou esquerda, porque eles recalculam layout e derrubam os 60 fps.
- Prefira autoAlpha a opacity nas entradas e saídas. O elemento some de verdade ao chegar a 0 e não fica invisível bloqueando nada.
- Copie este esqueleto de stagger para a legenda karaokê e ajuste só os inícios com os tempos reais de cada palavra.

```js
function renderFrame(n) {
  const palavras = [
    { t: "A LUA", inicio: 0 },
    { t: "ESTÁ", inicio: 24 },
    { t: "FUGINDO", inicio: 48 }
  ]
  const ativa = palavraNoBeat(n, palavras.map(p => p.inicio))
  let html = ""
  palavras.forEach((p, i) => {
    if (i > ativa) return
    const u = easeOutCubic(seg(n, p.inicio, p.inicio + 12))
    const dy = 700 + i * 170 + (1 - u) * 90
    html += `<div style="opacity:${u.toFixed(2)}"><div style="text-align:center"><div style="transform:translateY(${dy.toFixed(0)}px)"><span style="font-family:'Archivo Black'"><span style="font-size:150px"><span style="font-weight:900"><span style="color:#FFFFFF">${p.t}</span></span></span></span></div></div></div>`
  })
  stage.innerHTML = `${fundoEstudio(n, CORES.laranja)}${html}`
}
```

## Portão de vídeo estático

Origem: hyperframes e hyperframes-cli em https://github.com/heygen-com/hyperframes

- Rejeite o clipe com 3 segundos ou mais sem mudança visível. O portão é o conceito do check do HyperFrames, que falha a varredura de estático quando o vídeo passa 3 segundos sem mudar.
- Aplique o portão como método manual e não dependa da ferramenta. O check do HyperFrames é um comando do CLI da origem e o portão desta skill é a medição com ffmpeg e o teste do mudo.
- Meça a mudança comparando quadros com ffmpeg. Extraia 1 quadro por segundo e compare os quadros vizinhos. Quadros iguais por 3 segundos seguidos reprovam o clipe.
- Faça o teste do mudo em cada clipe. Assista sem som e marque cada mudança visível. Menos de 3 movimentos em 10 segundos é cena parada e o clipe volta para refação.
- Trate o portão como verificação de cena e não de vídeo inteiro. Um clipe parado no meio do vídeo reprova mesmo que o resto se mova.
- Registre o portão no checklist da cena. A cena só vai para a montagem depois de passar no portão, no teste do mudo e na sincronia em 6 inícios de cena.

## Checklist entrar, segurar, sair com vida no hold e payoff

Origem: remotion-motion-graphics em https://github.com/fernandokaraka/remotion-motion-graphics-skill

- Complete entrar, segurar e sair dentro da duração da cena. Nada aparece no quadro 0 e nada continua se movendo no último quadro. Reserve a saída dentro da duração.
- Comece com spring e nunca com movimento linear. A mola dá antecipação, overshoot e assentamento. Use easing só quando a mola não servir.
- Dê stagger de 6 a 10 quadros a 60 fps nas entradas e nas saídas, na mesma ordem. Entradas juntas parecem erro de montagem.
- Mantenha vida no hold sem wobble. Use flutuação suave, brilho lento ou varredura de luz, sentido e não notado.
- Coloque o payoff no momento chave. Pop de escala, anel, brilho e som caem juntos no beat da narração.
- Confira stills nos quadros chave antes do render completo. Meio da entrada, payoff, meio do hold e meio da saída, lidos em tamanho real.
- Diagnostique antes de decorar. Um gráfico sem graça costuma ser um defeito real, como interpolação sem clamp exibindo número errado, e não falta de molas.
- Respeite as margens de segurança de 5 a 10 por cento e uma sombra atrás do texto sobre imagem. Um único elemento focal fica em negrito e textos longos encolhem e quebram em vez de estourar.
- Corte o silêncio inicial do arquivo de áudio. Cerca de 80 ms de ar morto no começo deixam o áudio 80 ms atrasado e simulam dessincronia.

## Escolha o movimento pelo número

Fonte: motion-prompt, sintetizado com palavras próprias, em https://github.com/showheyohtaki/motion-prompt

- Escolha o movimento pelo nome e não pela descrição solta. A biblioteca tem 192 movimentos numerados em 8 pacotes de 24, com amostra animada, tempos, easing e código. A galeria está em https://showheyohtaki.github.io/motion-prompt/
- Mostre a galeria para o usuário escolher visualmente quando ele não souber o nome do efeito. Receba os números escolhidos e reconstrua exatamente aqueles, sem inventar, trocar ou acrescentar.
- Use 1 elemento em movimento por vez e 1 família de easing por vídeo. Faça cada entrada cair num beat e segure depois de cada movimento antes do próximo.
- Copie os números do spec, com durações, delays, easings, overshoot, distâncias, ângulos e escala. Troque só palavras, cores, logos e imagens.

## Dispare o visual na palavra

Fonte: explainer-animation, sintetizado com palavras próprias, em https://github.com/c-kick/hnl-agent-skills

- Dispare cada beat visual numa palavra da narração e não num tempo absoluto. O carimbo cai numa palavra e o congelamento cai noutra. A sincronia por palavra pesa mais na qualidade percebida que a sincronia por cena.
- Guie o visual pelo tempo da palavra falada, medido do faster-whisper. Se a narração for regravada, o visual se realinha sozinho pela palavra.
- Mantenha 1 ideia por beat e 1 foco por momento. Margem de 60 a 80 px das bordas e nunca sobreponha rótulos.
- Faça a transição com wipe de 0,65 segundo e som de rasgo. O wipe marca a troca de beat sem flash preto.

## Rolagem infinita sem corte

Fonte: remotion-3d-ticker, sintetizado com palavras próprias, em https://github.com/vibe-motion/skills

- Monte a rolagem infinita duplicando a lista de itens. Translade a coluna de 0 por cento a menos 50 por cento. O quadro em menos 50 por cento é idêntico ao de 0 por cento, então o loop fecha sem corte visível.
- Dê a cada coluna duração e direção próprias. Colunas em velocidades e sentidos opostos criam parallax.
- Use a rolagem infinita para mural de imagens, créditos e tela de próximo vídeo. Nunca use para o corpo do vídeo, porque rolagem contínua compete com a narração.
- Avise que o repositório de origem está sem manutenção e sem arquivo de licença. Use a técnica com palavras próprias e nunca copie o arquivo do componente.

## Tempos de respiro

Fonte: manim-video, sintetizado com palavras próprias, em https://github.com/NousResearch/hermes-agent

- Dê respiro depois de cada revelação. Título aparece em 1,5 segundo e espera 1 segundo. Revelação chave leva 2 segundos e espera 2 segundos. Momento de descoberta leva 2,5 segundos e espera 3 segundos.
- Nunca corra de uma animação para a outra. A pausa depois da revelação nunca é tempo perdido.
- Dirija a atenção por camadas de opacidade. Elemento primário em 1,0, contexto em 0,4 e estrutura em 0,15.
- Itere no rascunho leve e só renderize o final em qualidade cheia. Rascunho barato primeiro e 1080x1920 a 60 fps só no final.

## Beat-locked a 120 BPM com cortes nos beats

Origem: kinetic-reel em https://github.com/tuzhechen2005/opus-video-skills

- Trave o ritmo em 120 BPM quando o vídeo for de tipografia cinética ou reel. Um beat dura 0,5 segundo e um compasso dura 2 segundos.
- Corte nos beats e mude de capítulo nos compassos. O corte cai no beat e nunca entre beats.
- Sincronize letras, chips e contadores aos hits da trilha. Cada elemento entra rápido com expo-out, segura e passa no próximo hit.
- Marque os hits na timeline da cena antes de animar. A lista de hits vem da trilha e a animação segue a lista.
- Use a trilha sintetizada a partir da mesma timeline quando a música for gerada. Cada batida cai no quadro certo porque música e imagem nascem da mesma grade.
- Adapte o beat-locked ao Short narrado com folga. A narração manda no ritmo e o beat marca os cortes e os pops, sem atropelar a fala.

## Regra de honestidade de dados com selo ILUSTRATIVO

Origem: kinetic-reel em https://github.com/tuzhechen2005/opus-video-skills

- Use só números da fonte com escopo. O número entra no vídeo com a fonte e o recorte dele.
- Marque todo dado ilustrativo com o selo ILUSTRATIVO no HUD. O selo fica visível enquanto o dado estiver na tela.
- Nunca desenhe dado por dimensão que você não tem. Visualize o processo e não o número inventado.
- Trate o selo como regra de roteiro e não de edição. O roteiro já marca o que é ilustrativo antes do storyboard.
- Alinhe esta regra com o erro 7 e o erro 21 desta skill. Número sem fonte e estimativa tratada como exato já custaram retrabalho e confiança.
