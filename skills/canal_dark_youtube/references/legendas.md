# Legendas: o texto automático do áudio na tela

## O que é a legenda automática

A legenda automática é o texto da narração aparecendo na tela, sincronizado com o áudio, queimado no vídeo. Quem assiste sem som acompanha a história pela legenda. Quem assiste com som lê junto e entende melhor. É o padrão da skill e é o que faz o vídeo funcionar no celular, no ônibus e no trabalho.

## A legenda por plataforma

- No TikTok, a legenda queimada é indispensável. O TikTok tem legenda automática própria, mas ela erra nomes próprios, marcas e números, e não dá para adicionar legenda depois de publicar. Queime a legenda no vídeo antes de publicar.
- No Short do YouTube, a legenda queimada vai no centro e embaixo da zona segura, nunca no fundo do quadro, onde a interface cobre.
- No vídeo longo do YouTube, a legenda pode ser um arquivo SRT, mas a queimada continua sendo o padrão da skill, porque funciona sem o espectador ligar nada.

## O estilo da legenda

Copie este estilo. Ele é o estilo karaokê palavra por palavra: a palavra que está sendo falada no momento fica em amarelo e o resto do texto fica em branco, tudo em negrito com contorno preto, embaixo da tela.

- Fonte em negrito, como Montserrat Bold ou Arial Black.
- Texto branco com contorno preto de 2 pixels.
- A palavra ativa, a que está sendo falada no momento, fica em amarelo #FFFF00.
- O resto das palavras da frase fica em branco.
- Posição embaixo, no centro da tela, a cerca de 60 a 70 por cento da altura do vídeo vertical, fora da base coberta pela interface. No vídeo longo horizontal, use margem de 5 por cento da altura. Nunca coloque a legenda na base coberta de cerca de 420 px do vertical 1080x1920.
- Tamanho de 5 a 7 por cento da altura do vídeo. No Short vertical, a legenda fica maior. No vídeo longo horizontal, fica menor.
- No máximo 2 linhas por vez e no máximo 42 caracteres por linha.
- A legenda nunca cobre o assunto, o mecanismo ou o rosto do personagem. Se a cena tem o mecanismo embaixo, suba a legenda para o meio da tela naquela cena.
- A regra antiga de pintar a palavra-chave em laranja não vale mais. O amarelo agora marca a palavra falada no momento, e o branco marca o resto da frase.

## O tempo da legenda

- A legenda aparece palavra por palavra, no ritmo da fala. Cada palavra acende em amarelo no segundo exato em que é falada.
- Uma legenda por frase da narração. Nunca deixe a mesma legenda na tela durante o silêncio.
- Gere os tempos por palavra com o faster-whisper, com word_timestamps ligado, ou divida a narração por frase e marque o tempo de cada palavra.
- Confira a sincronia assistindo com som: se a palavra amarela aparece 1 segundo depois da palavra falada, o vídeo parece dublado errado.
- Não deixe buraco de legenda maior que 1 segundo, exceto pausa deliberada para suspense.

## Tempo de leitura

- Um espectador de primeira viagem precisa de cerca de 2 segundos para ler uma linha curta de texto. Fonte: pexo.ai, atualizado em 06/08/2026, pesquisa de 06/11/2026.
- A regra vale para o texto na tela, não para a legenda karaokê, que segue palavra por palavra no ritmo da fala. Um texto na tela como "220 METROS" precisa ficar pelo menos 2 segundos visível.
- Se o texto na tela some antes de 2 segundos, o espectador não lê. Se fica mais de 4 segundos parado, vira imagem parada. O certo é 2 a 4 segundos por texto na tela.
- No TikTok, mais de 30 por cento dos usuários assistem com o som desligado, segundo o TikTok for Business, atualizado em junho de 2025. A legenda queimada é indispensável porque é ela que carrega a história sem som.
- Confira o vídeo sem som e leia cada texto na tela em voz alta. Se você não consegue terminar de ler antes do texto sumir, o texto está rápido demais.

## Legenda não é texto na tela

Não confunda os dois. Cada um tem uma função.

- Legenda automática: o texto da narração, palavra por palavra, embaixo da tela. Vem do áudio.
- Texto na tela: a palavra-chave do fato, como "220 METROS" ou "SEM LUZ". Vem do roteiro e é feito na edição.
- Um vídeo pode ter os dois ao mesmo tempo: a legenda embaixo com a frase e o texto na tela no meio com a palavra-chave. Nunca use a legenda no lugar do texto na tela.

## Como fazer a legenda

1. Gere a narração por capítulo, em MP3, com a voz do perfil do canal.
2. Rode o faster-whisper na narração com word_timestamps ligado e gere o arquivo ASS com o tempo de cada palavra.
3. Revise o ASS: corrija os nomes próprios e os números, porque o Whisper erra nome e número.
4. Monte o ASS no estilo karaokê: cada palavra ganha o tempo de início e de fim dela, e a palavra ativa usa a cor amarela enquanto as outras usam branco.
5. Queime a legenda no vídeo final com o filtro subtitles do ffmpeg, com o estilo da seção acima.
6. Assista ao vídeo final sem som e confira se dá para acompanhar a história só pela legenda.

## Comando ffmpeg da legenda

- Queimar a legenda karaokê no vídeo: `ffmpeg -i video-final.mp4 -vf subtitles=legenda.ass:force_style='FontName=Montserrat Bold,FontSize=28,PrimaryColour=&HFFFFFF,OutlineColour=&H000000,Outline=2,Bold=1,Alignment=2,MarginV=60' -c:a copy video-com-legenda.mp4`.
- A cor amarela da palavra ativa vem do arquivo ASS, com o código de cor por palavra. No formato ASS a cor é BGR: amarelo é &H00FFFF& e branco é &HFFFFFF&.
- Ajuste o FontSize para o formato: o exemplo com FontSize 28 vale para 1280x720. Escale o valor na proporção da altura do vídeo e confira a legibilidade no celular antes de aprovar. Nunca copie o 28 para o vertical 1080x1920 sem escalar.
- Confira o arquivo final sem som antes de entregar.

## Checklist da legenda antes de entregar

1. A legenda é o texto exato da narração, sem resumir e sem inventar palavra.
2. Cada legenda aparece no mesmo segundo da palavra falada.
3. Nenhuma legenda fica na tela durante o silêncio.
4. No máximo 2 linhas e 42 caracteres por linha.
5. A palavra falada no momento está em amarelo e o resto da frase está em branco.
6. A legenda não cobre o assunto, o mecanismo ou o rosto.
7. O vídeo faz sentido assistido sem som, só com a legenda e a imagem.
8. Os nomes próprios e os números do ASS foram revisados.

## Modelo drop, rail e embed

Fonte: captions-overlay, sintetizado com palavras próprias, em https://github.com/heygen-com/hyperframes

- Classifique cada frase falada em drop, rail ou embed antes de compor a legenda.
- Solte os fillers com drop. Palavras como um, uh, gaguejos e autocorreções não aparecem na tela.
- Use rail como padrão. O rail é a legenda verbatim em lower-third, na frente do filme, e carrega a maior parte do texto.
- Promova só o pico a embed. O embed é a palavra gigante composta atrás do sujeito, com matte, para o beat de headline do vídeo.
- Decida a classificação pela frase, não pela palavra solta. A maioria das frases é rail e só o pico vira embed.

## Embed é escasso

Fonte: captions-overlay, sintetizado com palavras próprias, em https://github.com/heygen-com/hyperframes

- Limite o embed a no máximo 1 por batida ou frase. Embutir cada palavra é o erro padrão.
- Separe os embeds por pelo menos 1 batida e nunca deixe dois adjacentes ou co-visíveis.
- Use em geral 1 embed só em clipe curto. Um Short de 60 s pede 1 embed, não 1 por frase.
- Desenhe entrada e saída próprias para cada embed. Embed sem entrada desenhada vira texto gigante solto na tela.

## Lei do overlay

Fonte: captions-overlay, sintetizado com palavras próprias, em https://github.com/heygen-com/hyperframes

- Componha a legenda como camada POR CIMA do filme, nunca como faixa reservada embaixo.
- Dispense a faixa inferior reservada e não empurre o conteúdo para cima para abrir espaço para a legenda.
- Centralize a composição no centro vertical verdadeiro, com y igual a H dividido por 2. Em 1080x1920, o centro verdadeiro é 960 px.
- Deixe o conteúdo correr até as bordas do quadro. Sujeito em full-bleed, rail e fundo podem ir até embaixo sem medo.
- Evite texto pequeno crítico, como URL ou linha legal, nos cerca de 80 px centrais inferiores, onde a linha de legenda fica. Imagem grande e cards sob a legenda são aceitáveis.

## Destaque inline no rail

Fonte: captions-overlay, sintetizado com palavras próprias, em https://github.com/heygen-com/hyperframes

- Destaque a palavra de impacto com cor de acento e pop da palavra ativa, sem sair do rail.
- Mantenha o destaque no rail quando a palavra pede ênfase e não é pico de headline. O destaque inline resolve sem gastar um embed.
- Use o destaque inline como equivalente do karaokê da skill, com a palavra falada em amarelo #FFFF00 e o resto da frase em branco.
- Limite o destaque a 1 palavra por frase. Toda palavra destacada é nenhuma palavra destacada.

## Limite as palavras de ênfase

Fonte: claude-motion-studio, sintetizado com palavras próprias, em https://github.com/megomaged/claude-motion-studio

- Use no máximo 3 palavras de ênfase por vídeo. Ênfase em tudo é ênfase em nada.
- Mova 1 palavra cinética por vez. Duas palavras se movendo juntas disputam o olhar.
- Faça o corpo do texto com 40 px ou mais num quadro de 1080 de largura. Texto menor some no celular.
- Trate o quadro congelado no meio do vídeo como defeito e o quadro preto como inaceitável. Algo se move em todos os quadros até o hold final intencional.

## Hierarquia tipográfica

Fonte: kinetic-reel, sintetizado com palavras próprias, em https://github.com/tuzhechen2005/opus-video-skills

- Use Anton para headlines, com tipo condensado e pesado para o título na tela.
- Use Archivo Black para slams, com grotesk largo para a palavra de impacto.
- Use serifada itálica para a frase de voz, com uma só linha de voz por vídeo.
- Use JetBrains Mono para micro-texto, com rótulos, HUD e contadores.
- Mantenha uma só família de destaque por vídeo. Misturar Anton e Archivo Black no mesmo vídeo quebra a hierarquia.

## Zonas seguras 9:16

Fonte: motion-video-director, sintetizado com palavras próprias, em https://github.com/mattypark/Motion-graphics-skill

- Mantenha texto e rostos fora do topo de cerca de 220 px e da base de cerca de 420 px em 1080x1920, onde a interface do TikTok e do Reels cobre o quadro.
- Posicione as legendas a cerca de 60 a 70% da altura, fora da base coberta pela interface.
- Respeite a margem direita de cerca de 140 px, também coberta pela interface das plataformas.
- Confira as zonas seguras no frame final, com a interface da plataforma em mente, antes de entregar.
- Reponha o texto na cena quando ele cai na zona coberta. Texto coberto é texto perdido.

## Legendas como camada superior e por último

Fonte: raw-to-reel, sintetizado com palavras próprias, em https://github.com/jsath/claude-skills

- Rode as legendas depois do build visual, porque os layouts mudam a posição da legenda.
- Temporize as legendas a partir da transcrição do áudio já cortado, nunca do áudio original.
- Trate a legenda como camada superior, acima de todos os visuais, e queime por último na montagem.
- Refaça os tempos da legenda quando o áudio for recortado. Tempo de áudio antigo em vídeo novo é legenda dessincronizada.
