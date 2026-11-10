# Movimento profissional, a doutrina que une as trilhas

Use este guia quando o movimento parecer amador mesmo com desenho bonito. Ele vale para as 4 trilhas animadas e para a variante de histórias 2D. O formato mãe é o Short vertical 1080x1920 a 60 fps. Cada seção traz a skill de origem com o repositório. Leia a técnica na origem quando precisar do detalhe. Não copie listas inteiras das origens. Adapte cada número ao vertical e à narração real do canal.

- Aplique uma seção por vez em cada cena. Uma cena que cumpre a lei do vetor e tem um carrier já parece profissional.
- Confira o movimento no teste do mudo antes de aprovar. Pausar em qualquer segundo tem que mostrar algo no meio do voo.
- Mantenha a sincronia com os tempos reais da narração. Nenhuma regra deste guia autoriza escala uniforme no vídeo inteiro.

## A lei do vetor nas costuras e a regra do sinal Z

Origem: motion-doctrine em https://github.com/heygen-com/hyperframes

- Defina como a cena A sai antes de desenhar como a cena B entra. A saída manda na entrada.
- Mantenha o mesmo eixo dos dois lados do corte. O eixo x continua x, o eixo y continua y e o eixo Z continua Z. Nunca troque de eixo no corte.
- Preserve a direção sem espelhar. Uma saída para a esquerda pede uma entrada vindo da direita no mesmo eixo.
- Trate o sinal Z pela escala. Crescer é empurrar a câmera para frente e encolher é puxar a câmera para trás. Uma saída que encolhe respondida por uma entrada que cresce do pequeno é um vetor espelhado e é a violação mais comum, porque crescer do pequeno é a entrada padrão dos elementos.
- Case a velocidade da entrada com a velocidade final da saída. Use easings espelhados, como saída em power4.in e entrada em power4.out, com a mesma distância e a mesma duração.
- Corte no meio do movimento dos dois lados. Assentar antes do corte ou começar parado depois do corte é um tempo morto.
- Escreva o mapa de vetores antes de animar. Anote por costura o tempo do corte, o vetor de saída e o vetor de entrada com eixo e direção assinada. Corrija o plano quando uma linha divergir e nunca corrija só o easing.
- Reabra a auditoria da costura quando mudar o primeiro ou o último segundo de uma cena, incluindo retempo por narração nova.

## A corrente, uma direção dominante

Origem: motion-doctrine em https://github.com/heygen-com/hyperframes

- Escolha uma direção dominante por vídeo e use ela em todas as costuras comuns. O padrão da origem é para a esquerda, que marca progresso neutro para o próximo beat.
- Reserve os outros vetores para significados fixos. Subir marca elevação ou revelação, avançar em Z marca mergulho no mesmo pensamento, recuar em Z marca chegada de algo maior e explodir para fora marca saída de um mundo.
- Evite costuras consecutivas em direções opostas. O pingue-pongue lê como erro.
- Justifique toda mudança de direção com uma causa visível, como um clique, um impacto ou uma fronteira de capítulo.
- Gaste um vetor reservado só quando o significado pedir. Variedade sem motivo quebra a corrente.

## Carriers, o olho segue objetos e o crossfade é proibido

Origem: motion-doctrine em https://github.com/heygen-com/hyperframes

- Entregue um objeto concreto através do corte. O carrier é o cursor no meio do caminho, o container que encolhe e encaixa no próximo layout, a marca que voa para o lugar exato ou o grupo de palavras da entrada em cascata.
- Case posição e velocidade do carrier dos dois lados do corte. Sem carrier natural, use os heróis da cena com viagem parcial e fade antecipado e entre no meio do voo.
- Proíba o crossfade entre cenas. Ele não tem carrier nenhum e mata o impulso do olhar.
- Use no máximo 2 a 3 transições entre cenas por vídeo e repita elas. A fronteira padrão é o corte na curva na direção da corrente.
- Trate morphs de elemento compartilhado como exceção ao orçamento de transições, porque eles são o carrier em si.

## Movimento causal, o efeito começa no frame da causa

Origem: motion-doctrine em https://github.com/heygen-com/hyperframes

- Encadeie cada movimento a partir do anterior. Clique vira squash, squash vira mola, mola vira voo, voo vira impacto, impacto vira recuo e recuo vira revelação.
- Comece o efeito no mesmo frame da causa. Nunca deixe o efeito para logo depois.
- Escale a reação com a massa implícita. Elementos grandes rebatem devagar e elementos pequenos estalam rápido.
- Trate toda força como licença para mudar de direção. Uma virada sem causa é pingue-pongue.
- Coloque um som no frame da causa. O som marca a fronteira que o corte marcaria.

## Banimento de idle wobble

Origem: motion-doctrine em https://github.com/heygen-com/hyperframes

- Proíba loops senoidais de espera como movimento sustentado. Respirar, flutuar, derivar e pulsar leem como vídeo esperando.
- Trate a cena que termina a entrada com segundos sobrando como erro de planejamento. Adicione história e nunca adicione wobble.
- Atribua uma rota de sustentação a cada fase entre entrada e saída e nomeie a rota no plano. As rotas são revelações encenadas, câmera com intenção, vida sequenciada de interface, sequências animadas e ação guiada por cursor.
- Segure conteúdo para pagar nos beats da narração quando houver 2 ou mais grupos de conteúdo. O quadro continua ganhando informação.
- Mapeie um caminho de câmera com intenção quando a cena for estática. Estabeleça aberto, viaje e chegue no assunto.
- Faça o produto se comportar no tempo quando a cena for de interface. O progresso avança, o destaque anda e o contador marca.
- Teste pausando em qualquer segundo. Algo significativo tem que estar no meio do voo, como uma revelação pousando, a câmera viajando ou a interface fazendo o que a narração diz.

## Stillness before climax, a pausa de 0,3 a 0,75 s

Origem: motion-doctrine em https://github.com/heygen-com/hyperframes

- Programe uma pausa de 0,3 a 0,75 segundo entre a ação maior e o resultado dela. A pausa é a vírgula dramática.
- Evite pular direto da ação para o resultado. Sem a pausa, o clímax perde o peso.
- Use a pausa para segurar o olhar no quadro antes do payoff. O espectador sente que algo vai acontecer.
- Meça a pausa a partir dos tempos reais da narração. Dê à linha um tempo maior depois dela quando a imagem precisar de tempo para pousar, como numa contagem, numa legenda ou no silêncio antes do payoff.

## Arquétipos de movimento com números fechados e a regra 1/3

Origem: motion-design em https://github.com/LottieFiles/motion-design-skill

- Escolha um arquétipo por canal e aplique ele sempre. Nunca misture arquétipos no mesmo vídeo.
- Use Playful para mascote e ilustração leve. Duração de 150 a 300 ms, easing ease-out-back e overshoot de 10 a 20 por cento.
- Use Premium para produto e marca elegante. Duração de 350 a 600 ms, easing cubic-bezier(0.4, 0, 0.2, 1) e overshoot de 0 por cento.
- Use Corporate para explicação limpa e painel de dados. Duração de 200 a 400 ms, easing cubic-bezier(0.2, 0, 0, 1) e overshoot de 0 a 3 por cento.
- Use Energetic para gancho e ritmo rápido. Duração de 100 a 250 ms, easing ease-out-expo e overshoot de 15 a 30 por cento.
- Fixe a identidade de movimento do canal em 3 constantes. Uma curva assinatura para 80 por cento das animações, uma paleta de 3 durações com rápido, padrão e lento, e um padrão único de entrada.
- Aplique a regra 1/3 da distância. Nenhum movimento viaja mais de 1/3 da tela sem uma mudança de keyframe no meio.
- Aplique a regra 1/3 dos elementos. Com 3 ou mais elementos, no máximo 1/3 deles se move ao mesmo tempo.
- Respeite a hierarquia de camadas. A camada primária carrega a ação principal, a secundária dá riqueza de apoio e a ambiente dá vida de fundo. Animação plana é camada faltando.

## Os 12 princípios da Disney como lente de revisão

Origem: disney-animation-rule-skill em https://github.com/vibe-motion/skills

- Trate esta seção como síntese com as próprias palavras. A origem não tem arquivo de licença e o repositório não é mantido, então não copie trechos literais longos dela.
- Selecione o menor conjunto de princípios que resolve o problema percebido. Nunca force os 12 princípios em cada cena.
- Descreva a ação em uma frase antes de animar. Sujeito, intenção, força, destino e sensação desejada.
- Bloqueie as fases semânticas antes de escolher curvas de easing. Repouso, antecipação, lançamento, passagem, ápice, contato, overshoot e assentamento, adaptados à ação.
- Ordene a construção do movimento. Primeiro preserve função, contatos e limites, depois deixe o caminho principal legível com formas simples, depois some poses e deformação nos eventos de força e contato.
- Derive o secundário do primário. Deformação, atraso de extremidades, acentos e efeitos nascem do movimento principal ou do evento semântico, nunca sozinhos.
- Ajuste timing e spacing em quadros representativos e revise o movimento inteiro depois.
- Remova efeitos que escondem pose fraca, timing confuso, contato quebrado ou silhueta ilegível.
- Use os 12 princípios da skill em [animação](animacao.md) como referência de aplicação por trilha. Esta seção é a lente de revisão e a outra é o manual de aplicação.

## Vocabulário de 192 movimentos numerados

Origem: motion-prompt em https://github.com/showheyohtaki/motion-prompt

- Abra a galeria pública em https://showheyohtaki.github.io/motion-prompt/ quando precisar nomear um movimento. A galeria tem 192 movimentos numerados com amostra animada, especificação de tempos e easing, e código Canvas 2D sem dependências.
- Cite o movimento pelo número, como #012, e nunca só pelo nome. O número é a referência precisa.
- Linke a galeria e não copie a lista para dentro da skill. A lista muda com pacotes novos e a cópia desatualiza.
- Busque por palavras quando não souber o nome. A busca aceita inglês e japonês e filtra por pacote, como motion para títulos e texto, camera para movimentos de câmera e ui para partes de interface.
- Porte só os movimentos escolhidos e mantenha os números originais no código, como duração, atraso, easing, overshoot, distância e ângulo. Troque só o conteúdo mostrado e a paleta.
- Carregue a linha de atribuição MIT de cada elemento e de cada kit para o arquivo onde o código for parar. A licença MIT pede essa atribuição.
- Adapte o movimento ao vertical 1080x1920 e aos 60 fps do canal. Um movimento de galeria em 16:9 não cabe no vertical sem reenquadrar.
- Avise quando o movimento for para modelo de vídeo e não para código. Nesse caso escreva o prompt em frases a partir do nome em inglês e das linhas de especificação, com o que se move, em que ordem, por quanto tempo e onde termina, e diga que o resultado fica próximo do elemento e não exato.

## GSAP, easings, stagger para karaokê, timelines com labels e defaults do canal

Origem: gsap-core e gsap-timeline em https://github.com/greensock/gsap-skills

- Porte os easings do GSAP como funções puras de quadro no renderFrame(n). O GSAP não roda dentro do render determinístico, então o que viaja é a curva e não a biblioteca.
- Use power2.out como easing padrão de entradas. Use power3.inOut para morphs e transições suaves. Use back.out(1.7) para entradas de título com overshoot. Use power4.in na saída espelhada com power4.out na entrada.
- Evite bounce.out e elastic.out em entradas. O overshoot de back.out entre 1.4 e 1.7 é o limite aceito.
- Aplique stagger para revelar as palavras do karaokê, as letras do título e os itens de lista em cascata. Use cada de 0,08 a 0,1 segundo entre palavras e from center para títulos.
- Nomeie os beats da narração com labels na timeline. Gancho, revelação, virada e CTA viram labels com tempo, e a revisão busca direto pelo label em vez de caçar quadros.
- Monte uma timeline mãe por vídeo de 60 segundos com uma timeline filha por cena. A arquitetura é a mesma do formato mãe em partes.
- Fixe os defaults do canal com gsap.defaults. Duração de 0,5 segundo e ease power2.out para todos os tweens, salvo exceção nomeada no plano.
- Anime só transforms com x, y, scale, rotation e xPercent. Nunca anime width, height, top ou left, porque eles recalculam layout e derrubam os 60 fps.
- Prefira autoAlpha a opacity. O autoAlpha esconde o elemento de verdade ao chegar a 0 e evita elemento invisível bloqueando clique.
- Sobreponha entradas com posição relativa em vez de encadear delays frágeis. O texto entra 0,2 segundo antes do fim do movimento anterior.
- Guarde o retorno do tween para pausar, buscar e matar. Buscar por tempo é o que viabiliza a sincronia com os segundos reais da narração.

## Coreografia de logo e intro com proporção 20 por cento, 50 por cento e 30 por cento

Origem: pixel2motion em https://github.com/nolangz/pixel2motion

- Estruture o logo em partes semânticas antes de animar. Um elemento por parte com id estável, como marca, wordmark e ponto, e pathLength 1 para draw-on.
- Simplifique a geometria até ela virar animável. Um logo de 3 partes anima limpo e um traço com 400 pontos em escada não coreografa.
- Divida a coreografia em 20 por cento de antecipação, 50 por cento de ação e 30 por cento de follow-through. A antecipação prepara, a ação entrega e o follow-through assenta.
- Aplique stagger de 10 a 20 por cento entre as partes. As partes entram em cascata e nunca todas juntas.
- Feche sempre no Contrato do Quadro Final. A animação pousa exatamente no vetor estático aprovado, sem desvio de posição, escala ou cor.
- Escreva cubic-bezier literal dentro de keyframes. A variável de token dentro de keyframes é descartada em silêncio pelo Chromium e vira easing linear.
- Confira a suavidade com zoom de 200 a 400 por cento. Nenhuma borda suave sai em escada, mesmo com boa similaridade de área.
- Use a mesma coreografia no selo de 1 segundo depois do gancho, na intro e no outro. A assinatura de movimento é parte da identidade do canal.
- Documente a coreografia por canal com palavras de personalidade, princípios usados e tabela de timeline. O documento vira o motion spec do canal.

## Checklist de movimento por clipe

Origem: remotion-motion-graphics em https://github.com/fernandokaraka/remotion-motion-graphics-skill

- Complete entrar, segurar e sair dentro da duração do clipe. Nada aparece no quadro 0 e nada continua se movendo no último quadro. Reserve a saída dentro da duração.
- Comece com spring e nunca com movimento linear. A mola dá antecipação, overshoot e assentamento. Use easing só quando a mola não servir.
- Dê stagger de 6 a 10 quadros a 60 fps nas entradas e nas saídas, na mesma ordem. Entradas juntas parecem erro de montagem.
- Mantenha vida no hold sem wobble. Use flutuação suave, brilho lento ou varredura de luz, sentido e não notado.
- Coloque o payoff no momento chave. Pop de escala, anel, brilho e som caem juntos no beat da narração.
- Confira stills nos quadros chave antes do render completo. Meio da entrada, payoff, meio do hold e meio da saída, lidos em tamanho real.
- Diagnostique antes de decorar. Um gráfico sem graça costuma ser um defeito real, como interpolação sem clamp exibindo número errado, e não falta de molas.
- Respeite as margens de segurança de 5 a 10 por cento e uma sombra atrás do texto sobre imagem. Um único elemento focal fica em negrito e textos longos encolhem e quebram em vez de estourar.
- Corte o silêncio inicial do arquivo de áudio. Cerca de 80 ms de ar morto no começo deixam o áudio 80 ms atrasado e simulam dessincronia.

## Onde cada técnica entra por trilha

Use este mapa para aplicar a doutrina certa na trilha certa. Nenhuma técnica deste guia autoriza escala uniforme no vídeo inteiro e nenhuma dispensa o checklist de aceite da trilha em [animação](animacao.md).

- Aplique a lei do vetor e o mapa de vetores nas costuras das trilhas realista e Pixar por IA, porque o corte entre clipes gerados é onde o impulso do olhar mais morre. Escreva o mapa antes de gerar e reabra a auditoria quando mudar o primeiro ou o último segundo de uma cena.
- Aplique os carriers nas trilhas realista e Pixar por IA e na variante de histórias 2D. Use o cursor, o container e a marca como carrier e proíba o crossfade entre cenas em todas as trilhas.
- Aplique a corrente com direção dominante para a esquerda nas trilhas realista, Pixar por IA e 2D por código. Reserve subir para revelação, avançar em Z para mergulho no mesmo pensamento e explodir para fora para saída de um mundo.
- Aplique o movimento causal nas 4 trilhas animadas. Comece o efeito no mesmo frame da causa, com o som no frame da causa, e escale a reação com a massa implícita do elemento.
- Aplique o banimento de idle wobble nas 4 trilhas animadas. Dê uma rota de sustentação nomeada a cada fase entre entrada e saída e nunca preencha tempo parado com loop senoidal.
- Aplique a pausa de stillness before climax de 0,3 a 0,75 segundo nas trilhas realista, Pixar por IA e 2D por código, entre a ação maior e o resultado dela, medida a partir dos tempos reais da narração.
- Aplique os arquétipos com números fechados por canal, com 1 arquétipo por vídeo e nunca misturados. Use Playful para mascote, Premium para produto, Corporate para painel de dados e Energetic para gancho. Fixe a curva assinatura, a paleta de 3 durações e o padrão único de entrada do canal.
- Aplique os easings GSAP como funções puras de quadro na variante de histórias 2D e no infográfico 2D, com power2.out nas entradas, power3.inOut nos morphs, back.out(1.7) nos títulos e stagger de 6 a 10 quadros. Use a mesma tabela de easings para escrever os prompts de movimento das trilhas realista e Pixar, com o easing descrito em palavras no prompt.
- Aplique o vocabulário de 192 movimentos numerados quando precisar nomear um movimento. Cite o movimento pelo número e porte só os números escolhidos, com duração, atraso, easing, overshoot, distância e ângulo. Adapte o movimento ao vertical 1080x1920 e aos 60 fps do canal.
- Aplique a coreografia de logo com proporção 20 por cento, 50 por cento e 30 por cento no selo de 1 segundo depois do gancho, na intro e no outro, com a mesma coreografia nas 3 aparições.
- Aplique o checklist entrar, segurar e sair em cada cena das 4 trilhas animadas, com payoff no beat da narração e stills nos quadros chave conferidos em tamanho real antes do render completo.
- Aplique os portões de [portões de qualidade](portoes-qualidade.md) no fim de cada trilha, com o portão de ação visível, o portão de sincronia em 6 inícios de cena e a varredura de quadros pretos e congelados. Portão reprovado para a produção e volta para a etapa dele.
