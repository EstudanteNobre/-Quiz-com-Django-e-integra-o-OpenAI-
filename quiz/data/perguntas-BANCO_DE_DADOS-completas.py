"""
Arquivo contendo todas as perguntas do Info Quiz organizadas por tema, rodada e dificuldade.
Este arquivo foi gerado a partir do texto fornecido pelo usuário.
"""

# Estrutura: PERGUNTAS_DATA[tema][rodada][dificuldade] = [lista de perguntas]
# Cada pergunta tem: texto, alternativa_a, alternativa_b, alternativa_c, alternativa_d, resposta_correta

PERGUNTAS_DATA = {
    'Banco de Dados': {
        '1': {
            'facil': [
                {
                    'texto': 'O que é uma tabela em um banco de dados relacional?',
                    'alternativa_a': 'Um tipo de índice.',
                    'alternativa_b': 'Um conjunto de linhas e colunas que armazenam dados.',
                    'alternativa_c': 'Um script de backup.',
                    'alternativa_d': 'Uma coleção de JSON.',
                    'resposta_correta': 'B'
                },
                {
                    'texto': 'No MongoDB, os dados são armazenados em:',
                    'alternativa_a': 'Tabelas.',
                    'alternativa_b': 'Coleções de documentos.',
                    'alternativa_c': 'Planilhas.',
                    'alternativa_d': 'Views.',
                    'resposta_correta': 'B'
                },
                {
                    'texto': 'O Redis é um banco de dados do tipo:',
                    'alternativa_a': 'Colunar.',
                    'alternativa_b': 'Chave-valor.',
                    'alternativa_c': 'Documental.',
                    'alternativa_d': 'Relacional.',
                    'resposta_correta': 'B'
                },
                {
                    'texto': 'O Neo4j é um banco de dados baseado em:',
                    'alternativa_a': 'Documentos.',
                    'alternativa_b': 'Grafos.',
                    'alternativa_c': 'Colunas.',
                    'alternativa_d': 'Chave-valor.',
                    'resposta_correta': 'B'
                },
                {
                    'texto': 'Em SQL, o comando para listar todos os registros de uma tabela é:',
                    'alternativa_a': 'GET * FROM tabela.',
                    'alternativa_b': 'SELECT * FROM tabela.',
                    'alternativa_c': 'SHOW tabela.',
                    'alternativa_d': 'FIND tabela.',
                    'resposta_correta': 'B'
                }
            ],
            'medio': [
                {
                    'texto': 'Em bancos NoSQL, a escalabilidade horizontal significa:',
                    'alternativa_a': 'Aumentar CPU de um servidor.',
                    'alternativa_b': 'Adicionar novos servidores para distribuir dados.',
                    'alternativa_c': 'Reduzir memória.',
                    'alternativa_d': 'Criar backups.',
                    'resposta_correta': 'B'
                },
                {
                    'texto': 'No MongoDB, o comando db.collection.find({idade: {$gt: 18}}) retorna:',
                    'alternativa_a': 'Todos os registros.',
                    'alternativa_b': 'Documentos com idade maior que 18.',
                    'alternativa_c': 'Documentos com idade menor que 18.',
                    'alternativa_d': 'Apenas o primeiro documento.',
                    'resposta_correta': 'B'
                },
                {
                    'texto': 'Qual comando SQL cria uma tabela?',
                    'alternativa_a': 'MAKE TABLE.',
                    'alternativa_b': 'CREATE TABLE.',
                    'alternativa_c': 'ADD TABLE.',
                    'alternativa_d': 'INSERT TABLE.',
                    'resposta_correta': 'B'
                },
                {
                    'texto': 'O Cassandra é altamente escalável porque:',
                    'alternativa_a': 'Usa modelo peer-to-peer.',
                    'alternativa_b': 'Possui servidor central.',
                    'alternativa_c': 'É baseado em JSON.',
                    'alternativa_d': 'Não replica dados.',
                    'resposta_correta': 'A'
                },
                {
                    'texto': 'Em SQL, qual comando apaga uma tabela inteira?',
                    'alternativa_a': 'REMOVE TABLE.',
                    'alternativa_b': 'DELETE *.',
                    'alternativa_c': 'DROP TABLE.',
                    'alternativa_d': 'CLEAR TABLE.',
                    'resposta_correta': 'C'
                }
            ],
            'dificil': [
                {
                    'texto': 'O que significa ACID em bancos relacionais?',
                    'alternativa_a': 'Atomicidade, Consistência, Isolamento e Durabilidade.',
                    'alternativa_b': 'Autenticação, Cache, Integridade e Dados.',
                    'alternativa_c': 'Agilidade, Controle, Isolamento, Dados.',
                    'alternativa_d': 'Auditoria, Cálculo, Integridade, Duplicação.',
                    'resposta_correta': 'A'
                },
                {
                    'texto': 'O teorema CAP diz que um sistema distribuído pode garantir:',
                    'alternativa_a': 'Apenas duas das três propriedades: Consistência, Disponibilidade e Tolerância a Partições.',
                    'alternativa_b': 'Todas simultaneamente.',
                    'alternativa_c': 'Nenhuma das propriedades.',
                    'alternativa_d': 'Somente consistência.',
                    'resposta_correta': 'A'
                },
                {
                    'texto': 'O que é sharding?',
                    'alternativa_a': 'Particionar dados entre servidores.',
                    'alternativa_b': 'Compactar logs.',
                    'alternativa_c': 'Normalizar tabelas.',
                    'alternativa_d': 'Fazer backup.',
                    'resposta_correta': 'A'
                },
                {
                    'texto': 'Em bancos NoSQL, consistência eventual significa:',
                    'alternativa_a': 'Dados sempre sincronizados.',
                    'alternativa_b': 'Sincronização ocorre com atraso.',
                    'alternativa_c': 'Falha de replicação.',
                    'alternativa_d': 'Modo offline.',
                    'resposta_correta': 'B'
                },
                {
                    'texto': 'Qual comando SQL cria um índice?',
                    'alternativa_a': 'MAKE INDEX.',
                    'alternativa_b': 'CREATE INDEX.',
                    'alternativa_c': 'ADD INDEX.',
                    'alternativa_d': 'UPDATE INDEX.',
                    'resposta_correta': 'B'
                }
            ]
        },
        '2': {
            'facil': [
                {
                    'texto': 'O Cassandra é classificado como um banco de dados:',
                    'alternativa_a': 'De colunas largas.',
                    'alternativa_b': 'Relacional.',
                    'alternativa_c': 'Documental.',
                    'alternativa_d': 'Hierárquico.',
                    'resposta_correta': 'A'
                },
                {
                    'texto': 'Qual a principal característica dos bancos de dados NoSQL?',
                    'alternativa_a': 'Usam esquema fixo.',
                    'alternativa_b': 'Flexibilidade e ausência de estrutura rígida.',
                    'alternativa_c': 'Dependem de chaves estrangeiras.',
                    'alternativa_d': 'Só funcionam com SQL.',
                    'resposta_correta': 'B'
                },
                {
                    'texto': 'Em bancos relacionais, uma chave primária serve para:',
                    'alternativa_a': 'Permitir valores repetidos.',
                    'alternativa_b': 'Identificar unicamente cada registro.',
                    'alternativa_c': 'Criar índices compostos.',
                    'alternativa_d': 'Agrupar dados em partições.',
                    'resposta_correta': 'B'
                },
                {
                    'texto': 'Qual comando insere dados em uma tabela SQL?',
                    'alternativa_a': 'INSERT INTO.',
                    'alternativa_b': 'ADD NEW.',
                    'alternativa_c': 'APPEND.',
                    'alternativa_d': 'PUSH.',
                    'resposta_correta': 'A'
                },
                {
                    'texto': 'No Redis, qual comando armazena um valor?',
                    'alternativa_a': 'PUT.',
                    'alternativa_b': 'SAVE.',
                    'alternativa_c': 'SET.',
                    'alternativa_d': 'STORE.',
                    'resposta_correta': 'C'
                }
            ],
            'medio': [
                {
                    'texto': 'O comando INCR contador no Redis faz:',
                    'alternativa_a': 'Soma 1 ao valor da chave.',
                    'alternativa_b': 'Diminui 1.',
                    'alternativa_c': 'Exclui o valor.',
                    'alternativa_d': 'Cria uma lista.',
                    'resposta_correta': 'A'
                },
                {
                    'texto': 'Em um banco relacional, uma chave estrangeira:',
                    'alternativa_a': 'Referencia a chave primária de outra tabela.',
                    'alternativa_b': 'É uma coluna duplicada.',
                    'alternativa_c': 'Cria índices.',
                    'alternativa_d': 'É opcional em todas as tabelas.',
                    'resposta_correta': 'A'
                },
                {
                    'texto': 'O comando UPDATE em SQL é usado para:',
                    'alternativa_a': 'Inserir dados.',
                    'alternativa_b': 'Excluir registros.',
                    'alternativa_c': 'Modificar valores existentes.',
                    'alternativa_d': 'Criar índices.',
                    'resposta_correta': 'C'
                },
                {
                    'texto': 'No Neo4j, um relacionamento conecta:',
                    'alternativa_a': 'Dois índices.',
                    'alternativa_b': 'Dois nós.',
                    'alternativa_c': 'Dois clusters.',
                    'alternativa_d': 'Dois arquivos.',
                    'resposta_correta': 'B'
                },
                {
                    'texto': 'Em NoSQL, o termo “documento” representa:',
                    'alternativa_a': 'Um arquivo de texto.',
                    'alternativa_b': 'Um conjunto de pares chave-valor dentro de uma coleção.',
                    'alternativa_c': 'Uma query SQL.',
                    'alternativa_d': 'Um relacionamento.',
                    'resposta_correta': 'B'
                }
            ],
            'dificil': [
                {
                    'texto': 'O Redis pode ser usado além de cache como:',
                    'alternativa_a': 'Sistema de mensageria e filas.',
                    'alternativa_b': 'Banco relacional.',
                    'alternativa_c': 'Editor de texto.',
                    'alternativa_d': 'Compressão de dados.',
                    'resposta_correta': 'A'
                },
                {
                    'texto': 'O Cassandra é preferido em sistemas que exigem:',
                    'alternativa_a': 'Alta disponibilidade e volume massivo de dados.',
                    'alternativa_b': 'Poucos usuários.',
                    'alternativa_c': 'Operações offline.',
                    'alternativa_d': 'Dados imutáveis.',
                    'resposta_correta': 'A'
                },
                {
                    'texto': 'O Neo4j é vantajoso em consultas:',
                    'alternativa_a': 'Com poucos relacionamentos.',
                    'alternativa_b': 'Que envolvem redes complexas e conexões múltiplas.',
                    'alternativa_c': 'Com tabelas simples.',
                    'alternativa_d': 'Apenas numéricas.',
                    'resposta_correta': 'B'
                },
                {
                    'texto': 'Em SQL, qual JOIN retorna apenas os registros existentes em ambas as tabelas?',
                    'alternativa_a': 'LEFT JOIN.',
                    'alternativa_b': 'RIGHT JOIN.',
                    'alternativa_c': 'INNER JOIN.',
                    'alternativa_d': 'FULL JOIN.',
                    'resposta_correta': 'C'
                },
                {
                    'texto': 'O MongoDB Atlas fornece:',
                    'alternativa_a': 'Servidor local.',
                    'alternativa_b': 'Cluster distribuído na nuvem.',
                    'alternativa_c': 'Sistema de logs.',
                    'alternativa_d': 'Ferramenta de backup offline.',
                    'resposta_correta': 'B'
                }
            ]
        },
        '3': {
            'facil': [
                {
                    'texto': 'Qual linguagem é usada no Neo4j?',
                    'alternativa_a': 'SQL.',
                    'alternativa_b': 'Cypher.',
                    'alternativa_c': 'CQL.',
                    'alternativa_d': 'GraphQL.',
                    'resposta_correta': 'B'
                },
                {
                    'texto': 'O que caracteriza um banco de dados relacional?',
                    'alternativa_a': 'Armazenamento em grafos.',
                    'alternativa_b': 'Estrutura em tabelas com colunas e chaves.',
                    'alternativa_c': 'Dados em formato JSON.',
                    'alternativa_d': 'Somente leitura.',
                    'resposta_correta': 'B'
                },
                {
                    'texto': 'O MongoDB usa o formato:',
                    'alternativa_a': 'YAML.',
                    'alternativa_b': 'BSON (Binary JSON).',
                    'alternativa_c': 'XML.',
                    'alternativa_d': 'TXT.',
                    'resposta_correta': 'B'
                },
                {
                    'texto': 'A principal vantagem do NoSQL é:',
                    'alternativa_a': 'Escalabilidade horizontal.',
                    'alternativa_b': 'Suporte a triggers.',
                    'alternativa_c': 'Normalização rígida.',
                    'alternativa_d': 'Uso fixo de schemas.',
                    'resposta_correta': 'A'
                },
                {
                    'texto': 'No Redis, os dados ficam principalmente:',
                    'alternativa_a': 'Em disco.',
                    'alternativa_b': 'Em memória.',
                    'alternativa_c': 'Na nuvem.',
                    'alternativa_d': 'Em planilhas.',
                    'resposta_correta': 'B'
                }
            ],
            'medio': [
                {
                    'texto': 'Em bancos relacionais, o comando JOIN é usado para:',
                    'alternativa_a': 'Combinar dados de várias tabelas.',
                    'alternativa_b': 'Excluir tabelas.',
                    'alternativa_c': 'Normalizar registros.',
                    'alternativa_d': 'Criar índices.',
                    'resposta_correta': 'A'
                },
                {
                    'texto': 'O Redis é comumente usado para:',
                    'alternativa_a': 'Cache de dados.',
                    'alternativa_b': 'Processar vídeos.',
                    'alternativa_c': 'Armazenar imagens.',
                    'alternativa_d': 'Consultas gráficas.',
                    'resposta_correta': 'A'
                },
                {
                    'texto': 'Qual a linguagem usada para consultas no Cassandra?',
                    'alternativa_a': 'CQL (Cassandra Query Language).',
                    'alternativa_b': 'SQL.',
                    'alternativa_c': 'Cypher.',
                    'alternativa_d': 'RedisQL.',
                    'resposta_correta': 'A'
                },
                {
                    'texto': 'Em SQL, WHERE serve para:',
                    'alternativa_a': 'Criar colunas.',
                    'alternativa_b': 'Filtrar registros.',
                    'alternativa_c': 'Excluir tabelas.',
                    'alternativa_d': 'Somar valores.',
                    'resposta_correta': 'B'
                },
                {
                    'texto': 'O MongoDB é um banco ideal para:',
                    'alternativa_a': 'Dados estruturados e fixos.',
                    'alternativa_b': 'Dados sem estrutura definida.',
                    'alternativa_c': 'Consultas ACID.',
                    'alternativa_d': 'Processos financeiros.',
                    'resposta_correta': 'B'
                }
            ],
            'dificil': [
                {
                    'texto': 'O Redis armazena dados principalmente:',
                    'alternativa_a': 'No navegador.',
                    'alternativa_b': 'Em RAM.',
                    'alternativa_c': 'Em fitas.',
                    'alternativa_d': 'Em SSD.',
                    'resposta_correta': 'B'
                },
                {
                    'texto': 'Em NoSQL, qual modelo é mais adequado para redes sociais?',
                    'alternativa_a': 'Grafos.',
                    'alternativa_b': 'Colunas.',
                    'alternativa_c': 'Documentos.',
                    'alternativa_d': 'Chave-valor.',
                    'resposta_correta': 'A'
                },
                {
                    'texto': 'A normalização em bancos relacionais serve para:',
                    'alternativa_a': 'Reduzir redundância e melhorar integridade.',
                    'alternativa_b': 'Aumentar performance em consultas.',
                    'alternativa_c': 'Copiar dados.',
                    'alternativa_d': 'Gerar chaves estrangeiras automaticamente.',
                    'resposta_correta': 'A'
                },
                {
                    'texto': 'O Cassandra distribui dados por:',
                    'alternativa_a': 'Hash em nós do cluster.',
                    'alternativa_b': 'Servidor central.',
                    'alternativa_c': 'Backup em nuvem.',
                    'alternativa_d': 'Um único nó.',
                    'resposta_correta': 'A'
                },
                {
                    'texto': 'O Redis é chamado de banco in-memory porque:',
                    'alternativa_a': 'Os dados ficam salvos em memória RAM para respostas rápidas.',
                    'alternativa_b': 'Usa HD SSD.',
                    'alternativa_c': 'É um cache em disco.',
                    'alternativa_d': 'Depende de processador gráfico.',
                    'resposta_correta': 'A'
                }
            ]
        }
    }
}


