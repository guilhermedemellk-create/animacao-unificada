# Canal Dark no YouTube

## A regra do cifrão: só funciona com $ na frente

- Use $ na frente para chamar a skill e qualquer comando: $canal-dark, $canais, $help, $ideias, $nomes, $roteiro, $revisar, $thumbnail, $publicar, $status, $voz, $legenda, $capa, $musica, $plano, $concorrentes, $referencia, $titulo, $short, $stats, $logo, $banner, $descricao, $gancho, $agenda, $nicho, $serie, $audio, $efeitos, $intro, $checklist, $tema, $fontes, $template, $backup, $storyboard, $personagem, $teste, $corrigir, $monetizar, $automatizar, $portoes e $varredura.
- Veja o que funciona: `$canal-dark`, `$canal-dark quero um vídeo novo`, `$help`, `$ideias`.
- Veja o que não funciona: `/canal-dark`, `canal dark` sem $, `quero criar um canal dark`.
- Trate qualquer mensagem sem $ como mensagem normal: a skill não ativa sem o comando.

## Comando de ativação

- Ative a skill só com `$canal-dark`.
- Use `$canal-dark` sozinho para escolher qual canal continuar entre os perfis existentes, criar um canal novo, ou continuar o trabalho do canal ativo.
- Use `$canal-dark` com um pedido junto para começar com o pedido já dado.
- Veja os exemplos: `$canal-dark`, `$canal-dark quero um vídeo novo`, `$canal-dark cria um vídeo sobre mistérios`.
- Depois do comando, siga a entrevista de abertura na ordem: nome, estilo, promessa, formato e o resto.
- Use os comandos abaixo para ir direto ao trabalho sem refazer a entrevista.
- Use `$canal-dark` para começar a skill, escolher o canal entre os perfis existentes ou criar um canal novo. Leia o desenho de vários perfis em [perfis](references/perfis.md).
- Use `$canais` para ver os canais criados e trocar o perfil ativo.
- Use `$help` para ver a lista de todos os comandos com uma explicação curta de cada um.
- Use `$ideias` para ver ideias de vídeo para o canal que já existe.
- Use `$nomes` para ver 5 nomes novos de canal sem repetir os já sugeridos.
- Use `$roteiro` para escrever o roteiro do próximo vídeo do canal que já existe.
- Use `$revisar` para diagnosticar o roteiro aprovado antes de gerar narração ou clipe. Leia o guia em [revisar roteiro](references/revisar-roteiro.md).
- Use `$thumbnail` para criar título e thumbnail ou capa de um vídeo.
- Use `$publicar` para guiar a publicação e a medição do vídeo.
- Use `$status` para ver o perfil do canal salvo e o que já foi feito.
- Use `$voz` para ouvir as amostras das vozes e escolher a voz da narração.
- Use `$legenda` para escolher o estilo da legenda e conferir a legenda queimada.
- Use `$capa` para criar a capa do vídeo vertical para TikTok e Shorts.
- Use `$musica` para escolher a música e os efeitos sonoros do vídeo.
- Use `$plano` para ver o plano dos 10 primeiros vídeos e onde o canal está.
- Use `$concorrentes` para estudar os concorrentes do nicho antes do roteiro.
- Use `$referencia` para dissecar um vídeo de referência quadro a quadro antes de produzir. Leia o método em [referência](references/referencia.md).
- Use `$titulo` para gerar 5 opções de título para um vídeo.
- Use `$short` para adaptar um vídeo longo do YouTube para Short.
- Use `$stats` para medir o resultado dos vídeos publicados e saber o que mudar.
- Use `$logo` para criar a logo do canal a partir do perfil salvo.
- Use `$banner` para criar a arte do banner do canal no YouTube.
- Use `$descricao` para escrever a descrição do canal.
- Use `$gancho` para gerar 5 opções de gancho para um vídeo.
- Use `$agenda` para montar o calendário de postagens do canal.
- Use `$nicho` para trocar o nicho do canal sem trocar o nome.
- Use `$serie` para planejar uma série de vídeos sobre um tema, com a bíblia da série e o elenco de vozes quando os personagens falam.
- Use `$audio` para revisar o áudio de um vídeo pronto.
- Use `$efeitos` para montar o banco de efeitos sonoros do vídeo.
- Use `$intro` para criar a intro e o outro do canal.
- Use `$checklist` para rodar o checklist de pré-publicação do vídeo.
- Use `$tema` para pesquisar um tema a fundo antes do roteiro.
- Use `$fontes` para verificar as fontes dos fatos do roteiro.
- Use `$template` para criar o template fixo do vídeo do canal.
- Use `$backup` para fazer o backup dos arquivos do canal.
- Use `$storyboard` para montar o storyboard do roteiro aprovado antes de qualquer render ou geração.
- Use `$personagem` para criar a ficha do personagem ou mascote e manter ele igual em todos os clipes.
- Use `$teste` para produzir 1 clipe de teste e aprovar antes de produzir o vídeo inteiro.
- Use `$corrigir` para corrigir um problema específico de um vídeo pronto sem refazer o vídeo inteiro.
- Use `$monetizar` para conferir se o canal já pode monetizar e o que falta para liberar.
- Use `$automatizar` para configurar a automação do canal ativo com plataforma, agenda e teste de postagem e depois produzir e postar os vídeos da fila no calendário do canal. Leia o sistema completo em [automação](references/automacao.md).
- Use `$portoes` para rodar todos os portões de [portões de qualidade](references/portoes-qualidade.md) de uma vez no vídeo final e devolver aprovados e reprovados com o número de cada um.
- Use `$varredura` para rodar o blackdetect e o freezedetect no vídeo final e devolver os trechos com problema e o LUFS medido.
- Mostre a lista completa de comandos quando o usuário digitar `$help`, a qualquer momento, sem começar a entrevista e sem apagar o que já foi feito.
- Leia a lista completa de comandos com o que cada um faz, quando usar, exemplo e quando não serve em [comandos](references/comandos.md).

## Comece perguntando

- Antes de produzir qualquer coisa, faça a entrevista de abertura em [perguntas iniciais](references/perguntas-iniciais.md), salve as respostas no arquivo do perfil do canal novo e ative o perfil na hora, como manda [perfis](references/perfis.md).

- Pergunte primeiro se o usuário já tem nome para o canal. Se ele tiver, peça o nome e o @ e prossiga. Se ele não tiver, mostre os estilos e, dependendo do estilo que ele escolher, crie 5 nomes novos na hora e deixe ele escolher um. Nunca repita nomes já sugeridos em outro chat. Leia as fórmulas em [nomes](references/nomes.md).

- Em toda lista de opções que a skill mostrar, ofereça sempre a opção "Quero mais ideias". Quando o usuário pedir mais, gere 5 ideias novas sem repetir nenhuma já mostrada naquela conversa e sem repetir as registradas em ~/workspace/your_files/canal-dark-nomes-usados.md e ~/workspace/your_files/canal-dark-ideias-usadas.md. A regra completa está em [nomes](references/nomes.md), [ideias](references/ideias.md) e [título e thumbnail](references/titulo-thumbnail.md).

- O estilo escolhido no começo decide o resto da skill: formato, voz, thumbnail e títulos. Nunca ignore o estilo depois de escolhido. Pergunte o estilo e a promessa em uma frase antes de produzir qualquer roteiro.

- Pergunte a plataforma antes de escolher o formato. As opções são TikTok, YouTube longo, YouTube Shorts e os dois. A plataforma decide a proporção, a duração, o gancho, a legenda e a publicação. TikTok usa vídeo vertical 9:16, gancho em 1 a 2 segundos, legenda queimada indispensável e capa escolhida por frame. YouTube longo usa vídeo horizontal 16:9 de 10 a 12 minutos, com thumbnail 1280x720, título, descrição com fontes e tags. YouTube Shorts é uma plataforma própria, com vídeo vertical 9:16, gancho em 1 a 3 segundos e capa na grade do canal. Depois da plataforma, pergunte a duração do vídeo, com opções que dependem da plataforma escolhida. Depois que o usuário escolher a plataforma, siga só ela no vídeo inteiro. Leia as especificações em [perguntas iniciais](references/perguntas-iniciais.md).

- Pergunte a trilha do vídeo antes de qualquer produção. Esta é a decisão que muda o rumo inteiro da animação: ferramentas, custo, tempo, como se anima e como se testa. As opções são vídeo realista gerado por IA, animação 3D estilo Pixar gerada por IA, animação 3D low-poly feita por código com Blender e Python, infográfico 2D por código com Python e PIL ou com o renderizador CDP em HTML e CSS, com a variante de histórias 2D por código com renderFrame(n), e imagem estática com zoom. Compare as opções em [estilos visuais](references/estilos-visuais.md) e leia as cinco opções em [animação](references/animacao.md). O infográfico 2D é o estilo do vídeo 1 do O Laboratório Curioso, com o estudo de caso completo em [estudo de caso do Laboratório Curioso](references/estudo-caso-laboratorio-curioso.md). A variante de histórias usa os 4 estilos de quadros de movimento e está em [quadros de movimento](references/quadros-movimento.md). Depois que o usuário escolher, siga só aquela opção no vídeo inteiro.

- Pergunte se é uma série com personagens que falam, logo depois da trilha, só quando a trilha for a realista ou a Pixar por IA. Se for série com diálogo, monte o elenco com uma voz fixa por personagem e crie a bíblia da série antes do roteiro da parte 1. Leia o guia em [séries](references/series.md).

- Pergunte o formato do próximo vídeo antes de escrever. As opções são lista de dez itens, um mistério só aprofundado, compilado semanal, countdown de curiosidades rápidas, experimento mental "E se...?", quiz de verdade ou mentira, história animada narrada e história interativa com escolha no final.

- Pergunte o estilo da voz da narração antes de gerar áudio. São 26 estilos, do jovem animado ao grave misterioso, mais a opção Não entendi, que explica cada estilo com exemplo e pergunta de novo. Mostre o áudio de amostra de cada estilo junto com as opções, para o usuário ouvir cada voz antes de escolher. Ouça o hook com a voz escolhida antes de travar a escolha. Depois pergunte a origem: voz humana gravada, voz sintética fixa, voz clonada com consentimento ou usar o gerador de voz da skill. Leia os 26 estilos em [vozes](references/vozes.md) e o guia do gerador em [gerador de voz](references/gerador-voz.md). Registre a escolha no perfil do canal e não troque a voz no meio da série.

- Pergunte o estilo da legenda antes de montar o vídeo. As opções são legenda automática queimada no vídeo, só palavras-chave na tela e sem legenda. O padrão é a legenda karaokê: a palavra falada no momento fica em amarelo e o resto do texto fica em branco, com contorno preto. Leia o guia em [legendas](references/legendas.md).

- Pergunte o nível de animação antes de produzir. As opções são animação completa com gestos e câmera cortando a cada 2 a 4 segundos, animação simples com zoom e cortes a cada 5 a 10 segundos, e imagem estática. Leia as regras em [animação](references/animacao.md) e nunca entregue zoom lento como animação.

- Pergunte o estilo do ambiente antes de montar as cenas. As opções são um ambiente próprio por capítulo, um ambiente fixo para o vídeo inteiro e ambiente mínimo com fundo chapado. Leia o guia em [ambientação](references/ambientacao.md).

- Pergunte o áudio antes de gerar. As opções são narração com efeitos e música, narração só com música e narração sozinha. Leia o guia em [áudio](references/audio.md).

- Reuse o perfil do canal em cada novo vídeo e pergunte apenas o que mudou ou o que ainda falta. Não refaça a entrevista inteira quando o perfil já existe.
- Troque o perfil ativo com `$canais` quando o vídeo for de outro canal.

- Se o usuário responder só parte das perguntas, trabalhe com o que ele deu e deixe o resto com o padrão do formato mãe. Não trave o trabalho esperando todas as respostas.

## Define o formato do canal

- O estilo escolhido na entrevista decide o formato, a voz, a thumbnail e os títulos. Mistérios usa mistério único aprofundado com voz grave e misteriosa. Curiosidades usa lista de 10 com voz jovem e animada. Ciência usa "como funciona" com voz calma e didática. Terror usa compilado semanal com voz sussurrada. Espaço usa "E se...?" com voz de documentário. Crimes usa mistério único com voz feminina marcante. História usa documentário longo com mapas e voz de documentário. Tecnologia usa "como funciona" com voz calma e didática. Animais e natureza usa experimento mental com voz de documentário. Geografia usa mistério único com mapas e voz calma e didática. Dinheiro usa ascensão e queda com voz de documentário. Mitologia usa história completa longa com voz de documentário. Psicologia usa lista de sinais com voz calma e didática. Esportes usa história de um jogo ou ranking com voz de locutor de rádio. Games usa review antes de comprar ou teoria de jogo com voz jovem e animada. Comida e culinária usa receita passo a passo com voz calma e didática. Carros e máquinas usa como funciona de motor ou máquina com voz de documentário. Música usa ensaio sobre uma música ou um álbum com voz calma e didática. Profissões e trabalho usa como se constrói ou um dia na profissão com voz de documentário. Meio ambiente e clima usa fenômeno explicado com mapa e dados e voz de documentário. Construção e engenharia explicada em 3D usa Short passo a passo com voz calma e didática. Leia o mapa de cada estilo em [nomes](references/nomes.md).

- Fixe um formato mãe para os dez primeiros vídeos e repita esse formato sem misturar documentário longo, quiz e Shorts no mesmo período.

- O formato mãe muda com a plataforma. No YouTube longo, o formato mãe é o vídeo horizontal de 10 a 12 minutos. No YouTube Shorts, o formato mãe é o vídeo vertical de 15 a 60 segundos, com 1 fato por vídeo e gancho de 1 a 3 segundos. No TikTok, o formato mãe é o vídeo vertical, com o mesmo tema e a mesma promessa, cortado para o gancho de 1 a 2 segundos, na duração escolhida na entrevista.

- Use lista de dez itens com doze a quinze minutos e voz em off como formato mãe para curiosidades e fatos.

- Publique duas vezes por semana quando o canal tiver uma só pessoa produzindo e ajuste a frequência apenas depois de medir os dez primeiros vídeos.

- Escreva a descrição do canal em português direto com o tema, a frequência e o convite para sugerir o próximo tema.

- Rode um formato experimental por mês sem abandonar o formato mãe. Leia os cinco formatos em [ideias](references/ideias.md).

## Decide o rumo da animação

- Decida a trilha na entrevista, antes de qualquer produção. A trilha muda tudo: ferramentas, custo, tempo, como se anima, como se testa e como se monta o vídeo. O padrão da skill é vídeo realista gerado por IA. A trilha Pixar por IA é a alternativa quando o usuário pedir história seriada com protagonista fixo em animação 3D estilo Pixar, como o Crânio Era. A trilha 3D por código é a alternativa quando o usuário pedir animação 3D low-poly. A trilha 2D por código é a alternativa quando o usuário pedir motion graphics infográfico, com diagramas, mapas e números grandes, como o vídeo 1 do O Laboratório Curioso. Leia o estudo de caso em [estudo de caso do Laboratório Curioso](references/estudo-caso-laboratorio-curioso.md).

- Use a trilha realista quando o usuário quer visual de cinema, pessoas e lugares de verdade, e produção rápida. O desafio é a continuidade: o mesmo personagem igual em todos os clipes, com a ficha dele copiada em todos os prompts. O custo é por crédito e cada clipe dura cerca de 10 segundos.
- Use a trilha Pixar por IA quando o usuário quer história seriada com protagonista fixo em animação 3D estilo Pixar, como o Crânio Era. O desafio é a continuidade: o mesmo personagem igual em todos os clipes, com a ficha dele e o bloco de estilo copiados em todos os prompts. O custo é por crédito e cada clipe dura cerca de 10 segundos. Leia as regras em [animação](references/animacao.md).
- Crie a ficha do personagem com `$personagem` antes de gerar o primeiro clipe realista ou Pixar por IA, para copiar a mesma ficha em todos os prompts e manter o personagem igual do começo ao fim.

- Use a trilha 3D por código quando o usuário quer o vídeo todo animado, com identidade visual própria e sem depender de crédito de IA. O desafio é o tempo de render: cerca de 20 minutos por clipe de 10 segundos. O ganho é controle total de cada movimento. Use as bibliotecas 3D CC0 em [bibliotecas 3D](references/bibliotecas-3d.md) para personagens, objetos e cenários prontos e adapte cada modelo à paleta do canal antes de animar.

- Use a trilha 2D por código quando o usuário quer um vídeo todo animado com diagramas, mapas e números grandes, sem depender de crédito de IA e sem esperar horas de render. O desafio é desenhar cada diagrama por código. O ganho é render em segundos por cena, texto e números exatos, e identidade visual própria. O exemplo é o vídeo 1 do O Laboratório Curioso, com 72 cenas renderizadas em 20 a 30 minutos no total. A variante de histórias usa o renderizador CDP com renderFrame(n), com os 4 estilos de quadros de movimento, e está em [quadros de movimento](references/quadros-movimento.md).

- Nunca misture as trilhas no mesmo vídeo. Um vídeo realista com um clipe low-poly no meio quebra a identidade. Um vídeo por código com um clipe realista no meio quebra a identidade do mesmo jeito.

- Quando o usuário não souber, mostre as cinco opções com custo e tempo e deixe ele escolher. Não escolha por ele.

- Leia as regras das cinco opções em [animação](references/animacao.md) antes de produzir qualquer clipe.

## Estuda os concorrentes

- Comece pela biblioteca de canais da skill: [canais dark do Brasil](references/canais-dark-brasil.md) com 17 fichas e [canais dark do mundo](references/canais-dark-mundo.md) com 36 fichas. Cada ficha tem inscritos, formato, hook, thumbnail, vídeos mais vistos, o que copiar e o que evitar, tudo com fonte e data.
- Estude os vídeos modelo por nicho em [vídeos de referência](references/videos-referencia.md), com título, canal, fonte e data verificados e o que copiar de cada um. Assista ao vídeo inteiro antes de escrever qualquer roteiro inspirado nele e copie a estrutura e o ritmo, nunca as frases e as imagens.

- Pesquise cinco a oito canais do mesmo nicho antes de escrever e registre inscritos, frequência, duração típica e os três vídeos mais vistos de cada um.

- Use o conector vidIQ para buscar canais, vídeos, palavras chave e outliers e leia o documento do conector antes de chamar qualquer ferramenta dele.

- Compare apenas canais sem rosto com canais sem rosto e canais com apresentador com canais com apresentador.

- Anote a fórmula de título de cada vídeo de sucesso com número, tema famoso e gatilho de segredo ou medo.

- Anote o padrão de thumbnail de cada vídeo de sucesso com uma imagem, alto contraste e no máximo quatro palavras que complementam o título sem repetir o título.

- Corrija a premissa quando um canal citado não for dark ou não tiver o tamanho imaginado e registre o que foi verificado e o que ficou sem verificação.

- Amostre a gramática do estilo da referência, com estrutura, ritmo, visual, gráficos e som. Nunca copie rosto, voz, footage, logo ou nome do criador original. Disseque o vídeo de referência quadro a quadro com `$referencia` antes de produzir. Leia o método em [referência](references/referencia.md).

- Nunca invente número de inscritos ou de views. Cite fonte e data de cada número ou marque como não verificado.

## Escreve o roteiro

- Escreva o hook antes do resto do roteiro. O hook tem trinta segundos com dez segundos provando que o título é verdade, dez segundos dizendo por que isso importa e dez segundos de roteiro em uma frase. Entregue a promessa do título nos primeiros 15 segundos, com o primeiro beat real de ensino por volta de 30 a 45 segundos. Hook que só promete depois de 15 segundos reprova no diagnóstico de [revisar roteiro](references/revisar-roteiro.md).

- O hook muda com a plataforma. No vídeo longo do YouTube, o hook tem 30 segundos. No Short, o hook tem 1 a 3 segundos. No TikTok, o hook tem 1 a 2 segundos. Escreva o hook no tamanho da plataforma escolhida.
- No formato curto, use a estrutura em 4 partes: gancho de 0 a 3 segundos, setup de 3 a 15 segundos, valor até 5 segundos antes do fim e CTA nos últimos 5 segundos, com um reset de retenção aos 25 a 30 segundos no vídeo de 60 segundos. Uma ideia por vídeo.

- Abra sem saudação, sem logo animada e sem pedido de inscrição antes dos trinta segundos.

- Divida o roteiro em capítulos com um capítulo a cada setenta segundos e escreva o número do item na tela para quem assiste sem som.

- Coloque o melhor momento do vídeo aos dois terços do vídeo e solte um teaser do próximo item a cada dois ou três minutos.

- Escreva frases curtas para o ouvido e leia o hook em voz alta para testar o ritmo antes de aprovar.

- Estruture o roteiro com uma das 4 estruturas verificadas e escolha antes de escrever. A jornada do herói de Campbell 1949 usa partida, iniciação e retorno em 17 estágios. Os 3 atos de Field 1979 usam preparação com 25 por cento, confronto com 50 por cento e resolução com 25 por cento. O Save the Cat de Snyder 2005 usa 15 beats com catalisador perto de 10 por cento, ponto médio em 50 por cento e tudo perdido perto de 75 por cento. O círculo de Dan Harmon usa 8 passos e funciona melhor para vídeos curtos e seriados porque cada vídeo é uma volta completa no círculo.

- Use a jornada do herói para vídeos de mitologia, história e crimes com a pergunta como alguém entrou, o que enfrentou e com o que voltou. Comprima em 3 batidas no vídeo curto: mundo normal, mundo estranho e volta transformada.

- Use os 3 atos como régua de proporção para vídeos de 10 a 12 minutos. Se o ato 2 não tem metade do vídeo, o meio arrasta. No Short de 60 segundos, os 3 atos viram 15 segundos, 30 segundos e 15 segundos.

- Use os 15 beats do Save the Cat como checklist de diagnóstico. Se o vídeo não tem catalisador claro nem ponto médio, o meio morre. Use o par imagem de abertura e imagem final como thumbnail e frase final com antes você achava X e agora sabe Y.

- Use o círculo de Dan Harmon para séries. O passo 5, encontrar o que queria, fica no meio da história e não no fim, o que evita finais previsíveis.

- Escreva o hook com um dos 5 tipos verificados para vídeo curto: pergunta que o espectador já se pergunta, revelação com o resultado primeiro, contradição que desafia uma crença comum, choque visual no primeiro quadro e tensão como é por isso que X falhou.

- Teste o hook com a regra prática das fontes de 2026: se a primeira frase precisa de contexto para fazer sentido, está lenta demais. Reescreva até a frase funcionar sozinha.

- Passe o título, o hook e o fato central pelo checklist SUCCESs de Heath e Heath 2007. Simples com o núcleo claro, inesperado com quebra de padrão, concreto com detalhe sensorial, crível sem apelar só para autoridade, emocional com algo que importa e histórias com uma micro-história para o espectador ensaiar mentalmente. A maldição do conhecimento explica por que roteiro de especialista soa frio: quem sabe demais esquece o que é óbvio para quem não sabe.

- Dê a cada fato uma micro-história com quem, o que estava em jogo e o que aconteceu, em vez de listar o fato sozinho. A lição vem de Choy 2017: histórias fazem o trabalho de convencer que fatos sozinhos não fazem.
- Escreva o hook para o cérebro que já vem programado para história. A lição vem de Wired for Story, de Lisa Cron, 2012: o cérebro filtra milhões de informações por segundo e só deixa passar o que parece história com aposta. Abra cada fato com o que está em jogo para alguém, e não com o fato seco.
- Trate o título e o hook como um Hook Point só. A lição vem de Hook Point, de Brendan Kane, 2020: o espectador decide em 3 segundos e o Hook Point é a mensagem curta que para a rolagem. Leia o título e a primeira frase em voz alta e pergunte se funcionam sozinhos, sem contexto. Se precisarem de contexto, reescreva.

- Abra o vídeo com um incidente incitante claro nos primeiros segundos e feche com um clímax que muda o que o espectador acreditava. A lição vem de McKee 1997: história é forma e não fórmula, e o clímax é a mudança final e irreversível.

- Cite duas a três fontes por vídeo na descrição com links quando possível e escreva o roteiro com palavras próprias sem copiar o roteiro de outro canal.

- Planeje dez vídeos com três temas evergreen famosos, três listas de dez itens, duas sequências de um vídeo que performou bem e dois experimentos de formato. Siga [o plano dos dez primeiros vídeos](references/plano-10-videos.md).

- Faça a parte dois do melhor vídeo no quinto vídeo e compile os melhores trechos em um especial de uma hora no décimo vídeo.

- Escolha o tema do próximo vídeo em [ideias](references/ideias.md) quando o usuário não trouxer um tema. São 300 ideias com título e gancho prontos. Mostre sempre a opção "Quero mais ideias" e gere 5 ideias novas por pedido, sem repetir nada da conversa e nada do arquivo de ideias já usadas. Marque a melhor aposta em cada leva de 5 ideias, com o motivo.

- Quando o usuário escolher uma ideia, verifique no YouTube se já existe canal cobrindo aquele tema, antes de escrever o roteiro. Use o conector vidIQ primeiro e, se não resolver, a busca do YouTube.
- Mostre os principais canais e vídeos com o tema, com inscritos e views do vídeo mais visto, e diga se a ideia parece saturada ou aberta, para o usuário decidir se segue com ela ou troca.

- Diagnostique o roteiro com `$revisar` antes de gerar narração ou clipe. O diagnóstico acha as 4 assinaturas de falha de retenção, marca os cut points e confere o orçamento de palavras. Leia o guia em [revisar roteiro](references/revisar-roteiro.md).

## Monta o storyboard

- Quebre o roteiro em cenas de cerca de 10 segundos antes de animar qualquer coisa. Cada cena vira 1 clipe. Siga [storyboard](references/storyboard.md).

- Escreva cada cena com narração, ação do personagem, ação do assunto, ambiente, câmera, efeito sonoro, texto na tela e transição. Cena sem ação não existe. Reescreva.

- Os tempos do storyboard são estimativas. A duração real de cada cena vem da transcrição da narração pronta, medida cena por cena na montagem. Nunca monte o vídeo com os tempos estimados. Leia a regra de sincronia em [montagem](references/montagem.md).

- Mostre o storyboard ao usuário e aprove antes de qualquer render ou geração. Mostrar o storyboard primeiro evita refazer clipes.
- Peça o storyboard com `$storyboard` depois de aprovar o roteiro.

- Em vídeo longo, 1 capítulo tem 5 a 8 cenas. Em Short de 50 a 60 segundos, o vídeo tem 5 a 6 cenas.

## Produz a narração e o visual

- Escolha a voz no estilo registrado no perfil do canal e declare a voz sintética na descrição quando usar voz sintética.

- Produza a narração, os efeitos e a música seguindo [áudio](references/audio.md). Respeite o ritmo de cerca de cento e trinta palavras por minuto e gere a narração em uma só passada suave por capítulo, sem pausas bruscas entre as frases. Gere a narração com o gerador de voz da skill, seguindo [gerador de voz](references/gerador-voz.md). Quando a série tem personagens que falam, gere cada voz numa só passada suave por cena e marque cada fala com o nome de quem fala no roteiro. Leia o elenco em [séries](references/series.md).

- Produza o visual na rota escolhida na entrevista de abertura e siga [estilos visuais](references/estilos-visuais.md) para custo, tempo e limite de cada rota.

- Crie um gráfico ou mapa próprio por vídeo e nunca baixe um clipe de outro canal do YouTube.

- Gere imagens e vídeos de apoio com as ferramentas de geração de mídia disponíveis. O conector Runway não está conectado, então não gere nada com Runway até conectar a conta.

## Anima o vídeo de verdade

- Anime cada clipe na opção escolhida na entrevista, realista, Pixar por IA, 3D por código, 2D por código ou imagem estática com zoom. Cada opção tem ferramentas, custo e técnica próprios. Siga [animação](references/animacao.md) e não misture as opções no mesmo vídeo. Na imagem estática não há animação de verdade, então vale o aviso de retenção de [estilos visuais](references/estilos-visuais.md).
- Anime a história 2D com as 5 regras do movimento profissional e os 4 estilos de quadros de movimento. Leia [quadros de movimento](references/quadros-movimento.md) antes de escrever a primeira cena.

- Dirija o movimento de cada cena com a doutrina de movimento profissional. Leia [movimento profissional](references/movimento-profissional.md) antes de animar a primeira cena. A lei do vetor manda nas costuras, o crossfade é proibido e o idle wobble é erro.

- Nunca entregue zoom lento sobre imagem parada como animação. Se o usuário disser que está parado, ele está certo. Refaça.
- Produza 1 clipe de teste com `$teste` e mostre ao usuário antes de produzir o vídeo inteiro. O clipe de teste aprova visual, movimento e voz com 1 cena em vez de refazer o vídeo todo.
- Confira o checklist de aceite da trilha do vídeo em [animação](references/animacao.md) antes de aprovar qualquer clipe. Clipe que falha em 1 item do checklist volta para regeneração ou refação.
- Aplique a doutrina de [movimento profissional](references/movimento-profissional.md) na costura entre cenas e nunca use crossfade sem carrier.

- Faça o teste do mudo antes de entregar: assista ao clipe sem som e conte os movimentos em 10 segundos. Menos de 3 movimentos é clipe parado.

- Mantenha o mascote em movimento em todos os capítulos. Ele pisca, aponta e reage a cada fato.

- Siga o ritmo de 4 tempos dentro de cada clipe de 10 segundos e use as receitas de cena quando o roteiro pedir revelação, mecanismo, comparação, escala ou mistério. Leia o ritmo e as receitas em [animação](references/animacao.md).

- Dirija o olhar do espectador em cada cena com uma imagem que carrega o sentido da ideia. A lição vem de Glebas 2008: cada cena precisa de uma imagem que conta sozinha, não só de narração por cima de B-roll.

- Dê uma intenção a cada gesto antes de animar. A lição vem de Goldberg 2008: o personagem aponta porque acabou de perceber algo e recua porque ficou com medo. Gesto sem intenção é boneco mexendo o braço.

- Grave a narração antes de animar o gesto. A lição vem de Culhane 1988: o pipeline é roteiro, storyboard, voz, animação e montagem, e o timing da fala manda no timing do movimento.

- Troque a imagem ou o plano a cada cinco a dez segundos em vídeo sem rosto. Imagem parada por trinta segundos faz o espectador sair mesmo com boa narração.

## Cria o ambiente de cada cena

- Monte um ambiente próprio por capítulo, com 3 camadas: primeiro plano, plano do meio com o assunto e o mecanismo, e fundo com profundidade. Siga [ambientação](references/ambientacao.md).

- Enquadre o assunto grande no quadro e o mecanismo no centro. Nunca use paisagem aberta e vazia com personagem pequeno no meio.

- Respeite a paleta fixa do canal, azul-marinho com laranja, e use uma cor de destaque por capítulo.

- Dê luz e atmosfera a cada cena: sol, sombras, neblina, poeira, raios de luz ou bolhas, conforme o clima do capítulo.

## Cria o áudio completo

- Monte o áudio em 3 camadas: narração, efeitos sonoros e música. Nunca entregue um vídeo sem áudio, a não ser que o usuário tenha pedido um teste só visual. Siga [áudio](references/audio.md).

- Coloque um efeito sonoro por ideia ou ação, no mesmo segundo da ação na tela.

- Deixe a música baixa sob a narração e confira o volume final no alvo do YouTube, menos 14 LUFS.

- Assista ao vídeo final 2 vezes antes de entregar: uma com som e uma sem som.

## Monta o vídeo final

- Junte os clipes na ordem do storyboard, junte a narração por capítulo, coloque os efeitos no mesmo segundo da ação e a música baixa sob a narração. Siga [montagem](references/montagem.md).

- Alinhe cada cena à duração real da fala dela, medida da transcrição da narração pronta. Nunca use uma escala uniforme no vídeo inteiro para casar a duração total. A escala uniforme desalinha cena por cena e o áudio fica atrás ou na frente da imagem. A narração nunca é regravada nem editada para caber no vídeo. É o vídeo que segue a narração. O procedimento completo está em [montagem](references/montagem.md).

- Exporte o vídeo longo em 1920x1080 e o Short em 1080x1920, a 60 fps, com 40 fps como mínimo aceitável, e com o mesmo fps do começo ao fim. Exporte o vídeo do TikTok em 1080x1920, com a mesma proporção do começo ao fim.

- Confira o volume final no alvo do YouTube, menos 14 LUFS, antes de entregar.

## Coloca legenda automática no vídeo

- Queime a legenda automática no vídeo final no estilo karaokê: o texto da narração aparece embaixo, branco em negrito com contorno preto, e a palavra falada no momento fica em amarelo, sincronizado com o áudio. Siga [legendas](references/legendas.md).

- Gere o SRT com o Whisper a partir da narração, revise os nomes próprios e os números, e queime a legenda na montagem com o filtro subtitles do ffmpeg.

- A legenda é o texto exato da narração. O texto na tela é só a palavra-chave do fato. Não use um no lugar do outro.

- Assista ao vídeo final sem som e confira se dá para acompanhar a história só pela legenda e pela imagem.

## Confere a qualidade antes de entregar

- Confira o vídeo com o checklist de qualidade antes de mostrar ao usuário. Não entregue vídeo sem conferir.

- Faça o teste do mudo: assista sem som e conte os movimentos em 10 segundos. Menos de 3 movimentos é clipe parado. Refaça.

- Faça o teste do som: assista com som e confira sincronia de gesto e efeito, volume da narração e da música, e o alvo de menos 14 LUFS.

- Faça o teste de sincronia de áudio e imagem: extraia o frame no início de pelo menos 6 cenas espalhadas pelo vídeo e confira se o visual e a legenda batem com a fala daquele segundo. Se alguma cena estiver desalinhada, remonte aquela cena com a duração real da fala. Nunca entregue um vídeo com áudio atrasado ou adiantado em relação à imagem.

- Confira a continuidade: mesmo personagem, mesma roupa, mesmo cenário e mesma voz do começo ao fim.

- Confira o roteiro no vídeo: cada fato do roteiro aparece na tela, cada fonte citada está na descrição e o título é provado nos primeiros 10 segundos.

- Leia [erros comuns](references/erros-comuns.md) antes de entregar. Cada erro da lista já aconteceu neste canal e custou retrabalho.
- Confira o checklist de aceite da trilha do vídeo em [animação](references/animacao.md) e o checklist da cena de história em [quadros de movimento](references/quadros-movimento.md) quando o vídeo for 2D de histórias.
- Rode os portões de [portões de qualidade](references/portoes-qualidade.md) antes de entregar. Nenhum vídeo passa sem o portão de ação visível, o portão de voz, a varredura de quadros congelados e pretos e a verificação de sincronia em 6 inícios de cena.
- Rode `$portoes` no vídeo final para rodar todos os portões de uma vez e devolver aprovados e reprovados com o número de cada um. Portão reprovado para a produção e volta para a etapa dele.
- Rode `$varredura` no vídeo final para varrer quadros pretos, brancos e congelados e medir o LUFS. Reprove qualquer trecho preto ou branco acima de 0,1 segundo e qualquer trecho congelado acima de 0,5 segundo.
- Corrija um problema específico com `$corrigir` quando o vídeo voltar com defeito, em vez de refazer o vídeo inteiro.

## Cria título e thumbnail

- Escreva o título com uma das 23 fórmulas e a thumbnail com uma imagem só e no máximo quatro palavras. Siga [título e thumbnail](references/titulo-thumbnail.md). Mostre sempre a opção "Quero mais ideias" e gere 5 títulos novos e 5 conceitos novos de thumbnail por pedido, sem repetir nada da conversa. Marque a melhor aposta entre os 5 títulos, com o motivo.

- No TikTok e no Shorts não existe thumbnail. A capa é um frame do vídeo, escolhido na hora de publicar. Faça o primeiro frame valer como capa, com o assunto e o texto no centro da zona segura.

- Prometa apenas o que o vídeo entrega e prove o título nos primeiros 10 segundos.

- Teste até 3 títulos e thumbnails por vídeo no Test & Compare quando o canal permitir. O YouTube escolhe a vencedora por participação no tempo de exibição e não por taxa de cliques. O teste leva de alguns dias a até 2 semanas e só funciona no desktop. Não funciona para Shorts.

## Publica e mede

- Publique com o título e a thumbnail prontos, seguindo [título e thumbnail](references/titulo-thumbnail.md).

- No YouTube, publique o vídeo longo como público, com descrição, tags e tela final. No YouTube Shorts, publique o vídeo vertical com título curto, descrição com fontes e capa na grade do canal. No TikTok, publique o vídeo vertical com descrição curta, 2 a 3 hashtags e a capa escolhida por frame. Cada plataforma tem seu próprio passo de publicação. Não publique o mesmo arquivo nas duas sem adaptar proporção, duração e capa.

- Escreva a descrição com resumo narrativo, pergunta nos comentários e cinco a dez hashtags incluindo a marca do canal.

- Use dez a quinze variações da busca principal nas tags com pergunta, afirmação, verdade, segredo e o nome do tema.

- Publique um Short de menos de quarenta segundos por vídeo longo com o fato mais visual e legenda grande.

- Aponte a tela final para a parte dois ou para o vídeo mais parecido do catálogo.

- Meça os dez primeiros vídeos por retenção, cliques na thumbnail e tempo de exibição e mude apenas uma variável por vez entre um vídeo e o próximo.

- Considere acima da média segurar 35 a 40 por cento da audiência. A média do YouTube é 23,7 por cento e só 16,8 por cento dos vídeos seguram mais da metade. O YouTube não publica meta oficial de retenção. Compare cada vídeo com os 10 vídeos recentes de duração parecida do próprio canal.
- Confira se o canal já pode monetizar com `$monetizar` depois dos primeiros vídeos publicados e descubra o que falta para liberar a monetização.
- Leia a retenção de 2026 com os sinais de satisfação juntos. O YouTube passou a pesar pesquisas pós-assistir, revisão do vídeo, continuação da sessão, compartilhamentos e sentimento dos comentários junto com a retenção. Um vídeo com retenção boa e comentários ruins não cresce como um vídeo com retenção boa e comentários bons. Fonte: tubelab.net, guia de retenção de 2026, consulta em 06/11/2026.
- Leia o gráfico de retenção com os nomes atuais do YouTube Studio: Intro, Top Moments, Spikes e Dips. A Intro são os primeiros 30 segundos. Fonte: YouTube Help, citado em teleprompter.com, guia de 2026, consulta em 06/11/2026.
- Proteja o primeiro minuto acima de tudo. Mais de 55 por cento dos espectadores saem no primeiro minuto e vídeos com retenção acima de 65 por cento no primeiro minuto veem 58 por cento a mais de duração média assistida. Fonte: contentgrove.io, 2026, consulta em 06/11/2026. É benchmark de terceiros, não número oficial.
- No TikTok, mire a maior conclusão possível, sem número mágico. Guias de criadores citam 70 por cento de conclusão e rewatch de 15 a 20 por cento ou mais como sinal forte, mas o TikTok nunca publicou limiar nem peso para viralizar, então não trate 70 por cento como regra. Compartilhamentos e salvamentos pesam mais que curtidas. Fontes: transformationjunction.com, atualizado em junho de 2026, Sprout Social, 6 de fevereiro de 2026, e checagem de mitos do FastClip, 4 de outubro de 2026. São guias de criadores, sem confirmação oficial do TikTok.
- Aprenda a crescer com os livros certos. A lição vem de YouTube Secrets, de Sean Cannell e Benji Travis, 2ª edição ampliada, 2022: o canal cresce em cima de nicho, título, thumbnail e consistência, e não em cima de truque de algoritmo. A lição vem de The YouTube Formula, de Derral Eves, 2ª edição, 2026: o algoritmo responde a satisfação do espectador medida em dados, então cada vídeo é um teste e a decisão do próximo vídeo vem do Analytics e não do palpite. A biblioteca completa de 68 livros, com ano, fonte e aplicação prática, está em [livros](references/livros.md).

## Evita a desmonetização

- Recuse clickbait que o vídeo não entrega mesmo quando o título promete muitos cliques.

- Recuse slideshow de imagens de banco com narração genérica e recuse repetir o mesmo template em todos os vídeos apenas trocando o tema.
- Respeite a regra de conteúdo inautêntico do YouTube, esclarecida em 16 de julho de 2026: não monetizam conteúdo genérico ou repetitivo, conteúdo insatisfatório ou perturbador, e personas de IA dando informação sobre temas sensíveis, como saúde, finanças e leis. Conteúdo feito com IA e template genérico, sem a visão original do criador, está na lista de inelegível. O selo de IA sozinho não desmonetiza e o que desmonetiza é produção em massa com template. Fonte: TechCrunch, 20 de julho de 2026, e políticas de monetização do YouTube, citados em getorange.ai e vidpal.ai, outubro de 2026.
- Varie cada vídeo de verdade em substância, com apuração, roteiro próprio e estrutura própria. Repetir o mesmo template trocando só o tema é exatamente o que a política de 2026 chama de conteúdo genérico.

- Verifique cada fato sensível antes de publicar e evite afirmar como verdade uma alegação sem fonte.

- Apresente teorias como teorias e desminta teorias da conspiração com fontes em vez de alimentá-las.

- Declare thumbnail gerada por inteligência artificial quando a imagem não for uma foto real do fato.

- Trate uma acusação de cópia feita por terceiros como alegação e não como fato estabelecido até existir prova direta.

- Não prometa ganhos com números de páginas de venda de cursos. O dado verificável é volume de views e não promessa de renda.

## Available connectors

- [vidIQ](/opt/hatch/connectors/vidiq_mcp/CONNECTOR.md) for research on YouTube channels, videos, keywords, trends and competitors and for scoring titles and thumbnails.

- Runway is not connected. Do not generate anything with Runway until the account is connected. See the connector doc at /opt/hatch/connectors/runway_mcp/CONNECTOR.md only to check the connection status.

- Use `muse.connector_search` to find other connectors and `muse.skill_search` to find related skills.

- If nothing here fits, look on the web for a maintained API or MCP server and set it up with [Custom Connectors and MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md), or build a custom connector.

## Websites

- [YouTube Studio](https://studio.youtube.com/) for channel analytics and publishing. Carry the exact channel, video and period into the browser task and verify each figure with its metric name.

- [YouTube](https://www.youtube.com/) for watching competitor videos and reading descriptions, chapters and credits. Carry the exact channel and video links into the browser task and report what was watched and what was only inferred from text.

## Alternatives for better results

- Pergunte ao usuário qual canal concorrente ele quer como modelo principal antes de fechar o guia de estilo.

- Quando o usuário trouxer um vídeo de referência, assista ao vídeo e descreva formato, edição e estrutura antes de sugerir o nicho ou o formato.
