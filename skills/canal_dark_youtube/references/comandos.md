# Comandos da skill canal dark

Use um comando para chamar a skill sem precisar explicar o que você quer do zero. Cada comando abaixo mostra o que ele faz, quando usar, um exemplo de quando digitar e quando ele não serve.

## A regra do cifrão: só funciona com $ na frente

Use $ na frente para chamar a skill e qualquer comando. Funciona: `$canal-dark`, `$help`, `$ideias`. Não funciona: `/canal-dark`, `canal dark` sem $, `quero criar um canal dark`. Sem o $ é só uma mensagem normal e a skill não ativa.

## $canal-dark

O comando principal da skill. Começa a entrevista de abertura quando nenhum canal existe, mostra os canais criados para escolher qual continuar quando já existe perfil, e cria um canal novo sem apagar os outros.

Use quando quiser criar o canal do zero ou quando quiser voltar a trabalhar num canal que já existe sem lembrar onde parou.

Exemplos de quando digitar:

- `$canal-dark` para escolher qual canal continuar ou criar um canal novo
- `$canal-dark quero um vídeo novo` para começar com o pedido já dado
- `$canal-dark cria um vídeo sobre mistérios` para começar com o tema já escolhido

Quando não serve: quando você só quer ver a lista de comandos sem começar nada. Nesse caso use `$help`.

O que a skill faz: sem perfil salvo, ela começa a entrevista de abertura na ordem nome, estilo, promessa, formato e o resto. Com pelo menos um perfil salvo, ela mostra os perfis existentes para você escolher qual continuar, mais a opção de criar um canal novo. Escolher um perfil o torna ativo e mostra o resumo dele. Criar um novo roda a entrevista normal e salva o perfil novo sem apagar os outros. Com perfil ativo, ela lê o perfil em `~/workspace/your_files/canal-dark-perfil.md` e pergunta só o que mudou ou o que ainda falta. Ela nunca refaz a entrevista inteira quando o perfil já existe. O desenho completo de vários perfis está em [perfis](perfis.md).

## $canais

Mostra os canais criados na máquina, com nome, @, nicho e plataforma de cada um e qual é o ativo, e deixa trocar o perfil ativo tocando num deles.

Use quando você criou mais de um canal e quer ver todos, ou quando quer trocar o canal ativo para continuar outro canal.

Exemplo de quando digitar:

- `$canais` quando você quer continuar outro canal e não lembra quais canais já criou

Quando não serve: quando só existe um canal, porque não há nada para trocar. Nesse caso use `$canal-dark` para continuar o canal que já existe.

O que a skill faz: ela lê o diretório de perfis em `~/workspace/your_files/canal-dark-perfis/` na hora, por isso a lista está sempre atualizada e todo canal novo aparece sem precisar registrar a lista em outro lugar. Ela mostra nome, @, nicho e plataforma de cada canal e marca qual é o ativo. Tocando num canal, ela o torna ativo: copia o arquivo dele por cima do perfil ativo e atualiza o apontador. Ela nunca apaga perfil nenhum ao trocar. A lista é só local, da máquina da pessoa. O desenho completo está em [perfis](perfis.md).

## $help

Mostra a lista de todos os comandos com uma explicação curta de cada um.

Use a qualquer momento, no meio de qualquer trabalho, quando você esquecer qual comando existe ou o que cada um faz.

Exemplo de quando digitar:

- `$help` no meio de um roteiro para lembrar como pedir ideias novas

Quando não serve: quando você já sabe o que quer e quer ir direto ao trabalho. Nesse caso digite o comando certo em vez de pedir ajuda.

O que a skill faz: ela mostra a lista completa de comandos e volta para o ponto onde você estava, sem começar a entrevista e sem apagar nada do que já foi feito.

## $ideias

Mostra ideias de vídeo para o canal, sem começar tudo de novo.

Use quando você já tem um canal com perfil salvo e precisa de um tema para o próximo vídeo.

Exemplo de quando digitar:

- `$ideias` depois de terminar um vídeo e não saber qual tema vem agora

Quando não serve: quando o canal ainda não existe e não tem perfil salvo, porque a skill não sabe o nicho nem o formato para sugerir ideias que combinem. Nesse caso a skill avisa que falta a entrevista e oferece começar com `$canal-dark`.

O que a skill faz: ela lê o perfil salvo e o nicho do canal, mostra ideias no formato mãe do canal e usa as 300 ideias de [ideias](ideias.md) como base. Quando você pedir mais ideias aqui, ela gera 5 ideias novas sem repetir as já mostradas. Ela nunca repete uma ideia que já foi usada no canal. Quando você escolher uma ideia, ela verifica no YouTube se já existe canal cobrindo aquele tema, antes de escrever o roteiro. Ela usa o conector vidIQ primeiro e, se não resolver, a busca do YouTube. Ela mostra os principais canais e vídeos com o tema, com inscritos e views do vídeo mais visto, e diz se a ideia parece saturada ou aberta, para você decidir se segue com ela ou troca.

## $nomes

Mostra nomes novos de canal, sem repetir os já sugeridos.

Use quando você ainda não escolheu o nome do canal ou quando quer trocar o nome antes de confirmar.

Exemplo de quando digitar:

- `$nomes` quando você não gostou dos 5 nomes que a skill mostrou e quer 5 nomes novos

Quando não serve: quando o nome do canal já foi confirmado e registrado no perfil, porque trocar o nome depois de confirmado quebra a identidade do canal. Nesse caso a skill avisa que o nome já está confirmado e pergunta se você quer mesmo trocar.

O que a skill faz: ela cria 5 nomes novos seguindo as fórmulas de [nomes](nomes.md) para o estilo escolhido e confere o registro em `~/workspace/your_files/canal-dark-nomes-usados.md` antes de sugerir. Ela nunca sugere um nome que já está no registro. Depois que você escolher um nome, ela registra a escolha no mesmo arquivo.

## $roteiro

Escreve o roteiro do próximo vídeo do canal que já existe, usando o perfil salvo.

Use quando o canal já tem nome, plataforma, formato mãe, voz e trilha definidos e você quer o roteiro do próximo vídeo.

Exemplo de quando digitar:

- `$roteiro` quando o canal já existe e você quer o roteiro do vídeo seguinte

Quando não serve: quando não existe perfil salvo do canal, porque a skill não sabe o formato mãe, a voz, a plataforma nem a trilha para escrever o roteiro. Nesse caso a skill diz que falta a entrevista e oferece começar com `$canal-dark`.

O que a skill faz: ela lê o perfil salvo, escolhe o tema com você quando você não trouxer um tema, e escreve o roteiro no formato mãe com hook, capítulos, fontes e tela final, seguindo as regras de roteiro da skill. Se você trouxer um tema junto, como `$roteiro sobre mistérios do Brasil`, ela usa esse tema.

## $revisar

Diagnostica o roteiro aprovado antes de gerar narração ou clipe, achando onde o roteiro sangra espectadores.

Use quando o roteiro já está escrito e você quer saber o que está fraco nele antes de gastar crédito ou tempo de render, ou quando um vídeo não reteve e você quer saber se o problema nasceu no roteiro.

Exemplo de quando digitar:

- `$revisar` depois de aprovar o roteiro, para diagnosticar antes do storyboard

Quando não serve: quando ainda não existe roteiro, porque não há nada para diagnosticar. Nesse caso escreva o roteiro com `$roteiro` primeiro.

O que a skill faz: ela lê o roteiro e procura as 4 assinaturas de falha de retenção, com promessa fraca, resposta enterrada, trecho morto e final sem loop, confere o gancho em 2 a 2,5 segundos no Short, marca os cut points com timestamps e tags de margem, confere o orçamento de palavras e devolve o diagnóstico com 2 a 4 pontos de sangria e a reescrita anotada. Ela só libera o roteiro para produção quando o diagnóstico não encontra mais nenhuma assinatura de falha. O guia completo está em [revisar roteiro](revisar-roteiro.md).

## $storyboard

Monta o storyboard do roteiro aprovado, com 1 cena por clipe de cerca de 10 segundos, antes de qualquer render ou geração.

Use quando o roteiro já foi aprovado e você precisa ver cena por cena o que vai aparecer na tela, o que o personagem faz e o que o assunto faz, antes de gastar crédito ou tempo de render.

Exemplo de quando digitar:

- `$storyboard` depois de aprovar o roteiro, para ver as cenas antes de gerar os clipes

Quando não serve: quando o roteiro ainda não existe ou ainda não foi aprovado, porque o storyboard nasce do roteiro aprovado. Nesse caso escreva o roteiro com `$roteiro` primeiro.

O que a skill faz: ela quebra o roteiro em cenas de cerca de 10 segundos e escreve cada cena com narração, ação do personagem, ação do assunto, ambiente, câmera, efeito sonoro, texto na tela e transição, seguindo [storyboard](storyboard.md). Os tempos são estimativas e a duração real de cada cena só vem da transcrição da narração pronta na montagem. Ela mostra o storyboard para você aprovar antes de qualquer render ou geração.

## $personagem

Cria a ficha do personagem ou mascote do canal, com aparência, roupa, cores e referências, para manter ele igual em todos os clipes.

Use quando o vídeo usa a trilha realista, a trilha Pixar por IA ou a trilha 3D por código e o personagem aparece em mais de 1 clipe, ou quando o personagem mudou de um clipe para o outro e você quer travar a aparência dele. Na trilha Pixar a ficha é obrigatória, porque a continuidade do protagonista é o maior risco da trilha.

Exemplo de quando digitar:

- `$personagem` antes de gerar o primeiro clipe, para fixar como o personagem é e copiar a ficha em todos os prompts

Quando não serve: quando o vídeo usa a trilha 2D infográfico sem apresentador, porque não há personagem para manter igual. Nesse caso o vídeo não precisa de ficha.

O que a skill faz: ela cria a ficha com rosto, cabelo, idade aparente, roupa, cores, acessórios, altura e jeito de se mover, e registra a ficha no perfil do canal. Ela copia a mesma ficha em todos os prompts de clipe e confere a continuidade no teste de qualidade. Ela nunca muda a roupa, o cabelo ou as cores do personagem no meio do vídeo sem você pedir. Quando a série tem personagens que falam, a ficha ganha o campo Voz, com estilo, nome e ID da voz, velocidade e impressão digital de voz, e a voz do personagem não muda no meio da série. Leia o elenco em [séries](series.md).

## $teste

Produz 1 clipe de teste do vídeo, com 1 cena do storyboard, para aprovar visual, movimento e voz antes de produzir o vídeo inteiro.

Use quando o storyboard já foi aprovado e você quer ver como o vídeo vai ficar de verdade, com 1 cena só, antes de gastar crédito ou horas de render no vídeo todo.

Exemplo de quando digitar:

- `$teste` depois de aprovar o storyboard, para ver 1 cena pronta antes de produzir as outras

Quando não serve: quando ainda não existe storyboard aprovado, porque o clipe de teste é 1 cena do storyboard. Nesse caso monte o storyboard com `$storyboard` primeiro.

O que a skill faz: ela escolhe a cena mais representativa do storyboard, gera o clipe na trilha do canal com narração, efeitos e legenda karaokê, e mostra o clipe para você aprovar ou pedir ajuste. Ela só produz o resto do vídeo depois da sua aprovação. Ela nunca produz o vídeo inteiro sem teste aprovado, nem na automação. Sem aprovação do teste, a produção para e avisa o que falta.

## $thumbnail

Cria título e thumbnail de um vídeo, ou capa no TikTok.

Use quando o vídeo já está pronto ou o roteiro já existe e você precisa do título e da imagem que vão chamar o clique.

Exemplo de quando digitar:

- `$thumbnail` depois de aprovar o roteiro do vídeo sobre o tema escolhido

Quando não serve: quando ainda não existe vídeo nem roteiro, porque a skill precisa saber o que o vídeo entrega para prometer só o que ele entrega. Nesse caso a skill avisa que falta o roteiro e oferece escrever com `$roteiro`.

O que a skill faz: ela escreve o título com uma das 23 fórmulas e cria a thumbnail com uma imagem só e no máximo quatro palavras, seguindo [título e thumbnail](titulo-thumbnail.md). Ela monta a thumbnail por camadas, com a placa sem texto feita pelo modelo de imagem e as palavras compostas por código, e confere a vista de 168 px aberta na tela antes de aprovar. No TikTok e no Shorts não existe thumbnail, então ela prepara a capa como um frame do vídeo com o assunto e o texto no centro da zona segura.

## $publicar

Guia a publicação e a medição do vídeo.

Use quando o vídeo, o título e a thumbnail já estão prontos e você quer publicar e saber o que medir depois.

Exemplo de quando digitar:

- `$publicar` quando o vídeo final está pronto e você quer subir no YouTube

Quando não serve: quando o vídeo ainda não está pronto, porque publicar sem vídeo não faz sentido. Nesse caso a skill avisa o que ainda falta e volta para a etapa que falta.

O que a skill faz: ela prepara título, descrição com fontes, tags, visibilidade e tela final no YouTube longo, título curto, descrição com fontes e capa no YouTube Shorts, ou descrição curta, hashtags e capa no TikTok. Depois da publicação ela diz o que medir: retenção, cliques na thumbnail e tempo de exibição, e lembra de mudar só uma variável por vez entre um vídeo e o próximo. Depois de publicar, ela tria os comentários em 4 pilhas, com perguntas, correções, elogios e isca, e anota as perguntas repetidas como temas do próximo vídeo. O método está em [ideias](ideias.md).

## $status

Mostra o perfil do canal salvo e o que já foi feito.

Use quando você voltar depois de um tempo e quiser lembrar onde parou, ou quando quiser conferir as decisões do canal antes de pedir o próximo vídeo.

Exemplo de quando digitar:

- `$status` quando você volta depois de dias sem abrir o chat e quer ver o que já foi feito

Quando não serve: quando o canal ainda não existe e não tem perfil salvo, porque não há nada para mostrar. Nesse caso a skill diz que não há perfil salvo e oferece começar com `$canal-dark`.

O que a skill faz: ela lê o perfil em `~/workspace/your_files/canal-dark-perfil.md` e mostra nome, @, logo, plataforma, formato mãe, voz, trilha e frequência, e lista o que já foi feito: vídeos prontos, roteiros escritos e ideias já usadas. Ela também diz que `$canais` lista todos os canais criados e deixa trocar o ativo.

## $voz

Escolhe e testa a voz da narração do canal, sem refazer a entrevista.

Use quando quiser trocar o estilo da voz, testar uma voz nova no hook ou conferir a voz registrada no perfil antes de gerar a narração.

Exemplo de quando digitar:

- `$voz` quando você quiser ouvir as amostras das vozes antes de escolher a voz do canal

Quando não serve: quando o canal ainda não existe e não tem perfil salvo, porque a skill não sabe o estilo nem a plataforma para recomendar uma voz. Nesse caso use `$canal-dark`.

O que a skill faz: ela lê a voz registrada no perfil, mostra os 26 estilos com o canal modelo de cada um e a opção "Não entendi", mostra o áudio de amostra de cada estilo para você ouvir antes de escolher, gera o hook com a voz escolhida para você ouvir antes de aprovar e registra a escolha no perfil. As amostras ficam em amostras-voz dentro da pasta da skill e o mapa de estilo para voz está em [vozes](vozes.md) e [gerador de voz](gerador-voz.md).

## $legenda

Escolhe o estilo da legenda e confere a legenda queimada no vídeo.

Use quando quiser mudar o estilo da legenda, conferir se a legenda está legível no celular ou corrigir uma legenda que ficou fora de sincronia.

Exemplo de quando digitar:

- `$legenda` quando a legenda do vídeo ficou pequena demais no Short

Quando não serve: quando o vídeo ainda não tem narração pronta, porque a legenda nasce da transcrição da narração. Nesse caso gere a narração primeiro.

O que a skill faz: ela mostra as 3 opções de legenda, com a legenda karaokê como padrão, e aplica o estilo escolhido a partir da transcrição real da narração, com a palavra falada em amarelo e o resto em branco. O guia completo está em [legendas](legendas.md).

## $capa

Cria a capa do vídeo vertical para TikTok e Shorts.

Use quando o vídeo vertical já está pronto e você precisa da capa que aparece na grade e na busca.

Exemplo de quando digitar:

- `$capa` depois de aprovar o vídeo do TikTok e antes de publicar

Quando não serve: quando o vídeo é longo do YouTube, porque vídeo longo usa thumbnail, não capa. Nesse caso use `$thumbnail`.

O que a skill faz: ela escolhe o melhor frame do vídeo, com 1 ponto focal só, o assunto grande, alto contraste e o texto no centro da zona segura, no máximo 3 palavras, e confere se nada importante fica coberto pela interface. As regras estão em [título e thumbnail](titulo-thumbnail.md).

## $musica

Escolhe a música e os efeitos sonoros do vídeo.

Use quando o vídeo já tem roteiro e você precisa da trilha e dos efeitos antes de montar.

Exemplo de quando digitar:

- `$musica` quando o vídeo é de terror e precisa de uma trilha tensa e de efeitos de suspense

Quando não serve: quando o roteiro ainda não existe, porque a música e os efeitos seguem o clima e as ações do roteiro. Nesse caso escreva o roteiro com `$roteiro`.

O que a skill faz: ela escolhe uma família de música licenciada que combina com o clima do vídeo, define o volume da música baixa sob a narração e prepara a mixagem no alvo de menos 14 LUFS. Os efeitos sonoros por cena ficam com `$efeitos`. O guia completo está em [áudio](audio.md).

## $plano

Mostra o plano dos 10 primeiros vídeos do canal e onde o canal está nele.

Use quando quiser saber qual vídeo vem agora, planejar a semana ou ver se o canal já testou um formato novo.

Exemplo de quando digitar:

- `$plano` no começo da semana para escolher os temas dos próximos vídeos

Quando não serve: quando o canal ainda não existe e não tem perfil salvo, porque o plano depende do formato mãe e da frequência do canal. Nesse caso use `$canal-dark`.

O que a skill faz: ela lê o perfil e o arquivo de ideias já usadas, mostra os 10 vídeos do plano com o tema de cada um e marca os que já foram produzidos. O plano completo está em [plano dos 10 primeiros vídeos](plano-10-videos.md).

## $concorrentes

Estuda os concorrentes do nicho antes de escrever o roteiro.

Use quando quiser saber o que os canais do mesmo nicho estão fazendo, copiar o formato que funciona e evitar o que não funciona.

Exemplo de quando digitar:

- `$concorrentes` antes de escrever o roteiro do vídeo 1, para ver os 3 vídeos mais vistos de cada canal do nicho

Quando não serve: quando você já estudou os concorrentes e só quer o roteiro. Nesse caso use `$roteiro`.

O que a skill faz: ela pesquisa 5 a 8 canais do mesmo nicho na biblioteca da skill e no vidIQ, anota inscritos, frequência, duração típica, fórmula de título e padrão de thumbnail, e corrige a premissa quando um canal citado não for dark. Nunca inventa números. Ela ranqueia os vídeos pelo múltiplo sobre a mediana do próprio canal, com pelo menos 4 vídeos por canal e 2 vezes ou mais a mediana como outlier. As fichas estão em [canais dark do Brasil](canais-dark-brasil.md) e [canais dark do mundo](canais-dark-mundo.md).

## $referencia

Disseca um vídeo de referência quadro a quadro antes de produzir, medindo ritmo, cortes e camadas para copiar a gramática do estilo sem copiar a identidade do criador.

Use quando o usuário mandar um vídeo de referência e você quiser estudar como ele é feito de verdade, antes de escrever o roteiro ou o storyboard.

Exemplo de quando digitar:

- `$referencia` com o link do vídeo de referência, para medir cortes, ritmo e camadas antes de produzir

Quando não serve: quando não existe vídeo de referência, porque não há nada para dissecar. Nesse caso estude os concorrentes com `$concorrentes` ou escolha o tema com `$ideias`.

O que a skill faz: ela faz o probe do original, mede todos os cortes incluindo jump cuts e punch-ins, lê frames consecutivos onde algo muda, reconstrói o vídeo por camadas e compara a reconstrução com o original por diff, e entrega um arquivo de notas com o que foi reconstruído, o que é aproximado e os números do último diff. Ela só disseca vídeos que se tem direito de usar e nunca copia rosto, voz, footage, logo ou nome do criador original. O método completo está em [referência](referencia.md).

## $titulo

Gera opções de título para um vídeo, sem mexer na thumbnail.

Use quando o vídeo já tem roteiro e você precisa de títulos para escolher, ou quando o título atual está fraco e você quer 5 opções novas.

Exemplo de quando digitar:

- `$titulo` quando o roteiro está pronto e você quer 5 títulos no padrão do nicho

Quando não serve: quando ainda não existe roteiro, porque o título precisa prometer só o que o vídeo entrega. Nesse caso escreva o roteiro com `$roteiro`.

O que a skill faz: ela escreve 5 títulos com as 23 fórmulas de [título e thumbnail](titulo-thumbnail.md), marca a melhor aposta com o motivo e mostra sempre a opção "Quero mais ideias". Ela nunca repete um título já mostrado na conversa. Ela passa cada título pela régua de corte em 60 caracteres no desktop e 40 no feed do celular, com no máximo 2 palavras em caixa alta, e rejeita o título que a thumbnail repete.

## $short

Adapta um vídeo longo do YouTube para Short.

Use quando o vídeo longo já está pronto e você quer um Short de divulgação com o fato mais visual dele.

Exemplo de quando digitar:

- `$short` depois de publicar o vídeo longo, para cortar o melhor fato em menos de 40 segundos

Quando não serve: quando o canal é só TikTok ou só Shorts, porque não há vídeo longo para adaptar. Nesse caso o vídeo já nasce vertical.

O que a skill faz: ela escolhe o fato mais visual do vídeo longo, escreve o gancho novo de 1 a 3 segundos, corta o trecho em vertical 1080x1920, queima a legenda karaokê e aponta o Short para o vídeo longo. O Short de divulgação tem menos de 40 segundos. O limite da plataforma é 60 segundos, e o Short de divulgação fica abaixo de 40 segundos por regra da skill. A capa segue as regras de [título e thumbnail](titulo-thumbnail.md).

## $stats

Mede o resultado dos vídeos publicados e diz o que mudar no próximo.

Use quando os primeiros vídeos já estão no ar e você quer saber o que está funcionando.

Exemplo de quando digitar:

- `$stats` depois de uma semana com os 3 primeiros vídeos publicados, para comparar retenção e decidir o próximo tema

Quando não serve: quando nenhum vídeo foi publicado ainda, porque não há dado para medir. Nesse caso publique o primeiro vídeo com `$publicar`.

O que a skill faz: ela lê os números do YouTube Studio ou do TikTok, compara retenção, tempo de exibição e cliques na thumbnail entre os vídeos, e recomenda mudar só uma variável por vez no próximo vídeo. Acima da média é segurar 35 a 40 por cento da audiência. Ela lê a queda em 3 problemas: vazamento de gancho nos primeiros 30 segundos, com perda abaixo de 25 por cento saudável e correção nos primeiros 15 segundos do roteiro, penhasco num ponto só, com a frase dita naquele segundo, e deslizamento no meio, que se corrige cortando e não reescrevendo. Ela entrega o maior vazamento e 1 mudança para ele. Se o gancho está saudável e o meio está plano, o problema é a embalagem e a correção vai para $thumbnail.

## $monetizar

Confere se o canal já pode monetizar no YouTube, o que falta para liberar e o que precisa mudar para não perder a monetização.

Use quando os primeiros vídeos já estão publicados e você quer saber se o canal já cumpre os requisitos do Programa de Parcerias do YouTube, ou quando um vídeo perdeu a monetização e você quer saber o motivo.

Exemplo de quando digitar:

- `$monetizar` depois dos 10 primeiros vídeos publicados, para ver o que falta para liberar a monetização

Quando não serve: quando o canal ainda não tem vídeo publicado, porque não há nada para medir. Nesse caso publique o primeiro vídeo com `$publicar`.

O que a skill faz: ela confere inscritos, horas assistidas, vídeos publicados e conformidade com as políticas do YouTube, incluindo a regra de conteúdo inautêntico de 2026, e lista o que já está cumprido e o que falta. Ela nunca promete valor de ganho nem prazo de liberação, porque o YouTube não publica esses números. Ela aponta o que corrigir no canal para manter a monetização depois de liberada.

## $logo

Cria a logo do canal a partir do perfil salvo, com o nome, o estilo e a paleta do canal, para usar como foto de perfil no YouTube e no TikTok.

Use quando o canal ainda não tem logo, quando a logo atual não combina mais com o canal ou quando você quer uma variação nova para testar.

Exemplo de quando digitar:

- `$logo` depois de confirmar o nome e o estilo do canal, para criar a foto de perfil

Quando não serve: quando o canal ainda não tem nome nem estilo definidos, porque a logo depende dos dois. Nesse caso use `$canal-dark` para fazer a entrevista primeiro.

O que a skill faz: ela lê o nome, o estilo e a paleta do perfil, gera a imagem quadrada com a fórmula de prompt de [logo](logo.md), com 1 símbolo só e bloco negativo, salva em `~/workspace/your_files/logo-<nome-do-canal>.png` e registra o caminho no perfil. Ela reduz cada versão para 98x98 e para 32x32 e confere mono preto, mono branco, versão clara e versão reversa antes de mostrar, e cada versão nova é uma ideia nova sem repetir a anterior. Se não houver perfil salvo, ela pede o nome do canal e o estilo e cria a logo mesmo assim.

## $banner

Cria a arte do banner do canal, com o nome, a promessa e a identidade visual do canal.

Use quando o canal está pronto para o YouTube e precisa do banner da página do canal, ou quando a promessa do canal mudou e o banner ficou desatualizado.

Exemplo de quando digitar:

- `$banner` depois de criar a logo, para completar a identidade visual do canal no YouTube

Quando não serve: quando o canal é só TikTok, porque o TikTok não usa banner. Nesse caso a logo basta.

O que a skill faz: ela lê o nome, a promessa e a paleta do perfil, cria a arte em 2560x1440 com o combination mark, símbolo com nome e promessa, legíveis na zona segura central, salva em `~/workspace/your_files/banner-<nome-do-canal>.png` e registra o caminho no perfil. Ela nunca coloca texto pequeno nem detalhe nas bordas, porque o YouTube corta as bordas no celular e na TV, e nunca coloca o símbolo sozinho sem o nome no banner, porque o banner é onde o lockup completo vive.

## $descricao

Escreve ou reescreve a descrição do canal, com tema, frequência e convite para sugerir o próximo tema.

Use quando o canal está pronto para publicar e precisa da descrição da página Sobre, ou quando a promessa ou a frequência do canal mudou.

Exemplo de quando digitar:

- `$descricao` quando a promessa do canal mudou e a descrição antiga não diz mais o que o canal entrega

Quando não serve: quando você precisa da descrição de um vídeo, porque a descrição do vídeo tem resumo, fontes e hashtags do tema. Nesse caso use `$publicar`.

O que a skill faz: ela lê a promessa, o estilo e a frequência do perfil, escreve a descrição em português direto com o tema, a frequência e o convite para sugerir o próximo tema, mostra o texto para você aprovar e registra a descrição no perfil. Ela nunca promete o que o canal não entrega.

## $gancho

Gera 5 opções de gancho para um vídeo, antes de escrever o roteiro.

Use quando você já tem o tema do vídeo e quer escolher o melhor jeito de abrir, ou quando o gancho atual do roteiro está fraco e você quer opções novas.

Exemplo de quando digitar:

- `$gancho` com o tema do próximo vídeo, para escolher como abrir antes de escrever o roteiro

Quando não serve: quando ainda não existe tema para o vídeo, porque o gancho nasce do tema. Nesse caso escolha o tema com `$ideias` primeiro.

O que a skill faz: ela lê o tema, a plataforma e o formato mãe do perfil, escreve 5 ganchos no tamanho da plataforma, com 30 segundos no vídeo longo e 1 a 3 segundos no Short e no TikTok, marca a melhor aposta com o motivo e mostra sempre a opção "Quero mais ideias". Ela nunca repete um gancho já mostrado na conversa.

## $agenda

Monta o calendário de postagens do canal, com data, vídeo e prazo de cada entrega.

Use quando o plano dos 10 primeiros vídeos já existe e você quer transformar o plano em datas, ou no começo do mês para organizar a produção da semana.

Exemplo de quando digitar:

- `$agenda` no começo do mês para ver que vídeo sai em cada dia e o que precisa ficar pronto até quando

Quando não serve: quando o canal ainda não tem plano nem frequência definidos, porque a agenda nasce do plano e da frequência. Nesse caso use `$plano` primeiro.

O que a skill faz: ela lê o plano dos 10 primeiros vídeos e a frequência do perfil, monta o calendário com a data de cada publicação e o prazo de roteiro, produção e montagem de cada vídeo, e marca os vídeos já publicados. Ela respeita a frequência do canal e nunca agenda mais vídeos do que o produtor consegue entregar.

## $nicho

Troca o nicho do canal sem trocar o nome, atualizando formato, voz e thumbnail para o nicho novo.

Use quando o canal não está performando no nicho atual e você quer testar outro nicho com o mesmo nome, ou quando o tema do canal mudou de rumo.

Exemplo de quando digitar:

- `$nicho` quando o canal de curiosidades não cresce e você quer testar o nicho de mistérios

Quando não serve: quando você quer trocar o nome do canal junto com o nicho, porque trocar o nome é outro passo. Nesse caso troque o nome com `$nomes` e depois use `$nicho`.

O que a skill faz: ela mostra os 21 estilos, aplica o mapa do estilo novo em [nomes](nomes.md) para atualizar formato mãe, voz, thumbnail e fórmula de título, atualiza o perfil e sugere refazer a logo com `$logo` quando o símbolo da logo não combina mais com o nicho novo. Ela avisa que trocar de nicho muda a audiência do canal e recomenda testar o nicho novo por 10 vídeos antes de decidir.

## $serie

Planeja uma série de vídeos sobre um tema, com arco, ordem e gancho de um episódio para o próximo.

Use quando um tema rende mais de um vídeo e você quer prender o espectador com uma sequência, ou quando quer um formato fixo semanal com começo, meio e fim.

Exemplo de quando digitar:

- `$serie` quando o vídeo sobre mistérios do Brasil performou bem e você quer uma série com um mistério por estado

Quando não serve: quando o canal ainda não tem formato mãe nem frequência, porque a série precisa caber no ritmo do canal. Nesse caso use `$canal-dark` para definir o canal primeiro.

O que a skill faz: ela lê o tema, o formato mãe e a frequência do perfil, divide o tema em episódios com título e gancho de cada um, ordena os episódios do mais forte para o mais fraco com o melhor no meio da série, e aponta cada episódio para o próximo na tela final. Ela registra a série no plano dos 10 primeiros vídeos quando a série cabe nele. Quando a série tem personagens que falam, ela cria a bíblia da série antes do roteiro da parte 1, com premissa, arco completo, regras do mundo e o bloco de cada personagem, e monta o elenco com uma voz fixa por personagem, com audição antes de atribuir. Leia o guia completo em [séries](series.md).

## $audio

Revisa o áudio de um vídeo pronto, conferindo narração, efeitos, música, volume e sincronia.

Use quando o vídeo já está montado e você quer conferir o áudio antes de publicar, ou quando o áudio de um vídeo publicado soou estranho e você quer saber o que corrigir.

Exemplo de quando digitar:

- `$audio` depois de montar o vídeo, para conferir o volume e a sincronia antes de publicar

Quando não serve: quando o vídeo ainda não tem narração pronta, porque não há áudio para revisar. Nesse caso gere a narração primeiro.

O que a skill faz: ela ouve o áudio do vídeo final, confere a clareza da narração, a presença de pausas bruscas entre as frases, o volume no alvo de menos 14 LUFS, a música baixa sob a narração e cada efeito sonoro no mesmo segundo da ação na tela. Ela lista o que está certo e o que precisa corrigir, cena por cena, e nunca aprova um vídeo com áudio desalinhado da imagem.

## $efeitos

Monta o banco de efeitos sonoros do vídeo, com 1 efeito por ação do storyboard, no segundo exato da ação.

Use quando o roteiro e o storyboard já existem e você precisa da lista de efeitos antes de montar o áudio, ou quando um vídeo soou vazio e você quer saber que efeito faltou em cada cena.

Exemplo de quando digitar:

- `$efeitos` depois de aprovar o storyboard, para listar o som de cada ação antes de montar

Quando não serve: quando ainda não existe storyboard, porque o efeito nasce da ação da cena. Nesse caso escreva o roteiro com `$roteiro` primeiro.

O que a skill faz: ela lê cada cena do storyboard, escolhe 1 efeito sonoro por ação com o segundo exato, a duração e a intensidade, e monta a lista de efeitos com o arquivo de cada um. Ela nunca coloca 2 efeitos no mesmo segundo nem efeito sem ação na tela. A música fica com `$musica` e a revisão do áudio pronto fica com `$audio`.

## $intro

Cria a intro e o outro do canal, com abertura fixa e tela final que aponta para o próximo vídeo.

Use quando o canal já tem identidade visual e você quer uma abertura fixa que o público reconheça em 2 segundos, ou quando a tela final do vídeo não está levando ninguém para o próximo vídeo.

Exemplo de quando digitar:

- `$intro` depois de criar a logo, para fechar a abertura e o encerramento padrão do canal

Quando não serve: quando o canal ainda não tem nome, estilo e paleta definidos, porque a intro usa a identidade do canal. Nesse caso use `$canal-dark` primeiro.

O que a skill faz: ela cria a intro curta de 3 a 5 segundos com o símbolo da logo, o som de abertura e o bordão do canal, e o outro com a chamada para o próximo vídeo e a tela final apontando para a parte 2 ou para o vídeo mais parecido. Ela nunca coloca intro longa antes do hook, porque o hook vem primeiro e a intro só entra depois dos 30 segundos no vídeo longo, ou não entra no Short e no TikTok.

## $checklist

Roda o checklist de pré-publicação do vídeo, conferindo tudo que precisa estar certo antes de subir.

Use quando o vídeo final já está montado e você quer conferir tudo de uma vez antes de publicar, para não descobrir um erro depois de publicado.

Exemplo de quando digitar:

- `$checklist` com o vídeo final pronto, antes de apertar o botão de publicar

Quando não serve: quando o vídeo ainda não está montado, porque não há nada para conferir. Nesse caso termine a montagem primeiro.

O que a skill faz: ela confere título com a fórmula e a promessa provada nos primeiros 10 segundos, thumbnail com no máximo 4 palavras, descrição com fontes, tags, legenda karaokê sincronizada, áudio em menos 14 LUFS, sincronia de áudio e imagem em 6 cenas, continuidade do personagem e da voz, e as regras de desmonetização. Ela lista o que passou e o que falhou, cena por cena, e só libera a publicação com `$publicar` quando tudo passa.

## $portoes

Roda todos os portões de [portões de qualidade](portoes-qualidade.md) de uma vez no vídeo final e devolve aprovados e reprovados com o número de cada um.

Use quando o vídeo final já está montado e você quer a decisão de entrega com número, sem conferir portão por portão na mão.

Exemplo de quando digitar:

- `$portoes` com o vídeo final pronto, para saber se o vídeo passa ou volta para a etapa dele

Quando não serve: quando o vídeo ainda não está montado, porque não há arquivo final para medir. Nesse caso termine a montagem primeiro.

O que a skill faz: ela roda na ordem da produção o portão de trilha, a régua da MELHOR APOSTA, o portão de saturação, a escolha da cena de teste, o portão de ação visível, o portão de voz, a varredura de quadros pretos e congelados, o portão de sincronia, o portão de legenda, o portão de thumbnail, a leitura de retenção e o limite entre corrigir e refazer, e devolve a lista de aprovados e reprovados com o número medido de cada um. Portão reprovado para a produção e volta para a etapa dele. Nenhum portão pode ser pulado por pressa ou por prazo. Depois de $corrigir, ela roda de novo só os portões que reprovaram. Ela é diferente de $checklist, porque $checklist confere os itens de pré-publicação e $portoes mede os portões com número no vídeo final.

## $varredura

Roda o blackdetect e o freezedetect no vídeo final e devolve os trechos com problema e o LUFS medido.

Use quando o vídeo final já está montado e você quer a varredura rápida de quadros pretos, brancos e congelados antes de entregar, ou depois de $corrigir para conferir só a parte corrigida.

Exemplo de quando digitar:

- `$varredura` com o vídeo final pronto, para varrer os quadros e medir o LUFS antes de entregar

Quando não serve: quando o vídeo ainda não está montado, porque não há arquivo final para varrer. Nesse caso termine a montagem primeiro.

O que a skill faz: ela roda `ffmpeg -i video-final.mp4 -vf blackdetect=d=0.1:pic_th=0.98 -f null -` e `ffmpeg -i video-final.mp4 -vf freezedetect=n=0.003:d=0.5 -f null -` em todo o vídeo final, mede o LUFS com loudnorm e devolve os trechos pretos e congelados com o tempo de cada um. Ela reprova qualquer trecho preto ou branco acima de 0,1 segundo fora de corte deliberado e qualquer trecho congelado acima de 0,5 segundo. Ela guarda a saída dos dois detectores junto com o vídeo final, com o número medido de LUFS. Ela é o portão de varredura dentro de $portoes, rodado sozinho quando você só precisa da varredura.

## $corrigir

Corrige um problema específico de um vídeo pronto, sem refazer o vídeo inteiro.

Use quando o vídeo voltou com um defeito claro, como áudio dessincronizado, fundo escuro demais, cena parada, texto errado na tela ou personagem diferente do resto, e você quer arrumar só o que está errado.

Exemplo de quando digitar:

- `$corrigir` quando o áudio do vídeo final ficou atrás da imagem e você quer só remontar as cenas desalinhadas

Quando não serve: quando o vídeo tem problema em tudo e precisa ser refeito do zero, porque corrigir cena por cena sai mais caro que refazer. Nesse caso a skill avisa e sugere refazer com `$roteiro` e `$storyboard`.

O que a skill faz: ela identifica as cenas com problema, refaz só essas cenas com a correção pedida, remonta o vídeo com a mesma narração e a mesma sincronia por cena, e confere o resultado nos 6 inícios de cena antes de entregar. Ela nunca reedita a narração para caber no vídeo e nunca refaz cenas que já estavam certas.

## $tema

Pesquisa um tema a fundo antes de escrever o roteiro, validando se o tema rende vídeo e o que já existe sobre ele.

Use quando você tem um tema em mente e quer saber se ele tem fontes, se já foi feito por outro canal e qual ângulo ainda está livre, antes de gastar tempo com roteiro.

Exemplo de quando digitar:

- `$tema` com o tema que você pensou, para validar antes de pedir o roteiro

Quando não serve: quando você ainda não tem nenhum tema e quer ideias prontas. Nesse caso use `$ideias`.

O que a skill faz: ela busca 2 a 3 fontes confiáveis sobre o tema, confere o que os canais do nicho já fizeram sobre ele, aponta o ângulo livre e os fatos que precisam de confirmação, e diz se o tema rende vídeo longo, Short ou os dois. Ela nunca aprova um tema sem fonte nem recomenda tema que o canal já produziu.

## $fontes

Verifica as fontes dos fatos do roteiro, com 2 a 3 fontes por afirmação.

Use quando o roteiro já está escrito e você quer conferir cada fato antes de gravar, ou quando um fato parece bom demais e precisa de prova.

Exemplo de quando digitar:

- `$fontes` depois de aprovar o roteiro, para checar cada afirmação antes de gerar a narração

Quando não serve: quando ainda não existe roteiro, porque não há afirmação para verificar. Nesse caso escreva o roteiro com `$roteiro` primeiro.

O que a skill faz: ela lê cada afirmação do roteiro, busca 2 a 3 fontes confiáveis para cada uma, marca as que não têm fonte e as que têm fontes que discordam, e devolve o roteiro com a fonte de cada fato e o aviso do que não pode ser afirmado como verdade. Ela nunca inventa fonte e marca como não verificado o que não conseguiu confirmar.

## $template

Cria o template fixo do vídeo do canal, com estrutura, tempos, legenda, paleta e áudio padrão.

Use quando o canal já tem formato mãe e você quer que todo vídeo novo nasça com a mesma estrutura, sem redesenhar tudo do zero, ou quando a identidade dos vídeos está variando demais de um para o outro.

Exemplo de quando digitar:

- `$template` depois dos 3 primeiros vídeos, para fixar a estrutura que funcionou

Quando não serve: quando o canal ainda não tem formato mãe nem vídeo publicado, porque não há estrutura testada para fixar. Nesse caso use `$canal-dark` e produza os primeiros vídeos primeiro.

O que a skill faz: ela lê o formato mãe, a plataforma e a duração do perfil, fixa a estrutura com tempos de hook, capítulos, melhor momento e CTA, o estilo de legenda karaokê, a paleta e o padrão de áudio, e salva o template para o próximo vídeo começar dele. Ela avisa que o template não pode virar repetição genérica e que cada vídeo precisa variar em substância, como manda a regra de desmonetização.

## $backup

Faz o backup dos arquivos do canal: perfil, roteiros, narrações, vídeos e ideias usadas.

Use no fim da semana ou antes de qualquer mudança grande no canal, para nunca perder o trabalho feito.

Exemplo de quando digitar:

- `$backup` no fim da semana, para guardar uma cópia de tudo que foi produzido

Quando não serve: quando o canal ainda não tem nada produzido, porque não há nada para guardar. Nesse caso produza o primeiro vídeo primeiro.

O que a skill faz: ela lista o perfil do canal ativo, o diretório inteiro de perfis, os roteiros, as narrações, os vídeos finais, as thumbnails, a logo e o banner, e os arquivos de nomes e ideias usadas, confere que cada arquivo existe e registra a cópia com a data. Ela nunca apaga o original e avisa quando algum arquivo do registro sumiu.

## $automatizar

Liga a automação de conteúdo do canal ativo: pergunta a plataforma e a agenda, roda o teste de postagem com 1 vídeo manual e só depois liga a produção e a postagem no calendário, sem você pedir cada etapa.

Use quando o canal já tem fila de vídeos com roteiros prontos e você quer que a produção e a postagem aconteçam no calendário fixo do canal, com produção de manhã e postagem no horário marcado.

Exemplo de quando digitar:

- `$automatizar` para configurar a automação do canal ativo do zero, com plataforma, agenda e teste de postagem
- `$automatizar` para retomar a fila depois que os clipes de um vídeo falharam e deixar o vídeo pronto para o próximo dia de postagem

Quando não serve: quando o vídeo da vez ainda não tem roteiro aprovado, porque a automação produz a partir do roteiro pronto e não inventa tema na hora. Nesse caso escreva o roteiro com `$roteiro` primeiro. Também não serve quando você quer publicar um vídeo avulso fora do calendário, porque a automação segue a fila e os horários fixos. Nesse caso use `$publicar`. Também não serve quando o teste de postagem ainda não foi feito, porque a automação só liga depois de 1 vídeo postado manualmente com `$publicar`.

O que a skill faz: ela pergunta a plataforma e o modelo de agenda antes de ligar qualquer coisa, mostra o resumo da configuração para você confirmar e roda o teste de postagem com 1 vídeo manual antes de automatizar. Depois de confirmado, ela lê a fila em [automação](automacao.md), produz o próximo vídeo na ordem da fila com o pipeline completo e posta no horário do calendário. Ela nunca posta vídeo com clipes faltando, áudio fora de sincronia ou sem legenda. Se os clipes falharem, ela tenta de novo mais tarde no mesmo dia e, se continuar falhando, deixa para o dia seguinte e avisa. Se o login falhar, ela para e avisa, sem repetir tentativas. Se a postagem falhar por captcha, desafio de login ou erro de upload, ela para, mantém o vídeo pronto e avisa com o erro exato, sem repetir o upload em loop. A automação agendada pertence ao canal para o qual foi criada e não muda quando você troca o perfil ativo: cada canal tem sua própria agenda e sua própria fila. Leia a exceção em [perfis](perfis.md).

## Resumo rápido

- `$canal-dark` começa ou continua o canal
- `$canais` mostra os canais criados e deixa trocar o perfil ativo
- `$help` mostra esta lista a qualquer momento
- `$ideias` mostra ideias de vídeo para o canal que já existe
- `$nomes` mostra 5 nomes novos sem repetir os já sugeridos
- `$roteiro` escreve o roteiro do próximo vídeo do canal que já existe
- `$revisar` diagnostica o roteiro aprovado antes de produzir
- `$storyboard` monta o storyboard do roteiro aprovado antes de gerar os clipes
- `$personagem` cria a ficha do personagem para manter ele igual em todos os clipes
- `$teste` produz 1 clipe de teste para aprovar antes do vídeo inteiro
- `$thumbnail` cria título e thumbnail ou capa do vídeo
- `$publicar` guia a publicação e a medição do vídeo
- `$status` mostra o perfil salvo e o que já foi feito
- `$voz` escolhe e testa a voz da narração
- `$legenda` escolhe o estilo da legenda e confere a legenda queimada
- `$capa` cria a capa do vídeo vertical para TikTok e Shorts
- `$musica` escolhe a música e os efeitos sonoros do vídeo
- `$plano` mostra o plano dos 10 primeiros vídeos e onde o canal está
- `$concorrentes` estuda os concorrentes do nicho antes do roteiro
- `$referencia` disseca um vídeo de referência quadro a quadro antes de produzir
- `$titulo` gera 5 opções de título para um vídeo
- `$short` adapta um vídeo longo do YouTube para Short
- `$stats` mede o resultado dos vídeos publicados e diz o que mudar
- `$monetizar` confere se o canal já pode monetizar e o que falta para liberar
- `$logo` cria a logo do canal para usar como foto de perfil
- `$banner` cria a arte do banner do canal no YouTube
- `$descricao` escreve a descrição do canal
- `$gancho` gera 5 opções de gancho para um vídeo
- `$agenda` monta o calendário de postagens do canal
- `$nicho` troca o nicho do canal sem trocar o nome
- `$serie` planeja uma série de vídeos sobre um tema
- `$audio` revisa o áudio de um vídeo pronto
- `$efeitos` monta o banco de efeitos sonoros do vídeo
- `$intro` cria a intro e o outro do canal
- `$checklist` roda o checklist de pré-publicação do vídeo
- `$corrigir` corrige um problema específico do vídeo pronto sem refazer tudo
- `$tema` pesquisa um tema a fundo antes do roteiro
- `$fontes` verifica as fontes dos fatos do roteiro
- `$template` cria o template fixo do vídeo do canal
- `$backup` faz o backup dos arquivos do canal
- `$automatizar` configura a automação do canal ativo com plataforma, agenda e teste de postagem e depois produz e posta os vídeos da fila no calendário
- `$portoes` roda todos os portões de qualidade de uma vez no vídeo final e devolve aprovados e reprovados
- `$varredura` roda o blackdetect e o freezedetect no vídeo final e devolve os trechos com problema e o LUFS medido
