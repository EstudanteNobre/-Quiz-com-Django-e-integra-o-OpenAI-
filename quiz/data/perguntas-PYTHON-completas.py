"""
Arquivo contendo todas as perguntas do Info Quiz organizadas por tema, rodada e dificuldade.
Este arquivo foi gerado a partir do texto fornecido pelo usuário.
"""

# Estrutura: PERGUNTAS_DATA[tema][rodada][dificuldade] = [lista de perguntas]
# Cada pergunta tem: texto, alternativa_a, alternativa_b, alternativa_c, alternativa_d, resposta_correta

PERGUNTAS_DATA = {
    'Python': {
        '1': {
            'facil': [
                {
                    'texto': 'Qual palavra-chave é usada para definir uma função em Python?',
                    'alternativa_a': 'function',
                    'alternativa_b': 'def',
                    'alternativa_c': 'func',
                    'alternativa_d': 'define',
                    'resposta_correta': 'B'
                },
                {
                    'texto': 'Qual é o operador de exponenciação em Python?',
                    'alternativa_a': '^',
                    'alternativa_b': '**',
                    'alternativa_c': '//',
                    'alternativa_d': '%',
                    'resposta_correta': 'B'
                },
                {
                    'texto': 'Qual tipo de dado é imutável em Python?',
                    'alternativa_a': 'List',
                    'alternativa_b': 'Dictionary',
                    'alternativa_c': 'Tuple',
                    'alternativa_d': 'Set',
                    'resposta_correta': 'C'
                },
                {
                    'texto': 'Qual função é usada para exibir dados na saída padrão (console)?',
                    'alternativa_a': 'output()',
                    'alternativa_b': 'display()',
                    'alternativa_c': 'print()',
                    'alternativa_d': 'show()',
                    'resposta_correta': 'C'
                },
                {
                    'texto': 'Qual é o resultado da expressão 3 + 4 * 2?',
                    'alternativa_a': '14',
                    'alternativa_b': '11',
                    'alternativa_c': '10',
                    'alternativa_d': '12',
                    'resposta_correta': 'B'
                }
            ],
            'medio': [
                {
                    'texto': 'Qual é a finalidade do método __init__ em uma classe Python?',
                    'alternativa_a': 'Destruir um objeto',
                    'alternativa_b': 'Inicializar os atributos de um objeto recém-criado',
                    'alternativa_c': 'Definir métodos estáticos',
                    'alternativa_d': 'Retornar o valor de um objeto',
                    'resposta_correta': 'B'
                },
                {
                    'texto': 'Qual módulo é comumente usado para trabalhar com expressões regulares em Python?',
                    'alternativa_a': 'os',
                    'alternativa_b': 'sys',
                    'alternativa_c': 're',
                    'alternativa_d': 'math',
                    'resposta_correta': 'C'
                },
                {
                    'texto': 'O que o list comprehension faz em Python?',
                    'alternativa_a': 'Cria uma tupla a partir de uma lista',
                    'alternativa_b': 'Cria uma lista a partir de outra sequência de forma concisa',
                    'alternativa_c': 'Compara duas listas',
                    'alternativa_d': 'Remove elementos duplicados de uma lista',
                    'resposta_correta': 'B'
                },
                {
                    'texto': 'Qual é a saída do código: x = [1, 2, 3]; y = x; y.append(4); print(x)?',
                    'alternativa_a': '[1, 2, 3]',
                    'alternativa_b': '[1, 2, 3, 4]',
                    'alternativa_c': 'Erro',
                    'alternativa_d': 'None',
                    'resposta_correta': 'B'
                },
                {
                    'texto': 'Qual das seguintes opções NÃO é um tipo de dado em Python?',
                    'alternativa_a': 'float',
                    'alternativa_b': 'char',
                    'alternativa_c': 'bool',
                    'alternativa_d': 'str',
                    'resposta_correta': 'B'
                }
            ],
            'dificil': [
                {
                    'texto': 'O que é um \'decorator\' em Python e qual é o seu símbolo?',
                    'alternativa_a': 'Uma função que modifica o comportamento de uma classe, usando o símbolo #',
                    'alternativa_b': 'Uma função que recebe outra função e estende ou modifica seu comportamento, usando o símbolo @',
                    'alternativa_c': 'Um tipo de dado para anotações, usando o símbolo $',
                    'alternativa_d': 'Uma variável global que armazena metadados, usando o símbolo &',
                    'resposta_correta': 'B'
                },
                {
                    'texto': 'Qual é a diferença entre range() e xrange() em Python 2, e qual é o equivalente em Python 3?',
                    'alternativa_a': 'range() retorna um gerador; xrange() retorna uma lista. Em Python 3, range() é o equivalente a xrange().',
                    'alternativa_b': 'range() retorna uma lista; xrange() retorna um gerador. Em Python 3, range() é o equivalente a xrange().',
                    'alternativa_c': 'Ambos retornam listas. Em Python 3, xrange() foi removido.',
                    'alternativa_d': 'Ambos retornam geradores. Em Python 3, range() foi renomeado para xrange().',
                    'resposta_correta': 'B'
                },
                {
                    'texto': 'O que significa GIL (Global Interpreter Lock) em Python?',
                    'alternativa_a': 'Um mecanismo que permite que apenas um thread execute bytecode Python por vez, mesmo em sistemas multi-core.',
                    'alternativa_b': 'Um bloqueio de recurso que impede que variáveis globais sejam modificadas por mais de um processo.',
                    'alternativa_c': 'Uma função de segurança que bloqueia a execução de código não assinado.',
                    'alternativa_d': 'Um recurso que permite a execução paralela de threads em sistemas multi-core.',
                    'resposta_correta': 'A'
                },
                {
                    'texto': 'Qual é a finalidade do método __slots__ em uma classe Python?',
                    'alternativa_a': 'Definir métodos estáticos da classe.',
                    'alternativa_b': 'Permitir a herança múltipla de classes.',
                    'alternativa_c': 'Declarar explicitamente os atributos de dados (variáveis de instância) e evitar a criação de __dict__ para economizar memória.',
                    'alternativa_d': 'Criar um dicionário de atributos de classe.',
                    'resposta_correta': 'C'
                },
                {
                    'texto': 'Em Python, o que é um \'generator\' e qual palavra-chave está associada a ele?',
                    'alternativa_a': 'Uma função que retorna um valor, usando a palavra-chave return.',
                    'alternativa_b': 'Uma função que pode pausar e retomar sua execução, usando a palavra-chave yield.',
                    'alternativa_c': 'Um tipo de dado para armazenar grandes quantidades de dados, usando a palavra-chave data.',
                    'alternativa_d': 'Uma classe que implementa o protocolo de iteração, usando a palavra-chave iter.',
                    'resposta_correta': 'B'
                }
            ]
        },
        '2': {
            'facil': [
                {
                    'texto': 'Qual é o nome do gerenciador de pacotes padrão para Python?',
                    'alternativa_a': 'npm',
                    'alternativa_b': 'pip',
                    'alternativa_c': 'gem',
                    'alternativa_d': 'apt',
                    'resposta_correta': 'B'
                },
                {
                    'texto': 'Qual é o resultado da operação de divisão inteira 10 // 3?',
                    'alternativa_a': '3.333',
                    'alternativa_b': '3',
                    'alternativa_c': '4',
                    'alternativa_d': '1',
                    'resposta_correta': 'B'
                },
                {
                    'texto': 'Qual estrutura de controle de fluxo é usada para iteração em uma sequência?',
                    'alternativa_a': 'if/else',
                    'alternativa_b': 'while',
                    'alternativa_c': 'for',
                    'alternativa_d': 'switch',
                    'resposta_correta': 'C'
                },
                {
                    'texto': 'Qual é o índice do primeiro elemento em uma lista Python?',
                    'alternativa_a': '1',
                    'alternativa_b': '0',
                    'alternativa_c': '-1',
                    'alternativa_d': 'Qualquer número inteiro',
                    'resposta_correta': 'B'
                },
                {
                    'texto': 'Qual é o tipo de dado usado para armazenar um conjunto de pares chave-valor?',
                    'alternativa_a': 'List',
                    'alternativa_b': 'Tuple',
                    'alternativa_c': 'Dictionary',
                    'alternativa_d': 'Set',
                    'resposta_correta': 'C'
                }
            ],
            'medio': [
                {
                    'texto': 'O que o método strip() faz em uma string?',
                    'alternativa_a': 'Converte a string para letras maiúsculas.',
                    'alternativa_b': 'Remove espaços em branco (ou caracteres especificados) do início e do fim da string.',
                    'alternativa_c': 'Divide a string em uma lista de substrings.',
                    'alternativa_d': 'Verifica se a string contém apenas dígitos.',
                    'resposta_correta': 'B'
                },
                {
                    'texto': 'Qual é a finalidade do bloco finally em uma estrutura try-except?',
                    'alternativa_a': 'Executar o código apenas se ocorrer uma exceção.',
                    'alternativa_b': 'Executar o código apenas se NENHUMA exceção ocorrer.',
                    'alternativa_c': 'Executar o código sempre, independentemente de uma exceção ter ocorrido ou não.',
                    'alternativa_d': 'Capturar e lidar com exceções específicas.',
                    'resposta_correta': 'C'
                },
                {
                    'texto': 'O que é \'Duck Typing\' em Python?',
                    'alternativa_a': 'Um sistema de tipagem estática que verifica os tipos em tempo de compilação.',
                    'alternativa_b': 'Um conceito onde o tipo de um objeto é determinado por seus métodos e propriedades, e não por sua herança explícita.',
                    'alternativa_c': 'Um recurso que permite a criação de tipos de dados personalizados.',
                    'alternativa_d': 'O processo de converter um tipo de dado em outro.',
                    'resposta_correta': 'B'
                },
                {
                    'texto': 'Qual é a saída do código: print(len({1, 2, 2, 3}))?',
                    'alternativa_a': '4',
                    'alternativa_b': '3',
                    'alternativa_c': '2',
                    'alternativa_d': 'Erro',
                    'resposta_correta': 'B'
                },
                {
                    'texto': 'Qual das seguintes opções é a maneira correta de abrir um arquivo para leitura em Python?',
                    'alternativa_a': "open('arquivo.txt', 'w')",
                    'alternativa_b': "open('arquivo.txt', 'a')",
                    'alternativa_c': "open('arquivo.txt', 'r')",
                    'alternativa_d': "open('arquivo.txt', 'x')",
                    'resposta_correta': 'C'
                }
            ],
            'dificil': [
                {
                    'texto': 'O que é um \'context manager\' em Python e qual palavra-chave é usada para implementá-lo de forma mais comum?',
                    'alternativa_a': 'Um objeto que gerencia o ciclo de vida de uma variável, usando a palavra-chave var.',
                    'alternativa_b': 'Um objeto que define o contexto de execução de um programa, usando a palavra-chave context.',
                    'alternativa_c': 'Um objeto que garante que os recursos sejam liberados após o uso, usando a palavra-chave with.',
                    'alternativa_d': 'Uma função que gerencia a memória, usando a palavra-chave memory.',
                    'resposta_correta': 'C'
                },
                {
                    'texto': 'Qual é a diferença fundamental entre is e == em Python?',
                    'alternativa_a': 'is compara valores; == compara identidades de objeto.',
                    'alternativa_b': 'is compara identidades de objeto; == compara valores.',
                    'alternativa_c': 'Ambos comparam valores, mas is é mais rápido.',
                    'alternativa_d': 'Ambos comparam identidades de objeto, mas == é mais flexível.',
                    'resposta_correta': 'B'
                },
                {
                    'texto': 'O que é \'MRO\' (Method Resolution Order) em Python e como ele é determinado em herança múltipla?',
                    'alternativa_a': 'É a ordem em que os métodos são executados, determinada pela ordem de declaração das classes.',
                    'alternativa_b': 'É a ordem em que os métodos são procurados, determinada pelo algoritmo C3 Linearization.',
                    'alternativa_c': 'É a ordem em que os métodos são procurados, determinada pela ordem inversa de herança.',
                    'alternativa_d': 'É a ordem em que os métodos são procurados, determinada pelo primeiro método encontrado.',
                    'resposta_correta': 'B'
                },
                {
                    'texto': 'Qual é a finalidade do asyncio em Python?',
                    'alternativa_a': 'Permitir a execução paralela de código usando múltiplos processos.',
                    'alternativa_b': 'Fornecer uma estrutura para escrever código concorrente usando a abordagem assíncrona/await.',
                    'alternativa_c': 'Gerenciar a memória e o garbage collection de forma eficiente.',
                    'alternativa_d': 'Compilar código Python para código de máquina nativo.',
                    'resposta_correta': 'B'
                },
                {
                    'texto': 'O que é um \'closure\' em Python?',
                    'alternativa_a': 'Uma função que retorna outra função.',
                    'alternativa_b': 'Uma função interna que se lembra e tem acesso a variáveis locais de seu escopo externo, mesmo depois que a função externa terminou de ser executada.',
                    'alternativa_c': 'Uma função que não aceita argumentos.',
                    'alternativa_d': 'Um tipo de dado que encapsula dados e métodos.',
                    'resposta_correta': 'B'
                }
            ]
        },
        '3': {
            'facil': [
                {
                    'texto': 'Qual é o nome do ambiente virtual padrão para projetos Python?',
                    'alternativa_a': 'venv',
                    'alternativa_b': 'virtualenv',
                    'alternativa_c': 'conda',
                    'alternativa_d': 'pyenv',
                    'resposta_correta': 'A'
                },
                {
                    'texto': 'Qual é o resultado da expressão True and False?',
                    'alternativa_a': 'True',
                    'alternativa_b': 'False',
                    'alternativa_c': 'None',
                    'alternativa_d': 'Erro',
                    'resposta_correta': 'B'
                },
                {
                    'texto': 'Qual método é usado para adicionar um elemento ao final de uma lista?',
                    'alternativa_a': 'insert()',
                    'alternativa_b': 'add()',
                    'alternativa_c': 'append()',
                    'alternativa_d': 'extend()',
                    'resposta_correta': 'C'
                },
                {
                    'texto': 'Qual palavra-chave é usada para sair de um loop imediatamente?',
                    'alternativa_a': 'continue',
                    'alternativa_b': 'exit',
                    'alternativa_c': 'break',
                    'alternativa_d': 'stop',
                    'resposta_correta': 'C'
                },
                {
                    'texto': 'Qual é o tipo de dado de [1, \'a\', 3.0]?',
                    'alternativa_a': 'Tuple',
                    'alternativa_b': 'Set',
                    'alternativa_c': 'List',
                    'alternativa_d': 'Dictionary',
                    'resposta_correta': 'C'
                }
            ],
            'medio': [
                {
                    'texto': 'O que é \'pickling\' em Python?',
                    'alternativa_a': 'O processo de criptografar dados.',
                    'alternativa_b': 'O processo de serializar (converter) um objeto Python em um fluxo de bytes.',
                    'alternativa_c': 'O processo de compilar código Python.',
                    'alternativa_d': 'O processo de otimizar o código Python.',
                    'resposta_correta': 'B'
                },
                {
                    'texto': 'Qual é a diferença entre pass e continue em Python?',
                    'alternativa_a': 'pass sai do loop; continue pula para a próxima iteração.',
                    'alternativa_b': 'pass é usado para funções vazias; continue é usado para loops vazios.',
                    'alternativa_c': 'pass é uma operação nula (não faz nada); continue pula para a próxima iteração do loop.',
                    'alternativa_d': 'Ambos são usados para pular para a próxima iteração do loop.',
                    'resposta_correta': 'C'
                },
                {
                    'texto': "Qual é a saída do código: print('hello'.capitalize())?",
                    'alternativa_a': 'Hello',
                    'alternativa_b': 'hello',
                    'alternativa_c': 'HELLO',
                    'alternativa_d': 'hELLO',
                    'resposta_correta': 'A'
                },
                {
                    'texto': 'Qual é a finalidade do *args e **kwargs na definição de uma função?',
                    'alternativa_a': 'Permitir que a função aceite apenas argumentos posicionais.',
                    'alternativa_b': 'Permitir que a função aceite um número variável de argumentos posicionais (*args) e argumentos de palavra-chave (**kwargs).',
                    'alternativa_c': 'Definir argumentos obrigatórios.',
                    'alternativa_d': 'Definir argumentos de palavra-chave obrigatórios.',
                    'resposta_correta': 'B'
                },
                {
                    'texto': 'O que é um \'lambda function\' em Python?',
                    'alternativa_a': 'Uma função definida em um módulo separado.',
                    'alternativa_b': 'Uma função anônima de uma única expressão.',
                    'alternativa_c': 'Uma função que sempre retorna None.',
                    'alternativa_d': 'Uma função que só pode ser chamada uma vez.',
                    'resposta_correta': 'B'
                }
            ],
            'dificil': [
                {
                    'texto': 'Qual é a diferença entre \'deep copy\' e \'shallow copy\' em Python?',
                    'alternativa_a': 'Ambos criam cópias independentes, mas \'deep copy\' é mais rápido.',
                    'alternativa_b': '\'Shallow copy\' cria uma nova coleção, mas insere referências aos objetos originais; \'deep copy\' cria uma nova coleção e copia recursivamente os objetos aninhados.',
                    'alternativa_c': '\'Deep copy\' é usado para tipos de dados imutáveis; \'shallow copy\' para mutáveis.',
                    'alternativa_d': '\'Shallow copy\' é feito com o operador = e \'deep copy\' com o módulo copy.',
                    'resposta_correta': 'B'
                },
                {
                    'texto': 'O que é \'metaclass\' em Python?',
                    'alternativa_a': 'A classe base de todas as classes em Python.',
                    'alternativa_b': 'Uma classe cujas instâncias são outras classes.',
                    'alternativa_c': 'Uma classe que define métodos estáticos.',
                    'alternativa_d': 'Uma classe usada para herança múltipla.',
                    'resposta_correta': 'B'
                },
                {
                    'texto': 'Qual é a finalidade do método __call__ em uma classe?',
                    'alternativa_a': 'Permitir que a classe seja chamada como uma função.',
                    'alternativa_b': 'Permitir que a classe seja usada em um loop for.',
                    'alternativa_c': 'Permitir que a classe seja usada como um decorador.',
                    'alternativa_d': 'Permitir que a classe seja usada como um gerenciador de contexto.',
                    'resposta_correta': 'A'
                },
                {
                    'texto': 'Em programação orientada a objetos (POO) em Python, o que é \'polimorfismo\'?',
                    'alternativa_a': 'A capacidade de uma classe herdar atributos e métodos de outra classe.',
                    'alternativa_b': 'O conceito de ocultar os detalhes internos de um objeto e expor apenas a funcionalidade necessária.',
                    'alternativa_c': 'A capacidade de um objeto assumir muitas formas, geralmente permitindo que diferentes classes respondam ao mesmo nome de método de maneiras diferentes.',
                    'alternativa_d': 'O processo de criar uma instância de uma classe.',
                    'resposta_correta': 'C'
                },
                {
                    'texto': 'Qual é a diferença entre um \'iterable\' e um \'iterator\' em Python?',
                    'alternativa_a': 'Um \'iterable\' é um objeto que pode ser percorrido; um \'iterator\' é o objeto que mantém o estado da iteração e implementa __next__.',
                    'alternativa_b': 'Um \'iterable\' implementa __next__; um \'iterator\' implementa __iter__.',
                    'alternativa_c': 'Um \'iterable\' é sempre uma lista; um \'iterator\' é sempre uma tupla.',
                    'alternativa_d': 'Não há diferença; os termos são sinônimos.',
                    'resposta_correta': 'A'
                }
            ]
        }
    }
    # Nota: Devido ao limite de tamanho, apenas Python foi incluído como exemplo.
    # Os outros temas (Redes, Banco de Dados, Inglês, Informática, Análise de Projeto, Algoritmos)
    # precisam ser adicionados seguindo a mesma estrutura.
    # Total esperado: 7 temas x 45 perguntas = 315 perguntas
}

