# Referência: dissecar um vídeo quadro a quadro antes de produzir

Use este guia como base do comando $referencia. O método abaixo vem do reverse-any-video, da HeyGen HyperFrames, em https://github.com/heygen-com/hyperframes, sintetizado com palavras próprias. A ferramenta Reverse é paga, recurso do HyperFrames Pro. Importe o método, não a ferramenta. Não prometa a ferramenta como gratuita e não dependa dela para produzir. O trabalho aqui é feito com probe, medição de cortes, leitura de frames e diff, com ffmpeg e com os próprios olhos.

## Direitos de uso e limite ético

Fonte: reverse-any-video, em https://github.com/heygen-com/hyperframes, e style-sampling, em https://github.com/heygen-com/hyperframes

- Dissequem só vídeos que se tem direito de usar. Sem direito de uso, não baixe, não reconstrua e não reaproveite o vídeo.
- Amostre a gramática do estilo, com estrutura, ritmo, visual, gráficos e som. Nunca copie rosto, voz, footage, logo ou nome do criador original.
- Reconstrua o vídeo como ele é para estudar. Remixem só quando o pedido for remixar.
- Anote no arquivo de notas de onde veio a referência e o que foi amostrado dela, para o limite ficar registrado.

## O original decide o quadro

Fonte: reverse-any-video, sintetizado com palavras próprias, em https://github.com/heygen-com/hyperframes

- Faça probe do original antes de definir qualquer número. O probe define o tamanho exato da composição, o fps e a duração.
- Use o fps real do original, com fração quando for NTSC, como 30000/1001. Não arredonde o fps na medição.
- Calcule a duração como frames dividido por fps, não como a duração do áudio. A duração do áudio não define o quadro.
- Anote tamanho, fps fracionário e duração em frames no arquivo de notas antes de medir os cortes.
- Adapte a gramática medida para o Short vertical 1080x1920 a 60 fps na hora de produzir. Copie o ritmo e a estrutura, não os números crus do original.

## Medir cortes, incluindo jump cuts e punch-ins

Fonte: reverse-any-video, sintetizado com palavras próprias, em https://github.com/heygen-com/hyperframes

- Meça todos os cortes do original, incluindo jump cuts e punch-ins dentro de um mesmo take, que o detector de cena do ffmpeg não vê.
- Liste cada corte com o frame exato. Cada shot começa no tempo listado, sem arredondamento para cima.
- Escreva os tempos como frame dividido por fps e arredondado para baixo. Um tempo arredondado para cima cai um frame atrasado.
- Monte a lista de shots com início, fim e duração em frames. A lista de shots é o esqueleto do ritmo do original.

## Ler frames consecutivos onde algo muda

Fonte: reverse-any-video, sintetizado com palavras próprias, em https://github.com/heygen-com/hyperframes

- Leia frames consecutivos em cada ponto de mudança, com alguns frames de cada lado. Planilhas com 1 s ou 0,25 s de intervalo perdem esses detalhes.
- Observe entradas, saídas, transições, dissolves e flashes de 1 frame. Um flash de 1 frame some em qualquer amostragem espaçada.
- Note como cada elemento entra e sai, com direção, velocidade e blur. A entrada diz tanto sobre o estilo quanto o elemento parado.
- Leia o frame de troca da legenda a partir dos pixels da faixa de legenda, não da transcrição. A troca na tela é o tempo real.
- Dimensione o texto pela tinta dele, com o tamanho medido no frame, não pelo tamanho declarado em nenhum arquivo.

## Reconstruir por camadas

Fonte: reverse-any-video, sintetizado com palavras próprias, em https://github.com/heygen-com/hyperframes

- Reconstrua por camadas separadas, com texto, legendas, cartões, gráficos e mapas cada um na sua camada.
- Separe cada componente visual, como texto, legenda, adesivo, cartão, interface, gráfico e mapa, para medir cada um sozinho.
- Corte cada sub-asset na sua própria caixa, como foto, clipe, capa, logo ou ícone. Nunca use o quadro inteiro do original como asset.
- Refaça cada camada do zero no formato da skill, com renderFrame, imagem gerada ou código, conforme a trilha. A camada reconstruída é estudo, não cópia do arquivo original.
- Mantenha o som original como referência de ritmo durante a reconstrução, sem extrair ou reencodar a faixa para o vídeo final.

## Verificação por diff contra o original

Fonte: reverse-any-video, sintetizado com palavras próprias, em https://github.com/heygen-com/hyperframes

- Compare a reconstrução com o original por diff, lado a lado, nos piores momentos.
- Liste os cortes perdidos e os cortes extras, a duração, o offset do som e os trechos com conteúdo faltando.
- Corrija o que o diff aponta e que dá para ver, como corte faltando, elemento faltando, tempo errado, tamanho errado, peso errado ou cor errada.
- Rode o diff de novo depois da correção e pare na segunda rodada. Diff infinito vira polimento sem fim.
- Registre os números do último diff no arquivo de notas, mesmo quando ainda há diferença. Número registrado é prova, número escondido é chute.

## O que a dissecação entrega para cada trilha

Anote no arquivo de notas o que cada trilha tira do original. A dissecação sem entrega por trilha vira estudo sem uso na produção.

- Entregue para as trilhas realista e Pixar por IA os tokens de estilo do original, com paleta, luz, proporção do personagem e 2 traços marcantes, e a lista de movimentos de câmera com duração de cada um. Copie os tokens para o bloco de estilo travado e para a ficha do personagem, sem copiar rosto, voz, footage, logo ou nome do criador.
- Entregue para a trilha realista e a Pixar por IA o mapa de beats do original, com a duração de cada beat, a ação de cada beat e a palavra que ancora cada corte. Use o mapa para planejar os beats de 8 segundos na Pixar e os 3 beats por clipe de 10 segundos na realista.
- Entregue para a trilha 3D por código a lista de cortes de câmera com o tempo de cada corte, o plano de cada shot e o gesto que cai em cada corte. Use a lista para escrever os keyframes com o timing medido, em vez de adivinhar o ritmo.
- Entregue para a trilha 2D por código os easings, as durações e os staggers medidos do original, com o tempo de cada entrada, de cada morph e de cada contador. Porte os números para as receitas GSAP de [quadros de movimento](quadros-movimento.md) e para as receitas de cena de [animação](animacao.md).
- Entregue para a trilha 2D por código a gramática de tipografia do original, com tamanho, peso, cor e tempo de leitura de cada palavra gigante. Use a gramática para o estilo tipografia clara e meça a largura real com o helper medeTexto antes de aprovar.
- Entregue para a imagem estática o que não copiar. Anote os trechos parados do original e a queda de ritmo deles, para o rascunho não virar final sem o aviso de retenção.

## Entrega com um arquivo de notas

Fonte: reverse-any-video, sintetizado com palavras próprias, em https://github.com/heygen-com/hyperframes

- Escreva um arquivo de notas ao fim da dissecação, com o que foi reconstruído, o que é aproximado e os números do último diff.
- Liste o que foi reconstruído camada por camada, com os tempos de corte e os tempos de troca de legenda.
- Liste o que é aproximado, como fonte substituída, cor aproximada ou movimento estimado, sem esconder a aproximação.
- Liste os números do último diff, com cortes perdidos e extras, duração, offset do som e piores momentos.
- Guarde o arquivo de notas junto do roteiro e do storyboard. A próxima produção do mesmo estilo começa por ele, não por uma nova dissecação do zero.
