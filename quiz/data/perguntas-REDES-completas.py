"""
Arquivo contendo todas as perguntas do Info Quiz organizadas por tema, rodada e dificuldade.
Este arquivo foi gerado a partir do texto fornecido pelo usuário.
"""

# Estrutura: PERGUNTAS_DATA[tema][rodada][dificuldade] = [lista de perguntas]
# Cada pergunta tem: texto, alternativa_a, alternativa_b, alternativa_c, alternativa_d, resposta_correta

PERGUNTAS_DATA = {
    'Redes': {
        '1': {
            'facil': [
                {
                    'texto': 'O que é uma rede de computadores?',
                    'alternativa_a': 'Um único computador.',
                    'alternativa_b': 'Um conjunto de computadores interligados para compartilhar recursos.',
                    'alternativa_c': 'Um cabo de energia.',
                    'alternativa_d': 'Um software antivírus.',
                    'resposta_correta': 'B'
                },
                {
                    'texto': 'O que significa IP?',
                    'alternativa_a': 'Internet Program.',
                    'alternativa_b': 'Internet Protocol.',
                    'alternativa_c': 'Internal Process.',
                    'alternativa_d': 'Information Port.',
                    'resposta_correta': 'B'
                },
                {
                    'texto': 'O que significa LAN?',
                    'alternativa_a': 'Local Area Network.',
                    'alternativa_b': 'Large Application Node.',
                    'alternativa_c': 'Logical Area Network.',
                    'alternativa_d': 'Local Access Number.',
                    'resposta_correta': 'A'
                },
                {
                    'texto': 'O que faz um roteador?',
                    'alternativa_a': 'Controla impressoras.',
                    'alternativa_b': 'Conecta redes diferentes.',
                    'alternativa_c': 'Armazena arquivos.',
                    'alternativa_d': 'Produz energia.',
                    'resposta_correta': 'B'
                },
                {
                    'texto': 'Qual protocolo é usado para navegação na Web?',
                    'alternativa_a': 'HTTP.',
                    'alternativa_b': 'FTP.',
                    'alternativa_c': 'SMTP.',
                    'alternativa_d': 'POP3.',
                    'resposta_correta': 'A'
                }
            ],
            'medio': [
                {
                    'texto': 'Qual protocolo é usado para enviar e-mails?',
                    'alternativa_a': 'HTTP.',
                    'alternativa_b': 'SMTP.',
                    'alternativa_c': 'FTP.',
                    'alternativa_d': 'DNS.',
                    'resposta_correta': 'B'
                },
                {
                    'texto': 'O que é NAT?',
                    'alternativa_a': 'Traduz endereços IP privados em públicos.',
                    'alternativa_b': 'Envia pacotes de e-mail.',
                    'alternativa_c': 'Atribui IPs automaticamente.',
                    'alternativa_d': 'Cria topologias de rede.',
                    'resposta_correta': 'A'
                },
                {
                    'texto': 'Quantos bits possui um endereço IPv4?',
                    'alternativa_a': '16.',
                    'alternativa_b': '32.',
                    'alternativa_c': '64.',
                    'alternativa_d': '128.',
                    'resposta_correta': 'B'
                },
                {
                    'texto': 'O que é topologia de rede?',
                    'alternativa_a': 'Tipo de protocolo.',
                    'alternativa_b': 'Forma de interligar dispositivos.',
                    'alternativa_c': 'Tipo de IP.',
                    'alternativa_d': 'Nome de rede.',
                    'resposta_correta': 'B'
                },
                {
                    'texto': 'Na topologia estrela, o ponto central é:',
                    'alternativa_a': 'Firewall.',
                    'alternativa_b': 'Switch.',
                    'alternativa_c': 'Roteador.',
                    'alternativa_d': 'Servidor.',
                    'resposta_correta': 'B'
                }
            ],
            'dificil': [
                {
                    'texto': 'Quantos bits possui um endereço IPv6?',
                    'alternativa_a': '32.',
                    'alternativa_b': '48.',
                    'alternativa_c': '64.',
                    'alternativa_d': '128.',
                    'resposta_correta': 'D'
                },
                {
                    'texto': 'Qual é a função do protocolo ICMP?',
                    'alternativa_a': 'Verificar erros e enviar mensagens de controle.',
                    'alternativa_b': 'Enviar arquivos.',
                    'alternativa_c': 'Traduzir nomes.',
                    'alternativa_d': 'Atribuir IPs.',
                    'resposta_correta': 'A'
                },
                {
                    'texto': 'O que significa MTU?',
                    'alternativa_a': 'Maximum Transmission Unit.',
                    'alternativa_b': 'Minimum Transfer Usage.',
                    'alternativa_c': 'Multi Transfer Utility.',
                    'alternativa_d': 'Maximum Traffic User.',
                    'resposta_correta': 'A'
                },
                {
                    'texto': 'O que é um gateway?',
                    'alternativa_a': 'Conecta redes com protocolos diferentes.',
                    'alternativa_b': 'Amplifica sinal.',
                    'alternativa_c': 'Define endereços IP.',
                    'alternativa_d': 'Bloqueia tráfego.',
                    'resposta_correta': 'A'
                },
                {
                    'texto': 'O que é um domínio público de IP?',
                    'alternativa_a': 'IP usado somente internamente.',
                    'alternativa_b': 'IP acessível na Internet.',
                    'alternativa_c': 'IP exclusivo de roteadores.',
                    'alternativa_d': 'IP dinâmico de LAN.',
                    'resposta_correta': 'B'
                }
            ]
        },
        '2': {
            'facil': [
                {
                    'texto': 'Qual a função do DNS?',
                    'alternativa_a': 'Traduz nomes de domínio em endereços IP.',
                    'alternativa_b': 'Armazena e-mails.',
                    'alternativa_c': 'Criptografa mensagens.',
                    'alternativa_d': 'Define senhas.',
                    'resposta_correta': 'A'
                },
                {
                    'texto': 'Qual a porta padrão do HTTP?',
                    'alternativa_a': '20.',
                    'alternativa_b': '21.',
                    'alternativa_c': '25.',
                    'alternativa_d': '80.',
                    'resposta_correta': 'D'
                },
                {
                    'texto': 'O que significa Wi-Fi?',
                    'alternativa_a': 'Wireless Fidelity.',
                    'alternativa_b': 'Wired Fiber.',
                    'alternativa_c': 'Wide Frequency.',
                    'alternativa_d': 'Web Function.',
                    'resposta_correta': 'A'
                },
                {
                    'texto': 'O que é um switch?',
                    'alternativa_a': 'Equipamento que conecta computadores em uma rede local.',
                    'alternativa_b': 'Dispositivo de armazenamento.',
                    'alternativa_c': 'Firewall.',
                    'alternativa_d': 'Modem.',
                    'resposta_correta': 'A'
                },
                {
                    'texto': 'O que é DHCP?',
                    'alternativa_a': 'Protocolo de envio de e-mail.',
                    'alternativa_b': 'Atribui IPs automaticamente.',
                    'alternativa_c': 'Define nomes de domínio.',
                    'alternativa_d': 'Gerencia firewall.',
                    'resposta_correta': 'B'
                }
            ],
            'medio': [
                {
                    'texto': 'Qual camada do modelo OSI lida com o endereçamento IP?',
                    'alternativa_a': 'Aplicação.',
                    'alternativa_b': 'Rede.',
                    'alternativa_c': 'Transporte.',
                    'alternativa_d': 'Enlace.',
                    'resposta_correta': 'B'
                },
                {
                    'texto': 'Qual é a porta padrão do HTTPS?',
                    'alternativa_a': '21.',
                    'alternativa_b': '25.',
                    'alternativa_c': '80.',
                    'alternativa_d': '443.',
                    'resposta_correta': 'D'
                },
                {
                    'texto': 'Qual camada do modelo OSI utiliza o protocolo TCP?',
                    'alternativa_a': 'Rede.',
                    'alternativa_b': 'Transporte.',
                    'alternativa_c': 'Aplicação.',
                    'alternativa_d': 'Enlace.',
                    'resposta_correta': 'B'
                },
                {
                    'texto': 'O que é ARP?',
                    'alternativa_a': 'Traduz IP em endereço MAC.',
                    'alternativa_b': 'Cria IPs novos.',
                    'alternativa_c': 'Define gateways.',
                    'alternativa_d': 'Gerencia DNS.',
                    'resposta_correta': 'A'
                },
                {
                    'texto': 'O que é firewall?',
                    'alternativa_a': 'Controla o tráfego entre redes.',
                    'alternativa_b': 'Gera endereços IP.',
                    'alternativa_c': 'Mede velocidade de conexão.',
                    'alternativa_d': 'Armazena arquivos.',
                    'resposta_correta': 'A'
                }
            ],
            'dificil': [
                {
                    'texto': 'O que é subnet mask (máscara de sub-rede)?',
                    'alternativa_a': 'Divide a rede em sub-redes menores.',
                    'alternativa_b': 'Define o gateway.',
                    'alternativa_c': 'Traduz nomes.',
                    'alternativa_d': 'Criptografa dados.',
                    'resposta_correta': 'A'
                },
                {
                    'texto': 'O que é latência?',
                    'alternativa_a': 'Tempo de resposta entre envio e recebimento de dados.',
                    'alternativa_b': 'Taxa de download.',
                    'alternativa_c': 'Largura de banda.',
                    'alternativa_d': 'Erro de transmissão.',
                    'resposta_correta': 'A'
                },
                {
                    'texto': 'O que o protocolo SNMP faz?',
                    'alternativa_a': 'Gerencia dispositivos de rede.',
                    'alternativa_b': 'Transfere arquivos.',
                    'alternativa_c': 'Cria topologias.',
                    'alternativa_d': 'Controla roteadores.',
                    'resposta_correta': 'A'
                },
                {
                    'texto': 'Qual protocolo é usado para acesso remoto seguro?',
                    'alternativa_a': 'Telnet.',
                    'alternativa_b': 'SSH.',
                    'alternativa_c': 'FTP.',
                    'alternativa_d': 'RDP.',
                    'resposta_correta': 'B'
                },
                {
                    'texto': 'O que é VLAN?',
                    'alternativa_a': 'Rede lógica dentro de uma rede física.',
                    'alternativa_b': 'Conexão via Wi-Fi.',
                    'alternativa_c': 'Protocolo de roteamento.',
                    'alternativa_d': 'Endereço de gateway.',
                    'resposta_correta': 'A'
                }
            ]
        },
        '3': {
            'facil': [
                {
                    'texto': 'O que é um endereço MAC?',
                    'alternativa_a': 'Identificador único da placa de rede.',
                    'alternativa_b': 'Senha de Wi-Fi.',
                    'alternativa_c': 'Endereço IP.',
                    'alternativa_d': 'Nome do host.',
                    'resposta_correta': 'A'
                },
                {
                    'texto': 'Qual comando mostra o IP do computador no Windows?',
                    'alternativa_a': 'ping.',
                    'alternativa_b': 'ipconfig.',
                    'alternativa_c': 'tracert.',
                    'alternativa_d': 'nslookup.',
                    'resposta_correta': 'B'
                },
                {
                    'texto': 'O que significa WAN?',
                    'alternativa_a': 'Wide Area Network.',
                    'alternativa_b': 'World Access Network.',
                    'alternativa_c': 'Web Area Node.',
                    'alternativa_d': 'Wireless Access Network.',
                    'resposta_correta': 'A'
                },
                {
                    'texto': 'O que é ping?',
                    'alternativa_a': 'Protocolo de backup.',
                    'alternativa_b': 'Teste de conectividade de rede.',
                    'alternativa_c': 'Software de antivírus.',
                    'alternativa_d': 'Programa de roteamento.',
                    'resposta_correta': 'B'
                },
                {
                    'texto': 'Qual é a camada do modelo OSI responsável pela transmissão de bits?',
                    'alternativa_a': 'Aplicação.',
                    'alternativa_b': 'Enlace.',
                    'alternativa_c': 'Física.',
                    'alternativa_d': 'Rede.',
                    'resposta_correta': 'C'
                }
            ],
            'medio': [
                {
                    'texto': 'Qual camada do modelo OSI é responsável pela criptografia de dados?',
                    'alternativa_a': 'Sessão.',
                    'alternativa_b': 'Apresentação.',
                    'alternativa_c': 'Transporte.',
                    'alternativa_d': 'Aplicação.',
                    'resposta_correta': 'B'
                },
                {
                    'texto': 'O que é largura de banda?',
                    'alternativa_a': 'Quantidade de dados transmitidos por segundo.',
                    'alternativa_b': 'Tipo de endereço IP.',
                    'alternativa_c': 'Tempo de resposta.',
                    'alternativa_d': 'Taxa de erro.',
                    'resposta_correta': 'A'
                },
                {
                    'texto': 'Qual comando exibe o caminho até um destino na rede?',
                    'alternativa_a': 'ping.',
                    'alternativa_b': 'ipconfig.',
                    'alternativa_c': 'tracert.',
                    'alternativa_d': 'nslookup.',
                    'resposta_correta': 'C'
                },
                {
                    'texto': 'O que é um host?',
                    'alternativa_a': 'Dispositivo conectado à rede.',
                    'alternativa_b': 'Somente servidor.',
                    'alternativa_c': 'Roteador.',
                    'alternativa_d': 'Firewall.',
                    'resposta_correta': 'A'
                },
                {
                    'texto': 'Qual protocolo usa a porta 53?',
                    'alternativa_a': 'FTP.',
                    'alternativa_b': 'DNS.',
                    'alternativa_c': 'DHCP.',
                    'alternativa_d': 'SMTP.',
                    'resposta_correta': 'B'
                }
            ],
            'dificil': [
                {
                    'texto': 'O que é QoS em redes?',
                    'alternativa_a': 'Quality of Service.',
                    'alternativa_b': 'Queue of System.',
                    'alternativa_c': 'Quick Operational Setup.',
                    'alternativa_d': 'Quality of Signal.',
                    'resposta_correta': 'A'
                },
                {
                    'texto': 'O que é proxy?',
                    'alternativa_a': 'Intermediário entre o cliente e a Internet.',
                    'alternativa_b': 'Servidor DNS.',
                    'alternativa_c': 'Switch central.',
                    'alternativa_d': 'Firewall físico.',
                    'resposta_correta': 'A'
                },
                {
                    'texto': 'O que é loopback address?',
                    'alternativa_a': 'Endereço que testa a própria máquina.',
                    'alternativa_b': 'IP inválido.',
                    'alternativa_c': 'IP de broadcast.',
                    'alternativa_d': 'IP público.',
                    'resposta_correta': 'A'
                },
                {
                    'texto': 'Qual é o endereço de loopback IPv4 padrão?',
                    'alternativa_a': '192.168.0.1.',
                    'alternativa_b': '10.0.0.1.',
                    'alternativa_c': '127.0.0.1.',
                    'alternativa_d': '255.255.255.0.',
                    'resposta_correta': 'C'
                },
                {
                    'texto': 'O que é um protocolo de roteamento dinâmico?',
                    'alternativa_a': 'Atualiza rotas automaticamente.',
                    'alternativa_b': 'Define rotas fixas.',
                    'alternativa_c': 'Envia pacotes locais.',
                    'alternativa_d': 'Controla velocidade de rede.',
                    'resposta_correta': 'A'
                }
            ]
        }
    }
}

