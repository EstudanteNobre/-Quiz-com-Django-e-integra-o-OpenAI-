"""
Arquivo contendo todas as perguntas do Info Quiz organizadas por tema, rodada e dificuldade.
Este arquivo foi gerado a partir do texto fornecido pelo usuário.
"""

# Estrutura: PERGUNTAS_DATA[tema][rodada][dificuldade] = [lista de perguntas]
# Cada pergunta tem: texto, alternativa_a, alternativa_b, alternativa_c, alternativa_d, resposta_correta

PERGUNTAS_DATA = {
    'Algoritmos': {
        '1': {
            'facil': [
                {
                    'texto': 'O que é um algoritmo?',
                    'alternativa_a': 'Um software completo.',
                    'alternativa_b': 'Um conjunto de instruções ordenadas para resolver um problema.',
                    'alternativa_c': 'Um hardware.',
                    'alternativa_d': 'Um banco de dados.',
                    'resposta_correta': 'B'
                },
                {
                    'texto': 'Em um algoritmo, uma variável serve para:',
                    'alternativa_a': 'Guardar informações temporariamente.',
                    'alternativa_b': 'Exibir dados na tela.',
                    'alternativa_c': 'Criar laços infinitos.',
                    'alternativa_d': 'Interromper o programa.',
                    'resposta_correta': 'A'
                },
                {
                    'texto': 'A estrutura de sequência executa:',
                    'alternativa_a': 'Um bloco de comandos apenas se uma condição for verdadeira.',
                    'alternativa_b': 'Um bloco repetidamente.',
                    'alternativa_c': 'Os comandos em ordem, um após o outro.',
                    'alternativa_d': 'Nenhum comando.',
                    'resposta_correta': 'C'
                },
                {
                    'texto': 'Um exemplo de estrutura condicional é:',
                    'alternativa_a': 'para.',
                    'alternativa_b': 'se...então...senão.',
                    'alternativa_c': 'enquanto.',
                    'alternativa_d': 'escreva.',
                    'resposta_correta': 'B'
                },
                {
                    'texto': 'O que faz a estrutura enquanto?',
                    'alternativa_a': 'Repete enquanto a condição for verdadeira.',
                    'alternativa_b': 'Executa apenas uma vez.',
                    'alternativa_c': 'Verifica a entrada do usuário.',
                    'alternativa_d': 'Encerra o programa.',
                    'resposta_correta': 'A'
                }
            ],
            'medio': [
                {
                    'texto': 'Em um algoritmo, o comando para i de 1 até 5 executa:',
                    'alternativa_a': '6 vezes.',
                    'alternativa_b': '5 vezes.',
                    'alternativa_c': '4 vezes.',
                    'alternativa_d': '1 vez.',
                    'resposta_correta': 'B'
                },
                {
                    'texto': 'O comando repita...até executa:',
                    'alternativa_a': 'Enquanto a condição for verdadeira.',
                    'alternativa_b': 'Até que a condição seja verdadeira.',
                    'alternativa_c': 'Somente uma vez.',
                    'alternativa_d': 'Indefinidamente.',
                    'resposta_correta': 'B'
                },
                {
                    'texto': 'Qual é o resultado da expressão (5 > 3) e (2 < 4)?',
                    'alternativa_a': 'Falso.',
                    'alternativa_b': 'Verdadeiro.',
                    'alternativa_c': 'Erro.',
                    'alternativa_d': 'Nulo.',
                    'resposta_correta': 'B'
                },
                {
                    'texto': 'O comando se aninhado significa:',
                    'alternativa_a': 'Vários “se” dentro de outro “se”.',
                    'alternativa_b': 'Estruturas paralelas.',
                    'alternativa_c': 'Um loop.',
                    'alternativa_d': 'Um caso único.',
                    'resposta_correta': 'A'
                },
                {
                    'texto': 'O que é um vetor em algoritmos?',
                    'alternativa_a': 'Um tipo de dado simples.',
                    'alternativa_b': 'Uma variável que armazena vários valores do mesmo tipo.',
                    'alternativa_c': 'Um operador lógico.',
                    'alternativa_d': 'Uma função.',
                    'resposta_correta': 'B'
                }
            ],
            'dificil': [
                {
                    'texto': 'O que significa a complexidade O(n²) de um algoritmo?',
                    'alternativa_a': 'Cresce linearmente.',
                    'alternativa_b': 'Cresce quadraticamente com a entrada.',
                    'alternativa_c': 'Cresce exponencialmente.',
                    'alternativa_d': 'É constante.',
                    'resposta_correta': 'B'
                },
                {
                    'texto': 'O algoritmo de busca binária só pode ser aplicado se:',
                    'alternativa_a': 'Os dados estiverem desordenados.',
                    'alternativa_b': 'Os dados estiverem ordenados.',
                    'alternativa_c': 'Existirem dados duplicados.',
                    'alternativa_d': 'O vetor for pequeno.',
                    'resposta_correta': 'B'
                },
                {
                    'texto': 'O algoritmo de ordenação bolha (Bubble Sort) funciona por:',
                    'alternativa_a': 'Divisão e conquista.',
                    'alternativa_b': 'Trocas sucessivas de elementos adjacentes.',
                    'alternativa_c': 'Inserção direta.',
                    'alternativa_d': 'Seleção de pivôs.',
                    'resposta_correta': 'B'
                },
                {
                    'texto': 'Um algoritmo recursivo é aquele que:',
                    'alternativa_a': 'Chama a si mesmo.',
                    'alternativa_b': 'Nunca termina.',
                    'alternativa_c': 'Não tem retorno.',
                    'alternativa_d': 'Usa apenas laços.',
                    'resposta_correta': 'A'
                },
                {
                    'texto': 'O pseudocódigo é importante porque:',
                    'alternativa_a': 'É a linguagem de máquina.',
                    'alternativa_b': 'Ajuda a representar a lógica sem depender de uma linguagem específica.',
                    'alternativa_c': 'Substitui o código-fonte.',
                    'alternativa_d': 'Serve apenas para fluxogramas.',
                    'resposta_correta': 'B'
                }
            ]
        },
        '2': {
            'facil': [
                {
                    'texto': 'Em algoritmos, entrada significa:',
                    'alternativa_a': 'Dados fornecidos pelo usuário.',
                    'alternativa_b': 'Resultados do programa.',
                    'alternativa_c': 'Processamento interno.',
                    'alternativa_d': 'Saída de texto.',
                    'resposta_correta': 'A'
                },
                {
                    'texto': 'O comando escreva() ou print() serve para:',
                    'alternativa_a': 'Ler dados.',
                    'alternativa_b': 'Exibir dados na tela.',
                    'alternativa_c': 'Calcular somas.',
                    'alternativa_d': 'Armazenar variáveis.',
                    'resposta_correta': 'B'
                },
                {
                    'texto': 'Qual é o operador de igualdade?',
                    'alternativa_a': '=',
                    'alternativa_b': '==',
                    'alternativa_c': '!=',
                    'alternativa_d': '=>',
                    'resposta_correta': 'B'
                },
                {
                    'texto': 'Um algoritmo em pseudocódigo é:',
                    'alternativa_a': 'Um programa executável.',
                    'alternativa_b': 'Uma descrição textual das instruções de forma lógica.',
                    'alternativa_c': 'Um erro de sintaxe.',
                    'alternativa_d': 'Um código binário.',
                    'resposta_correta': 'B'
                },
                {
                    'texto': 'O que significa fluxograma?',
                    'alternativa_a': 'Representação gráfica de um algoritmo.',
                    'alternativa_b': 'Diagrama de classes.',
                    'alternativa_c': 'Estrutura de banco de dados.',
                    'alternativa_d': 'Código-fonte.',
                    'resposta_correta': 'A'
                }
            ],
            'medio': [
                {
                    'texto': 'Em um vetor de 10 posições, o primeiro índice normalmente é:',
                    'alternativa_a': '0.',
                    'alternativa_b': '1.',
                    'alternativa_c': '10.',
                    'alternativa_d': '-1.',
                    'resposta_correta': 'A'
                },
                {
                    'texto': 'O que é uma função em um algoritmo?',
                    'alternativa_a': 'Um conjunto de instruções que retorna um valor.',
                    'alternativa_b': 'Um laço infinito.',
                    'alternativa_c': 'Um tipo de variável.',
                    'alternativa_d': 'Um operador.',
                    'resposta_correta': 'A'
                },
                {
                    'texto': 'E um procedimento?',
                    'alternativa_a': 'Um conjunto de instruções que não retorna valor.',
                    'alternativa_b': 'Um loop.',
                    'alternativa_c': 'Uma variável.',
                    'alternativa_d': 'Uma constante.',
                    'resposta_correta': 'A'
                },
                {
                    'texto': 'O comando interrompa (break) faz:',
                    'alternativa_a': 'Reinicia o loop.',
                    'alternativa_b': 'Sai imediatamente do loop.',
                    'alternativa_c': 'Continua o loop.',
                    'alternativa_d': 'Recomeça o algoritmo.',
                    'resposta_correta': 'B'
                },
                {
                    'texto': 'A modularização de um algoritmo serve para:',
                    'alternativa_a': 'Dividir o problema em partes menores.',
                    'alternativa_b': 'Aumentar o tamanho do código.',
                    'alternativa_c': 'Complicar o programa.',
                    'alternativa_d': 'Ignorar funções.',
                    'resposta_correta': 'A'
                }
            ],
            'dificil': [
                {
                    'texto': 'O algoritmo de seleção (Selection Sort) faz:',
                    'alternativa_a': 'Trocas aleatórias.',
                    'alternativa_b': 'Escolhe o menor elemento e coloca na posição correta.',
                    'alternativa_c': 'Multiplica os valores.',
                    'alternativa_d': 'Usa pilhas.',
                    'resposta_correta': 'B'
                },
                {
                    'texto': 'A recursão precisa de:',
                    'alternativa_a': 'Um caso base e uma chamada recursiva.',
                    'alternativa_b': 'Um laço infinito.',
                    'alternativa_c': 'Uma função sem retorno.',
                    'alternativa_d': 'Um operador lógico.',
                    'resposta_correta': 'A'
                },
                {
                    'texto': 'A diferença entre pilha e fila é:',
                    'alternativa_a': 'Pilha: FIFO / Fila: LIFO.',
                    'alternativa_b': 'Pilha: LIFO / Fila: FIFO.',
                    'alternativa_c': 'Ambas FIFO.',
                    'alternativa_d': 'Ambas LIFO.',
                    'resposta_correta': 'B'
                },
                {
                    'texto': 'Em algoritmos de busca linear, a complexidade é:',
                    'alternativa_a': 'O(1).',
                    'alternativa_b': 'O(n).',
                    'alternativa_c': 'O(log n).',
                    'alternativa_d': 'O(n²).',
                    'resposta_correta': 'B'
                },
                {
                    'texto': 'A análise de complexidade mede:',
                    'alternativa_a': 'O tamanho do código.',
                    'alternativa_b': 'O tempo e o espaço que o algoritmo consome.',
                    'alternativa_c': 'A legibilidade do código.',
                    'alternativa_d': 'A quantidade de variáveis.',
                    'resposta_correta': 'B'
                }
            ]
        },
        '3': {
            'facil': [
                {
                    'texto': 'O símbolo de decisão em um fluxograma é:',
                    'alternativa_a': 'Retângulo.',
                    'alternativa_b': 'Losango.',
                    'alternativa_c': 'Círculo.',
                    'alternativa_d': 'Triângulo.',
                    'resposta_correta': 'B'
                },
                {
                    'texto': 'A saída de um algoritmo é:',
                    'alternativa_a': 'O dado inserido pelo usuário.',
                    'alternativa_b': 'O resultado gerado após o processamento.',
                    'alternativa_c': 'O comando de repetição.',
                    'alternativa_d': 'O pseudocódigo.',
                    'resposta_correta': 'B'
                },
                {
                    'texto': 'O comando de atribuição em algoritmos pode ser representado por:',
                    'alternativa_a': '⇐ ou :=.',
                    'alternativa_b': '==.',
                    'alternativa_c': '=>.',
                    'alternativa_d': '++.',
                    'resposta_correta': 'A'
                },
                {
                    'texto': 'A operação “x ← x + 1” representa:',
                    'alternativa_a': 'Decremento.',
                    'alternativa_b': 'Incremento.',
                    'alternativa_c': 'Multiplicação.',
                    'alternativa_d': 'Divisão.',
                    'resposta_correta': 'B'
                },
                {
                    'texto': 'O tipo de dado lógico (booleano) aceita:',
                    'alternativa_a': 'Letras.',
                    'alternativa_b': 'Números.',
                    'alternativa_c': 'Verdadeiro ou Falso.',
                    'alternativa_d': 'Texto.',
                    'resposta_correta': 'C'
                }
            ],
            'medio': [
                {
                    'texto': 'O que faz o operador % (módulo)?',
                    'alternativa_a': 'Soma.',
                    'alternativa_b': 'Resto da divisão.',
                    'alternativa_c': 'Multiplicação.',
                    'alternativa_d': 'Potência.',
                    'resposta_correta': 'B'
                },
                {
                    'texto': 'Um algoritmo que verifica se um número é par ou ímpar utiliza:',
                    'alternativa_a': 'O operador lógico OU.',
                    'alternativa_b': 'O operador de módulo (%).',
                    'alternativa_c': 'O operador de soma.',
                    'alternativa_d': 'O operador de multiplicação.',
                    'resposta_correta': 'B'
                },
                {
                    'texto': 'O loop infinito ocorre quando:',
                    'alternativa_a': 'A condição nunca se torna falsa.',
                    'alternativa_b': 'Há erro de sintaxe.',
                    'alternativa_c': 'O algoritmo para sozinho.',
                    'alternativa_d': 'O programa compila.',
                    'resposta_correta': 'A'
                },
                {
                    'texto': 'O que é um contador?',
                    'alternativa_a': 'Variável usada para contar iterações.',
                    'alternativa_b': 'Um tipo de vetor.',
                    'alternativa_c': 'Um comando condicional.',
                    'alternativa_d': 'Um operador.',
                    'resposta_correta': 'A'
                },
                {
                    'texto': 'O acumulador serve para:',
                    'alternativa_a': 'Guardar um único valor fixo.',
                    'alternativa_b': 'Somar valores ao longo da execução.',
                    'alternativa_c': 'Limitar loops.',
                    'alternativa_d': 'Reiniciar variáveis.',
                    'resposta_correta': 'B'
                }
            ],
            'dificil': [
                {
                    'texto': 'Um vetor bidimensional também é chamado de:',
                    'alternativa_a': 'Lista.',
                    'alternativa_b': 'Matriz.',
                    'alternativa_c': 'Fila.',
                    'alternativa_d': 'Pilha.',
                    'resposta_correta': 'B'
                },
                {
                    'texto': 'O que é um algoritmo iterativo?',
                    'alternativa_a': 'Que utiliza chamadas recursivas.',
                    'alternativa_b': 'Que repete instruções com laços.',
                    'alternativa_c': 'Que não usa condições.',
                    'alternativa_d': 'Que termina sem execução.',
                    'resposta_correta': 'B'
                },
                {
                    'texto': 'Em busca binária, o vetor é dividido:',
                    'alternativa_a': 'Em três partes.',
                    'alternativa_b': 'Ao meio a cada iteração.',
                    'alternativa_c': 'Em blocos de 10.',
                    'alternativa_d': 'Aleatoriamente.',
                    'resposta_correta': 'B'
                },
                {
                    'texto': 'A eficiência de um algoritmo depende de:',
                    'alternativa_a': 'Seu consumo de recursos e tempo de execução.',
                    'alternativa_b': 'Tamanho do código.',
                    'alternativa_c': 'Linguagem usada.',
                    'alternativa_d': 'Nome das variáveis.',
                    'resposta_correta': 'A'
                },
                {
                    'texto': 'O algoritmo de inserção (Insertion Sort) é mais eficiente:',
                    'alternativa_a': 'Em vetores aleatórios.',
                    'alternativa_b': 'Em vetores quase ordenados.',
                    'alternativa_c': 'Em vetores muito grandes.',
                    'alternativa_d': 'Nunca é eficiente.',
                    'resposta_correta': 'B'
                }
            ]
        }
    }
}


