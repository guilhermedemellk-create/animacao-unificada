# Áudio completo — narração, efeitos e música

## A regra das 3 camadas

Todo vídeo tem 3 camadas de áudio. Nunca entregue um vídeo sem áudio, a não ser que o usuário tenha pedido um teste só visual e saiba disso.

1. Narração: conta a história e guia o espectador.
2. Efeitos sonoros: marcam cada ação e cada ideia na tela.
3. Música: dá o clima e costura as cenas.

## Narração

- Ritmo de 135 a 150 palavras por minuto, ou 2,3 a 2,6 palavras por segundo. Escreva frases curtas para o ouvido. O número antigo de 130 palavras por minuto estava abaixo do orçamento de palavras de [revisar roteiro](revisar-roteiro.md) e foi corrigido aqui.
- Ajuste a duração da narração à plataforma e à duração escolhida na entrevista: no TikTok e no Shorts, na duração escolhida, de 15 segundos a 3 minutos no TikTok e de 15 a 60 segundos no Shorts, e 10 a 12 minutos no vídeo longo do YouTube.
- Gere a narração em uma só passada suave por capítulo, sem pausas bruscas entre as frases, para corrigir um trecho sem regravar o vídeo inteiro. No formato curto, gere a narração inteira em uma só passada. O guia completo está em [gerador de voz](gerador-voz.md).
- A voz é fixa e está registrada no perfil do canal. Nunca troque a voz no meio da série.
- Declare voz sintética na descrição quando usar voz sintética.
- Leia o hook em voz alta para testar o ritmo antes de aprovar.
- Para planejar a narração, use [Generate Podcast](/opt/muse/skills/generate_podcast/SKILL.md) e [Spoken Audio](/opt/muse/skills/spoken-audio/SKILL.md).
- A narração do clipe entra no vídeo com ffmpeg, junto com o MP4, no passo de montagem.
- A narração nunca é regravada nem editada para caber no vídeo. É o vídeo que segue a narração, cena por cena, com a duração real de cada fala. A regra completa está em [montagem](montagem.md).

## Narração é voice-over, não fala para a câmera

- A narração é voice-over. O personagem gesticula, aponta e reage, com o rosto em reação, e não fala para a câmera. A sincronia labial real não é possível com as ferramentas disponíveis, e tentar imitar deixa a boca fora de sincronia com as palavras.
- O erro que criou esta regra: no Short 2, a narração dizia que o personagem abriu a geladeira e tocou atrás dela, mas o vídeo nunca mostrava ele tocando atrás. Várias ações narradas não apareciam acontecendo na tela. A lição é que cada ação narrada precisa estar visível acontecendo no mesmo segundo.
- Escreva a narração para o ouvido e a imagem para o olho, e case as duas no storyboard. Se a frase diz "ele toca", a cena mostra a mão tocando.
- A voz marca as viradas da história com mudança de ritmo. No catalisador, a voz acelera. No ponto médio, a voz muda de tom. No "tudo perdido", a voz baixa e pausa. No clímax, a voz volta com força. As estruturas de história estão no SKILL.md, na seção "Escreve o roteiro".
- Varie o ritmo dentro do capítulo. Narração em velocidade constante soa robótica, mesmo com a voz certa. A pausa de 1 segundo antes do fato mais chocante já está no checklist, use também uma pausa curta depois da revelação, para o espectador absorver.

## Camada de ambiente

- Além das 3 camadas, cada capítulo tem um som de ambiente contínuo por baixo de tudo: vento na caverna, água na lagoa, grilos na mata, silêncio abafado no túnel.
- O som de ambiente mantém a cena viva mesmo quando ninguém fala. Ele é o equivalente sonoro do movimento do fundo na imagem.
- Troque o som de ambiente junto com o capítulo. O mesmo vento em todos os capítulos vira ruído de fundo sem sentido.
- O som de ambiente fica mais baixo que a música e some nas pausas de suspense, quando o silêncio é o efeito.
- Escolha o som de ambiente pelo lugar da cena, não pela narração. A cena manda no som, como manda no efeito.

## Efeitos sonoros

- Um efeito por ideia ou ação. Água espirrando, passos, porta abrindo, trovão, coração batendo, vento, pássaro.
- O efeito entra no mesmo segundo da ação na tela. Efeito fora de sincronia confunde mais do que silêncio.
- Gere efeitos com o ElevenLabs ou use biblioteca licenciada. O conector Runway não está conectado, então não gere nada com Runway até conectar a conta. Verifique o saldo de créditos antes de gerar.
- Não use efeito de outro canal e não use música comercial como efeito.
- Em cada clipe de 10 segundos, pelo menos 1 efeito sonoro audível.

## Música

- Trilha instrumental licenciada ou original, da mesma família em toda a série.
- A música fica baixa sob a narração e cresce nas transições e no final.
- Evite música comercial sem licença para não receber reivindicação de direitos.
- Escolha a música antes de montar o vídeo e não troque de faixa no meio do capítulo.

## Mixagem

- Narração no topo, música baixa e efeitos como acento.
- Não deixe buraco de silêncio maior que 1 segundo, exceto pausa deliberada para suspense.
- Alvo de volume do YouTube: menos 14 LUFS. Confira com o filtro loudnorm do ffmpeg antes de entregar.
- Atenção: menos 14 LUFS não é um alvo oficial publicado pelo YouTube nem pelo TikTok. É um valor amplamente praticado. As plataformas reduzem o volume de uploads mais altos, mas nem sempre elevam os mais baixos. Um só master em menos 14 LUFS serve ao YouTube, ao TikTok e ao Instagram. Fontes: soundveo.com, atualizado há 29 dias, e audiopod.ai, atualizado há 135 dias, consultas em 06/11/2026.
- Faça a normalização em dois passes com o loudnorm do ffmpeg, porque um só passe estima e desvia do alvo.
- Assista ao vídeo final 2 vezes: uma com som e uma sem som. Com som, confira sincronia e volume. Sem som, confira se a imagem se sustenta sozinha.

## Mixagem fina

- Ducking da música: as fontes divergem nos números, então use o valor novo como ponto de partida e valide de ouvido. Música de 18 a 24 dB abaixo da voz enquanto o narrador fala, com 22 a 24 dB para conteúdo informativo e educacional, onde cada frase importa, e 16 a 20 dB para história e documentário. Ducking de 6 a 10 dB por sidechain, com ataque de cerca de 120 milissegundos e release de cerca de 400 milissegundos. Outra fonte usa música 6 LU abaixo da fala, subindo para 3 LU abaixo nas pausas. Uma fonte mais antiga usava música de 8 a 12 dB abaixo da voz, com ataque de 10 a 30 milissegundos e release de 200 a 400 milissegundos. Cheque em alto-falante de celular e em fone. Fontes: FalconVid, 2026, melliusai.com, 28/09/2026, e mediastrategylab.com, consultas em 06/11/2026.
- Narração como âncora: meça a voz sozinha antes de somar música e efeitos. A voz fica em torno de menos 16 LUFS integrado, com short-term entre menos 16 e menos 14 LUFS durante a fala, e true peak sempre abaixo de menos 1 dBTP. Fonte: FalconVid, 2026, consulta em 06/11/2026.
- Acessibilidade, W3C: música 20 dB abaixo da fala em primeiro plano. É o piso mínimo de separação entre voz e música.
- Hierarquia de efeitos: diálogo no topo, efeitos entre diálogo e música, música como base. Efeito de transição com 400 a 500 milissegundos, começando 10 a 20 milissegundos antes do visual. Valores de uma só fonte agregadora, não verificados em segunda fonte.
- EQ da voz como referência: high-pass em 80 Hz, corte perto de 500 Hz, boost de 2 a 5 kHz e corte de 6 a 8 kHz. Valores de uma só fonte agregadora, não verificados em segunda fonte. Teste de ouvido antes de fixar.
- Nunca use música com letra sob a narração. Duas vozes competindo confundem o ouvido e a narração perde.
- Confira a mixagem em 3 dispositivos antes de entregar: alto-falante de celular, fone de ouvido e, se houver, caixa de som. O público assiste no celular, e é no celular que a mixagem precisa estar certa.
- Deixe a música crescer nas transições e no final, e sumir nas pausas de suspense. Música alta no momento da revelação rouba o impacto da frase.
- Corte a música no fim da frase, nunca no meio dela. Um corte no meio da palavra quebra a passada suave da narração.

## Pipeline de áudio

1. Roteiro aprovado por capítulo.
2. Narração gerada por capítulo, em MP3.
3. Efeitos gerados por cena, com o nome da ação no arquivo.
4. Música escolhida e cortada para a duração do vídeo.
5. Montagem com ffmpeg: vídeo, narração, efeitos e música em um só MP4.
6. Checagem de volume com loudnorm e teste com e sem som.

## Voz do canal

- A voz é decidida na entrevista de abertura: escolha um dos 26 estilos em [vozes](vozes.md) e depois a origem, humana gravada, sintética fixa ou clonada com consentimento.
- Registre o nome e o ID da voz no perfil do canal.
- A voz do canal Por Dentro de Tudo não é a voz deste canal. Cada canal tem sua voz própria.

## Catálogo de efeitos por tipo de cena

- Água: espirro, bolhas, mergulho, onda, chuva.
- Porta e objeto: porta abrindo, chave girando, livro caindo, vidro quebrando.
- Corpo: passos, coração batendo, respiração, suspiro.
- Clima: trovão, vento, chuva, pássaro, grilo.
- Suspense: batida grave, risada baixa, som abafado, silêncio com respiração.
- Transição: whoosh, batida, sino, subida de tom.
- Escolha o efeito pelo que está na tela, não pelo que está na narração. O efeito ilustra a imagem.

## Como escolher a música

- A música combina com o clima do vídeo: mistério usa grave e lento, curiosidade usa leve e curioso, susto usa tenso e rápido.
- Uma só família de música por série. Trocar de estilo a cada vídeo quebra a identidade do canal.
- Prefira biblioteca licenciada com busca por clima e andamento. Anote a licença e o link da faixa na descrição do vídeo.
- Nunca use música comercial sem licença. Uma reivindicação de direitos tira a monetização do vídeo inteiro.
- Teste a música sob a narração antes de montar. Se a música compete com a voz, ela está alta demais ou errada.

## Comandos ffmpeg de áudio

- Juntar vídeo sem som com narração: `ffmpeg -i video.mp4 -i narracao.mp3 -c:v copy -c:a aac -shortest saida.mp4`.
- Misturar narração, efeitos e música com volumes: use o filtro amix com um volume por entrada, como narração em 1.0, efeitos em 0.8 e música em 0.25.
- Conferir o volume final no alvo do YouTube: `ffmpeg -i saida.mp4 -af loudnorm=I=-14:TP=-1:LRA=11 -f null -`.
- Cortar a música para a duração do vídeo: use `-t` com a duração em segundos.
- Sempre confira o arquivo final com o teste de volume antes de entregar.

## Checklist de narração por capítulo

- O hook foi lido em voz alta e o ritmo está bom.
- As frases são curtas e cabem em uma respiração.
- As palavras difíceis foram pronunciadas certo na primeira vez.
- A ênfase cai na palavra do fato chocante, não na palavra comum.
- Não há gagueira, repetição nem corte no meio da frase.
- O silêncio antes do fato mais chocante dura 1 segundo, para suspense.

## Hierarquia fixa e mix com números fechados

Fonte: sound-design, sintetizado com palavras próprias, em https://github.com/krusemediallc/video-editor-agent

- Normalize a narração primeiro, antes de ajustar trilha ou SFX. Use `ffmpeg -i vo.wav -af loudnorm=I=-14:TP=-1.2:LRA=11 -ar 48000 vo-norm.wav`. Mixar contra uma voz sem normalizar deixa todos os números abaixo errados.
- Coloque a trilha em 0,13 a 0,18 de volume linear, com 0,15 como ponto de partida e 0,18 como opção mais alta. Contra uma voz normalizada em -14 LUFS, isso deixa a trilha cerca de 19 a 20 dB abaixo dos picos da voz.
- Ajuste cada SFX por tipo, em volume linear de 0,28 a 0,50. Whoosh suave fica em 0,28 a 0,35. Pop fica em 0,32. Count-up fica em 0,40 a 0,45. Impacto, carimbo e sub-drop ficam em 0,50.
- Escalone o kit inteiro com um só ganho-mestre perto de 1,95, com teto em 0,8, para nenhum impacto enterrar a voz. Um só ganho-mestre vira um só ajuste quando o kit inteiro precisa ficar mais alto ou mais baixo.
- Feche o master final em -14 a -13 LUFS, no alvo de -14 LUFS da skill. Confira o master com medição, nunca só de ouvido.
- Verifique cada hit com volumedetect numa janela ao redor do hit. A janela do hit deve medir de 3 a 5 dB acima dos picos da voz para soar punchy.
- Use estes números como complemento da seção de mixagem fina acima, que já traz o ducking por sidechain. Os dois conjuntos se somam, com a voz sempre no topo.

## Colocação dos SFX

Fonte: sound-design, sintetizado com palavras próprias, em https://github.com/krusemediallc/video-editor-agent, e motion-video-director, sintetizado com palavras próprias, em https://github.com/mattypark/Motion-graphics-skill

- Caia cada hit de SFX na palavra exata, não no início da frase. O SFX de fogo cai na palavra fogo.
- Reserve whoosh só para cortes de seção. Whoosh em todo cartão soa forçado e vira ruído.
- Use um único grande swell por vídeo, na abertura ou na revelação final. Se tudo é grande, nada é grande.
- Monte o trio riser, impacto e whoosh, com o riser antes da revelação, o impacto no pico e o whoosh na transição.
- Sincronize o transiente do SFX ao frame do pico visual, com tolerância de mais ou menos 1 frame. Em 60 fps, 1 frame é cerca de 17 ms.
- Combine camadas no impacto, com corpo grave, punch médio e brilho alto, para o hit ter peso em alto-falante de celular e em fone.

## Kit de SFX com auditoria

Fonte: sound-design, sintetizado com palavras próprias, em https://github.com/krusemediallc/video-editor-agent

- Gere o kit de SFX via ElevenLabs, com whooshes, pops, impactos, count-ups, sub-drops e risers, um arquivo por efeito e com o nome da ação no arquivo.
- Audite todos os arquivos com volumedetect, sem exceção. Cerca de 1/3 das gerações sai quase muda e um kit sem auditoria entrega hits que ninguém ouve.
- Regenere os fracos com "loud, punchy:" no início do prompt. Arquivo com pico abaixo de -12 dB é dud e volta para regeneração.
- Normalize o kit inteiro a -3 dB de pico, para os valores de volume da mixagem valerem igual para todos os arquivos.
- Sinalize arquivos com início tardio acima de 0,15 s. Início tardio cai fora do beat, então regenere com ataque afiado no prompt ou corte o início do arquivo.

## Sub-drop de abertura

Fonte: sound-design, sintetizado com palavras próprias, em https://github.com/krusemediallc/video-editor-agent

- Gere o sub-drop de abertura como SFX de 1,2 s, com grave cinematográfico e pitch caindo.
- Verifique o grave de verdade com lowpass em 120 Hz e volumedetect. Laptop não reproduz sub e um boom sem grave real é um dud.
- Confira o sub-drop também no master final, com lowpass nos primeiros 1,4 s. Sem energia abaixo de 120 Hz, não há sub-drop.
- Use o sub-drop como o grande swell do vídeo quando ele abre o vídeo. Não empilhe outro swell na revelação final.

## Composição de trilha

Fonte: music-studio, sintetizado com palavras próprias, em https://github.com/EtienneLescot/claude-music-skill

- Componha a trilha pelo método de compositor, não por prompt solto. O método é brief curto, motivo primeiro, harmonia e forma, orquestração e crítica após cada render.
- Escreva o motivo primeiro, com 2 a 3 candidatos, e fique com o mais forte, dizendo por que ele venceu.
- Monte harmonia e forma depois, com uma lista de seções e uma meta de energia por seção.
- Comece do estilo dark-suspense para terror e do estilo cinematic-pop para Shorts curtos e grudentos.
- Peça a trilha com gênero, BPM, bateria, baixo, política de melodia, arco de energia e a instrução de soar quieta e seca sob narração, sem vocais e com sensação de loop contínuo.
- Entregue a trilha com stems separados, para o ducking da trilha sob a narração funcionar na montagem.
- Entregue masterizada a -14 LUFS, no alvo da skill, e compare versões lado a lado em loudness igual antes de escolher.

## Voice settings do ElevenLabs por estilo

Fonte: elevenlabs, sintetizado com palavras próprias, em https://github.com/digitalsamba/claude-code-video-toolkit

- Use os valores abaixo como ponto de partida no modelo eleven_multilingual_v2, que aceita stability, similarity, style e speed. O modelo eleven_v4 aceita só stability e similarity, sem style e speed.
- Ajuste o estilo natural e profissional com stability de 0,75 a 0,85, similarity 0,9, style de 0 a 0,1 e speed 1,0.
- Ajuste o estilo conversacional com stability de 0,5 a 0,6, similarity 0,85, style de 0,3 a 0,4 e speed de 0,9 a 1,0.
- Ajuste o estilo energético com stability de 0,3 a 0,5, similarity 0,75, style de 0,5 a 0,7 e speed de 1,0 a 1,1.
- Teste os valores na voz fixa do perfil do canal antes de gerar a narração inteira. Valor de outro canal não transfere sem teste.
- Use audio tags para emoção e pausa, com [whispers] para sussurro, [excited] para animação, [sigh] para suspiro, [laughs] para riso e [warm] para calor. Escreva a tag de forma clara, porque o modelo pode ler a tag como efeito sonoro.

## Pausas reais

Fonte: elevenlabs, sintetizado com palavras próprias, em https://github.com/digitalsamba/claude-code-video-toolkit

- Faça pausas reais com quebras de parágrafo, que criam cerca de 0,3 a 0,5 s de pausa natural.
- Faça pausas reais com a tag [long pause] nos modelos v3 e v4, que aceitam audio tags.
- Insira silêncio com ffmpeg no pós, cortando o áudio e inserindo o silêncio exato, quando a pausa precisa de precisão.
- Evite usar elipse ... como pausa confiável. A elipse pode ser vocalizada como palavra ou som.
- Ajuste a pausa depois de ouvir a narração gerada. Se a pausa não ficou precisa o bastante, corrija no pós com ffmpeg em vez de brigar com o gerador de voz.

## Scribe v2 como base do karaokê

Fonte: elevenlabs, sintetizado com palavras próprias, em https://github.com/digitalsamba/claude-code-video-toolkit

- Transcreva a narração final com Scribe v2, que entrega word timestamps com início e fim de cada palavra.
- Use esses tempos palavra por palavra como base do karaokê, no lugar de estimar tempos na montagem.
- Gere o arquivo ASS a partir dos tempos do Scribe e revise nomes próprios e números, porque o reconhecimento erra nome e número.
- Mantenha a transcrição do Scribe junto da narração, para a legenda e a sincronia de cena usarem os mesmos tempos reais.

## Ar morto no início do áudio

Fonte: remotion-motion-graphics, sintetizado com palavras próprias, em https://github.com/fernandokaraka/remotion-motion-graphics-skill

- Corte o silêncio inicial do arquivo de áudio antes de montar. Um arquivo com 80 ms de ar morto cai 80 ms atrasado no vídeo.
- Meça o início do áudio com volumedetect ou com a forma de onda antes de juntar com o vídeo. Silêncio no início não aparece ouvindo rápido.
- Corte o ar morto em todos os arquivos de narração, SFX e música que entram na montagem, não só na narração.
