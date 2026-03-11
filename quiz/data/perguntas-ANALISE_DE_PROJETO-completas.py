"""
Arquivo contendo todas as perguntas do Info Quiz organizadas por tema, rodada e dificuldade.
Este arquivo foi gerado a partir do texto fornecido pelo usuário.
"""

# Estrutura: PERGUNTAS_DATA[tema][rodada][dificuldade] = [lista de perguntas]
# Cada pergunta tem: texto, alternativa_a, alternativa_b, alternativa_c, alternativa_d, resposta_correta

PERGUNTAS_DATA = {
    'Análise de Projeto': {
        '1': {
            'facil': [
                {
                    'texto': 'A Análise de Sistemas tem como objetivo principal:',
                    'alternativa_a': 'Criar hardware.',
                    'alternativa_b': 'Entender e modelar as necessidades do usuário.',
                    'alternativa_c': 'Programar o sistema.',
                    'alternativa_d': 'Executar testes de software.',
                    'resposta_correta': 'B'
                },
                {
                    'texto': 'O que é um sistema?',
                    'alternativa_a': 'Um conjunto de partes independentes.',
                    'alternativa_b': 'Um conjunto de elementos inter-relacionados com um objetivo comum.',
                    'alternativa_c': 'Um software isolado.',
                    'alternativa_d': 'Apenas uma base de dados.',
                    'resposta_correta': 'B'
                },
                {
                    'texto': 'O primeiro passo no desenvolvimento de sistemas é:',
                    'alternativa_a': 'Implantação.',
                    'alternativa_b': 'Análise de requisitos.',
                    'alternativa_c': 'Codificação.',
                    'alternativa_d': 'Testes.',
                    'resposta_correta': 'B'
                },
                {
                    'texto': 'O que significa a sigla UML?',
                    'alternativa_a': 'Universal Modeling Language.',
                    'alternativa_b': 'Unified Modeling Language.',
                    'alternativa_c': 'Universal Model Logic.',
                    'alternativa_d': 'User Model Language.',
                    'resposta_correta': 'B'
                },
                {
                    'texto': 'Em análise de sistemas, requisito funcional é:',
                    'alternativa_a': 'A cor da interface.',
                    'alternativa_b': 'O que o sistema deve fazer.',
                    'alternativa_c': 'O tempo de resposta.',
                    'alternativa_d': 'O desempenho.',
                    'resposta_correta': 'B'
                }
            ],
            'medio': [
                {
                    'texto': 'O diagrama de classes representa:',
                    'alternativa_a': 'O comportamento do usuário.',
                    'alternativa_b': 'A estrutura estática do sistema e seus relacionamentos.',
                    'alternativa_c': 'O fluxo de dados.',
                    'alternativa_d': 'O cronograma de desenvolvimento.',
                    'resposta_correta': 'B'
                },
                {
                    'texto': 'O modelo em espiral combina:',
                    'alternativa_a': 'Desenvolvimento e testes simultâneos.',
                    'alternativa_b': 'Ciclos curtos e protótipos.',
                    'alternativa_c': 'Fases lineares.',
                    'alternativa_d': 'Desenvolvimento sem documentação.',
                    'resposta_correta': 'A'
                },
                {
                    'texto': 'Um caso de uso descreve:',
                    'alternativa_a': 'O comportamento do sistema em um cenário específico.',
                    'alternativa_b': 'A estrutura do banco de dados.',
                    'alternativa_c': 'O código-fonte.',
                    'alternativa_d': 'O manual do usuário.',
                    'resposta_correta': 'A'
                },
                {
                    'texto': 'O diagrama de sequência mostra:',
                    'alternativa_a': 'A relação entre classes.',
                    'alternativa_b': 'A interação entre objetos ao longo do tempo.',
                    'alternativa_c': 'O fluxo de dados.',
                    'alternativa_d': 'A arquitetura física.',
                    'resposta_correta': 'B'
                },
                {
                    'texto': 'O modelo incremental tem como característica:',
                    'alternativa_a': 'Entregar o sistema completo no final.',
                    'alternativa_b': 'Entregas parciais e evolutivas.',
                    'alternativa_c': 'Desenvolvimento sem requisitos.',
                    'alternativa_d': 'Falta de testes.',
                    'resposta_correta': 'B'
                }
            ],
            'dificil': [
                {
                    'texto': 'A análise orientada a objetos tem como foco principal:',
                    'alternativa_a': 'Processos e fluxos de dados.',
                    'alternativa_b': 'Entidades, atributos e relacionamentos.',
                    'alternativa_c': 'Objetos e suas interações.',
                    'alternativa_d': 'Diagramas de sequência.',
                    'resposta_correta': 'C'
                },
                {
                    'texto': 'O diagrama de pacotes é usado para:',
                    'alternativa_a': 'Dividir o sistema em partes organizadas e independentes.',
                    'alternativa_b': 'Mostrar os requisitos.',
                    'alternativa_c': 'Exibir fluxos de dados.',
                    'alternativa_d': 'Representar o banco.',
                    'resposta_correta': 'A'
                },
                {
                    'texto': 'Um requisito não funcional de usabilidade mede:',
                    'alternativa_a': 'A aparência do sistema.',
                    'alternativa_b': 'A facilidade de uso e aprendizado.',
                    'alternativa_c': 'O custo do projeto.',
                    'alternativa_d': 'O desempenho.',
                    'resposta_correta': 'B'
                },
                {
                    'texto': 'A matriz de rastreabilidade serve para:',
                    'alternativa_a': 'Controlar o orçamento.',
                    'alternativa_b': 'Relacionar requisitos às fases e artefatos do projeto.',
                    'alternativa_c': 'Gerar diagramas UML.',
                    'alternativa_d': 'Testar performance.',
                    'resposta_correta': 'B'
                },
                {
                    'texto': 'O modelo RAD (Rapid Application Development) visa:',
                    'alternativa_a': 'Desenvolvimento rápido com prototipação.',
                    'alternativa_b': 'Testes automatizados.',
                    'alternativa_c': 'Desenvolvimento sem análise.',
                    'alternativa_d': 'Alta documentação.',
                    'resposta_correta': 'A'
                }
            ]
        },
        '2': {
            'facil': [
                {
                    'texto': 'O analista de sistemas atua principalmente em:',
                    'alternativa_a': 'Suporte técnico.',
                    'alternativa_b': 'Levantamento e especificação de requisitos.',
                    'alternativa_c': 'Design gráfico.',
                    'alternativa_d': 'Instalação de redes.',
                    'resposta_correta': 'B'
                },
                {
                    'texto': 'A etapa de levantamento de requisitos busca:',
                    'alternativa_a': 'Implementar código.',
                    'alternativa_b': 'Entender as necessidades do cliente.',
                    'alternativa_c': 'Criar o banco de dados.',
                    'alternativa_d': 'Elaborar manuais.',
                    'resposta_correta': 'B'
                },
                {
                    'texto': 'O modelo em cascata é caracterizado por:',
                    'alternativa_a': 'Fases paralelas.',
                    'alternativa_b': 'Fases sequenciais e rígidas.',
                    'alternativa_c': 'Iterações contínuas.',
                    'alternativa_d': 'Prototipagem.',
                    'resposta_correta': 'B'
                },
                {
                    'texto': 'O diagrama de casos de uso mostra:',
                    'alternativa_a': 'A arquitetura física do sistema.',
                    'alternativa_b': 'As funcionalidades e os atores que interagem com o sistema.',
                    'alternativa_c': 'O código-fonte.',
                    'alternativa_d': 'O fluxo de dados.',
                    'resposta_correta': 'B'
                },
                {
                    'texto': 'O projeto de sistema transforma requisitos em:',
                    'alternativa_a': 'Códigos prontos.',
                    'alternativa_b': 'Modelos técnicos e estruturais.',
                    'alternativa_c': 'Documentos administrativos.',
                    'alternativa_d': 'Diagramas decorativos.',
                    'resposta_correta': 'B'
                }
            ],
            'medio': [
                {
                    'texto': 'Em análise de sistemas, stakeholders são:',
                    'alternativa_a': 'Apenas os desenvolvedores.',
                    'alternativa_b': 'Todos os envolvidos ou afetados pelo sistema.',
                    'alternativa_c': 'Somente os usuários finais.',
                    'alternativa_d': 'Só a equipe de projeto.',
                    'resposta_correta': 'B'
                },
                {
                    'texto': 'O que é engenharia reversa?',
                    'alternativa_a': 'Traduzir diagramas em código.',
                    'alternativa_b': 'Recriar o projeto a partir do código-fonte existente.',
                    'alternativa_c': 'Otimizar o banco de dados.',
                    'alternativa_d': 'Reorganizar o cronograma.',
                    'resposta_correta': 'B'
                },
                {
                    'texto': 'O modelo DFD (Diagrama de Fluxo de Dados) representa:',
                    'alternativa_a': 'As tabelas do banco.',
                    'alternativa_b': 'O fluxo de informações e processos do sistema.',
                    'alternativa_c': 'O layout da interface.',
                    'alternativa_d': 'A sequência de eventos.',
                    'resposta_correta': 'B'
                },
                {
                    'texto': 'O diagrama de estado é útil para:',
                    'alternativa_a': 'Mostrar mudanças de estado de um objeto.',
                    'alternativa_b': 'Exibir conexões de rede.',
                    'alternativa_c': 'Mapear atores.',
                    'alternativa_d': 'Calcular custos.',
                    'resposta_correta': 'A'
                },
                {
                    'texto': 'O cronograma do projeto é definido na etapa de:',
                    'alternativa_a': 'Análise.',
                    'alternativa_b': 'Planejamento.',
                    'alternativa_c': 'Codificação.',
                    'alternativa_d': 'Teste.',
                    'resposta_correta': 'B'
                }
            ],
            'dificil': [
                {
                    'texto': 'O diagrama de implantação (deployment) mostra:',
                    'alternativa_a': 'O fluxo de informações.',
                    'alternativa_b': 'A disposição física dos componentes e servidores.',
                    'alternativa_c': 'O código.',
                    'alternativa_d': 'Os atores.',
                    'resposta_correta': 'B'
                },
                {
                    'texto': 'A modelagem de dados normalmente usa:',
                    'alternativa_a': 'DFD.',
                    'alternativa_b': 'DER (Diagrama Entidade-Relacionamento).',
                    'alternativa_c': 'UML.',
                    'alternativa_d': 'JSON.',
                    'resposta_correta': 'B'
                },
                {
                    'texto': 'No modelo de casos de uso, as extensões representam:',
                    'alternativa_a': 'Erros.',
                    'alternativa_b': 'Cenários alternativos.',
                    'alternativa_c': 'Funções principais.',
                    'alternativa_d': 'Classes abstratas.',
                    'resposta_correta': 'B'
                },
                {
                    'texto': 'O modelo iterativo é caracterizado por:',
                    'alternativa_a': 'Repetição de ciclos de desenvolvimento com melhorias sucessivas.',
                    'alternativa_b': 'Etapas lineares.',
                    'alternativa_c': 'Falta de planejamento.',
                    'alternativa_d': 'Ausência de testes.',
                    'resposta_correta': 'A'
                },
                {
                    'texto': 'A ferramenta CASE é usada para:',
                    'alternativa_a': 'Compilar código.',
                    'alternativa_b': 'Apoiar o desenvolvimento e modelagem de sistemas.',
                    'alternativa_c': 'Criar hardware.',
                    'alternativa_d': 'Testar redes.',
                    'resposta_correta': 'B'
                }
            ]
        },
        '3': {
            'facil': [
                {
                    'texto': 'O ator em um caso de uso representa:',
                    'alternativa_a': 'Um desenvolvedor.',
                    'alternativa_b': 'Um usuário ou sistema externo que interage com o sistema.',
                    'alternativa_c': 'Um módulo interno.',
                    'alternativa_d': 'Uma função abstrata.',
                    'resposta_correta': 'B'
                },
                {
                    'texto': 'Qual é o principal documento criado pelo analista?',
                    'alternativa_a': 'O manual de usuário.',
                    'alternativa_b': 'O diagrama de classes.',
                    'alternativa_c': 'O documento de requisitos.',
                    'alternativa_d': 'O código do sistema.',
                    'resposta_correta': 'C'
                },
                {
                    'texto': 'O que é um protótipo?',
                    'alternativa_a': 'Um modelo preliminar do sistema para validação.',
                    'alternativa_b': 'Um código final.',
                    'alternativa_c': 'Um modelo de banco de dados.',
                    'alternativa_d': 'Um teste automatizado.',
                    'resposta_correta': 'A'
                },
                {
                    'texto': 'Um requisito não funcional está relacionado a:',
                    'alternativa_a': 'O que o sistema faz.',
                    'alternativa_b': 'Como o sistema deve funcionar.',
                    'alternativa_c': 'O banco de dados.',
                    'alternativa_d': 'O código.',
                    'resposta_correta': 'B'
                },
                {
                    'texto': 'O diagrama de atividades é usado para:',
                    'alternativa_a': 'Mostrar as classes.',
                    'alternativa_b': 'Representar fluxos de processos e ações.',
                    'alternativa_c': 'Apresentar interfaces.',
                    'alternativa_d': 'Exibir tabelas de banco.',
                    'resposta_correta': 'B'
                }
            ],
            'medio': [
                {
                    'texto': 'O termo reengenharia se refere a:',
                    'alternativa_a': 'Corrigir erros.',
                    'alternativa_b': 'Refazer sistemas antigos com melhorias estruturais.',
                    'alternativa_c': 'Criar novos sistemas do zero.',
                    'alternativa_d': 'Compactar código.',
                    'resposta_correta': 'B'
                },
                {
                    'texto': 'A UML foi criada para:',
                    'alternativa_a': 'Substituir linguagens de programação.',
                    'alternativa_b': 'Padronizar a modelagem de sistemas.',
                    'alternativa_c': 'Criar bancos de dados.',
                    'alternativa_d': 'Organizar relatórios.',
                    'resposta_correta': 'B'
                },
                {
                    'texto': 'O diagrama de componentes mostra:',
                    'alternativa_a': 'Fluxos lógicos.',
                    'alternativa_b': 'A organização física e os módulos do sistema.',
                    'alternativa_c': 'Tabelas.',
                    'alternativa_d': 'Códigos.',
                    'resposta_correta': 'B'
                },
                {
                    'texto': 'O modelo ágil é caracterizado por:',
                    'alternativa_a': 'Pouca comunicação com o cliente.',
                    'alternativa_b': 'Entregas rápidas e colaboração contínua.',
                    'alternativa_c': 'Planejamento fixo.',
                    'alternativa_d': 'Documentação pesada.',
                    'resposta_correta': 'B'
                },
                {
                    'texto': 'O teste de integração é aplicado para:',
                    'alternativa_a': 'Verificar a comunicação entre módulos.',
                    'alternativa_b': 'Validar o banco de dados.',
                    'alternativa_c': 'Testar o hardware.',
                    'alternativa_d': 'Examinar a interface.',
                    'resposta_correta': 'A'
                }
            ],
            'dificil': [
                {
                    'texto': 'O diagrama de comunicação substitui o:',
                    'alternativa_a': 'Diagrama de classes.',
                    'alternativa_b': 'Diagrama de sequência.',
                    'alternativa_c': 'Diagrama de pacotes.',
                    'alternativa_d': 'Diagrama de estados.',
                    'resposta_correta': 'B'
                },
                {
                    'texto': 'A engenharia de requisitos inclui atividades como:',
                    'alternativa_a': 'Implementação e manutenção.',
                    'alternativa_b': 'Levantamento, análise e validação de requisitos.',
                    'alternativa_c': 'Teste e implantação.',
                    'alternativa_d': 'Prototipação.',
                    'resposta_correta': 'B'
                },
                {
                    'texto': 'A arquitetura cliente-servidor é baseada em:',
                    'alternativa_a': 'Um único computador.',
                    'alternativa_b': 'Divisão entre quem solicita e quem fornece serviços.',
                    'alternativa_c': 'Processamento local apenas.',
                    'alternativa_d': 'Comunicação offline.',
                    'resposta_correta': 'B'
                },
                {
                    'texto': 'O diagrama de tempo é utilizado para:',
                    'alternativa_a': 'Representar mudanças de estado de objetos com base em tempo.',
                    'alternativa_b': 'Mostrar tabelas.',
                    'alternativa_c': 'Exibir requisitos.',
                    'alternativa_d': 'Apresentar classes.',
                    'resposta_correta': 'A'
                },
                {
                    'texto': 'O modelo de prototipagem evolutiva é ideal quando:',
                    'alternativa_a': 'Os requisitos estão bem definidos.',
                    'alternativa_b': 'Os requisitos são incertos e podem mudar.',
                    'alternativa_c': 'Não há interação com o cliente.',
                    'alternativa_d': 'O sistema é pequeno.',
                    'resposta_correta': 'B'
                }
            ]
        }
    }
}


