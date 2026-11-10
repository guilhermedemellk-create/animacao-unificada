# Montagem: do clipe solto ao vídeo final

## A ordem da montagem

Monte o vídeo nesta ordem e não pule etapas. Cada etapa tem um arquivo de saída que a próxima etapa usa.

- Junte os clipes na ordem do storyboard, com o nome de cada clipe na ordem da cena.
- Junte a narração por capítulo, na ordem do roteiro, com os blocos de áudio na ordem das cenas.
- Coloque os efeitos sonoros no mesmo segundo da ação na tela.
- Coloque a música por baixo de tudo, baixa sob a narração.
- Queime a legenda karaokê no vídeo com o arquivo ASS da narração, seguindo [legendas](legendas.md).
- Exporte o vídeo final e assista 2 vezes antes de entregar, uma com som e uma sem som.

## A regra de sincronia: a imagem e a narração andam juntas

Esta é a regra mais importante da montagem. O vídeo e a narração têm que andar juntos, cena por cena, do começo ao fim. Se a imagem mostra uma coisa e a narração fala outra, o espectador percebe e o vídeo parece dublado errado.

- Nunca use uma escala uniforme no vídeo inteiro para casar a duração total. A escala uniforme é proibida nesta skill.
- O que aconteceu no vídeo 1 do O Laboratório Curioso: a primeira montagem usou uma escala uniforme de 0,9737, que é 699 segundos de clipes divididos por 680,58 segundos de narração. A sincronia derivou cena por cena. No meio do vídeo o áudio ficou até 6 segundos atrás da imagem. No fim a narração ficou até 14 segundos na frente da imagem. O usuário percebeu e pediu para arrumar.
- O problema da escala uniforme é que a narração real não segue o ritmo estimado do storyboard em cada cena. Uma cena pode ter a fala mais rápida que o estimado e a próxima mais lenta. Uma só escala para o vídeo inteiro não corrige nenhuma das duas.
- A narração nunca é regravada nem editada para caber no vídeo. É o vídeo que segue a narração.
- A duração de cada cena na montagem é a duração real da fala daquela cena. Nunca a duração estimada do storyboard.

## Procedimento de sincronia passo a passo

Siga estes passos em todo vídeo, sem pular nenhum.

1. Gere a narração completa e guarde o arquivo de áudio. Ele não muda mais.
2. Transcreva a narração real com o faster-whisper e gere o arquivo `.ass` com o tempo de cada segmento. É a transcrição real que dá os tempos verdadeiros, não o storyboard.
3. Meça o início real de cada cena: encontre no `.ass` o segmento onde começa a fala da cena e anote o tempo em segundos. A duração real da cena é o início da próxima cena menos o início desta. A última cena vai até o fim da narração.
4. Cenas sem narração, como flashes visuais, ganham a duração do intervalo sem fala entre os segmentos vizinhos no `.ass`.
5. Ajuste cada clipe para a duração real da fala dele. Se o clipe for mais longo que a fala, corte o final. Se o clipe for mais curto, desacelere com `setpts` no máximo em 1,3 vezes, ou congele o último quadro com `tpad` para completar. Nunca estique um clipe além de 1,3 vezes, porque o movimento fica arrastado.
6. No trilho 2D por código, ajuste os movimentos dentro da cena para a nova duração: use o fator de escala de tempo da cena para manter a posição relativa de cada evento, como a contagem do número e a queda do carimbo.
7. Concatene os clipes ajustados, junte a narração intocada e queime a legenda com o mesmo arquivo `.ass`. Os tempos da legenda continuam válidos, porque a legenda é timed ao áudio e o vídeo agora segue o áudio.
8. Verifique a sincronia antes de entregar: extraia o frame no início de pelo menos 6 cenas espalhadas pelo vídeo, do começo, do meio e do fim, e confira se o visual e a legenda batem com a fala daquele segundo. Se alguma cena estiver desalinhada, volte ao passo 5 naquela cena. No vídeo 1 do O Laboratório Curioso, a verificação em 6 inícios de cena deu desvio zero.
9. Só entregue o vídeo depois que a verificação passar. Nunca entregue confiando só na duração total.

## Nomes de arquivo

Use nomes que mostram a ordem e o conteúdo. Nunca deixe clipe com nome genérico.

- Clipes: `capitulo-01-cena-01.mp4`, `capitulo-01-cena-02.mp4`, e assim por diante.
- Narração: `narracao-capitulo-01.mp3`, um arquivo por capítulo.
- Lista de montagem: `lista-clipes.txt`, com um clipe por linha na ordem do vídeo.
- Transcrição da narração: `transcricao.json` e `video-legendas.ass`, com o tempo real de cada segmento.
- Vídeo final: `canal-video-01-titulo-curto.mp4`.
- Guarde os clipes crus e a narração crua. Se um trecho precisar de refação, você remonta só aquele trecho.

## Juntar os clipes com ffmpeg

- Liste os clipes em `lista-clipes.txt`, com uma linha por clipe no formato `file 'capitulo-01-cena-01.mp4'`.
- Junte com `ffmpeg -f concat -safe 0 -i lista-clipes.txt -c copy video-junto.mp4`.
- Todos os clipes precisam ter a mesma resolução, o mesmo fps e o mesmo codec. Se um clipe for diferente, converta ele antes de juntar.
- Confira o vídeo junto antes de colocar o áudio. Se um clipe entrar fora de ordem, o erro aparece aqui.

## Juntar vídeo, narração, efeitos e música

- Junte o vídeo sem som com a narração com `ffmpeg -i video-junto.mp4 -i narracao.mp3 -c:v copy -c:a aac -shortest video-com-narracao.mp4`.
- Some os efeitos e a música por cima com o filtro `amix`, com a música em volume baixo.
- Deixe a narração sempre na frente. Efeito e música nunca cobrem a voz.
- Sincronize o gesto com o efeito no mesmo segundo. Se o efeito entra 1 segundo depois da ação, o vídeo parece dublado errado.

## Ajustar a duração de um clipe

- Cortar o final do clipe: `ffmpeg -i cena.mp4 -t DURACAO -c copy cena-cortada.mp4`, com a duração real da fala em segundos.
- Desacelerar o clipe até 1,3 vezes: `ffmpeg -i cena.mp4 -vf setpts=PTS*FATOR -an cena-lenta.mp4`, com o fator igual à duração real dividida pela duração do clipe.
- Congelar o último quadro para completar: use o filtro `tpad` com `stop_mode=clone` e a duração que falta.
- Nunca use `setpts` no vídeo inteiro. O ajuste é por cena, uma por vez, com a duração real da fala de cada uma.

## Volume final

- Alvo de volume do YouTube: menos 14 LUFS.
- Confira o volume com `ffmpeg -i video-final.mp4 -af loudnorm=I=-14:TP=-1:LRA=11 -f null -`.
- Se o volume estiver acima do alvo, abaixe o ganho e exporte de novo. Não suba o volume de um áudio baixo com compressão forte, porque a voz fica estourada.
- O volume da música fica pelo menos 20 por cento abaixo do volume da narração.

## Formato de exportação

- Vídeo longo do YouTube: 1920x1080, 60 fps, com 40 fps como mínimo aceitável, H.264, AAC.
- Short do YouTube: 1080x1920, 60 fps, com 40 fps como mínimo aceitável, H.264, AAC.
- Vídeo do TikTok: 1080x1920, 60 fps, com 40 fps como mínimo aceitável, H.264, AAC.
- Use o mesmo fps do começo ao fim. Misturar fps diferentes no mesmo vídeo trava a montagem. Nunca entregue abaixo de 40 fps.
- Exporte em qualidade alta e deixe a plataforma comprimir. Nunca exporte já comprimido demais.

## Checklist da montagem antes de entregar

Confira estes itens no vídeo final. Se algum faltar, volte na etapa dele.

1. Ordem: os clipes seguem o storyboard, sem cena fora de ordem.
2. Narração: a voz é a mesma do começo ao fim e cada fato do roteiro aparece na tela.
3. Sincronia: cada cena começa no mesmo segundo da fala dela, medida da transcrição real, sem escala uniforme.
4. Verificação de sincronia: pelo menos 6 inícios de cena conferidos por frame, do começo, do meio e do fim, com visual e legenda batendo com a fala.
5. Gestos e efeitos: cada gesto tem o efeito dele no mesmo segundo.
6. Volume: o vídeo final está no alvo de menos 14 LUFS.
7. Continuidade: mesmo personagem, mesma roupa, mesmo cenário e mesma voz.
8. Texto na tela: cada texto foi feito na edição, nunca gerado pela IA.
9. Teste do mudo: 3 ou mais movimentos visíveis em 10 segundos sem som.
10. Teste do som: assista com som e confira que nada está fora de sincronia.
11. Legenda: o texto da legenda é o texto exato da narração, no estilo karaokê com a palavra falada em amarelo e o resto em branco, sincronizado com o áudio, legível no celular e sem cobrir o assunto.
12. Beats: o catalisador, o ponto médio e o tudo perdido marcados no storyboard aparecem nas cenas certas, com o corte mais forte neles.
13. Pré-publicação: rode $checklist antes de subir o vídeo, com título, descrição, tags, thumbnail, visibilidade e tela final conferidos.
14. Backup: rode $backup depois de entregar o vídeo final, com o vídeo, a narração, o roteiro e o storyboard salvos.

## Portões de edição no vídeo final

Fonte: edit-style, sintetizado com palavras próprias, em https://github.com/jsath/claude-skills

- Rode os portões abaixo no vídeo final renderizado, nunca no rascunho. Portão medido no rascunho não vale para o arquivo entregue.
- Meça o ar morto com a retranscrição do vídeo final. Nenhum intervalo sem palavra passa de 0,25 segundo numa junção e nenhum passa de 0,35 segundo em qualquer ponto do vídeo.
- Meça o envelope da junção com o nível de áudio. Nenhum trecho quieto abaixo de menos 36 dBFS passa de 0,25 segundo dentro de 0,5 segundo de uma junção e nenhum passa de 0,35 segundo dentro da fala. O envelope pega buraco de som ambiente que o Whisper esconde.
- Meça a sincronia da legenda no render final. Retranscreva o vídeo final e compare com as legendas por capítulo. A mediana fica em até 0,12 segundo e o p95 fica em até 0,25 segundo. Legenda sincronizada no rascunho e dessincronizada no final reprova.
- Confira o comprimento de áudio e vídeo. A diferença fica dentro de 1 quadro.
- Confira a codificação. O vídeo sai em yuv420p, faixa de TV, BT.709 e 8 Mbps ou mais.
- Confira se a primeira palavra sobreviveu. Retranscreva os primeiros 2 segundos e confirme que a primeira palavra do roteiro está lá.
- Abra a contact sheet e olhe cada quadro. Confira o recorte 4 para 5, de y 285 a 1635 em 1080x1920, sem legenda sobre a boca ou o assunto, sem logo errado e sem nada privado na tela.
- Confira as afirmações. Cada número na tela tem uma fonte nomeada e conferida no dia. Fala falsa é cortada e listada, não mantida.
- Troque o layout visual a cada 2 a 5 segundos. Alterne assunto em tela cheia, gráfico em tela cheia e tela dividida com assunto e gráfico. Nunca abra com cartão de título, gravação de tela ou logo sozinha. Abra no assunto desde o quadro 1 e feche o CTA no gráfico.
- Acerte cada junção com precisão. O início e o fim de cada clipe caem dentro de 0,08 segundo da primeira e da última palavra. Olhe os primeiros e os últimos 0,5 segundo de cada clipe. Junção esconde ar morto, mão buscando a câmera e corpo se acomodando.
- Mantenha o último take da frase repetida. Corte os takes anteriores e nunca corte no meio de uma palavra.
- Aperte os silêncios com o limiar de menos 50 dB, nunca com menos 38 dB. O limiar fraco corta fim de palavra.
- Use J-cut de cerca de 1 segundo quando o som da próxima cena entra antes do corte. O áudio adiantado puxa o espectador para a próxima cena. Fonte: claymation-ad, sintetizado com palavras próprias, em https://github.com/brycefinnerty/ray-3.2-ad-generator
- Faça o probe antes de montar. Rode ffprobe em cada arquivo e nunca assuma número de duração, resolução, fps ou codec. Correção de drift com confiança abaixo de 0,3 é suspeita e pede checagem manual. Fonte: ffmpeg-skill, sintetizado com palavras próprias, em https://github.com/kajisho5/ffmpeg-skill
- Remuxe sem re-render quando só o áudio mudar. Junte o vídeo pronto com o áudio novo com `ffmpeg -i video.mp4 -i audio-novo.mp3 -map 0:v -map 1:a -c:v copy video-remux.mp4`. Troca de áudio não pede render novo. Fonte: kinetic-reel, sintetizado com palavras próprias, em https://github.com/tuzhechen2005/opus-video-skills
- Guarde o resultado de cada portão junto com o vídeo final. Portão sem número guardado não conta. Rode $varredura para a varredura de quadros e $portoes para todos os portões de uma vez.

## Monte para os beats da história

- A montagem não é só juntar clipes em ordem. Os beats da história pedem cortes diferentes. O catalisador pede corte seco e rápido. O ponto médio pede virada de ritmo, com música subindo ou caindo. O tudo perdido pede pausa e silêncio antes da virada final.
- O melhor momento do vídeo fica aos dois terços, não no final. Na montagem, confira que a cena do clímax está mesmo aos dois terços da duração, e não escorregou para o fim.
- O teaser do próximo item, a cada dois ou três minutos, é um corte de montagem: feche a cena com a pergunta do próximo item na tela e na narração.
- No vídeo curto, o reset de retenção aos 25 a 30 segundos é um corte de montagem: mude o ângulo, o lugar ou o assunto naquela cena, com uma pergunta nova na narração.
- A estrutura escolhida no roteiro está no SKILL.md, na seção "Escreve o roteiro". A montagem segue a estrutura, não o contrário.

## Checklist do upload

Confira esta lista antes de chamar $publicar.

- Título pronto, seguindo [título e thumbnail](titulo-thumbnail.md).
- Descrição com resumo narrativo, pergunta nos comentários, fontes com links e cinco a dez hashtags.
- Tags com dez a quinze variações da busca principal.
- Thumbnail pronta, com no máximo quatro palavras.
- Short de menos de quarenta segundos com o fato mais visual, apontando para o vídeo longo.
- Tela final apontando para a parte dois ou para o vídeo mais parecido do catálogo.

## Checklist do upload no YouTube Shorts

O Shorts é uma plataforma própria, não é adaptação do vídeo longo. Chame $publicar quando esta lista estiver completa.

- Vídeo vertical 1080x1920, na duração escolhida na entrevista.
- Título curto, com número, tema e gatilho.
- Descrição com fontes e hashtags, incluindo a marca do canal.
- Capa escolhida por frame, com o assunto e o texto no centro da zona segura.
- Legenda karaokê queimada no vídeo, com a palavra falada em amarelo e o resto em branco.
- Gancho de 1 a 3 segundos no começo do vídeo.
- Sem tela final. Ela não existe no Shorts.

## Checklist do upload no TikTok

Chame $publicar quando esta lista estiver completa.

- Vídeo vertical 1080x1920, na duração escolhida na entrevista.
- Descrição curta, com o gancho na primeira linha e 2 a 3 hashtags.
- Capa escolhida por frame, com o assunto e o texto no centro da zona segura.
- Legenda karaokê queimada no vídeo, com a palavra falada em amarelo e o resto em branco, porque a legenda automática do TikTok erra nomes próprios e números.
- Sem thumbnail e sem tela final. Elas não existem no TikTok.

## Workflow de montagem

Fonte: ffmpeg-skill, sintetizado com palavras próprias, em https://github.com/kajisho5/ffmpeg-skill

- Faça probe primeiro e nunca assuma números. Planeje a montagem a partir dos números reais do probe.
- Prefira lossless sem re-encode quando corte ou remux bastam. Re-encode sem necessidade perde qualidade e tempo.
- Planeje com dry-run antes de rodar. Confie nos números do plano, não na linha de resumo.
- Encadeie na ordem cor, corte, junção, silêncio, fit, legenda e overlay, sync, áudio, loudness e export. A ordem evita refazer etapa por causa de etapa fora de lugar.
- Cheque por plataforma antes de entregar, com os requisitos de TikTok, Shorts ou vídeo longo conforme o destino.
- Verifique a saída com probe e olhe os pixels depois de qualquer mudança de imagem. Sem olhar os pixels, a verificação não está completa.
- Guarde os originais e nunca sobrescreva a fonte. Sobrescrever só vale para arquivos do próprio trabalho ou para arquivos que o usuário pediu para substituir.

## Anti-erros

Fonte: ffmpeg-skill, sintetizado com palavras próprias, em https://github.com/kajisho5/ffmpeg-skill

- Preserve o original sem sobrescrever. O original guardado é o que permite remontar o trecho sem regravar.
- Converta VFR de celular para CFR no re-encode. Vídeo de celular em frame rate variável dessincroniza na montagem.
- Lembre que corte com -c copy pode começar no frame errado. Corte sem re-encode só começa em keyframe.
- Lembre que normalizar pode ainda clipar. Confira o true peak depois de normalizar, não só o LUFS integrado.
- Coloque legendas depois do crop. Legendas antes do crop caem fora do quadro.
- Respeite as zonas seguras de TikTok e Reels, com a base e a direita cobertas pela interface.
- Ajuste formato, duração, aspecto, fps ou loudness só quando o pedido implica a mudança. Não corrija o que não foi pedido.

## Manifesto de tempos por segmento

Fonte: explainer-video, sintetizado com palavras próprias, em https://github.com/bobobo2026/explainer-video

- Gere script.json ou timeline.json palavra por palavra com faster-whisper, com duração, fps e frases com início, fim e tempos de cada palavra.
- Ancore visuais e SFX em palavra e não em tempo absoluto. Cardar a imagem na palavra dentro da frase faz a montagem realinhar sozinha se a narração for regravada.
- Separe o que é dito do que aparece na tela. O campo de fala guarda a narração e o campo de exibição guarda o texto na tela.
- Guarde o manifesto como fonte única de verdade do vídeo. Narração, cena e legenda derivam dele e não de três arquivos separados.
- Regenere o manifesto quando a narração mudar. Manifesto velho com narração nova é deriva garantida.

## Pipeline áudio-primeiro

Fonte: story-studio, sintetizado com palavras próprias, licença CC BY-NC-SA 4.0, em https://github.com/konlu/story-studio, e motion-video-director, sintetizado com palavras próprias, em https://github.com/mattypark/Motion-graphics-skill

- Gere a narração real primeiro, com a voz fixa do perfil do canal, em uma só passada suave.
- Transcreva a narração real com timestamps e só então monte o storyboard. Cada imagem casa com a frase que está sendo dita.
- Coloque imagem na primeira frase já no frame 0. A primeira frase sem imagem é tela vazia no gancho.
- Espere o MP3 final da narração antes de construir ou renderizar cenas. O vídeo inteiro é temporizado pela narração real.
- Evite dividir o roteiro em cenas de forma mecânica antes de ouvir a narração. A divisão mecânica quebra a frase no meio e o visual não casa com a fala.
- Trave os tempos reais em beats.json a partir do áudio, com os tempos da transcrição comparados com o roteiro aprovado.

## Verificação semântica imagem contra narração

Fonte: story-studio, sintetizado com palavras próprias, licença CC BY-NC-SA 4.0, em https://github.com/konlu/story-studio

- Confira cada imagem contra a pessoa ou evento da narração naquele trecho, antes de exportar.
- Bloqueie a exportação quando alguma imagem não corresponder à narração do trecho. Sem correspondência, o vídeo não sai como verificado.
- Faça a checagem por trecho, com imagem, tempo de início, tempo de fim e frase da narração lado a lado.
- Corrija a imagem errada ou o tempo errado antes de exportar. Exportar com imagem errada é entregar erro conhecido.

## Remux sem re-render quando só o áudio muda

Fonte: ffmpeg-skill, sintetizado com palavras próprias, em https://github.com/kajisho5/ffmpeg-skill, e kinetic-reel, sintetizado com palavras próprias, em https://github.com/tuzhechen2005/opus-video-skills

- Troque só o áudio com remux e -c:v copy quando só o áudio muda. O vídeo passa intacto e só a faixa de áudio é substituída.
- Use o remux para trocar narração, música ou SFX sem re-render do vídeo inteiro. Re-render para trocar áudio é tempo jogado fora.
- Confira o vídeo remontado com probe e com os tempos da legenda, porque o áudio novo pode ter duração diferente do antigo.

## QA com gates medidos

Fonte: cartoon-3d-short, sintetizado com palavras próprias, em https://github.com/mromidev/claude-animated-shorts, e raw-to-reel, sintetizado com palavras próprias, em https://github.com/jsath/claude-skills

- Varra todos os frames atrás de quadros pretos, brancos, congelados e pop, com gate medido e não com impressão visual.
- Meça o loudness no gate, com o master em -14 LUFS, e registre o número medido.
- Revise por contact sheet por cena, com um still por cena, e por strip de cada transição.
- Acompanhe a saída final com o arquivo de legendas, com H.264 e AAC, e com os números do gate anotados.
- Trave as constantes de tempo da imagem antes de fazer o som. Qualquer mudança de timing depois obriga refazer o áudio.
