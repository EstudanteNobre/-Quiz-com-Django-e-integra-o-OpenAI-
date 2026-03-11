"""
Serviço de integração com a API da OpenAI para geração de perguntas de quiz.
"""
import json
import logging
import random
from typing import Optional
from django.conf import settings

try:
    from openai import OpenAI
except ImportError:
    OpenAI = None

logger = logging.getLogger(__name__)


class OpenAIQuizService:
    """
    Serviço para gerar perguntas de quiz usando a API da OpenAI.
    
    Estrutura do quiz:
    - 3 rodadas
    - 3 níveis de dificuldade por rodada (fácil, médio, difícil)
    - 5 perguntas por nível
    - Total: 45 perguntas por tema (15 por rodada)
    """
    
    def __init__(self):
        if OpenAI is None:
            raise ImportError("A biblioteca 'openai' não está instalada. Execute: pip install openai")
        
        self.api_key = getattr(settings, 'OPENAI_API_KEY', None)
        self.model = getattr(settings, 'OPENAI_MODEL', 'gpt-4o-mini')
        
        if not self.api_key:
            raise ValueError(
                "OPENAI_API_KEY não configurada. "
                "Adicione OPENAI_API_KEY no arquivo .env ou settings.py"
            )
        
        self.client = OpenAI(api_key=self.api_key)
    
    def _criar_prompt_sistema(self) -> str:
        """Cria o prompt de sistema para a IA."""
        return """Você é um especialista em criar perguntas de quiz educacionais em português brasileiro.

REGRAS IMPORTANTES:
1. Todas as perguntas devem ser em PORTUGUÊS BRASILEIRO
2. As perguntas devem ser claras, objetivas e sem ambiguidade
3. As alternativas devem ser plausíveis, mas apenas UMA deve ser correta
4. A dificuldade deve corresponder ao nível especificado:
   - FÁCIL: Conceitos básicos, definições simples
   - MÉDIO: Aplicação de conceitos, comparações
   - DIFÍCIL: Casos avançados, análise crítica, detalhes técnicos

FORMATO DE RESPOSTA:
Retorne APENAS um JSON válido, sem markdown ou explicações adicionais.
"""

    def _criar_prompt_perguntas(self, tema: str, dificuldade: str, quantidade: int) -> str:
        """Cria o prompt para gerar perguntas específicas."""
        nivel_desc = {
            'facil': 'FÁCIL - conceitos básicos e definições simples',
            'medio': 'MÉDIO - aplicação de conceitos e comparações',
            'dificil': 'DIFÍCIL - casos avançados, análise crítica e detalhes técnicos'
        }
        
        return f"""Gere {quantidade} perguntas de quiz sobre o tema "{tema}" com nível de dificuldade {nivel_desc.get(dificuldade, dificuldade)}.

FORMATO OBRIGATÓRIO (retorne APENAS este JSON, sem markdown):
{{
    "perguntas": [
        {{
            "texto": "Pergunta aqui?",
            "alternativa_a": "Opção A",
            "alternativa_b": "Opção B",
            "alternativa_c": "Opção C",
            "alternativa_d": "Opção D",
            "resposta_correta": "A"
        }}
    ]
}}

REGRAS:
- resposta_correta deve ser apenas "A", "B", "C" ou "D"
- Todas as alternativas devem ser plausíveis
- Varie a posição da resposta correta entre as alternativas
- As perguntas devem ser únicas e não repetidas
- Use termos técnicos apropriados para o tema
"""

    def gerar_perguntas(
        self, 
        tema: str, 
        dificuldade: str, 
        quantidade: int = 5
    ) -> list[dict]:
        """
        Gera perguntas de quiz para um tema e dificuldade específicos.
        
        Args:
            tema: Nome do tema (ex: "Python", "Redes", "Banco de Dados")
            dificuldade: Nível de dificuldade ("facil", "medio", "dificil")
            quantidade: Número de perguntas a gerar (padrão: 5)
            
        Returns:
            Lista de dicionários com as perguntas geradas
        """
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": self._criar_prompt_sistema()},
                    {"role": "user", "content": self._criar_prompt_perguntas(tema, dificuldade, quantidade)}
                ],
                temperature=0.7,
                max_tokens=4000,
                response_format={"type": "json_object"}
            )
            
            content = response.choices[0].message.content
            data = json.loads(content)
            perguntas = data.get('perguntas', [])
            
            # Validar, embaralhar e normalizar as perguntas
            perguntas_validadas = []
            for p in perguntas:
                if self._validar_pergunta(p):
                    # Normalizar resposta_correta para maiúscula
                    p['resposta_correta'] = p['resposta_correta'].upper()
                    # Embaralhar alternativas para distribuir respostas corretas aleatoriamente
                    p_embaralhada = self._embaralhar_alternativas(p)
                    perguntas_validadas.append(p_embaralhada)
            
            logger.info(f"Geradas {len(perguntas_validadas)} perguntas para {tema} ({dificuldade})")
            return perguntas_validadas
            
        except json.JSONDecodeError as e:
            logger.error(f"Erro ao decodificar JSON da resposta: {e}")
            raise ValueError("A IA retornou uma resposta inválida. Tente novamente.")
        except Exception as e:
            logger.error(f"Erro ao gerar perguntas: {e}")
            raise
    
    def _validar_pergunta(self, pergunta: dict) -> bool:
        """Valida se uma pergunta tem todos os campos necessários."""
        campos_obrigatorios = [
            'texto', 'alternativa_a', 'alternativa_b', 
            'alternativa_c', 'alternativa_d', 'resposta_correta'
        ]
        
        for campo in campos_obrigatorios:
            if campo not in pergunta or not pergunta[campo]:
                logger.warning(f"Pergunta inválida: campo '{campo}' ausente ou vazio")
                return False
        
        # Validar resposta_correta
        if pergunta['resposta_correta'].upper() not in ['A', 'B', 'C', 'D']:
            logger.warning(f"Resposta correta inválida: {pergunta['resposta_correta']}")
            return False
        
        return True
    
    def _embaralhar_alternativas(self, pergunta: dict) -> dict:
        """
        Embaralha as alternativas de uma pergunta de forma aleatória.
        Atualiza a resposta_correta para a nova posição.
        
        Args:
            pergunta: Dicionário com a pergunta e alternativas
            
        Returns:
            Pergunta com alternativas embaralhadas
        """
        # Mapear letra para alternativa
        mapa_letras = {
            'A': 'alternativa_a',
            'B': 'alternativa_b',
            'C': 'alternativa_c',
            'D': 'alternativa_d'
        }
        
        # Obter a resposta correta atual
        resposta_correta_letra = pergunta['resposta_correta'].upper()
        resposta_correta_campo = mapa_letras[resposta_correta_letra]
        resposta_correta_texto = pergunta[resposta_correta_campo]
        
        # Criar lista de alternativas com seus textos
        alternativas = [
            pergunta['alternativa_a'],
            pergunta['alternativa_b'],
            pergunta['alternativa_c'],
            pergunta['alternativa_d']
        ]
        
        # Embaralhar as alternativas
        random.shuffle(alternativas)
        
        # Encontrar a nova posição da resposta correta
        nova_posicao = alternativas.index(resposta_correta_texto)
        letras = ['A', 'B', 'C', 'D']
        nova_resposta_correta = letras[nova_posicao]
        
        # Atualizar a pergunta com as alternativas embaralhadas
        pergunta_embaralhada = {
            'texto': pergunta['texto'],
            'alternativa_a': alternativas[0],
            'alternativa_b': alternativas[1],
            'alternativa_c': alternativas[2],
            'alternativa_d': alternativas[3],
            'resposta_correta': nova_resposta_correta
        }
        
        return pergunta_embaralhada
    
    def gerar_rodada_completa(self, tema: str) -> dict:
        """
        Gera uma rodada completa de perguntas (15 perguntas: 5 fáceis + 5 médias + 5 difíceis).
        
        Args:
            tema: Nome do tema
            
        Returns:
            Dicionário com perguntas organizadas por dificuldade
        """
        rodada = {
            'facil': [],
            'medio': [],
            'dificil': []
        }
        
        for dificuldade in ['facil', 'medio', 'dificil']:
            perguntas = self.gerar_perguntas(tema, dificuldade, quantidade=5)
            rodada[dificuldade] = perguntas
        
        return rodada
    
    def gerar_quiz_completo(self, tema: str) -> dict:
        """
        Gera um quiz completo com 3 rodadas (45 perguntas no total).
        
        Args:
            tema: Nome do tema
            
        Returns:
            Dicionário com todas as rodadas e perguntas
        """
        quiz = {
            '1': self.gerar_rodada_completa(tema),
            '2': self.gerar_rodada_completa(tema),
            '3': self.gerar_rodada_completa(tema)
        }
        
        return quiz


def gerar_perguntas_openai(tema: str, dificuldade: str, quantidade: int = 5) -> list[dict]:
    """
    Função de conveniência para gerar perguntas usando OpenAI.
    
    Args:
        tema: Nome do tema
        dificuldade: Nível ("facil", "medio", "dificil")
        quantidade: Número de perguntas
        
    Returns:
        Lista de perguntas geradas
    """
    service = OpenAIQuizService()
    return service.gerar_perguntas(tema, dificuldade, quantidade)

