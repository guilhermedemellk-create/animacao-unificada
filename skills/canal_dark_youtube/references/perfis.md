# Perfis de canal — vários canais na mesma skill

A skill opera um canal por vez, mas guarda vários perfis. O usuário cria um canal novo sem apagar os outros e troca o canal ativo quando quiser. A lista de canais é só local, da máquina da pessoa. Nada é compartilhado nem enviado para lugar nenhum.

## Onde fica cada coisa

- `~/workspace/your_files/canal-dark-perfis/` — um arquivo por canal, com o nome do canal em minúsculas e hífens. O arquivo do O Mundo das Descobertas é `o-mundo-das-descobertas.md`.
- `~/workspace/your_files/canal-dark-perfil.md` — o perfil ATIVO. É uma cópia exata do arquivo do canal ativo no diretório de perfis. Todos os comandos da skill e a automação leem este arquivo e continuam funcionando sem mudar nada.
- `~/workspace/your_files/canal-dark-perfil-ativo.txt` — uma linha só, com o nome do arquivo do perfil ativo, sem a extensão. Serve para o comando `$canais` saber qual canal está ativo sem adivinhar pelo conteúdo.

## Trocar o perfil ativo

- Copie o arquivo do canal escolhido por cima de `~/workspace/your_files/canal-dark-perfil.md`.
- Escreva o nome do arquivo do canal escolhido em `~/workspace/your_files/canal-dark-perfil-ativo.txt`.
- Confira que a cópia ficou idêntica ao arquivo de origem antes de continuar.
- Nunca edite o perfil ativo direto sem copiar a mudança de volta para o arquivo do canal no diretório de perfis. O arquivo do diretório é a fonte da verdade e o perfil ativo é só a cópia em uso.

## O canal ativo manda em todos os comandos

- O canal escolhido no `$canal-dark` vira o canal ativo e TODOS os comandos passam a valer para ele: `$status`, `$roteiro`, `$ideias`, `$plano`, `$agenda`, `$logo`, `$publicar` e os demais. Cada comando lê o perfil ativo e trabalha com o nicho, o formato, a voz e a trilha dele.
- Se o usuário trocar de canal no `$canal-dark` ou no `$canais`, todos os comandos passam a valer para o canal novo, sem precisar refazer nada. O canal antigo continua guardado no diretório de perfis, com tudo o que já foi feito para ele.
- A única exceção é a automação agendada, descrita na seção de compatibilidade abaixo.

## Criar um canal novo

- Rode a entrevista normal de `$canal-dark` e salve as respostas num arquivo novo no diretório de perfis, com o nome do canal em minúsculas e hífens.
- Ative o canal novo na hora: copie o arquivo novo por cima do perfil ativo e atualize o apontador.
- Nunca apague nem sobrescreva o perfil de outro canal ao criar um novo. O passo antigo de fazer backup manual do perfil por cima do arquivo único acabou.
- Registre o nome novo em `~/workspace/your_files/canal-dark-nomes-usados.md`, como já manda a regra de nomes.
- O arquivo de ideias já usadas continua único e global em `~/workspace/your_files/canal-dark-ideias-usadas.md`. Uma ideia usada num canal não é sugerida de novo em outro canal.

## O fluxo do $canal-dark com vários perfis

- Sem nenhum perfil, `$canal-dark` começa a entrevista de abertura do zero.
- Com pelo menos um perfil, `$canal-dark` mostra primeiro os perfis existentes para o usuário escolher qual continuar, mais a opção "Criar um canal novo".
- Escolher um perfil o torna ativo e mostra o resumo dele: nome, @, nicho, plataforma, formato mãe, voz e onde o canal parou.
- Criar um novo roda a entrevista normal e salva o perfil novo sem apagar os outros.
- Com um pedido junto, como `$canal-dark quero um vídeo novo`, o pedido vale para o perfil ativo depois da escolha. Se o usuário já disse qual canal quer continuar, não pergunte de novo.

## O comando $canais

- `$canais` lê o diretório de perfis na hora, por isso a lista está sempre atualizada: cada canal novo criado aparece na próxima vez que o comando roda, sem precisar registrar a lista em outro lugar.
- Mostre para cada canal o nome, o @, o nicho, a plataforma e qual é o ativo.
- Deixe o usuário trocar o ativo tocando num dos canais da lista. Trocar o ativo é copiar o arquivo do canal por cima do perfil ativo e atualizar o apontador, como descrito acima.
- Se o diretório estiver vazio, diga que não há canal criado e ofereça começar com `$canal-dark`.
- A lista é só local. Não publique, não compartilhe e não envie a lista para ninguém.

## Compatibilidade com a automação e os comandos antigos

- Nenhum comando antigo muda de comportamento: todos leem o perfil ativo em `~/workspace/your_files/canal-dark-perfil.md`, que continua existindo e continua sendo uma cópia fiel do canal ativo.
- A automação agendada é a única exceção. Os crons de produção e postagem e o arquivo de estado pertencem ao canal para o qual a automação foi criada, que hoje é o O Mundo das Descobertas, com fila, agenda e horários próprios. Trocar o perfil ativo NÃO muda os horários agendados e NÃO move a automação para o outro canal: os vídeos agendados continuam sendo os do canal automatizado, na agenda dele. Cada canal tem sua própria agenda e sua própria fila. Para automatizar outro canal, ative o perfil dele e crie a automação dele do zero com `$automatizar`.
- `$status` mostra o perfil ativo e diz que `$canais` lista todos os canais.
- `$backup` guarda o perfil ativo e o diretório inteiro de perfis, para nenhum canal se perder.

## Arquivado: O Laboratório Curioso

- O perfil do O Laboratório Curioso continua guardado em `~/workspace/your_files/canal-dark-perfil-laboratorio-curioso.md`, como arquivo avulso, fora do diretório de perfis.
- Ele NÃO aparece em `$canais` e NÃO pode ser escolhido como ativo, porque o nicho foi abandonado e nenhum canal foi criado para ele. O arquivo fica só como registro do trabalho feito.
- Se o usuário pedir para retomar esse nicho um dia, crie o perfil dele no diretório de perfis a partir desse arquivo e ative com `$canais`.
