"""
Arquivo contendo todas as perguntas do Info Quiz organizadas por tema, rodada e dificuldade.
Este arquivo foi gerado a partir do texto fornecido pelo usuário.
"""

# Estrutura: PERGUNTAS_DATA[tema][rodada][dificuldade] = [lista de perguntas]
# Cada pergunta tem: texto, alternativa_a, alternativa_b, alternativa_c, alternativa_d, resposta_correta

PERGUNTAS_DATA = {
    'Informática': {
        '1': {
            'facil': [
                {
                    'texto': 'Quem é considerado o “pai da computação”?',
                    'alternativa_a': 'Steve Jobs.',
                    'alternativa_b': 'Charles Babbage.',
                    'alternativa_c': 'Alan Turing.',
                    'alternativa_d': 'Bill Gates.',
                    'resposta_correta': 'B'
                },
                {
                    'texto': 'O principal componente responsável pelo processamento de dados é:',
                    'alternativa_a': 'HD.',
                    'alternativa_b': 'Placa de vídeo.',
                    'alternativa_c': 'CPU.',
                    'alternativa_d': 'Memória RAM.',
                    'resposta_correta': 'C'
                },
                {
                    'texto': 'Qual é a função da memória RAM?',
                    'alternativa_a': 'Armazenar dados permanentemente.',
                    'alternativa_b': 'Armazenar dados temporariamente enquanto o computador está ligado.',
                    'alternativa_c': 'Controlar dispositivos externos.',
                    'alternativa_d': 'Alimentar o sistema.',
                    'resposta_correta': 'B'
                },
                {
                    'texto': 'O sistema operacional é um tipo de:',
                    'alternativa_a': 'Hardware.',
                    'alternativa_b': 'Software.',
                    'alternativa_c': 'Memória.',
                    'alternativa_d': 'Processador.',
                    'resposta_correta': 'B'
                },
                {
                    'texto': 'O que significa a sigla “PC”?',
                    'alternativa_a': 'Power Chip.',
                    'alternativa_b': 'Personal Computer.',
                    'alternativa_c': 'Private Control.',
                    'alternativa_d': 'Primary Connection.',
                    'resposta_correta': 'B'
                }
            ],
            'medio': [
                {
                    'texto': 'O sistema binário utiliza apenas os números:',
                    'alternativa_a': '1 e 2.',
                    'alternativa_b': '0 e 1.',
                    'alternativa_c': '1 e 10.',
                    'alternativa_d': '0 e 9.',
                    'resposta_correta': 'B'
                },
                {
                    'texto': 'Quem criou o primeiro algoritmo destinado a ser processado por uma máquina?',
                    'alternativa_a': 'Ada Lovelace.',
                    'alternativa_b': 'Alan Turing.',
                    'alternativa_c': 'Grace Hopper.',
                    'alternativa_d': 'Konrad Zuse.',
                    'resposta_correta': 'A'
                },
                {
                    'texto': 'O que significa a sigla CPU?',
                    'alternativa_a': 'Computer Power Unit.',
                    'alternativa_b': 'Central Processing Unit.',
                    'alternativa_c': 'Core Processing User.',
                    'alternativa_d': 'Control Processing Unit.',
                    'resposta_correta': 'B'
                },
                {
                    'texto': 'O que é um software livre?',
                    'alternativa_a': 'Um software gratuito, mas sem código aberto.',
                    'alternativa_b': 'Um software com código aberto e uso livre.',
                    'alternativa_c': 'Um software sem licença.',
                    'alternativa_d': 'Um programa pirata.',
                    'resposta_correta': 'B'
                },
                {
                    'texto': 'Qual a principal função do sistema operacional?',
                    'alternativa_a': 'Organizar o hardware e gerenciar os recursos do sistema.',
                    'alternativa_b': 'Executar apenas jogos.',
                    'alternativa_c': 'Controlar a energia do computador.',
                    'alternativa_d': 'Substituir o BIOS.',
                    'resposta_correta': 'A'
                }
            ],
            'dificil': [
                {
                    'texto': 'O conceito de “bug” na computação surgiu:',
                    'alternativa_a': 'De um erro em software.',
                    'alternativa_b': 'De um inseto real encontrado em um computador.',
                    'alternativa_c': 'De falhas na internet.',
                    'alternativa_d': 'De erros lógicos em linguagens.',
                    'resposta_correta': 'B'
                },
                {
                    'texto': 'A “Lei de Moore” prevê que:',
                    'alternativa_a': 'A velocidade dos HDs dobraria a cada 18 meses.',
                    'alternativa_b': 'O número de transistores em um chip dobraria a cada 18-24 meses.',
                    'alternativa_c': 'A memória RAM duplicaria a cada ano.',
                    'alternativa_d': 'Os preços dos chips diminuiriam.',
                    'resposta_correta': 'B'
                },
                {
                    'texto': 'O ENIAC utilizava:',
                    'alternativa_a': 'Transistores.',
                    'alternativa_b': 'Válvulas eletrônicas.',
                    'alternativa_c': 'Microchips.',
                    'alternativa_d': 'Discos rígidos.',
                    'resposta_correta': 'B'
                },
                {
                    'texto': 'Qual a principal função da BIOS?',
                    'alternativa_a': 'Armazenar dados do usuário.',
                    'alternativa_b': 'Iniciar e testar o hardware do sistema.',
                    'alternativa_c': 'Controlar a energia.',
                    'alternativa_d': 'Salvar arquivos.',
                    'resposta_correta': 'B'
                },
                {
                    'texto': 'O primeiro sistema operacional da Microsoft foi:',
                    'alternativa_a': 'MS-DOS.',
                    'alternativa_b': 'Windows 95.',
                    'alternativa_c': 'Windows XP.',
                    'alternativa_d': 'Xenix.',
                    'resposta_correta': 'A'
                }
            ]
        },
        '2': {
            'facil': [
                {
                    'texto': 'Qual desses é um sistema operacional?',
                    'alternativa_a': 'Excel.',
                    'alternativa_b': 'Windows.',
                    'alternativa_c': 'Mouse.',
                    'alternativa_d': 'BIOS.',
                    'resposta_correta': 'B'
                },
                {
                    'texto': 'O mouse e o teclado são exemplos de:',
                    'alternativa_a': 'Saída.',
                    'alternativa_b': 'Entrada.',
                    'alternativa_c': 'Armazenamento.',
                    'alternativa_d': 'Processamento.',
                    'resposta_correta': 'B'
                },
                {
                    'texto': 'O primeiro computador eletrônico do mundo foi o:',
                    'alternativa_a': 'Mark I.',
                    'alternativa_b': 'ENIAC.',
                    'alternativa_c': 'Altair 8800.',
                    'alternativa_d': 'UNIVAC.',
                    'resposta_correta': 'B'
                },
                {
                    'texto': 'Qual destes não é um dispositivo de armazenamento?',
                    'alternativa_a': 'HD.',
                    'alternativa_b': 'Pen drive.',
                    'alternativa_c': 'Impressora.',
                    'alternativa_d': 'SSD.',
                    'resposta_correta': 'C'
                },
                {
                    'texto': 'O que é software?',
                    'alternativa_a': 'Parte física do computador.',
                    'alternativa_b': 'Programas e instruções que controlam o hardware.',
                    'alternativa_c': 'Cabos e conectores.',
                    'alternativa_d': 'Dispositivo de entrada.',
                    'resposta_correta': 'B'
                }
            ],
            'medio': [
                {
                    'texto': 'O que é firmware?',
                    'alternativa_a': 'Um vírus.',
                    'alternativa_b': 'Um software gravado em hardware.',
                    'alternativa_c': 'Um programa temporário.',
                    'alternativa_d': 'Um tipo de driver.',
                    'resposta_correta': 'B'
                },
                {
                    'texto': 'O primeiro computador pessoal vendido comercialmente foi o:',
                    'alternativa_a': 'ENIAC.',
                    'alternativa_b': 'Altair 8800.',
                    'alternativa_c': 'UNIVAC.',
                    'alternativa_d': 'IBM 360.',
                    'resposta_correta': 'B'
                },
                {
                    'texto': 'Qual dispositivo não é de saída?',
                    'alternativa_a': 'Monitor.',
                    'alternativa_b': 'Impressora.',
                    'alternativa_c': 'Microfone.',
                    'alternativa_d': 'Caixa de som.',
                    'resposta_correta': 'C'
                },
                {
                    'texto': 'O que faz a memória ROM?',
                    'alternativa_a': 'Armazena dados temporários.',
                    'alternativa_b': 'Armazena instruções permanentes.',
                    'alternativa_c': 'Executa programas.',
                    'alternativa_d': 'Gerencia arquivos.',
                    'resposta_correta': 'B'
                },
                {
                    'texto': 'Qual componente é essencial para conectar o computador à internet?',
                    'alternativa_a': 'GPU.',
                    'alternativa_b': 'Modem.',
                    'alternativa_c': 'SSD.',
                    'alternativa_d': 'Fonte.',
                    'resposta_correta': 'B'
                }
            ],
            'dificil': [
                {
                    'texto': 'Qual das opções é um exemplo de software de aplicação?',
                    'alternativa_a': 'Windows.',
                    'alternativa_b': 'Excel.',
                    'alternativa_c': 'BIOS.',
                    'alternativa_d': 'Firmware.',
                    'resposta_correta': 'B'
                },
                {
                    'texto': 'A unidade lógica e aritmética (ALU) é responsável por:',
                    'alternativa_a': 'Armazenar dados.',
                    'alternativa_b': 'Executar cálculos matemáticos e lógicos.',
                    'alternativa_c': 'Controlar periféricos.',
                    'alternativa_d': 'Reproduzir som.',
                    'resposta_correta': 'B'
                },
                {
                    'texto': 'A arquitetura Von Neumann é baseada na ideia de:',
                    'alternativa_a': 'Separar memória e processador.',
                    'alternativa_b': 'Usar uma mesma memória para dados e instruções.',
                    'alternativa_c': 'Multiprocessadores independentes.',
                    'alternativa_d': 'Processamento paralelo.',
                    'resposta_correta': 'B'
                },
                {
                    'texto': 'O primeiro navegador gráfico popular foi o:',
                    'alternativa_a': 'Netscape Navigator.',
                    'alternativa_b': 'Internet Explorer.',
                    'alternativa_c': 'Mosaic.',
                    'alternativa_d': 'Chrome.',
                    'resposta_correta': 'A'
                },
                {
                    'texto': 'Qual é a diferença entre SSD e HD?',
                    'alternativa_a': 'SSD usa discos magnéticos.',
                    'alternativa_b': 'SSD é mais rápido e usa memória flash.',
                    'alternativa_c': 'HD é mais rápido.',
                    'alternativa_d': 'SSD armazena menos dados sempre.',
                    'resposta_correta': 'B'
                }
            ]
        },
        '3': {
            'facil': [
                {
                    'texto': 'O que é “boot”?',
                    'alternativa_a': 'Instalação de aplicativos.',
                    'alternativa_b': 'Processo de inicialização do sistema.',
                    'alternativa_c': 'Remoção de vírus.',
                    'alternativa_d': 'Reinício de programas.',
                    'resposta_correta': 'B'
                },
                {
                    'texto': 'O sistema operacional Linux é:',
                    'alternativa_a': 'Pago e fechado.',
                    'alternativa_b': 'Aberto e gratuito.',
                    'alternativa_c': 'Exclusivo da Microsoft.',
                    'alternativa_d': 'Um antivírus.',
                    'resposta_correta': 'B'
                },
                {
                    'texto': 'A unidade de medida usada para armazenar dados é:',
                    'alternativa_a': 'Watt.',
                    'alternativa_b': 'Byte.',
                    'alternativa_c': 'Volt.',
                    'alternativa_d': 'Hertz.',
                    'resposta_correta': 'B'
                },
                {
                    'texto': 'O componente que exibe imagens no monitor é:',
                    'alternativa_a': 'Placa de som.',
                    'alternativa_b': 'Placa de vídeo.',
                    'alternativa_c': 'Processador.',
                    'alternativa_d': 'SSD.',
                    'resposta_correta': 'B'
                },
                {
                    'texto': 'O inventor do primeiro mouse foi:',
                    'alternativa_a': 'Alan Turing.',
                    'alternativa_b': 'Douglas Engelbart.',
                    'alternativa_c': 'Bill Gates.',
                    'alternativa_d': 'Tim Berners-Lee.',
                    'resposta_correta': 'B'
                }
            ],
            'medio': [
                {
                    'texto': 'O termo “hardware” se refere a:',
                    'alternativa_a': 'Programas.',
                    'alternativa_b': 'Peças físicas do computador.',
                    'alternativa_c': 'Rede.',
                    'alternativa_d': 'Sistema operacional.',
                    'resposta_correta': 'B'
                },
                {
                    'texto': 'O sistema operacional Android é baseado em:',
                    'alternativa_a': 'Linux.',
                    'alternativa_b': 'Windows.',
                    'alternativa_c': 'UNIX.',
                    'alternativa_d': 'MacOS.',
                    'resposta_correta': 'A'
                },
                {
                    'texto': 'Quem desenvolveu a linguagem C?',
                    'alternativa_a': 'Steve Wozniak.',
                    'alternativa_b': 'Dennis Ritchie.',
                    'alternativa_c': 'Alan Kay.',
                    'alternativa_d': 'Linus Torvalds.',
                    'resposta_correta': 'B'
                },
                {
                    'texto': 'Qual é o principal tipo de memória volátil?',
                    'alternativa_a': 'ROM.',
                    'alternativa_b': 'RAM.',
                    'alternativa_c': 'SSD.',
                    'alternativa_d': 'Cache.',
                    'resposta_correta': 'B'
                },
                {
                    'texto': 'O processador Intel 4004 foi o primeiro:',
                    'alternativa_a': 'Microprocessador comercial.',
                    'alternativa_b': 'Sistema operacional.',
                    'alternativa_c': 'Armazenamento óptico.',
                    'alternativa_d': 'Monitor digital.',
                    'resposta_correta': 'A'
                }
            ],
            'dificil': [
                {
                    'texto': 'O componente responsável por resfriar o processador é:',
                    'alternativa_a': 'Cooler.',
                    'alternativa_b': 'Fonte.',
                    'alternativa_c': 'Placa-mãe.',
                    'alternativa_d': 'Bateria.',
                    'resposta_correta': 'A'
                },
                {
                    'texto': 'O Linux foi criado por:',
                    'alternativa_a': 'Linus Torvalds.',
                    'alternativa_b': 'Bill Gates.',
                    'alternativa_c': 'Steve Jobs.',
                    'alternativa_d': 'Alan Turing.',
                    'resposta_correta': 'A'
                },
                {
                    'texto': 'A linguagem Assembly é classificada como:',
                    'alternativa_a': 'Alta nível.',
                    'alternativa_b': 'Baixo nível.',
                    'alternativa_c': 'Visual.',
                    'alternativa_d': 'Interativa.',
                    'resposta_correta': 'B'
                },
                {
                    'texto': 'O que caracteriza o software de sistema?',
                    'alternativa_a': 'É usado para entretenimento.',
                    'alternativa_b': 'Gerencia hardware e recursos do computador.',
                    'alternativa_c': 'Serve apenas para edição de textos.',
                    'alternativa_d': 'É instalado em celulares apenas.',
                    'resposta_correta': 'B'
                },
                {
                    'texto': 'O primeiro microprocessador da Intel, o 4004, foi lançado em:',
                    'alternativa_a': '1965.',
                    'alternativa_b': '1971.',
                    'alternativa_c': '1984.',
                    'alternativa_d': '1990.',
                    'resposta_correta': 'B'
                }
            ]
        }
    }
}


