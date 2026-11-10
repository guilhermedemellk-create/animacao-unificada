# Renderizador CDP frame a frame

Renderiza uma página HTML que define `renderFrame(n)` quadro a quadro num Chromium sem tela, via Chrome DevTools Protocol. É a opção B do trilho 2D infográfico. Use quando a cena tem muito texto e a tipografia do HTML e do CSS ganha do desenho por PIL.

## O que é

- Um script só, `render.mjs`, em `~/workspace/tools/renderizador-cdp/render.mjs`, sem dependências npm. Usa só o Node 22 ou mais novo, com o WebSocket global e o `fetch` nativos.
- O script lança o Chromium sem tela, conecta no DevTools, abre a página, verifica que ela define `renderFrame(n)`, chama `renderFrame(n)` para cada quadro de 0 até o total menos 1 e fotografa com `Page.captureScreenshot`.
- A saída é um JPG por quadro, `frame-0000.jpg`, `frame-0001.jpg` e assim por diante, no diretório de saída, porque o padrão do `FMT` é JPEG. Use `FMT=png` para sair em PNG, só para preview.
- O render é determinístico: a mesma página gera os mesmos pixels em toda rodada, porque cada quadro é desenhado por uma chamada explícita a `renderFrame(n)`, sem relógio e sem aleatoriedade.

## Requisitos

- Node 22 ou mais novo, com WebSocket global. Testado com Node v24.22.1.
- Um Chromium sem tela. O usado no teste é o `/opt/meta-chromium/chrome`, o Muse Browser 155.0.8059.91, que já vem na imagem da máquina e sobrevive a reinicializações. Nada foi instalado.
- O Chromium da imagem exige a política WebGL da imagem para iniciar. O arquivo `webgl-policy.txt` fica ao lado do `render.mjs`, com o cabeçalho `hatch-webgl-allowed-domains-v1` e os domínios, um por linha, ordenados e terminando com quebra de linha. O `render.mjs` calcula o SHA-256 desse arquivo e lança o Chromium com as flags `--hatch-webgl-allowed-domains-file` e `--hatch-webgl-allowed-domains-sha256`. Sem isso o Chromium morre na largada com a mensagem `Hatch WebGL domain policy is required for browser startup`.
- A variável de ambiente `CHROME_BIN` aponta outro binário de Chromium, quando existir um.
- A variável de ambiente `FMT` escolhe o formato dos quadros: `jpeg` é o padrão, com quality 90 e arquivos `.jpg`, e `png` sai em PNG. O padrão é JPEG porque o vertical é o formato mãe e o PNG em vertical é inviável, com 1,59 fps medido. O `preview.mjs` tem padrão próprio, `png`, e aceita `FMT=jpeg` para sair em JPG.
- A variável de ambiente `PORT` fixa a porta do DevTools. No `render.mjs` o padrão é uma porta sorteada entre 9333 e 9832, e no `preview.mjs` o padrão é 9333. Fixe a porta quando vários renders rodam ao mesmo tempo.
- O ffmpeg monta o MP4 a partir dos JPGs. Ele não faz parte do renderizador.

## Uso

```
node render.mjs <pagina.html> <dir_frames> <num_frames> [largura] [altura]
```

- `pagina.html` é a página da cena, que precisa definir `window.renderFrame(n)` e desenhar o quadro `n` quando chamada.
- `dir_frames` é o diretório onde saem os JPGs. O script cria o diretório quando não existe.
- `num_frames` é o total de quadros. A 60 fps, 120 quadros são 2 segundos.
- `largura` e `altura` são opcionais e o padrão é 1280x720. Para TikTok e Shorts use 1080x1920.
- Para montar o vídeo, rode o ffmpeg depois do render:

```
ffmpeg -y -framerate 60 -i <dir_frames>/frame-%04d.jpg -c:v libx264 -pix_fmt yuv420p <saida>.mp4
```

## Quando usar o renderizador CDP e quando usar o PIL

- Use o renderizador CDP quando a cena tem muito texto, com títulos longos, parágrafos, listas e números grandes com tipografia cuidada. O HTML e o CSS resolvem quebra de linha, alinhamento e fontes do sistema sem desenhar letra por letra.
- Use o PIL quando a cena é um diagrama com geometria exata, com formas, linhas e setas desenhadas por coordenadas. O PIL é o caminho provado em produção, com as 72 cenas do vídeo 1 do O Laboratório Curioso renderizadas em 20 a 30 minutos no total.
- Nunca misture os dois no mesmo vídeo. Escolha um na entrevista e siga só ele até o fim.
- Os 12 princípios da animação valem iguais nos dois. A contagem do número, o easing e o carimbo seguem as mesmas receitas da trilha 2D em [animação](animacao.md).

## Erros

- O script falha com mensagem clara e código de saída diferente de zero quando o Chromium não é encontrado, quando a página não existe, quando a página não define `renderFrame(n)`, quando o DevTools não responde no tempo limite ou quando um screenshot vem vazio.
- Quando a página não define `renderFrame`, a mensagem diz o tipo encontrado, para diferenciar página errada de página que ainda não carregou.

## Teste feito e resultado medido

Teste rodado em 2026-11-06, em 3 rodadas, com a página `teste-cena.html` em `~/workspace/tools/renderizador-cdp/`. A cena é no estilo do canal: fundo azul-marinho `#1A305A`, título `A LUA ESTÁ FUGINDO DA TERRA`, contador grande de 0 a 47 e barra laranja crescendo de 0 por cento a 100 por cento.

- Comando: `node render.mjs teste-cena.html frames-teste 48 1280 720`
- Quadros gerados: 48 de 48, PNG 1280x720.
- Os quadros mudam de verdade: os md5 dos 6 quadros amostrados, 0000, 0009, 0019, 0029, 0039 e 0047, são todos diferentes entre si.
- Determinístico: o `frame-0000.png` tem o mesmo md5, `5a06ebbcec1e00514254cdc1c1bc72ab`, nas 3 rodadas.
- Tempo medido, em sequência, em 06/11/2026, com 48 quadros em 1280x720: PNG 4,58 segundos de parede, 10,48 fps (interno 12,11), 1.781.460 bytes no total. JPEG 4,28 segundos de parede, 11,20 fps (interno 13,01), 2.235.372 bytes no total. A maior parte do tempo é a captura de screenshot e o Chromium sobe em cerca de 1 segundo.
- Tempo medido em vertical 1080x1920, com o `template.html` e 120 quadros: JPEG 12,22 segundos de parede, 9,82 fps (interno 10,32), 10.514.122 bytes no total. PNG 75,40 segundos de parede, 1,59 fps (interno 1,60), 82.577.477 bytes no total.
- Um Short vertical de 60 segundos em JPEG leva cerca de 6,1 minutos de render a 60 fps (3.600 quadros), cerca de 4,1 minutos a 40 fps (2.400 quadros) e cerca de 2,4 minutos a 24 fps (1.440 quadros).
- A montagem a 60 fps foi verificada: 120 quadros JPEG viraram MP4 1080x1920 a 60 fps com 2,000 s, conferido com `ffprobe`.
- Correção honesta sobre o JPEG: a afirmação de que o JPEG é cerca de 2 vezes mais rápido que o PNG não se confirmou em 720p, onde o JPEG foi só cerca de 7 por cento mais rápido que o PNG. Em vertical, o JPEG é 6,2 vezes mais rápido que o PNG. O JPEG continua o padrão porque o vertical é o formato mãe e o PNG em vertical é inviável, com 1,59 fps.
- MP4 de teste: `teste-cena.mp4`, h264, 1280x720, 24 fps, duração de 2,000 segundos, 49 KB, verificado com `ffprobe`. É o teste original, a 24 fps, antes do padrão mudar para 60 fps.

## As 3 peças novas

As 3 peças ficam ao lado do `render.mjs` em `~/workspace/tools/renderizador-cdp/` e foram testadas em 06/11/2026. A origem das 3 é o repositório IuryDevz/Motion-Frames-Skill-Muse-AI, que não tem arquivo LICENSE. Mantenha a atribuição à origem quando copiar ou adaptar qualquer uma delas.

- `template.html`: página base 1080x1920 para começar uma cena nova, com os helpers `spring`, `seg` e `hash` e a estrutura `renderFrame(n)`. O `spring` é um spring analítico subamortecido, o `seg` dá o progresso de 0 a 1 de uma janela de tempo entre os quadros a e b, e o `hash` dá um número determinístico para um aleatório reprodutível. A cena de exemplo é a Lua fugindo da Terra, no estilo do canal. Teste feito: 24 de 24 quadros verticais renderizados, todos diferentes. Copie o arquivo e reescreva a cena, sem mudar os helpers.
- `preview.mjs`: renderiza só os quadros listados, para conferir a cena sem renderizar tudo. Uso: `node preview.mjs <pagina.html> <dir_frames> <quadros_csv> <total_quadros> [largura] [altura]`. Exemplo: `node preview.mjs cena.html prev "0,60,160,300" 840 1080 1920`. A saída é `f0000.png`, `f0060.png` e assim por diante, com o FMT padrão `png`, e aceita `FMT=jpeg` para sair em JPG. Teste feito com os quadros 0, 12 e 24, com a correção do FMT verificada com JPGs de verdade. A porta padrão do DevTools é 9333 e pode ser fixada com `PORT`.
- `sfx_kit.py`: kit de efeitos sonoros sintetizados com numpy e scipy, com os 6 sons amarrados ao número do quadro: `pop` para clique e palavra-chave, `tick` para digitação e contador, `whoosh` para transição e morph, `shimmer` para confirmação, `tone` para nota e `pad` para cama harmônica. Uso: crie um `Track(dur_s, seed, fps=60)` e chame um som com o número do quadro, como `tr.pop(158)`. O quadro N corresponde ao instante N dividido por 60 segundos do vídeo, que é o mesmo fps do render. Rode com o python3 do sistema, porque o scipy 1.11.4 já está nele e nenhuma adaptação foi necessária. O venv `~/.venv-whisper` tem numpy mas não tem scipy, então não rode o kit nele. Teste feito: wav de 5,000 s, 48000 Hz, 1 canal, com um evento de cada som. Mixe a trilha de efeitos a cerca de 0,5 para ela ficar sob a narração.
- Detalhe corrigido no teste: a primeira versão deixava o processo parado por cerca de 12 segundos no fim, porque o processo crashpad do Chromium segurava os pipes de saída. O script agora sai explicitamente após o término e nenhum processo do Chromium fica pendurado.

## Limites conhecidos

- A velocidade medida, em JPEG, é de 11,20 quadros por segundo em 1280x720 e 9,82 quadros por segundo em vertical 1080x1920, limitada pela captura de screenshot. É mais lenta que o PIL na cena de teste, que rendeu 240 frames em 10,4 segundos, ou cerca de 23 quadros por segundo. Um Short vertical de 60 segundos em JPEG leva cerca de 6,1 minutos a 60 fps e cerca de 4,1 minutos a 40 fps. Para um vídeo longo, some o tempo antes de prometer prazo.
- A página carrega de `file://`, então fontes externas e recursos de rede precisam estar em arquivos locais ou a página precisa de rede no momento do render.
- A página não pode depender de relógio nem de aleatoriedade, senão o render deixa de ser determinístico.
