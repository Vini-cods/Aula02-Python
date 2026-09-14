# Aula 02 - Equações do 1º grau em Python

Este projeto reúne 12 exercícios de matemática resolvidos com Python. A ideia é
mostrar como transformar um enunciado em uma equação, calcular o valor de `x` e
usar o programa para conferir se a resposta está correta.

## Como o projeto está organizado

- `equacao01.py` até `equacao12.py`: versões resolvidas com os valores do enunciado.
  Elas são boas para estudar o passo a passo e ler os comentários.
- `com_inputs/equacao01.py` até `com_inputs/equacao12.py`: versões interativas.
  Nelas, o programa usa `input()` para receber os valores durante a execução.

Os nomes dos arquivos são iguais nas duas versões para facilitar a comparação.

## Como executar

Abra um terminal nesta pasta e execute um arquivo resolvido:

```text
python equacao01.py
```

Para executar a versão com entradas:

```text
python com_inputs\equacao01.py
```

Em alguns computadores, o comando pode ser `python3` no lugar de `python`.
Nas versões interativas, digite os números pedidos e pressione `Enter`. Os
valores são convertidos para `float`, por isso também é possível testar números
decimais.

## O que foi praticado

- Variáveis para guardar números e resultados.
- Operações de soma, subtração, multiplicação e divisão.
- `input()` para receber dados do usuário.
- `float()` para converter texto em número decimal.
- F-string para montar mensagens com resultados.
- Comparação com `==` para conferir uma solução.
- Organização do raciocínio matemático em comentários.

## Resumo dos exercícios

| Arquivo        | Equação principal   | Ideia da resolução                                |
| -------------- | ------------------- | ------------------------------------------------- |
| `equacao01.py` | `x + 2x = 36`       | `3x = 36`, então `x = 12`.                        |
| `equacao02.py` | `x - x/3 = 20`      | A terça parte de `30` é `10`; a diferença é `20`. |
| `equacao03.py` | `P + 2P + P = 60`   | `4P = 60`, então Pedro tem `15` anos.             |
| `equacao04.py` | `3x - 9 = x`        | `2x = 9`, então `x = 4,5`.                        |
| `equacao05.py` | `3x - 5 = 2x + 1`   | `x = 6`.                                          |
| `equacao06.py` | `x + (x + 1) = 47`  | Os consecutivos são `23` e `24`.                  |
| `equacao07.py` | `x/2 + 7 = 19`      | `x/2 = 12`, então `x = 24`.                       |
| `equacao08.py` | `4x - 8 = 28`       | `4x = 36`, então `x = 9`.                         |
| `equacao09.py` | `4x + 10 = 3x + 22` | `x = 12`.                                         |
| `equacao10.py` | `5x + 2 = 7x`       | `2x = 2`, então `x = 1`.                          |
| `equacao11.py` | `x + 3(x + 1) = 74` | `4x = 71`, então `x = 17,75`.                     |
| `equacao12.py` | `4x - 5 = 2x + 11`  | `2x = 16`, então `x = 8`.                         |

## Como estudar pelos arquivos

1. Leia o problema e escolha uma letra para representar o número desconhecido.
2. Escreva a equação usando as operações descritas no enunciado.
3. Isole o `x`, fazendo a mesma operação nos dois lados da igualdade.
4. Reproduza a conta no código usando variáveis com nomes claros.
5. Confira o resultado substituindo o valor encontrado na equação original.

As linhas de conferência são importantes: não basta o programa mostrar um
número; também precisamos verificar se esse número realmente satisfaz a regra
do exercício.
