# Estudo de caso — vídeo 1 do O Laboratório Curioso

Este é o primeiro vídeo feito com esta skill que virou caso de estudo. Ele é a quarta das cinco opções de estilo da skill, o infográfico 2D por código. Leia este arquivo antes de oferecer essa opção ao usuário e antes de produzir um vídeo nesse estilo.

## O vídeo

- Canal: O Laboratório Curioso, @olaboratoriocurioso, estilo ciência explicada.
- Formato mãe: quiz verdade ou mentira, 10 a 12 minutos.
- Título: "10 COISAS que a NASA não quer que você saiba — VERDADE ou MENTIRA?".
- Duração final: 11 minutos e 20 segundos, 680,58 segundos.
- Resolução: 1280x720 horizontal, 24 fps, H.264 e AAC.
- Cenas: 72 cenas, uma por diagrama, uma por fato. As cenas 49 e 56 são flashes visuais sem narração.
- Roteiro: `~/workspace/your_files/roteiro-video-1-laboratorio-curioso-nasa.md`.
- Narração: `~/workspace/your_files/narracao-video-1-laboratorio-curioso-nasa.mp3`, 680,58 segundos, nunca regravada e nunca editada.
- Vídeo final: `~/workspace/your_files/video-1-laboratorio-curioso/video-1-final.mp4`.
- Legenda: `video-1-legendas.ass`, 217 segmentos da transcrição real, palavras-chave em laranja.
- Thumbnail: `thumbnail-video-1.png`, 1280x720, Lua com "10", ponto de interrogação gigante em laranja e "VERDADE OU MENTIRA?".

## O estilo: infográfico 2D por código

- Motion graphics 2D infográfico, feito por código com Python e PIL, sem apresentador, sem boneco e sem caixa 3D.
- Linguagem visual: linhas finas, mapas, diagramas, números grandes animados, carimbos de VERDADE e MENTIRA, painéis e grades.
- Paleta fixa: fundo #1A305A, painel #264476, linhas #8FB4E3, texto branco, laranja #FF8C1A, azul-aço #6EA8DC.
- Cores proibidas neste estilo: vermelho, amarelo e verde.
- A referência de estilo foi um vídeo de 176 segundos sobre a Guerra Fria e os 13 dias de outubro de 1962, que o Lorenzo enviou. Só a linguagem 2D veio da referência. As cores são as do canal, não as da referência.

## O pipeline

- Um script `render_cenaNN.py` por cena, numa pasta `scripts2d`, com uma biblioteca partilhada `lib_info.py` que guarda a paleta, o tamanho do quadro, o fps e as funções de desenho.
- Cada script desenha os frames da cena em PNG a 24 fps. O ffmpeg monta o MP4 de cada cena e depois concatena as 72 cenas.
- A legenda é queimada com o filtro `subtitles` do ffmpeg, a partir do arquivo `.ass` da transcrição real.
- O áudio final é a narração intocada, com efeitos e música, no alvo de menos 14 LUFS.
- Velocidade medida: a cena 1 de teste rendeu 240 frames em 10,4 segundos. As 72 cenas levaram de 20 a 30 minutos no total. É cerca de 50 vezes mais rápido que o Blender, que levava cerca de 20 minutos por clipe de 10 segundos.
- Antes do render completo de cada cena, renderize 1 frame de teste e confira: o frame não está preto, o diagrama está no centro e a legenda cabe no quadro.

## Como animar neste estilo

- Cada cena tem 1 diagrama e 1 ideia. O diagrama entra peça por peça, nunca inteiro e parado.
- O número grande conta de zero até o valor final com easing, nunca aparece pronto de uma vez.
- O carimbo de VERDADE ou MENTIRA cai no painel com antecipação e exagero, no mesmo segundo da palavra na narração.
- Linhas e setas crescem na direção do movimento. Gráficos de barra sobem com aceleração e desaceleração.
- Elementos secundários, como partículas e linhas de fundo, chegam alguns frames depois do elemento principal e oscilam antes de assentar.
- A câmera neste estilo não existe como objeto 3D. O movimento vem de zoom no diagrama, de corte entre diagramas e de deslocamento dos elementos no quadro.
- Leia os 12 princípios em [animação](animacao.md) e aplique a coluna do trilho 2D a cada cena.

## O que deu errado antes de dar certo

Leia esta história antes de oferecer o estilo. Ela é a prova de que o estilo nasce do gosto do usuário, não da ferramenta.

- A primeira versão foi feita em Blender 3D low-poly, com um boneco apresentador cientista-astronauta de fato azul-marinho, detalhes laranja e capacete com viseira escura. Foram 15 clipes renderizados e uma prévia de 2 minutos e 21 segundos. O Lorenzo rejeitou como horrível: o boneco era feio, os fundos eram vazios e as formas eram retangulares demais. A produção parou e os 15 clipes foram descartados.
- O Lorenzo enviou então o vídeo de referência da Guerra Fria e pediu aquele estilo. O estilo mudou para o infográfico 2D, sem apresentador e sem caixa 3D.
- A primeira paleta do 2D tinha o fundo #081226, escuro demais. O Lorenzo rejeitou a cor do fundo e a paleta foi clareada para #1A305A, com painel #264476. As 5 primeiras cenas renderizadas na paleta escura tiveram de ser refeitas.
- Lição: mostre 1 cena de teste ao usuário e espere a aprovação antes de renderizar as outras 71. O teste de 1 cena custa segundos e evita refazer o vídeo inteiro.

## A lição da sincronia

- A primeira montagem usou uma escala uniforme: 699 segundos de clipes multiplicados por 0,9737 para casar com 680,58 segundos de narração. A sincronia derivou cena por cena. No meio do vídeo o áudio ficou até 6 segundos atrás da imagem. No fim a narração ficou até 14 segundos na frente da imagem.
- O conserto foi remontar com a duração real de cada cena, medida da transcrição real da narração, sem escala uniforme. Cada cena começa exatamente quando a fala dela começa.
- A sincronia foi verificada em 6 inícios de cena espalhados, com desvio zero.
- A regra completa e o procedimento passo a passo estão em [montagem](montagem.md). Nunca use escala uniforme na montagem. Nunca edite a narração para caber no vídeo. É o vídeo que segue a narração.

## Quando oferecer este estilo

- Ofereça quando o usuário quer um vídeo todo animado, com identidade visual própria, sem depender de crédito de IA e sem esperar horas de render.
- Ofereça quando o tema é ciência, história, espaço ou qualquer assunto que se explica melhor com diagrama, mapa e número grande do que com personagem.
- Ofereça quando o usuário trouxer um vídeo de referência em linguagem infográfica.
- Não ofereça quando o usuário quer pessoas de verdade na tela ou um mascote apresentador. Nesses casos a trilha é a realista ou a 3D por código.
- Não misture este estilo com as outras trilhas no mesmo vídeo.

## Lições do estudo de 06/11/2026 aplicáveis a este estilo

Nada aqui muda os fatos do caso acima. São lições novas da pesquisa de expansão, aplicadas ao estilo 2D.

- Estrutura de história: o quiz verdade ou mentira já tem catalisador natural, que é a afirmação chocante, e ponto médio natural, que é o item 5 de 10. Aplique os 15 beats do Save the Cat de Snyder 2005 como checklist: se o meio do vídeo não tem virada, o item 5 precisa ser o mais chocante da lista, não um item qualquer.
- Incidente incitante e clímax: a lição de McKee 1997 vale aqui. O hook precisa de um incidente incitante claro nos primeiros segundos, e o último item precisa mudar o que o espectador acreditava, não só fechar a lista.
- Imagem que carrega o sentido: a lição de Glebas 2008 vale aqui. Cada cena tem 1 diagrama e 1 ideia, e o diagrama precisa contar sozinho, sem a narração. Se o diagrama não conta nada sem som, redesenhe o diagrama.
- Modelos de ambição: Kurzgesagt, 25,6 a 25,8 milhões de inscritos, é o teto de ambição do infográfico 2D, com pergunta gigante, paleta própria e narração calma. LEMMiNO, 5,93 milhões de inscritos, é o modelo de documentário longo com infográficos próprios e pesquisa profunda. Copie a ambição e a identidade visual, não o custo de estúdio.
- Título que compartilha: a lição de Berger 2013, STEPPS, vale para o título do vídeo. O título "10 COISAS que a NASA não quer que você saiba" tem moeda social, porque quem compartilha parece saber um segredo, e gatilho, porque NASA é tema que volta à conversa.
