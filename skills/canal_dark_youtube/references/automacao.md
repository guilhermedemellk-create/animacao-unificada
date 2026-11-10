# Automação de conteúdo

A automação produz e posta os vídeos da fila no calendário do canal, sem você pedir cada etapa. O comando `$automatizar` liga este sistema. A automação vale para qualquer canal da skill, em qualquer plataforma, e cada canal tem sua própria agenda e sua própria fila.

## O que a automação faz

- Produz o próximo vídeo da fila na manhã do dia da postagem, com o pipeline completo do canal.
- Posta o vídeo no horário do calendário, na plataforma do canal.
- Avisa você com o link do vídeo publicado e com o erro exato quando alguma etapa falha.
- Move o vídeo para o próximo dia de postagem quando o dia passa sem o vídeo ficar pronto, sem furar a fila.

## O que a automação não faz

- Deixe o roteiro pronto antes de ligar, porque a automação não inventa tema na hora e só produz a partir do roteiro aprovado.
- Publique vídeo avulso fora do calendário com `$automatizar`, porque a automação segue a fila e os horários fixos. Use `$publicar` para o vídeo avulso.
- Resolva captcha ou desafio de login sozinha, porque só você resolve no navegador.
- Troque de conta sozinha, porque a conta certa precisa ser confirmada antes de subir o vídeo.

## Antes de ligar

- Ative o perfil do canal que vai automatizar com `$canais`, porque a automação pertence a esse canal.
- Monte a fila com roteiros aprovados, porque a automação produz em ordem e nunca pula um vídeo sem você pedir.
- Escolha a voz fixa da narração com `$voz`, porque a automação usa a mesma voz em todos os vídeos.
- Faça o teste de postagem com 1 vídeo manual, porque a automação só liga depois do teste aprovado. Leia a seção de teste de postagem abaixo.
- Verifique o login da conta do canal no navegador, porque a postagem só acontece com login verificado.

## Configuração guiada

O `$automatizar` nunca liga nada antes de perguntar. Siga as perguntas nesta ordem.

- Pergunte a plataforma do canal: TikTok, YouTube longo, YouTube Shorts ou os dois.
- Pergunte o modelo de agenda: 3 vezes por semana, 1 vez por dia ou 2 vezes por dia. Leia os modelos de agenda abaixo.
- Pergunte os dias, os horários e o fuso horário da postagem.
- Pergunte quantos roteiros já estão prontos na fila e qual é o próximo vídeo.
- Mostre o resumo da configuração com plataforma, dias, horários, fuso e próximo vídeo e peça a confirmação antes de ligar.
- Rode o teste de postagem com 1 vídeo manual e só ligue os crons depois do teste aprovado.
- Registre a configuração no arquivo de estado da automação do canal, com plataforma, agenda, horários e fila, para a automação saber o que produzir e quando postar.

## Modelos de agenda prontos

Escolha um modelo na configuração guiada e ajuste os dias e horários com o usuário. Produza o vídeo na manhã do dia da postagem e produza com antecedência sempre que der, para a postagem não depender de uma geração na última hora.

### 3 vezes por semana

- Poste segunda, quarta e sexta, sempre no mesmo horário. Exemplo: segunda às 19h, quarta às 20h e sexta às 20h.
- Use este modelo para começar um canal novo ou para manter a constância sem produzir todo dia.
- Deixe 1 dia de folga entre as postagens para refazer um vídeo que falhar sem furar a fila.

### 1 vez por dia

- Poste todo dia no mesmo horário. Exemplo: todo dia às 18h.
- Use este modelo quando a fila já tem roteiros prontos para a semana inteira.
- Produza o vídeo do dia seguinte na véspera sempre que der, para não acumular produção na manhã.

### 2 vezes por dia

- Poste 2 vezes por dia em horários fixos. Exemplo: às 12h e às 21h, todos os dias.
- Use este modelo só quando a produção aguenta o ritmo, porque são 14 vídeos por semana.
- Mantenha 2 roteiros prontos na frente da fila, porque um atraso derruba as 2 postagens do dia.

## Como a automação produz cada vídeo

Siga as etapas nesta ordem para cada vídeo da fila.

- Escreva e aprove o roteiro com `$roteiro` antes de qualquer produção.
- Revise o roteiro aprovado com `$revisar` antes de gerar os clipes.
- Monte o storyboard com `$storyboard` e aprove 1 clipe de teste com `$teste` antes de produzir o vídeo inteiro.
- Gere a narração com a voz fixa do canal e confira a duração de cada narração nova, porque a velocidade não é linear e o mesmo ajuste muda a duração de forma diferente a cada texto. Ajuste a velocidade até a narração caber no limite de duração da plataforma.
- Gere os clipes na trilha do canal e nunca monte o vídeo com clipes faltando.
- Monte o vídeo com a sincronia por cena a partir da transcrição real da narração, com a duração real da fala de cada cena. Nunca use escala uniforme no vídeo inteiro para casar a duração total.
- Queime as legendas a partir da transcrição real, no estilo de legenda do canal.
- Mixe o áudio no alvo de menos 14 LUFS.
- Verifique a sincronia em 6 inícios de cena espalhados pelo vídeo antes de liberar para postagem.
- Rode o checklist de pré-publicação com `$checklist` e os portões de qualidade com `$portoes` antes de postar. Leia os portões em [portões de qualidade](portoes-qualidade.md).

## Postagem por plataforma

### TikTok

- Poste pelo navegador, na página de upload do TikTok, com o login salvo da conta do canal.
- Saiba que o TikTok não tem postagem por API para conta comum, então a postagem sempre passa pelo navegador.
- Use descrição curta, 2 a 3 hashtags e a capa escolhida por frame.
- Confira o vídeo publicado depois de subir e avise o usuário com o link.

### YouTube longo e Shorts

- Poste pelo YouTube Studio no navegador, com o login salvo da conta do canal.
- Use thumbnail 1280x720, título, descrição com fontes e tags no vídeo longo.
- Use vídeo vertical 9:16 e capa na grade do canal no Shorts.
- Publique na hora ou agende a publicação no Studio para o horário do calendário.
- Confira o vídeo publicado depois de subir e avise o usuário com o link.

### O que cada plataforma permite

- Agende a publicação no YouTube Studio quando quiser subir antes e estrear no horário marcado.
- Saiba que o TikTok pelo navegador não posta por API e depende do login salvo e da sessão ativa no navegador.
- Confira a conta logada antes de subir em qualquer plataforma, porque o vídeo vai para a conta que está logada.

## Checklist de verificação antes de postar

Rode este checklist em toda postagem, manual ou automática. Se um item falhar, não poste.

- Confira que o arquivo final do vídeo existe e que a duração e a resolução conferem com a plataforma.
- Confira que todos os clipes estão no vídeo e que nenhum trecho está preto ou congelado.
- Confira que a sincronia de áudio foi verificada em 6 inícios de cena.
- Confira que a legenda queimada está no vídeo e legível.
- Confira que o áudio está no alvo de menos 14 LUFS.
- Confira que a descrição, as hashtags e a capa estão prontas.
- Confira que a conta logada no navegador é a conta do canal.
- Rode `$checklist` e `$portoes` e só libere a postagem com os dois aprovados.

## Teste de postagem

- Poste 1 vídeo manualmente com `$publicar` antes de ligar a automação.
- Use o teste para confirmar o login, a conta certa, a descrição, as hashtags e a capa.
- Só ligue a automação depois do teste aprovado pelo usuário.
- Repita o teste quando trocar de plataforma ou de conta, porque o teste vale para a combinação de plataforma e conta testada.

## Regras de segurança

- Poste só vídeo verificado pronto, com sincronia verificada em 6 cenas e checklist de pré-publicação aprovado.
- Poste só com login verificado no navegador.
- Confirme a conta certa antes de subir qualquer vídeo.
- Pare na primeira falha e avise o usuário com o erro exato.
- Nunca poste vídeo com clipes faltando, áudio fora de sincronia ou sem legenda.
- Nunca use senha escrita no chat. A senha só entra pelo fluxo do Cofre Seguro.
- Nunca crie conta nova nem troque a senha sem o usuário pedir.
- Lembre que a automação agendada pertence ao canal para o qual foi criada e não muda quando você troca o perfil ativo. Cada canal tem sua própria agenda e sua própria fila. Leia a exceção em [perfis](perfis.md).

## Solução de problemas

### Login bloqueado por limite de frequência

- Pare todas as tentativas de login na hora.
- Espere o bloqueio expirar, sem tentar de novo, porque cada tentativa nova prolonga o bloqueio.
- Avise o usuário que o login está bloqueado e que o vídeo fica pronto para postagem manual.
- Só tente o login de novo depois que o usuário confirmar que o bloqueio passou.

### Captcha ou desafio de login

- Pare e avise o usuário com o que apareceu na tela.
- Nunca tente resolver o captcha em loop, porque as tentativas repetidas viram bloqueio.
- Deixe o usuário resolver o desafio no navegador dele e confirme o login depois.

### Código de verificação por e-mail

- Peça o código ao usuário quando a plataforma pedir.
- Nunca invente um código e nunca use um código de outro login.
- Avise o usuário quando o código expirar e peça um código novo.

### Conta errada logada

- Pare antes de subir qualquer vídeo.
- Avise o usuário qual conta está logada e qual conta é a do canal.
- Só poste depois que a sessão estiver na conta certa, confirmada na tela do perfil.

### Upload falhou

- Mantenha o vídeo pronto e avise o usuário com o erro exato.
- Nunca repita o upload em loop.
- Poste manualmente depois, no mesmo dia ou no próximo dia de postagem.

### Clipes falharam na geração

- Tente de novo mais tarde no mesmo dia, com intervalos espaçados.
- Deixe a produção para o dia seguinte quando continuar falhando e avise o usuário.
- Nunca monte o vídeo com clipes faltando.

### Narração passou do limite de duração

- Ajuste a velocidade da narração e meça a duração de novo.
- Gere a narração de novo quando o ajuste não resolver, porque cortar a fala no meio quebra o roteiro.

## Quando a automação falha

- Avise o usuário com o erro exato e com o que já está pronto.
- Deixe o vídeo pronto para postagem manual, com arquivo final, descrição, hashtags e capa.
- Mova o vídeo para o próximo dia de postagem quando o dia passar sem o vídeo ficar pronto, sem furar a fila.
- Nunca repita tentativas de login, de captcha ou de upload em loop para compensar a falha.

## Exemplo real: O Mundo das Descobertas

A primeira automação da skill foi a do canal O Mundo das Descobertas, no TikTok, com 3 vídeos por semana: segunda às 19h, quarta às 20h e sexta às 20h, no fuso America/Sao_Paulo. O arquivo de estado dessa automação fica em `~/workspace/goals/o-mundo-das-descobertas-channel/hidden_files/automacao-status.md`, com fila, agenda e histórico de execuções.

A lição desse caso é que o login do TikTok foi bloqueado por limite de frequência em novembro de 2026, depois de tentativas repetidas e de um captcha de slider. A automação parou, não tentou o login de novo e deixou os vídeos prontos para postagem manual. A regra que nasceu daí vale para todos os canais: postagem só com vídeo verificado pronto e login verificado, e qualquer falha vira aviso com postagem manual, nunca loop de tentativas.
