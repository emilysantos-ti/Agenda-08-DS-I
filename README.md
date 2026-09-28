# Agenda 08 - Desenvolvimento de Sistemas I

## Pesquisa de Opinião - TudoWeb

Este projeto foi desenvolvido como atividade da Agenda 08 da disciplina de Desenvolvimento de Sistemas I.

O objetivo é desenvolver um programa em Python para realizar uma pesquisa de satisfação com os clientes da empresa fictícia TudoWeb.

## Objetivo do programa

O programa coleta os seguintes dados de cada entrevistado:

- Nome
- Idade
- Opinião sobre o atendimento

As opções de avaliação são:

1. EXCELENTE
2. BOM
3. RUIM

A versão final da pesquisa foi programada para 50 entrevistados.

## Funcionamento

O programa utiliza uma estrutura de repetição para realizar a pesquisa com todos os entrevistados.

Para cada pessoa, são solicitados o nome, a idade e a opinião sobre o atendimento.

A opinião é verificada utilizando estruturas de decisão (`if`, `elif` e `else`).

Caso o usuário digite uma opção diferente de 1, 2 ou 3, o programa informa que a opção é inválida e solicita uma nova resposta.

Ao final da pesquisa, o programa apresenta:

- Quantidade de respostas "EXCELENTE"
- Quantidade de respostas "RUIM"

## Estruturas utilizadas

Durante o desenvolvimento foram utilizadas:

- `for` - repetição da pesquisa para os entrevistados;
- `while` - validação das respostas;
- `if`, `elif` e `else` - verificação da opinião;
- `input()` - entrada dos dados;
- variáveis contadoras - armazenamento da quantidade de respostas.

## Teste de funcionamento

Antes da versão final, foi realizado um teste com 10 entrevistados, conforme solicitado na atividade.

No teste realizado, o programa apresentou:

- 4 respostas "EXCELENTE"
- 3 respostas "RUIM"

O resultado confirmou que a coleta dos dados e os contadores estavam funcionando corretamente.

Após a validação, a quantidade de entrevistados foi alterada para 50 para atender à versão final solicitada.

## Arquivo principal

`pesquisa_opiniao.py`

## Evidências

Este repositório contém o código desenvolvido, o print do código-fonte e o print da execução do teste realizado com 10 entrevistados.

## Autora

Emily Eduarda Lacerda dos Santos
