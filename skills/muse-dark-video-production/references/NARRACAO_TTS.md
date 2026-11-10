# Narração, TTS e legendas

## Texto falado limpo
Mantenha dois campos separados:
- `NARRACAO_FALADA`: somente as palavras que devem ser pronunciadas.
- `DIRECAO_DE_VOZ`: tom, ritmo, emoção e pausas; nunca enviar como fala.

Exemplo:
NARRACAO_FALADA: "Você ouviu isso? A porta estava trancada."
DIRECAO_DE_VOZ: "Tom baixo e intrigante. Pequena pausa entre as frases."

## Pontuação
A pontuação controla entonação e pausa. Não é para ser pronunciada. Nunca escreva nomes de sinais de pontuação como instruções dentro do texto falado.
Se a ferramenta pronunciar “ponto”, “vírgula” ou qualquer instrução, limpe o texto de entrada e teste novamente.
SSML só deve ser usado quando a ferramenta confirmar suporte. Não suponha que qualquer TTS interprete tags SSML.

## Legendas
- Transcrever exatamente a fala.
- Não incluir notas de direção.
- Usar linhas curtas e legíveis.
- Sincronizar entrada/saída com a voz.
- Revisar nomes próprios, números e acentos.
- Não cobrir o assunto principal nem a área de interface.
