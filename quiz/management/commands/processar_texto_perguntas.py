"""
Script auxiliar para processar o texto das perguntas fornecido pelo usuário
e gerar o arquivo perguntas_completas.py completo.

Este script pode ser executado manualmente para atualizar as perguntas.
"""
import re
import os
from pathlib import Path

def extrair_perguntas_do_texto(texto):
    """
    Processa o texto fornecido e extrai as perguntas organizadas por tema, rodada e dificuldade.
    Retorna um dicionário com a estrutura PERGUNTAS_DATA.
    """
    perguntas = {}
    
    # Padrões para identificar seções
    padrao_tema = r'Tema:\s*([^\n]+)'
    padrao_rodada = r'Rodada\s+(\d+)\s+\(15\s+Perguntas\)'
    padrao_dificuldade = r'Dificuldade:\s*([^\n]+)'
    padrao_pergunta = r'(\d+)\.\s*Pergunta:\s*([^\n]+)'
    padrao_opcoes = r'Opções:\s*A\)\s*([^\n]+)\s*B\)\s*([^\n]+)\s*C\)\s*([^\n]+)\s*D\)\s*([^\n]+)'
    padrao_resposta = r'Resposta\s+Correta:\s*([A-D])\)'
    
    # Dividir por temas
    temas = re.split(r'Tema:\s*', texto)
    
    for tema_texto in temas[1:]:  # Pular o primeiro (vazio)
        # Extrair nome do tema
        match_tema = re.match(r'^([^\n]+)', tema_texto)
        if not match_tema:
            continue
        
        tema_nome = match_tema.group(1).strip()
        perguntas[tema_nome] = {}
        
        # Dividir por rodadas
        rodadas = re.split(r'Rodada\s+(\d+)', tema_texto)
        
        for i in range(1, len(rodadas), 2):
            if i + 1 >= len(rodadas):
                break
            
            rodada_num = rodadas[i]
            rodada_texto = rodadas[i + 1]
            perguntas[tema_nome][rodada_num] = {}
            
            # Dividir por dificuldades
            dificuldades_texto = re.split(
                r'Dificuldade:\s*(Fácil|Médio|Difícil)',
                rodada_texto
            )
            
            for j in range(1, len(dificuldades_texto), 2):
                if j + 1 >= len(dificuldades_texto):
                    break
                
                dificuldade_nome = dificuldades_texto[j].strip().lower()
                if dificuldade_nome == 'fácil':
                    dificuldade_nome = 'facil'
                elif dificuldade_nome == 'médio':
                    dificuldade_nome = 'medio'
                elif dificuldade_nome == 'difícil':
                    dificuldade_nome = 'dificil'
                
                perguntas_texto = dificuldades_texto[j + 1]
                perguntas[tema_nome][rodada_num][dificuldade_nome] = []
                
                # Extrair perguntas individuais
                perguntas_match = re.finditer(
                    r'(\d+)\.\s*Pergunta:\s*([^\n]+)\s*Opções:\s*A\)\s*([^\n]+)\s*B\)\s*([^\n]+)\s*C\)\s*([^\n]+)\s*D\)\s*([^\n]+)\s*Resposta\s+Correta:\s*([A-D])\)',
                    perguntas_texto,
                    re.MULTILINE | re.DOTALL
                )
                
                for match in perguntas_match:
                    perguntas[tema_nome][rodada_num][dificuldade_nome].append({
                        'texto': match.group(2).strip(),
                        'alternativa_a': match.group(3).strip(),
                        'alternativa_b': match.group(4).strip(),
                        'alternativa_c': match.group(5).strip(),
                        'alternativa_d': match.group(6).strip(),
                        'resposta_correta': match.group(7).strip()
                    })
    
    return perguntas

def gerar_arquivo_python(perguntas, caminho_arquivo):
    """Gera o arquivo Python com todas as perguntas"""
    linhas = [
        '"""',
        'Arquivo contendo todas as perguntas do Info Quiz organizadas por tema, rodada e dificuldade.',
        'Este arquivo foi gerado automaticamente a partir do texto fornecido.',
        '"""',
        '',
        '# Estrutura: PERGUNTAS_DATA[tema][rodada][dificuldade] = [lista de perguntas]',
        '# Cada pergunta tem: texto, alternativa_a, alternativa_b, alternativa_c, alternativa_d, resposta_correta',
        '',
        'PERGUNTAS_DATA = {'
    ]
    
    for tema_nome, rodadas in perguntas.items():
        linhas.append(f"    '{tema_nome}': {{")
        
        for rodada_num, dificuldades in sorted(rodadas.items(), key=lambda x: int(x[0])):
            linhas.append(f"        '{rodada_num}': {{")
            
            for dificuldade_nome in ['facil', 'medio', 'dificil']:
                if dificuldade_nome not in dificuldades:
                    continue
                
                linhas.append(f"            '{dificuldade_nome}': [")
                
                for pergunta in dificuldades[dificuldade_nome]:
                    linhas.append('                {')
                    linhas.append(f"                    'texto': {repr(pergunta['texto'])},\n")
                    linhas.append(f"                    'alternativa_a': {repr(pergunta['alternativa_a'])},\n")
                    linhas.append(f"                    'alternativa_b': {repr(pergunta['alternativa_b'])},\n")
                    linhas.append(f"                    'alternativa_c': {repr(pergunta['alternativa_c'])},\n")
                    linhas.append(f"                    'alternativa_d': {repr(pergunta['alternativa_d'])},\n")
                    linhas.append(f"                    'resposta_correta': {repr(pergunta['resposta_correta'])},\n")
                    linhas.append('                },')
                
                linhas.append('            ],')
            
            linhas.append('        },')
        
        linhas.append('    },')
    
    linhas.append('}')
    
    with open(caminho_arquivo, 'w', encoding='utf-8') as f:
        f.write('\n'.join(linhas))

if __name__ == '__main__':
    print("Este script processa o texto das perguntas e gera o arquivo perguntas_completas.py")
    print("Para usar, forneça o texto completo das perguntas como entrada")
    print("Ou execute: python manage.py popular_perguntas para popular o banco de dados")

