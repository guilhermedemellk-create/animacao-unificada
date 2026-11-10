# Bibliotecas 3D gratuitas para a trilha 3D por código

## O que este arquivo resolve

- Use este arquivo quando a trilha escolhida for animação 3D low-poly por código com Blender e Python.
- Pegue personagens, objetos e cenários prontos aqui em vez de modelar tudo do zero em cada vídeo.
- Confira a licença de cada biblioteca antes de usar qualquer modelo em vídeo publicado.
- Leia as regras de animação em [animação](animacao.md) e o custo e o tempo da trilha em [estilos visuais](estilos-visuais.md).

## Regra de licença da skill

- Use só modelos com licença que permite uso comercial gratuito.
- Prefira CC0 em todos os casos. CC0 é domínio público e não exige crédito.
- Aceite CC BY só com o crédito ao autor registrado junto com o modelo e incluído na descrição do vídeo.
- Rejeite qualquer modelo com CC BY-NC, CC BY-ND, Editorial ou licença de loja paga.
- Guarde o arquivo de licença original junto com os arquivos baixados. A licença que vale é a do dia do download.
- Verifique a licença de novo antes de cada entrega quando o modelo vier de fonte com licença por modelo.

## Bibliotecas avaliadas em 06/11/2026

### Poly Haven, CC0, baixado

- Abra o site em polyhaven.com e a API pública em api.polyhaven.com.
- Use para modelos realistas com textura PBR, texturas e HDRIs de iluminação.
- Confira a licença na página de licença do site. Todos os ativos são CC0 e valem para qualquer fim, inclusive comercial, sem crédito e com redistribuição permitida. Fonte: página de licença do Poly Haven, lida em outubro de 2026 por Lucky Graphics, e guia da Cinevva de setembro de 2026.
- Saiba que o acervo é realista e não low-poly. Use os modelos como objetos de apoio e os HDRIs para iluminar a cena. Não use um modelo realista como personagem principal de uma série low-poly.
- Saiba que o acervo cresceu em 07/11/2026 para 147 arquivos blend e 13 HDRIs. A lista completa está na seção de downloads abaixo.
- Apague os objetos com nome começado por `wdg_` depois de anexar um arquivo blend do Poly Haven. Esses objetos são controles da interface do arquivo e não fazem parte do modelo. O navio ship_pinnace e o fogão electric_stove trazem esses controles junto.
- Prefira o nível de detalhe baixo quando o modelo trouxer vários níveis. O arbusto shrub_01 traz 4 variantes com 4 níveis cada e o nível LOD3 tem só 392 a 648 vértices. Use o LOD3 na cena low-poly.
- Aplique o modificador Decimate antes de colocar na cena os modelos realistas mais pesados. O abacate food_avocado_01 tem 59.192 vértices e a planta potted_plant_02 tem 36.717 vértices. Use o modelo decimado ou reserve o modelo pesado para o close do objeto herói.
- Baixe pela API sem conta e sem chave. Liste os modelos em `https://api.polyhaven.com/assets?t=models` e pegue os arquivos em `https://api.polyhaven.com/files/<nome>`.
- Prefira a resolução 1k nos arquivos blend e hdr. A resolução 1k já basta para o render em 480x854 da skill e pesa cerca de 1 MB por arquivo.
- Saiba que o tamanho 1k se refere à textura e não à geometria. Dois modelos de árvore escaneados pesaram 571 MB e 219 MB mesmo em 1k e foram apagados no mesmo dia. Confira o tamanho do arquivo antes de baixar e prefira o modelo low-poly quando o scan pesar demais.
- Saiba que os nomes dos modelos diferenciam maiúsculas de minúsculas na API de arquivos. Use `Chandelier_01` e `Television_01` com a inicial maiúscula, como vem na lista da API, porque o nome em minúsculas devolve 404.

### Kenney, CC0, baixado

- Abra o site em kenney.nl.
- Use para pacotes low-poly de estilo consistente, com cores chapadas e polígonos baixos, prontos para histórias.
- Confira a licença na página de suporte do Kenney. Todos os ativos das páginas de assets são domínio público CC0, valem para uso comercial e não exigem crédito. A única reserva é o logotipo do Kenney, que não pode ser usado como se fosse projeto oficial do estúdio. Fonte: página de suporte do Kenney, lida em outubro de 2026 por Lucky Graphics, e guia da Cinevva de setembro de 2026.
- Baixe cada pacote com o link assinado do site. Abra a página do pacote, copie o valor de `data-download-id`, peça o link em `https://kenney.nl/download-link/<id>` e baixe o ZIP da URL devolvida. O link expira, então baixe na hora.
- Saiba que o pedido do link assinado só funciona com os cookies da visita à página e com o cabeçalho Referer da página do pacote. O pedido sem cookies devolve `{"error":"forbidden"}`. Busque a página primeiro com um arquivo de cookies e reuse os cookies no pedido do link.
- Saiba que os pacotes de personagens animados só trazem FBX e não trazem GLB. O modelo vem em um FBX e as animações idle, jump e run vêm em arquivos FBX separados na pasta Animations.
- Saiba que o FBX do personagem animado traz um objeto Icosphere oculto de 1,90 m junto com o modelo. Apague esse objeto à mão depois de importar, porque ele sobrevive ao select all e delete.
- Saiba que o pacote Mini Characters também traz um objeto Icosphere oculto de 1,90 m junto com cada personagem. Apague esse objeto à mão depois de importar, como nos pacotes de personagens animados.
- Saiba que o catálogo 3D do Kenney está completo na biblioteca desde 07/11/2026. Os 50 pacotes 3D do site estão baixados. Não falta nenhum kit 3D do Kenney para baixar.
- Saiba que o pacote 3D Road Tiles só traz GLTF e não traz GLB nem FBX. O arquivo GLTF é autocontido com o buffer embutido em base64 e importa sem arquivo .bin. O modelo roadTile_01 foi validado com 24 vértices e 3,00 x 3,00 x 0,46 m.
- Saiba que os pacotes não têm personagens rigados, com exceção dos dois pacotes de personagens animados acima. Os demais kits Kenney são ambientes, objetos e veículos. Personagens rigados com muitas animações vêm da KayKit abaixo.
- Saiba que a escala varia por kit. Meça cada modelo depois de importar e normalize a altura antes de animar. Leia a seção de adaptação abaixo.

### KayKit, CC0, baixado

- Abra os repositórios em github.com/KayKit-Game-Assets e a página do autor em kaylousberg.itch.io.
- Use para personagens low-poly rigados e animados e para cenários modulares no mesmo estilo visual.
- Confira a licença no arquivo LICENSE.txt de cada repositório. Cada pacote é CC0 1.0 Universal, com uso pessoal e comercial livre e sem atribuição. Fonte: README e LICENSE.txt dos repositórios KayKit, lidos em 06/11/2026.
- Baixe por git sem conta e sem token com `git clone --depth 1 https://github.com/KayKit-Game-Assets/<repositorio>.git`.
- Saiba que o pacote Adventurers tem 5 personagens no nível gratuito e 75 animações por personagem, segundo o README do pacote. O nível pago EXTRA acrescenta personagens e não foi baixado.
- Saiba que todos os 10 repositórios gratuitos da organização KayKit já foram baixados em 06/11/2026. A lista completa está na seção de downloads abaixo. Não existe outro repositório gratuito na organização para baixar.
- Saiba que os pacotes Bits da KayKit trazem cada modelo em FBX e em GLTF com bin e não trazem GLB. Importe o FBX ou o GLTF no Blender. O OBJ que vem junto é duplicado e foi apagado na limpeza.
- Saiba que o pacote Skeletons tem 4 esqueletos rigados com 95 animações cada um no GLB, medido na importação de teste em 06/11/2026 no Blender 4.5.3. O FBX de cada esqueleto pesa cerca de 22 MB e o GLB pesa cerca de 4,7 MB. Prefira o GLB.
- Saiba que cada personagem usa uma textura atlas em gradiente de 1024x1024. Recoloque a cor da roupa na textura ou no material quando for adaptar à paleta do canal.

### NASA 3D Resources, domínio público dos EUA com condições, baixado

- Abra o hub oficial em science.nasa.gov/3d-resources e o espelho no GitHub em github.com/nasa/NASA-3D-Resources.
- Use para naves, sondas, telescópios, astronautas e foguetes reais, com o formato exato das missões.
- Confira a licença nas NASA Images and Media Usage Guidelines em nasa.gov/nasa-brand-center/images-and-media. Os modelos são obra do governo dos Estados Unidos e não têm direito autoral nos Estados Unidos. O uso comercial é permitido com condições. Fonte: página do hub da NASA e guia da Cinevva, lidos em 06/11/2026.
- Dê crédito à NASA como fonte do material em todo vídeo que usar um destes modelos. Escreva o crédito na descrição do vídeo.
- Não insinue que a NASA endossa o canal ou o vídeo. Não use logotipo, insígnia ou marca da NASA, porque a insígnia e o logotipo são protegidos por lei e não são domínio público.
- Confira cada modelo antes de usar. Modelos enviados por parceiros externos podem ter material de terceiros com direito autoral.
- Baixe por sparse checkout no espelho do GitHub para não baixar o repositório inteiro de 5,2 GB. Clone com `git clone --filter=blob:none --no-checkout`, liste os GLB com `git ls-tree -r --name-only master` e baixe só os modelos da história com `git sparse-checkout set`.
- Saiba que a escala dos modelos da NASA é arbitrária. O Hubble chegou com 458 m de comprimento e o astronauta com 69 m de altura. Meça cada modelo depois de importar e normalize a altura antes de animar.
- Saiba que a estação Mir chegou com 1.037 x 1.395 x 1.686 m. Normalize a Mir para cerca de 100 m antes de usar.
- Saiba que o helicóptero Ingenuity chegou minúsculo, com o corpo de 0,14 x 0,20 x 0,18 m. Escale o Ingenuity para cerca de 1,20 m de envergadura.
- Saiba que o rover Opportunity chegou com 8,69 x 7,31 x 12,71 m, maior que o rover real de cerca de 3 m. Normalize o Opportunity para baixo.
- Saiba que o ônibus espacial chegou com o maior cilindro de 37,18 m de altura e com várias superfícies de 0,01 m junto. Normalize o ônibus espacial para cerca de 37 m e ignore as superfícies minúsculas.
- Saiba que a biblioteca tem 37 modelos da NASA desde 07/11/2026. Ainda faltam 220 modelos GLB no espelho para baixar quando a história pedir.
- Guarde as condições de uso em `cenarios/nasa-3d-resources/LICENCA-NASA.txt`.

### ambientCG, CC0, baixado

- Abra o site em ambientcg.com.
- Use para texturas PBR CC0 de superfícies, para dar material realista a pisos, paredes e objetos de apoio.
- Confira a licença na página de licença do site. Todas as texturas são CC0 1.0 Universal, com uso comercial livre e sem crédito.
- Baixe sem conta e sem chave pelo endereço `https://ambientcg.com/get?file=<AssetId>_1K-JPG.zip`. Troque `<AssetId>` pelo código da textura, como `PavingStones152`.
- Prefira a resolução 1k em JPG. O ZIP traz os mapas Color, Roughness, NormalGL, NormalDX, Displacement e AmbientOcclusion, mais os arquivos .blend, .usdc e .mtlx.
- Guarde só os mapas Color, Roughness e NormalGL. Apague os demais mapas e os arquivos .blend, .usdc e .mtlx na limpeza, como foi feito com as 12 texturas baixadas em 07/11/2026.
- Saiba que a skill usa materiais de cor chapada como padrão. Use a textura PBR só quando a cena pedir superfície realista, como piso de madeira, parede de tijolo ou asfalto de rua.
- Guarde a licença em `objetos/ambientcg-texturas/LICENCA-ambientCG.txt`.

### Quaternius, CC0, pendente de cota do Google Drive

- Abra o site em quaternius.com.
- Use para personagens low-poly rigados, monstros, veículos e cenários no mesmo estilo fofo e arredondado.
- Confira a licença no site do autor. Todos os pacotes são CC0, sem atribuição e com uso comercial permitido. Fonte: guia da Cinevva de setembro de 2026 e catálogo Free Game Dev Assets, medido em 23/09/2026.
- Saiba que a página antiga de pacotes `quaternius.com/packs/ultimatevehicles.html` devolveu 404 em 06/11/2026. O site mudou de estrutura e os downloads passam pelo itch.io do autor, que pede sessão de navegador.
- Saiba que o teste de 07/11/2026 achou um caminho novo de download direto. Cada página de pacote em `quaternius.com/packs/<pacote>.html` traz um botão de download para uma pasta pública do Google Drive, com as subpastas Blends, FBX e OBJ e o arquivo License.txt. Baixe só a subpasta FBX.
- Saiba que o download pelo Drive falhou em 07/11/2026 por cota excedida do Google Drive. O Drive devolveu "Quota exceeded" no peixe e no monstro, pelo curl e pelo gdown. A cota expira em até 24 horas. Tente de novo no dia seguinte ou baixe à mão no navegador.
- Saiba que as pastas Drive dos pacotes mais úteis já estão mapeadas no inventário, com o número de arquivos FBX de cada um. O mapa completo está em `/tmp/quaternius_map.json`.
- Saiba que o pacote bestiarydungeonmonsterskit não tem link de pasta Drive na página. Baixe esse pacote só pelo botão do Itch, que pede sessão de navegador.
- Baixe à mão no navegador quando precisar de um pacote Quaternius e registre o nome do pacote, a URL e a data no inventário. Não invente URL de download direto.
- Saiba que os pacotes mais úteis para as histórias são os de peixes animados, monstros animados, dinossauros animados e zumbis animados, que cobrem fundo do mar e monstros com animação pronta.

### BlenderKit, licenças Royalty Free e CC0 por ativo, pendente de conta

- Abra o site em blenderkit.com e o manual do Blender sobre o complemento.
- Use para vestir a cena sem sair do Blender, com modelos, materiais e HDRIs pesquisados dentro do programa.
- Confira a licença em cada ativo antes de usar. A biblioteca tem duas licenças e as duas permitem uso comercial, mas só os ativos CC0 são livres de restrição de revenda como arquivo. Os ativos Royalty Free não podem ser revendidos como ativos. Fonte: manual do Blender sobre o BlenderKit e guia SupaVoxel de outubro de 2026.
- Saiba que o plano gratuito tinha 23.877 modelos, 43.975 materiais e 5.113 HDRIs em outubro de 2026, segundo o guia SupaVoxel. O restante da biblioteca exige plano pago.
- Saiba que o uso exige conta no BlenderKit. Sem a conta do usuário não dá para baixar por aqui. Registre como pendente e peça a conta ao usuário antes de baixar.

### Sketchfab, licença por modelo, pendente de conta e de verificação por modelo

- Abra o site em sketchfab.com.
- Use só quando precisar de um modelo específico que nenhuma biblioteca CC0 tem.
- Confira a licença na página de cada modelo antes de baixar. A licença varia por modelo entre Standard, CC0, CC BY, CC BY-SA, CC BY-ND e CC BY-NC. Só CC0, CC BY e CC BY-SA valem para uso comercial com as condições de cada um. CC BY-NC e Editorial não valem para uso comercial. Fonte: centro de ajuda do Sketchfab e guia The 3D AI de 18/10/2026.
- Filtre a busca por Downloadable e por CC0 antes de escolher qualquer modelo.
- Saiba que o download exige conta no Sketchfab. Registre como pendente e verifique cada modelo à mão no navegador.
- Saiba que o Sketchfab foi vendido pela Epic à KitBash em 10/08/2026 e que os downloads gratuitos com licença Creative Commons continuavam funcionando em setembro de 2026, segundo o guia da Cinevva. Reconfirme antes de usar.

### Poly Pizza, CC0 e CC BY por modelo, pendente de chave de API

- Abra o site em poly.pizza.
- Use para objetos low-poly avulsos em um único arquivo GLB autocontido, incluindo o arquivo do Google Poly.
- Confira a licença em cada modelo. O acervo mistura CC0 e CC BY. Cerca de 69 por cento do catálogo é CC BY e exige crédito ao autor. Fonte: documentação do MCP for Blender e guia da Cinevva de setembro de 2026.
- Filtre sempre por CC0 quando não quiser obrigação de crédito.
- Saiba que a API em api.poly.pizza exige chave gratuita. A chamada sem chave devolveu 401 em 06/11/2026. Peça a chave no site e registre como pendente até lá.
- Saiba que a escala dos modelos do Google Poly é arbitrária. Meça e normalize a altura de cada modelo depois de importar.

### Mixamo, royalty free com conta Adobe, pendente de conta

- Abra o site em mixamo.com.
- Use para rigar um personagem humanoide próprio e para aplicar animações de captura de movimento prontas.
- Confira a licença no FAQ da Adobe. O serviço é gratuito com Adobe ID, sem assinatura do Creative Cloud, e personagens e animações são royalty free para projetos pessoais, comerciais e sem fins lucrativos, incluindo filmes e jogos. Não redistribua os arquivos crus. Fonte: FAQ da Adobe, lido em 22/10/2026 por StarterLoot, e guia da Cinevva de setembro de 2026.
- Saiba que o rig automático e a biblioteca só funcionam para humanoides bípedes em pose neutra.
- Saiba que o uso exige Adobe ID pessoal. Registre como pendente e peça a conta ao usuário antes de usar.

### Outras fontes avaliadas e não baixadas

- Saiba que o Poly Haven também tem texturas PBR CC0 pela mesma API pública, sem conta e sem chave. Não foram baixadas porque as 12 texturas do ambientCG já cobrem piso, parede, rua e natureza para as cenas da skill.

## O que foi baixado em 06/11/2026

- Guarde tudo em `~/workspace/tools/bibliotecas-3d/`, com as pastas `personagens`, `objetos` e `cenarios`.
- Leia o inventário completo com tamanhos medidos em `~/workspace/tools/bibliotecas-3d/INVENTARIO-downloads.txt`.
- Total baixado: 936 MB, 20.567 arquivos, 4.700 arquivos GLB, 5.809 FBX, 993 GLTF, 147 blend e 13 HDR, depois de remover pastas `.git` e formatos duplicados.
- Saiba que o conjunto inicial tinha 130 MB, 4.837 arquivos e 1.059 GLB. A expansão de 06/11/2026 somou 24 pacotes novos, 22 modelos novos do Poly Haven e 4 HDRIs novos. A expansão de 07/11/2026 somou 28 pacotes Kenney, 124 modelos novos do Poly Haven, 8 HDRIs novos, 29 modelos novos da NASA e 12 texturas do ambientCG.

### Personagens, 188 MB

- Baixe o KayKit Adventurers em `personagens/kaykit-adventurers`, 25 MB, 117 arquivos, 5 GLB, licença CC0.
- Use os 5 personagens rigados e animados: Barbarian, Knight, Mage, Rogue e Rogue_Hooded. Cada um tem 76 animações no arquivo GLB, medido na importação de teste em 06/11/2026 no Blender 4.5.3.
- Baixe o KayKit Skeletons em `personagens/kaykit-skeletons`, 111 MB, 65 arquivos, 4 GLB, licença CC0.
- Use os 4 esqueletos rigados e animados: Skeleton Mage, Skeleton Minion, Skeleton Rogue e Skeleton Warrior. Cada um tem 95 animações no arquivo GLB, medido na importação de teste em 06/11/2026 no Blender 4.5.3.
- Baixe o Kenney Animated Characters Protagonists em `personagens/kenney-animated-characters-protagonists`, 2,2 MB, 16 arquivos, 4 FBX, licença CC0.
- Use o personagem médio com 4 visuais de pele e animações idle, jump e run em FBX separados. Apague o objeto Icosphere oculto depois de importar.
- Baixe o Kenney Animated Characters Survivors em `personagens/kenney-animated-characters-survivors`, 2,4 MB, 17 arquivos, 4 FBX, licença CC0.
- Use o sobrevivente com visuais de pele e animações idle, jump e run em FBX separados. Apague o objeto Icosphere oculto depois de importar.
- Baixe o Kenney Blocky Characters em `personagens/kenney-blocky-characters`, 13 MB, 114 arquivos, 18 GLB, licença CC0.
- Use os 18 personagens de blocos para figurantes, multidões e personagens secundários de cidade e de fantasia.
- Baixe o Kenney Animated Characters Retro em `personagens/kenney-animated-characters-retro`, 2,2 MB, 10 arquivos, 4 FBX, licença CC0.
- Use o personagem médio retrô com 4 visuais de pele e animações idle, jump e run em FBX separados. Apague o objeto Icosphere oculto depois de importar.
- Baixe o Kenney Mini Characters em `personagens/kenney-mini-characters`, 20 MB, 134 arquivos, 43 GLB, licença CC0.
- Use os 43 personagens mini para figurantes, multidões e personagens secundários de cidade, de praia e de festa. Apague o objeto Icosphere oculto depois de importar.
- Guarde a licença em `personagens/kaykit-adventurers/LICENSE.txt` e em `personagens/kaykit-skeletons/LICENSE.txt`.

### Animais, 14 MB

- Baixe o Kenney Cube Pets em `personagens/kenney-cube-pets`, 14 MB, 81 arquivos, 24 GLB, licença CC0.
- Use os 24 animais de cubo, incluindo gato, cachorro, vaca, coelho, abelha, caranguejo e castor. O gato foi validado na importação de teste com 1.246 vértices e 1,25 x 1,33 x 1,40 m.
- Saiba que os animais de cubo combinam com o estilo low-poly da série e servem como bicho de estimação, como animal da fazenda e como animal da história.

### Objetos, 310 MB

- Baixe o Kenney Furniture Kit em `objetos/kenney-furniture-kit`, 11 MB, 986 arquivos, 140 GLB, licença CC0. Use para móveis e objetos de casa.
- Baixe o Kenney Car Kit em `objetos/kenney-car-kit`, 10 MB, 158 arquivos, 50 GLB, licença CC0. Use para carros, caminhões e veículos de rua.
- Baixe o Kenney Food Kit em `objetos/kenney-food-kit`, 12 MB, 609 arquivos, 200 GLB, licença CC0.
- Use os 200 alimentos low-poly, incluindo maçã, abacate, bacon, pão e legumes. A maçã foi validada na importação de teste com 294 vértices e 0,20 x 0,20 x 0,19 m.
- Baixe o Kenney Survival Kit em `objetos/kenney-survival-kit`, 4,6 MB, 252 arquivos, 80 GLB, licença CC0.
- Use as 80 ferramentas e objetos de sobrevivência, incluindo machado, barril, cantil e cama de acampamento. O machado foi validado na importação de teste com 270 vértices.
- Baixe o Kenney Pirate Kit em `objetos/kenney-pirate-kit`, 6,8 MB, 226 arquivos, 72 GLB, licença CC0.
- Use os 72 objetos de pirata e de navio antigo, incluindo canhão, barril, garrafa e barco a remo. O canhão foi validado na importação de teste com 426 vértices e 1,40 x 1,92 x 1,05 m.
- Baixe o Kenney Train Kit em `objetos/kenney-train-kit`, 13 MB, 321 arquivos, 103 GLB, licença CC0.
- Use os 103 vagões, trilhos e peças de trem. O vagão de carga foi validado na importação de teste com 1.874 vértices e 1,20 x 2,70 x 1,14 m.
- Baixe o Kenney Watercraft Kit em `objetos/kenney-watercraft-kit`, 4,2 MB, 147 arquivos, 46 GLB, licença CC0.
- Use os 46 barcos, incluindo barco de pesca, barco a vela e casa flutuante. O barco de pesca pequeno foi validado na importação de teste com 453 vértices e 1,78 x 3,87 x 2,60 m.
- Baixe o KayKit Restaurant Bits em `objetos/kaykit-restaurant-bits`, 17 MB, 591 arquivos, 288 FBX, licença CC0.
- Use as mesas, cadeiras, pratos, tigelas e objetos de cozinha e de restaurante. A cadeira foi validada na importação de teste com 296 vértices e 0,75 x 1,21 x 0,80 m.
- Baixe o KayKit Furniture Bits em `objetos/kaykit-furniture-bits`, 6,1 MB, 227 arquivos, 106 FBX, licença CC0.
- Use as poltronas, camas, mesas e móveis de interior. A poltrona foi validada na importação de teste com 312 vértices e 1,80 x 1,22 x 1,60 m.
- Baixe o KayKit Prototype Bits em `objetos/kaykit-prototype-bits`, 8,3 MB, 303 arquivos, 144 FBX, licença CC0.
- Use as peças cinza de prototipagem para montar a cena de teste antes de trocar pelos modelos finais.
- Baixe o Kenney Prototype Kit em `objetos/kenney-prototype-kit`, 9,1 MB, 446 arquivos, 145 GLB, licença CC0.
- Use as 145 peças cinza de prototipagem para montar a cena de teste antes de trocar pelos modelos finais.
- Baixe o Kenney Blaster Kit em `objetos/kenney-blaster-kit`, 3,2 MB, 127 arquivos, 40 GLB, licença CC0.
- Use os 40 blasters e armas de ficção para histórias de espaço, de batalha e de videogame. O blaster A foi validado na importação de teste com 724 vértices e 0,18 x 0,80 x 0,42 m.
- Baixe o Kenney Brick Kit em `objetos/kenney-brick-kit`, 11 MB, 894 arquivos, 296 GLB, licença CC0.
- Use os 296 tijolos e blocos de montar para construir paredes, casas e castelos por peças.
- Baixe o Kenney Marble Kit em `objetos/kenney-marble-kit`, 9,7 MB, 498 arquivos, 162 GLB, licença CC0.
- Use as 162 peças de pista de bolinha para histórias de como funciona uma máquina de bolinhas e de física.
- Baixe o Kenney Racing Kit em `objetos/kenney-racing-kit`, 9,5 MB, 812 arquivos, 112 GLB, licença CC0.
- Use os 112 carros de corrida e peças de pista para histórias de corrida e de velocidade.
- Baixe o Kenney Toy Car Kit em `objetos/kenney-toy-car-kit`, 10 MB, 486 arquivos, 157 GLB, licença CC0.
- Use os 157 carrinhos de brinquedo para histórias de criança, de trânsito e de cidade em miniatura.
- Baixe as texturas do ambientCG em `objetos/ambientcg-texturas`, 37 MB, 36 arquivos JPG 1k, licença CC0.
- Use as 12 texturas PBR para dar material realista a pisos, paredes e objetos de apoio: calçada, tijolo, piso de madeira, madeira, concreto, grama, asfalto, metal, mármore, carpete, reboco e azulejo. Cada textura traz os mapas Color, Roughness e NormalGL.
- Baixe o Poly Haven em `objetos/polyhaven`, 122 MB, 147 arquivos blend 1k, licença CC0.
- Use os 123 modelos realistas novos como objetos de apoio, além dos 24 que já estavam baixados: casa com sofá, mesa de jantar, cama gótica, lustre de parede e relógio de avô, cozinha com fogão elétrico, chaleira, micro-ondas e tábua de corte, terror com estátua gótica, máscara de gás antiga, lamparina e busto de mármore, rua com hidrante, poste, câmera de segurança e orelhão, comida com banana, abacate, kiwi e bolo de morango com chocolate, oficina com furadeira, pé de cabra, marreta e gerador, mar com boia salva-vidas, colete e navio veleiro, escola com carteira, cadeira e quadro, e natureza com arbusto, pedra e tronco. O sofá foi validado na importação de teste com 2.298 vértices e 1,57 x 0,66 x 0,80 m. O fogão foi validado com 3.160 vértices e 0,50 x 0,61 x 0,86 m.
- Saiba que o modelo de muda de pinheiro fir_sapling foi apagado no mesmo dia por peso, com 11,9 MB e 510 mil vértices. Use as árvores low-poly do Kenney Nature Kit no lugar.
- Guarde a licença de cada pacote Kenney no arquivo `License.txt` dentro da pasta do pacote.

### Cenários, 439 MB

- Baixe o Kenney Nature Kit em `cenarios/kenney-nature-kit`, 21 MB, 2.302 arquivos, 329 GLB, licença CC0. Use para floresta, árvores, pedras, pontes e plantas.
- Baixe o Kenney 3D Road Tiles em `cenarios/kenney-3d-road-tiles`, 3,1 MB, 307 arquivos, 302 GLTF, licença CC0.
- Use as 302 peças de rua em grade para montar ruas, cruzamentos e calçadas por módulos. O modelo roadTile_001 foi validado na importação de teste com 24 vértices e 3,00 x 3,00 x 0,46 m.
- Baixe o Kenney City Kit Commercial em `cenarios/kenney-city-kit-commercial`, 7,0 MB, 133 arquivos, 41 GLB, licença CC0.
- Use os 41 prédios comerciais para montar centro de cidade com lojas e escritórios. O prédio A foi validado na importação de teste com 2.074 vértices e 0,88 x 0,94 x 1,29 m. Escale de 5 a 10 vezes para virar prédio em tamanho de cena.
- Baixe o Kenney City Kit Industrial em `cenarios/kenney-city-kit-industrial`, 7,4 MB, 123 arquivos, 37 GLB, licença CC0.
- Use os 37 prédios industriais para montar zona industrial com galpões e chaminés.
- Baixe o Kenney Hexagon Kit em `cenarios/kenney-hexagon-kit`, 4,5 MB, 226 arquivos, 72 GLB, licença CC0.
- Use os 72 hexágonos para montar mapa de tabuleiro e terreno por peças hexagonais.
- Baixe o Kenney Modular Buildings em `cenarios/kenney-modular-buildings`, 4,2 MB, 334 arquivos, 108 GLB, licença CC0.
- Use as 108 peças modulares de prédio para montar casas e prédios por partes, com paredes, telhados e janelas.
- Baixe o Kenney Modular Cave Kit em `cenarios/kenney-modular-cave-kit`, 11 MB, 130 arquivos, 40 GLB, licença CC0.
- Use as 40 peças modulares de caverna para montar gruta e caverna por dentro, com estalactites e rochas.
- Baixe o Kenney Modular Dungeon Kit em `cenarios/kenney-modular-dungeon-kit`, 12 MB, 127 arquivos, 39 GLB, licença CC0.
- Use as 39 peças modulares de masmorra para montar corredor e sala de castelo por dentro. O corredor de canto foi validado na importação de teste com 1.534 vértices e 4,00 x 4,00 x 4,23 m.
- Baixe o Kenney Platformer Kit em `cenarios/kenney-platformer-kit`, 11 MB, 467 arquivos, 153 GLB, licença CC0.
- Use as 153 peças de plataforma para montar fase de jogo de plataforma com plataformas, escadas e moedas.
- Baixe o Kenney Retro Fantasy Kit em `cenarios/kenney-retro-fantasy-kit`, 4,7 MB, 348 arquivos, 105 GLB, licença CC0.
- Use as 105 peças de fantasia retrô para montar vila e castelo em estilo pixel retrô.
- Baixe o Kenney Retro Urban Kit em `cenarios/kenney-retro-urban-kit`, 4,9 MB, 441 arquivos, 124 GLB, licença CC0.
- Use as 124 peças urbanas retrô para montar cidade antiga com prédios, ruas e praças.
- Baixe o Kenney Space Station Kit em `cenarios/kenney-space-station-kit`, 4,4 MB, 299 arquivos, 97 GLB, licença CC0.
- Use as 97 peças de estação espacial para montar interior de estação, com camas, corredores e módulos. O piso de varanda foi validado na importação de teste com 72 vértices e 1,00 x 0,70 x 0,15 m.
- Baixe o Kenney Coaster Kit em `cenarios/kenney-coaster-kit`, 14 MB, 560 arquivos, 183 GLB, licença CC0.
- Use as 183 peças de montanha-russa para montar parque de diversões com trilhos, carrinhos e torres.
- Baixe o Kenney Tower Defense Kit em `cenarios/kenney-tower-defense-kit`, 12 MB, 488 arquivos, 160 GLB, licença CC0.
- Use as 160 peças de defesa de torre para montar campo de batalha com torres, muros e inimigos.
- Baixe o Kenney Holiday Kit em `cenarios/kenney-holiday-kit`, 7,6 MB, 307 arquivos, 99 GLB, licença CC0.
- Use as 99 peças de festa para montar Natal e festas com árvore, presentes e enfeites. A árvore decorada com neve foi validada na importação de teste com 1.636 vértices e 1,25 x 1,25 x 2,29 m.
- Baixe o Kenney Minigolf Kit em `cenarios/kenney-minigolf-kit`, 6,3 MB, 390 arquivos, 126 GLB, licença CC0.
- Use as 126 peças de minigolfe para montar campo de minigolfe com buracos, rampas e obstáculos.
- Baixe o Kenney Mini Arcade em `cenarios/kenney-mini-arcade`, 3,5 MB, 70 arquivos, 20 GLB, licença CC0.
- Use as 20 peças de fliperama em miniatura para montar salão de jogos em diorama.
- Baixe o Kenney Mini Arena em `cenarios/kenney-mini-arena`, 1,8 MB, 72 arquivos, 22 GLB, licença CC0.
- Use as 22 peças de arena em miniatura para montar estádio e combate em diorama.
- Baixe o Kenney Mini Forest em `cenarios/kenney-mini-forest`, 2,5 MB, 72 arquivos, 22 GLB, licença CC0.
- Use as 22 peças de floresta em miniatura para montar clareira e bosque em diorama.
- Baixe o Kenney Mini Shop em `cenarios/kenney-mini-shop`, 6,0 MB, 102 arquivos, 30 GLB, licença CC0.
- Use as 30 peças de loja em miniatura para montar lojinha e mercado em diorama.
- Baixe o Kenney Mini Skate em `cenarios/kenney-mini-skate`, 4,9 MB, 134 arquivos, 42 GLB, licença CC0.
- Use as 42 peças de pista de skate em miniatura para montar skatepark em diorama.
- Baixe o Kenney Fantasy Town Kit em `cenarios/kenney-fantasy-town-kit`, 9,3 MB, 512 arquivos, 167 GLB, licença CC0. Use para vila, casas e ruas de fantasia.
- Baixe o Kenney City Kit Roads em `cenarios/kenney-city-kit-roads`, 6,0 MB, 296 arquivos, 95 GLB, licença CC0. Use para ruas, estradas e cruzamentos de cidade.
- Baixe o Kenney City Kit Suburban em `cenarios/kenney-city-kit-suburban`, 5,5 MB, 136 arquivos, 40 GLB, licença CC0.
- Use os 40 prédios e casas de bairro para montar rua residencial e cidade pequena. O prédio tipo A foi validado na importação de teste com 1.870 vértices e 1,30 x 1,03 x 0,83 m. Escale de 5 a 10 vezes para virar prédio em tamanho de cena.
- Baixe o Kenney Building Kit em `cenarios/kenney-building-kit`, 4,4 MB, 249 arquivos, 79 GLB, licença CC0.
- Use as 79 peças modulares de construção, incluindo barricadas, portas e janelas, para montar prédios por partes.
- Baixe o Kenney Castle Kit em `cenarios/kenney-castle-kit`, 5,4 MB, 245 arquivos, 76 GLB, licença CC0.
- Use as 76 peças de castelo medieval, incluindo torres, muros e portões, para histórias de reis, cavaleiros e idade média.
- Baixe o Kenney Factory Kit em `cenarios/kenney-factory-kit`, 11 MB, 441 arquivos, 143 GLB, licença CC0.
- Use as 143 peças de fábrica e de indústria, incluindo máquinas, tubos e galpões, para histórias de como funciona uma fábrica.
- Baixe o Kenney Graveyard Kit em `cenarios/kenney-graveyard-kit`, 11 MB, 283 arquivos, 91 GLB, licença CC0.
- Use as 91 peças de cemitério, incluindo fantasma, lápides, altar e muros, para histórias de terror e de Halloween. O fantasma foi validado na importação de teste com 635 vértices.
- Baixe o Kenney Space Kit em `cenarios/kenney-space-kit`, 13 MB, 1.082 arquivos, 153 GLB, licença CC0.
- Use as 153 peças de espaço low-poly, incluindo astronautas, alienígenas, módulos e rochas. O astronauta foi validado na importação de teste com 538 vértices.
- Baixe o Kenney Modular Space Kit em `cenarios/kenney-modular-space-kit`, 14 MB, 133 arquivos, 40 GLB, licença CC0. Use para espaço, naves e estações.
- Baixe o Kenney Mini Dungeon em `cenarios/kenney-mini-dungeon`, 4,3 MB, 101 arquivos, 30 GLB, licença CC0. Use para interior de masmorra e caverna.
- Baixe o KayKit Dungeon Remastered em `cenarios/kaykit-dungeon-remastered`, 30 MB, 228 arquivos, 203 GLB, licença CC0. Use para pisos, paredes, pilares, tochas, baús e moedas de interior.
- Baixe o KayKit City Builder Bits em `cenarios/kaykit-city-builder-bits`, 7,9 MB, 179 arquivos, 82 FBX, licença CC0.
- Use as peças de construção de cidade, incluindo prédios, ruas e praças, para montar cidade por módulos.
- Baixe o KayKit Medieval Hexagon Pack em `cenarios/kaykit-medieval-hexagon-pack`, 48 MB, 952 arquivos, 442 FBX, licença CC0.
- Use os 442 hexágonos medievais, incluindo castelo, igreja, ferraria, casas, colinas e árvores, para montar mapa de reino por peças hexagonais. A colina com árvores foi validada na importação de teste com 873 vértices e 1,76 x 1,74 x 1,33 m.
- Baixe o KayKit Space Base Bits em `cenarios/kaykit-space-base-bits`, 8,7 MB, 243 arquivos, 114 FBX, licença CC0.
- Use as peças de base espacial modular, incluindo módulos, antenas e plataformas, para montar estação e base em outro planeta.
- Baixe o KayKit Halloween Bits em `cenarios/kaykit-halloween-bits`, 8,6 MB, 267 arquivos, 126 FBX, licença CC0.
- Use as peças de Halloween, incluindo abóboras, fantasmas, teias e doces, para histórias de terror e de festa.
- Baixe o NASA 3D Resources em `cenarios/nasa-3d-resources`, 73 MB, 38 arquivos, 37 GLB, domínio público dos EUA com condições.
- Use os 37 modelos reais da NASA: astronauta, módulo lunar Apollo, telescópio Hubble, telescópio James Webb, rover Perseverance, estação espacial ISS, foguete Saturno V e sonda Voyager, mais ônibus espacial, helicóptero Ingenuity, sonda Parker, sonda Cassini, sonda Juno, telescópio Kepler, rover Opportunity, módulo Viking, estação Skylab, estação Mir, traje espacial Z2, traje Gemini, traje de atividade extraveicular, robô Robonaut 2, prédio de montagem de veículos, transportador Crawler, sala de controle de missão, antena de 70 metros, asteroide Bennu, telescópios Chandra e Spitzer, capacete, luva de astronauta, martelo e chave inglesa. O Hubble foi validado na importação de teste com 23.058 vértices. Dê crédito à NASA na descrição do vídeo e não use a insígnia da NASA.
- Baixe os HDRIs em `cenarios`, licença CC0. Use para iluminar a cena com luz de ambiente real.
- Use o `autumn_field_puresky_1k.hdr` para iluminar cenas externas com céu de campo.
- Use o `belfast_sunset_puresky_1k.hdr` para iluminar cenas de pôr do sol.
- Use o `qwantani_night_1k.hdr` para iluminar cenas de noite. Foi validado como luz do mundo na importação de teste.
- Use o `lythwood_lounge_1k.hdr` para iluminar cenas de interior de casa.
- Use o `autumn_forest_01_1k.hdr` para iluminar cenas de floresta.
- Use o `snowy_cemetery_1k.hdr` para iluminar cenas de cemitério com neve. Foi validado como luz do mundo na importação de teste em 07/11/2026.
- Use o `gothic_manor_01_1k.hdr` para iluminar cenas de mansão gótica e de terror.
- Use o `cobblestone_street_night_1k.hdr` para iluminar cenas de rua de pedra à noite.
- Use o `garage_1k.hdr` para iluminar cenas de garagem e de porão de trabalho.
- Use o `hotel_room_1k.hdr` para iluminar cenas de quarto de hotel e de interior.
- Use o `small_empty_house_1k.hdr` para iluminar cenas de casa vazia e de porão.
- Use o `abandoned_hall_01_1k.hdr` para iluminar cenas de salão abandonado e de terror.
- Use o `moonlit_golf_1k.hdr` para iluminar cenas de noite ao ar livre com lua.
- Guarde a licença de cada pacote no arquivo de licença dentro da pasta do pacote.

## O que os modelos novos permitem de cena nova

- Monte histórias de terror e de Halloween com esqueletos rigados que andam e gesticulam, com o cemitério, com a casa de Halloween e com o fantasma.
- Monte histórias de cidade com prédios de bairro, com ruas, com carros, com trens e com multidões de personagens de blocos.
- Monte histórias de espaço com naves reais da NASA, com o astronauta real, com a estação espacial e com a base espacial low-poly.
- Monte histórias de como funciona uma fábrica, um trem, um barco e um restaurante com as peças de fábrica, de trem, de barco e de cozinha.
- Monte histórias de comida com 200 alimentos low-poly e com os modelos realistas de maçã, croissant e bolo para o close do objeto herói.
- Monte histórias de idade média com o castelo, com o mapa hexagonal de reino, com o pirata e com o canhão.
- Monte histórias de fundo do mar com barcos, com a boia, com a concha e com o caranguejo de cubo.
- Monte histórias com animais de estimação e de fazenda com os 24 animais de cubo.
- Monte histórias de mistério e de detetive com a lupa, com o relógio de bolso, com o baú do tesouro e com a katana antiga.
- Monte cenas de noite, de pôr do sol, de interior e de floresta com os 4 HDRIs novos de iluminação.
- Monte histórias de casa por dentro com o sofá realista, com a mesa de jantar, com a cama gótica, com o fogão elétrico e com o relógio de avô, com luz de interior do HDRI de quarto de hotel ou de casa vazia.
- Monte histórias de terror na casa assombrada com a estátua gótica, com a máscara de gás antiga, com a lamparina, com o busto de mármore e com a luz do HDRI de mansão gótica ou de salão abandonado.
- Monte histórias de rua à noite com o hidrante, com o poste, com a câmera de segurança, com o orelhão e com a luz do HDRI de rua de pedra à noite.
- Monte histórias de espaço com o ônibus espacial real, com o helicóptero Ingenuity em Marte, com o rover Opportunity, com a estação Mir e com a estação espacial low-poly.
- Monte histórias de como funciona um navio com o veleiro completo do Poly Haven, com velas, cordame e convés, e com os barcos low-poly do Kenney.
- Monte histórias de Natal e de festa com a árvore decorada, com os presentes, com os enfeites e com os personagens mini.
- Monte histórias de cidade completa com os prédios comerciais, com os prédios industriais, com as ruas em grade, com os carrinhos de brinquedo e com os 43 personagens mini como multidão.
- Monte histórias de masmorra e de caverna por dentro com os corredores modulares, com as peças de caverna e com o mapa hexagonal de reino.
- Monte histórias de montanha-russa, de minigolfe, de fliperama e de skate com as peças de parque, de campo e de diorama.
- Monte histórias de corrida com os carros de corrida, com os carrinhos de brinquedo e com a pista de bolinhas para explicar física e movimento.
- Monte histórias de cozinha com o fogão, com a chaleira, com o micro-ondas, com a tábua de corte e com os 200 alimentos low-poly.
- Monte cenas de cemitério com neve, de garagem, de porão e de quarto vazio com os 8 HDRIs novos de iluminação.
- Dê material realista a pisos e paredes com as texturas do ambientCG: piso de madeira na sala, tijolo na casa, asfalto na rua, concreto no porão e mármore no interior rico.

## Como importar no pipeline Blender da skill

- Rode tudo com o Blender 4.5.3 LTS portátil em `~/workspace/tools/blender-4.5.3-linux-x64/`.
- Lembre que o `bpy` só funciona dentro do Blender com `blender -b --python cena.py`.
- Siga o padrão do exemplo em `~/workspace/tools/blender-exemplo/cena_peixe_10s.py`. O exemplo limpa a cena, cria materiais chapados com `mat_flat`, cria primitivas com `mesh_obj` e usa shading plano com `poly.use_smooth = False`.
- Importe GLB com o operador de importação do Blender. O GLB já traz malha, materiais e, quando existe, armature com animações.

```python
import bpy
bpy.ops.import_scene.gltf(filepath="cenarios/kenney-nature-kit/Models/GLTF format/tree_oak.glb")
arvore = bpy.context.selected_objects[0]
```

- Importe FBX com `bpy.ops.import_scene.fbx(filepath="caminho/modelo.fbx")` quando o pacote só tiver FBX.
- Anexe objetos de um arquivo blend do Poly Haven com `libraries.load` e ligue cada objeto à coleção da cena.

```python
import bpy
caminho = "objetos/polyhaven/Lantern_01_1k.blend"
with bpy.data.libraries.load(caminho, link=False) as (origem, destino):
    destino.objects = origem.objects
for objeto in destino.objects:
    if objeto is not None:
        bpy.context.collection.objects.link(objeto)
```

- Carregue um HDRI como luz do mundo com nós de ambiente e textura de ambiente.

```python
import bpy
mundo = bpy.data.worlds["World"]
mundo.use_nodes = True
textura = mundo.node_tree.nodes.new("ShaderNodeTexEnvironment")
textura.image = bpy.data.images.load("cenarios/autumn_field_puresky_1k.hdr")
fundo = mundo.node_tree.nodes["Background"]
mundo.node_tree.links.new(textura.outputs["Color"], fundo.inputs["Color"])
```

- Confira a importação antes de animar. Rode 1 frame de teste e confira que o objeto aparece, que está grande no quadro e que o mecanismo está no centro.
- Importe cada modelo uma vez por cena e reutilize o mesmo arquivo blend de base nas cenas do mesmo vídeo. Não importe o mesmo GLB de novo em cada cena com nome diferente.

## Como adaptar um modelo para a história

### Ajuste a escala primeiro

- Meça o objeto depois de importar com `objeto.dimensions` e anote a altura real em metros.
- Normalize o personagem principal para cerca de 1,7 metro de altura e objetos de cena para a altura real que a história pede.
- Aplique a escala com `bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)` depois de ajustar.
- Lembre que a escala varia por fonte. Kenney e Poly Pizza usam escalas diferentes por kit. KayKit usa escala métrica real. Nunca confie na escala que veio no arquivo.
- Saiba que os modelos da NASA têm a escala mais arbitrária do acervo. O Hubble chegou com 458 m, o astronauta com 69 m e a ISS com 26 m. Normalize o Hubble para cerca de 13 m, o astronauta para cerca de 1,90 m e a ISS para cima, perto dos 109 m reais.
- Saiba que os prédios do City Kit Suburban são peças modulares de cerca de 1 m. Escale de 5 a 10 vezes para virar prédio em tamanho de cena.

### Recoloque a cor na paleta do canal

- Troque a cor base do material para a paleta fixa do canal: fundo azul-marinho `#1A305A`, painel `#264476` e laranja de destaque `#FF8C1A`, com texto branco.
- Troque a cor no material com o nó Principled BSDF, no campo Base Color, como faz a função `mat_flat` do exemplo.
- Dê uma cor de destaque por capítulo, sempre em laranja ou em uma cor de apoio do capítulo, e mantenha o resto da cena em azul-marinho e branco.
- Mantenha o material chapado com Roughness em 1.0 para o visual low-poly. Não use brilho especular em modelo low-poly de história.
- Recoloque a textura atlas da KayKit quando a roupa do personagem precisar mudar de cor. Troque a cor na textura e não só no material, porque o GLB usa a textura como cor final.

### Simplifique os polígonos quando o modelo pesar no render

- Conte os vértices com `len(objeto.data.vertices)` antes de decidir.
- Use o modificador Decimate em modo Collapse para reduzir a contagem de faces com pouca mudança de forma. Fonte: manual do Blender sobre o modificador Decimate.
- Comece com Ratio em 0.5 e confira a silhueta antes de aplicar. Desfaça quando a silhueta do personagem mudar.
- Nunca aplique Decimate em malha rigada sem testar a deformação depois. O peso dos ossos pode quebrar quando os vértices somem.
- Prefira o modelo low-poly original a um modelo realista decimado. Um Poly Haven decimado continua com cara de realista e quebra o estilo da série.

### Mantenha o shading plano

- Marque `poly.use_smooth = False` em todos os polígonos do modelo importado para manter o visual facetado low-poly.
- Confira que o modelo não chegou com Smooth ativado. Modelos GLB costumam chegar com normais suavizadas e perdem o visual low-poly se ninguém corrigir.

### Separe o herói do cenário

- Modele o personagem principal por código ou adapte um só modelo de biblioteca para ele e reuse o mesmo modelo em todas as cenas.
- Use os modelos de biblioteca para cenário, objetos e personagens secundários.
- Não troque o modelo do herói no meio do vídeo. A continuidade do personagem é regra da skill. Leia a seção de continuidade em [animação](animacao.md).

## Licenças e o que não pode ser usado

- Não use modelo com CC BY-NC, CC BY-NC-SA ou CC BY-NC-ND em vídeo monetizado. A cláusula NC proíbe uso comercial.
- Não use modelo com CC BY-ND quando precisar mudar o modelo. A cláusula ND proíbe derivados.
- Não use modelo Editorial do Sketchfab ou da Fab em vídeo comercial.
- Não revenda os arquivos crus baixados. Use os modelos dentro do vídeo pronto, não como pacote à venda.
- Não redistribua animações e personagens do Mixamo como arquivos. Use dentro do vídeo pronto.
- Não use o logotipo do Kenney como marca do canal. O logotipo é reservado para projetos oficiais do estúdio.
- Não use modelo de loja paga sem comprar a licença. Baixar grátis não é licença.
- Não confie em licença de site agregador. Confira a licença na página do modelo ou no arquivo LICENSE.txt que veio no download.
- Registre cada modelo usado em um vídeo com fonte, licença e data do download. Guarde o registro junto com o roteiro do vídeo.

## Pendências

- Tente de novo o download dos pacotes Quaternius pelo Google Drive no dia seguinte a 07/11/2026, quando a cota expirar. As pastas Drive já estão mapeadas no inventário. Os pacotes mais úteis são os de peixes animados, monstros animados, dinossauros animados e zumbis animados.
- Peça a conta do BlenderKit ao usuário antes de baixar qualquer ativo de lá.
- Peça a chave gratuita da API do Poly Pizza antes de baixar qualquer modelo de lá.
- Peça o Adobe ID ao usuário antes de rigar qualquer personagem no Mixamo.
- Baixe outros modelos da NASA por sparse checkout quando a história pedir. Ainda faltam 220 modelos GLB no espelho, incluindo o ônibus espacial em outras versões, a sonda Parker em outras versões e o módulo Gateway Core, que pesa 64 MB e foi pulado por peso.
