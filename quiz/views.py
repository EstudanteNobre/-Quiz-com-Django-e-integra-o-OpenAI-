from datetime import datetime
from typing import Optional
import logging
import random
import string

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import transaction
from django.db.models import Sum
from django.db.models.functions import Coalesce
from django.http import HttpResponse
from django.utils import timezone
from .forms import CadastroForm, ImportarPerguntasForm
from .models import PerfilUsuario, Tema, Progresso, Pergunta, Dificuldade, RespostaUsuario, Conquista, ConquistaUsuario, QuizIAHistorico, SessaoJogo, EstatisticaProgresso, Sala, PerguntaSala, AlunoSala, ProgressoSala, RespostaSala
from .utils import obter_ou_criar_sessao_ativa, atualizar_tempo_sessao, criar_estatistica_progresso

logger = logging.getLogger(__name__)


def home(request):
    """View para a página inicial do Info Quiz"""
    # Se o usuário estiver logado, redireciona para dashboard
    if request.user.is_authenticated:
        return redirect('quiz:dashboard')
    return render(request, 'quiz/home.html')


def cadastro(request):
    """View para o cadastro de novos usuários"""
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            try:
                user = form.save()
                # Criar perfil do usuário com tipo_usuario (padrão: aluno)
                tipo_usuario = form.cleaned_data.get('tipo_usuario', 'aluno')
                # Garantir que o tipo_usuario seja válido
                if tipo_usuario not in ['aluno', 'professor']:
                    tipo_usuario = 'aluno'
                PerfilUsuario.objects.create(usuario=user, tipo_usuario=tipo_usuario)
                messages.success(request, 'Cadastro realizado com sucesso! Faça login para continuar.')
                return redirect('quiz:login')
            except Exception as e:
                logger.error(f"Erro ao criar usuário: {e}")
                messages.error(request, 'Erro ao criar conta. Por favor, tente novamente.')
        else:
            # Mostrar erros do formulário
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'{form.fields[field].label if field in form.fields else field}: {error}')
    else:
        form = CadastroForm()
    
    return render(request, 'quiz/cadastro.html', {'form': form})


def login_view(request):
    """View para login de usuários"""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if username and password:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Bem-vindo, {user.username}!')
                if user.is_superuser:
                    return redirect('quiz:admin_dashboard')
                return redirect('quiz:dashboard')
            else:
                messages.error(request, 'Usuário ou senha incorretos.')
        else:
            messages.error(request, 'Por favor, preencha todos os campos.')
    
    return render(request, 'quiz/login.html')


@login_required
def dashboard(request):
    """View para o dashboard do usuário logado"""
    if request.user.is_superuser:
        return redirect('quiz:admin_dashboard')

    # Obter ou criar perfil do usuário
    perfil, created = PerfilUsuario.objects.get_or_create(usuario=request.user)
    
    # Obter todos os temas
    temas = Tema.objects.all()
    
    total_perguntas_por_rodada = 5 * 3  # 5 por nível x 3 níveis

    # Dicionário de conquistas por tema
    conquistas_temas = {
        'Python': {'icone': '🐍', 'titulo': 'Mestre Python', 'cor': '#3776ab'},
        'Redes': {'icone': '🌐', 'titulo': 'Expert em Redes', 'cor': '#00bcd4'},
        'Banco de Dados': {'icone': '💾', 'titulo': 'DBA Master', 'cor': '#ff9800'},
        'Inglês': {'icone': '🔤', 'titulo': 'Inglês Avançado', 'cor': '#4caf50'},
        'Informática': {'icone': '💻', 'titulo': 'Guru da Informática', 'cor': '#2196f3'},
        'Análise de Projeto': {'icone': '📊', 'titulo': 'Analista Expert', 'cor': '#9c27b0'},
        'Algoritmos': {'icone': '🧮', 'titulo': 'Mestre em Algoritmos', 'cor': '#e91e63'},
    }
    
    # Calcular progresso por tema
    progresso_por_tema = []
    conquistas_por_tema = []
    
    for tema in temas:
        # Buscar progressos do usuário para este tema
        progressos = Progresso.objects.filter(usuario=request.user, tema=tema)
        
        # Calcular rodadas completas válidas
        rodadas_completas = progressos.filter(
            rodada_completa=True,
            perguntas_respondidas__gte=total_perguntas_por_rodada
        ).count()
        
        # Calcular progresso da rodada atual (se houver)
        progresso_atual = progressos.filter(rodada_completa=False).first()
        progresso_rodada = 0
        if progresso_atual:
            # Cada rodada tem 15 perguntas (5 fácil + 5 médio + 5 difícil)
            progresso_rodada = (progresso_atual.perguntas_respondidas / total_perguntas_por_rodada) * 100
        
        # Progresso total do tema (3 rodadas possíveis)
        progresso_total = (rodadas_completas / 3) * 100
        
        progresso_por_tema.append({
            'tema': tema,
            'rodadas_completas': rodadas_completas,
            'progresso_rodada': min(progresso_rodada, 100),
            'progresso_total': min(progresso_total, 100),
            'progresso_atual': progresso_atual,
        })
        
        # Criar conquista do tema
        conquista_info = conquistas_temas.get(tema.nome, {
            'icone': '📚',
            'titulo': f'Mestre em {tema.nome}',
            'cor': '#667eea'
        })
        
        # Determinar status da conquista
        desbloqueada = progresso_total >= 100  # 100% = 3 rodadas completas
        
        conquistas_por_tema.append({
            'tema': tema.nome,
            'icone': conquista_info['icone'],
            'titulo': conquista_info['titulo'],
            'cor': conquista_info['cor'],
            'progresso': min(progresso_total, 100),
            'rodadas': rodadas_completas,
            'desbloqueada': desbloqueada,
            'requisito': 'Complete 3 rodadas',
        })
    
    # Recalcular estatísticas globais com base nos dados atuais
    rodadas_validas = Progresso.objects.filter(
        usuario=request.user,
        rodada_completa=True,
        perguntas_respondidas__gte=total_perguntas_por_rodada
    ).count()
    pontos_totais = RespostaUsuario.objects.filter(usuario=request.user).aggregate(
        total=Coalesce(Sum('pontuacao'), 0)
    )['total']
    
    # Calcular XP: cada ponto = 1 XP, cada rodada completa = 50 XP bônus
    xp_total = pontos_totais + (rodadas_validas * 50)
    
    # Atualizar perfil
    perfil_atualizado = False
    if perfil.rodadas_completas != rodadas_validas or perfil.pontos_totais != pontos_totais or perfil.xp_total != xp_total:
        perfil.rodadas_completas = rodadas_validas
        perfil.pontos_totais = pontos_totais
        perfil.xp_total = xp_total
        perfil_atualizado = True
    
    # Calcular nível baseado no XP
    nivel_calculado = perfil.calcular_nivel()
    if perfil.nivel != nivel_calculado:
        perfil.nivel = nivel_calculado
        perfil.titulo = perfil.obter_titulo()
        perfil_atualizado = True
    
    if perfil_atualizado:
        perfil.save(update_fields=['rodadas_completas', 'pontos_totais', 'xp_total', 'nivel', 'titulo'])
    
    # Obter conquistas desbloqueadas
    conquistas_desbloqueadas = ConquistaUsuario.objects.filter(usuario=request.user).select_related('conquista').order_by('-desbloqueada_em')[:6]
    todas_conquistas = Conquista.objects.all()[:12]  # Limitar para não sobrecarregar
    
    # Preparar dados para gráfico de barras (últimas rodadas)
    progressos_recentes = Progresso.objects.filter(
        usuario=request.user,
        rodada_completa=True,
        perguntas_respondidas__gte=total_perguntas_por_rodada
    ).order_by('-atualizado_em')[:7]
    
    dados_grafico_barras = []
    max_pontuacao = 100
    for prog in progressos_recentes:
        pontuacao = prog.pontuacao_total or 0
        if pontuacao > max_pontuacao:
            max_pontuacao = pontuacao
        dados_grafico_barras.append({
            'tema': prog.tema.nome,
            'pontuacao': pontuacao,
            'data': prog.atualizado_em.strftime('%d/%m')
        })
    
    if max_pontuacao == 0:
        max_pontuacao = 100

    # Histórico de Quizzes com IA (últimos 5)
    quizzes_ia_historico = QuizIAHistorico.objects.filter(
        usuario=request.user
    ).order_by('-concluido_em')[:5]
    
    # Estatísticas de Quizzes com IA
    total_quizzes_ia = QuizIAHistorico.objects.filter(usuario=request.user).count()
    pontos_quizzes_ia = QuizIAHistorico.objects.filter(usuario=request.user).aggregate(
        total=Coalesce(Sum('pontuacao'), 0)
    )['total']

    context = {
        'perfil': perfil,
        'progresso_por_tema': progresso_por_tema,
        'conquistas_por_tema': conquistas_por_tema,
        'conquistas_desbloqueadas': conquistas_desbloqueadas,
        'todas_conquistas': todas_conquistas,
        'dados_grafico_barras': dados_grafico_barras,
        'max_pontuacao_grafico': max_pontuacao,
        'quizzes_ia_historico': quizzes_ia_historico,
        'total_quizzes_ia': total_quizzes_ia,
        'pontos_quizzes_ia': pontos_quizzes_ia,
    }
    
    return render(request, 'quiz/dashboard.html', context)


@login_required
def revisar_perguntas_erradas(request, tema_id):
    """
    View para revisar as perguntas erradas de uma rodada concluída.
    """
    tema = get_object_or_404(Tema, pk=tema_id)
    
    # Buscar a última rodada concluída do usuário para este tema
    progresso = Progresso.objects.filter(
        usuario=request.user,
        tema=tema,
        rodada_completa=True
    ).order_by('-atualizado_em').first()
    
    if not progresso:
        messages.warning(request, 'Nenhuma rodada concluída encontrada para revisão.')
        return redirect('quiz:jogar_tema', tema_id=tema.id)
    
    # Buscar todas as respostas erradas desta rodada
    respostas_erradas = RespostaUsuario.objects.filter(
        usuario=request.user,
        progresso=progresso,
        correta=False
    ).select_related('pergunta', 'pergunta__dificuldade')
    
    if not respostas_erradas.exists():
        messages.info(request, 'Parabéns! Você não errou nenhuma pergunta nesta rodada!')
        return redirect('quiz:jogar_tema', tema_id=tema.id)
    
    # Preparar dados das perguntas erradas
    perguntas_erradas = []
    for resposta in respostas_erradas:
        pergunta = resposta.pergunta
        perguntas_erradas.append({
            'id': pergunta.id,
            'texto': pergunta.texto,
            'alternativa_a': pergunta.alternativa_a,
            'alternativa_b': pergunta.alternativa_b,
            'alternativa_c': pergunta.alternativa_c,
            'alternativa_d': pergunta.alternativa_d,
            'resposta_correta': pergunta.resposta_correta,
            'resposta_escolhida': resposta.resposta_escolhida,
            'nivel': pergunta.dificuldade.nivel,
            'nivel_nome': pergunta.dificuldade.nome,
        })
    
    # Gerar dicas de estudo usando IA
    dicas_estudo = []
    try:
        from .services.openai_service import OpenAIQuizService
        service = OpenAIQuizService()
        
        perguntas_texto = []
        for i, pergunta in enumerate(perguntas_erradas, 1):
            perguntas_texto.append(f"{i}. {pergunta['texto']}")
        
        prompt_dicas = f"""Com base nas seguintes perguntas sobre "{tema.nome}" que o usuário errou, forneça dicas de estudo concisas e práticas.

Perguntas erradas:
{chr(10).join(perguntas_texto)}

Forneça:
1. Um resumo geral dos conceitos que precisam ser revisados
2. Dicas específicas para cada pergunta (máximo 2-3 linhas por pergunta)
3. Recursos sugeridos para estudo (se aplicável)

Formato JSON:
{{
    "resumo_geral": "Resumo dos conceitos a revisar",
    "dicas_por_pergunta": [
        {{
            "pergunta": "Texto da pergunta",
            "dica": "Dica específica para esta pergunta"
        }}
    ],
    "recursos": ["Recurso 1", "Recurso 2"]
}}"""
        
        response = service.client.chat.completions.create(
            model=service.model,
            messages=[
                {"role": "system", "content": "Você é um tutor educacional especializado em fornecer dicas de estudo práticas e concisas."},
                {"role": "user", "content": prompt_dicas}
            ],
            temperature=0.7,
            max_tokens=2000,
            response_format={"type": "json_object"}
        )
        
        import json
        dicas_data = json.loads(response.choices[0].message.content)
        dicas_estudo = dicas_data
        
    except Exception as e:
        logger.error(f"Erro ao gerar dicas: {e}")
        dicas_estudo = {
            "resumo_geral": f"Revise os conceitos básicos sobre {tema.nome}. Pratique mais exercícios relacionados às perguntas que você errou.",
            "dicas_por_pergunta": [],
            "recursos": [f"Pesquise mais sobre {tema.nome}", "Pratique exercícios similares"]
        }
    
    # Combinar perguntas erradas com dicas
    perguntas_com_dicas = []
    dicas_por_pergunta = dicas_estudo.get('dicas_por_pergunta', [])
    
    for i, pergunta in enumerate(perguntas_erradas):
        dica = ""
        if i < len(dicas_por_pergunta):
            dica = dicas_por_pergunta[i].get('dica', '')
        elif dicas_por_pergunta:
            for dica_item in dicas_por_pergunta:
                if pergunta['texto'] in dica_item.get('pergunta', ''):
                    dica = dica_item.get('dica', '')
                    break
        
        perguntas_com_dicas.append({
            **pergunta,
            'dica': dica or f"Revise os conceitos relacionados a esta pergunta sobre {tema.nome}."
        })
    
    context = {
        'tema': tema,
        'perguntas_erradas': perguntas_com_dicas,
        'resumo_geral': dicas_estudo.get('resumo_geral', ''),
        'recursos': dicas_estudo.get('recursos', []),
        'total_erradas': len(perguntas_erradas),
        'rodada': progresso.rodada_atual,
    }
    
    return render(request, 'quiz/revisar_perguntas_erradas.html', context)


@login_required
def escolher_tema(request):
    """View para escolher o tema do quiz"""
    temas = Tema.objects.all()
    
    # Dicionário de emojis para cada tema
    emojis_temas = {
        'Python': '🐍',
        'Redes': '🌐',
        'Banco de Dados': '💾',
        'Inglês': '🔤',
        'Informática': '💻',
        'Análise de Projeto': '📊',
        'Algoritmos': '🧮',
    }
    
    # Adicionar emoji a cada tema
    temas_com_emoji = []
    for tema in temas:
        emoji = emojis_temas.get(tema.nome, '📚')
        temas_com_emoji.append({
            'tema': tema,
            'emoji': emoji,
        })
    
    # Ranking geral por tema - Top 5 de cada tema
    from django.db.models import Sum, Count
    from django.contrib.auth.models import User
    
    ranking_por_tema = {}
    
    for tema in temas:
        # Buscar usuários com progresso neste tema
        usuarios_tema = Progresso.objects.filter(
            tema=tema,
            rodada_completa=True
        ).values('usuario').annotate(
            total_pontos=Sum('pontuacao_total'),
            total_rodadas=Count('id')
        ).order_by('-total_pontos')[:5]
        
        ranking_tema = []
        for posicao, stats in enumerate(usuarios_tema, start=1):
            user = User.objects.get(id=stats['usuario'])
            is_current = user.id == request.user.id
            
            ranking_tema.append({
                'posicao': posicao,
                'usuario': user.get_full_name() or user.username,
                'pontos': stats['total_pontos'] or 0,
                'rodadas': stats['total_rodadas'] or 0,
                'atual': is_current,
            })
        
        if ranking_tema:
            ranking_por_tema[tema.id] = ranking_tema
    
    context = {
        'temas': temas_com_emoji,
        'ranking_por_tema': ranking_por_tema,
    }
    
    return render(request, 'quiz/escolher_tema.html', context)


@login_required
def admin_dashboard(request):
    if not request.user.is_superuser:
        messages.error(request, 'Você não tem permissão para acessar o painel administrativo.')
        return redirect('quiz:dashboard')
    return render(request, 'quiz/admin_dashboard.html')


def _obter_rotulo_dificuldade(nivel: str) -> str:
    """Retorna o rótulo legível para o nível de dificuldade informado."""
    mapa = dict(Dificuldade.NIVEL_CHOICES)
    return mapa.get(nivel, nivel.title())


def _calcular_pontos_pergunta(correta: bool, tempo_decorrido: Optional[float], pontos_base: int = 10) -> int:
    """
    Calcula a pontuação obtida na pergunta considerando tempo de resposta.
    
    Lógica de pontuação por tempo:
    - Até 15 segundos: 100% dos pontos (pontos_base)
    - 15-30 segundos: 80% dos pontos
    - 30-45 segundos: 60% dos pontos
    - 45-60 segundos: 40% dos pontos
    - 60+ segundos: 20% dos pontos (mínimo)
    """
    if not correta:
        return 0

    if tempo_decorrido is None:
        return pontos_base

    # Faixas de tempo e percentuais de pontuação
    if tempo_decorrido <= 15:
        # Até 15 segundos: pontuação máxima
        percentual = 1.0
    elif tempo_decorrido <= 30:
        # 15-30 segundos: 80%
        percentual = 0.8
    elif tempo_decorrido <= 45:
        # 30-45 segundos: 60%
        percentual = 0.6
    elif tempo_decorrido <= 60:
        # 45-60 segundos: 40%
        percentual = 0.4
    else:
        # 60+ segundos: 20% (mínimo)
        percentual = 0.2

    pontos = int(round(pontos_base * percentual))
    return max(1, pontos)  # Mínimo de 1 ponto


def _obter_proxima_pergunta(progresso: Progresso, limite_por_nivel: int = 5):
    """Retorna a próxima pergunta disponível de acordo com o andamento do progresso."""
    niveis_ordenados = ['facil', 'medio', 'dificil']
    tema = progresso.tema

    for nivel in niveis_ordenados:
        respostas_nivel = progresso.respostas.filter(
            pergunta__dificuldade__nivel=nivel
        ).count()

        if respostas_nivel >= limite_por_nivel:
            # Este nível já foi concluído, seguir para o próximo
            continue

        perguntas_disponiveis = Pergunta.objects.filter(
            tema=tema,
            dificuldade__nivel=nivel
        ).order_by('id')

        if respostas_nivel < min(perguntas_disponiveis.count(), limite_por_nivel):
            pergunta = perguntas_disponiveis[respostas_nivel]
            if progresso.nivel_atual != nivel:
                progresso.nivel_atual = nivel
                progresso.save(update_fields=['nivel_atual'])
            return pergunta

    # Nenhuma pergunta restante
    return None


@login_required
def jogar_tema(request, tema_id):
    """View principal da rodada de perguntas para o tema escolhido."""
    tema = get_object_or_404(Tema, pk=tema_id)
    perfil, _ = PerfilUsuario.objects.get_or_create(usuario=request.user)

    rodadas_totais = 3
    perguntas_por_nivel = 5
    niveis_ordenados = ['facil', 'medio', 'dificil']
    total_perguntas_por_rodada = perguntas_por_nivel * len(niveis_ordenados)

    if request.GET.get('reiniciar') == '1':
        with transaction.atomic():
            RespostaUsuario.objects.filter(
                usuario=request.user,
                pergunta__tema=tema
            ).delete()
            Progresso.objects.filter(
                usuario=request.user,
                tema=tema
            ).delete()

        rodadas_validas = Progresso.objects.filter(
            usuario=request.user,
            rodada_completa=True,
            perguntas_respondidas__gte=total_perguntas_por_rodada
        ).count()
        pontos_totais = RespostaUsuario.objects.filter(usuario=request.user).aggregate(
            total=Coalesce(Sum('pontuacao'), 0)
        )['total']
        perfil.rodadas_completas = rodadas_validas
        perfil.pontos_totais = pontos_totais
        perfil.save(update_fields=['rodadas_completas', 'pontos_totais'])

        messages.info(request, f'O tema {tema.nome} foi reiniciado. Boa sorte nas novas rodadas!')
        return redirect('quiz:jogar_tema', tema_id=tema.id)

    # Identificar progressos existentes
    progresso_em_andamento = Progresso.objects.filter(
        usuario=request.user,
        tema=tema,
        rodada_completa=False
    ).order_by('rodada_atual').first()

    rodadas_concluidas = Progresso.objects.filter(
        usuario=request.user,
        tema=tema,
        rodada_completa=True,
        perguntas_respondidas__gte=total_perguntas_por_rodada
    ).count()

    # Verificar solicitação explícita de nova rodada
    if request.GET.get('nova_rodada') == '1' and rodadas_concluidas < rodadas_totais:
        if progresso_em_andamento and not progresso_em_andamento.rodada_completa:
            # Não iniciar nova rodada enquanto houver uma em curso
            pass
        else:
            numero_rodada = rodadas_concluidas + 1
            progresso_em_andamento, _ = Progresso.objects.get_or_create(
                usuario=request.user,
                tema=tema,
                rodada_atual=numero_rodada,
                defaults={'nivel_atual': 'facil'}
            )
            if progresso_em_andamento.rodada_completa and progresso_em_andamento.perguntas_respondidas < total_perguntas_por_rodada:
                progresso_em_andamento.rodada_completa = False
                progresso_em_andamento.perguntas_respondidas = 0
                progresso_em_andamento.perguntas_corretas = 0
                progresso_em_andamento.nivel_atual = 'facil'
                progresso_em_andamento.save()

    # Criar progresso se necessário
    if not progresso_em_andamento and rodadas_concluidas < rodadas_totais:
        numero_rodada = rodadas_concluidas + 1
        progresso_em_andamento, _ = Progresso.objects.get_or_create(
            usuario=request.user,
            tema=tema,
            rodada_atual=numero_rodada,
            defaults={'nivel_atual': 'facil'}
        )
        if progresso_em_andamento.rodada_completa and progresso_em_andamento.perguntas_respondidas < total_perguntas_por_rodada:
            progresso_em_andamento.rodada_completa = False
            progresso_em_andamento.perguntas_respondidas = 0
            progresso_em_andamento.perguntas_corretas = 0
            progresso_em_andamento.nivel_atual = 'facil'
            progresso_em_andamento.save()

    # Caso todas as rodadas tenham sido concluídas
    if not progresso_em_andamento and rodadas_concluidas >= rodadas_totais:
        context = {
            'tema': tema,
            'perfil': perfil,
            'tema_concluido': True,
            'rodadas_totais': rodadas_totais,
        }
        return render(request, 'quiz/rodada.html', context)

    progresso = progresso_em_andamento

    feedback = None
    feedback_tipo = None
    resposta_correta = None
    rodada_concluida_agora = False

    session_key = None
    if progresso:
        session_key = f'quiz_pergunta_inicio_{progresso.pk}'

    if request.method == 'POST' and progresso and not progresso.rodada_completa:
        pergunta_id = request.POST.get('pergunta_id')
        resposta_escolhida = request.POST.get('resposta')

        if pergunta_id and resposta_escolhida:
            pergunta = get_object_or_404(Pergunta, pk=pergunta_id, tema=tema)

            # Evitar respostas duplicadas para a mesma pergunta na rodada
            resposta_existente = progresso.respostas.filter(pergunta=pergunta).first()

            if not resposta_existente:
                correta = pergunta.resposta_correta == resposta_escolhida
                agora = timezone.now()
                tempo_decorrido = None
                if session_key:
                    tempo_inicio_iso = request.session.pop(session_key, None)
                    if tempo_inicio_iso:
                        try:
                            tempo_inicio = datetime.fromisoformat(tempo_inicio_iso)
                            if timezone.is_naive(tempo_inicio):
                                tempo_inicio = timezone.make_aware(tempo_inicio, timezone.get_current_timezone())
                            tempo_decorrido = (agora - tempo_inicio).total_seconds()
                            tempo_decorrido = max(0, tempo_decorrido)
                        except ValueError:
                            tempo_decorrido = None

                # Pontuação base por nível de dificuldade
                pontos_base_por_nivel = {'facil': 5, 'medio': 10, 'dificil': 15}
                pontos_base = pontos_base_por_nivel.get(pergunta.dificuldade.nivel, 10)
                pontos_obtidos = _calcular_pontos_pergunta(correta, tempo_decorrido, pontos_base)

                with transaction.atomic():
                    # Rastrear sessão de jogo
                    sessao = obter_ou_criar_sessao_ativa(request.user, tema)
                    if tempo_decorrido:
                        atualizar_tempo_sessao(sessao, tempo_decorrido)
                    
                    resposta_usuario = RespostaUsuario.objects.create(
                        usuario=request.user,
                        pergunta=pergunta,
                        resposta_escolhida=resposta_escolhida,
                        correta=correta,
                        pontuacao=pontos_obtidos,
                        progresso=progresso
                    )

                    # Atualizar contadores
                    progresso.perguntas_respondidas = progresso.respostas.count()
                    progresso.perguntas_corretas = progresso.respostas.filter(correta=True).count()
                    progresso.pontuacao_total = progresso.respostas.aggregate(
                        total=Coalesce(Sum('pontuacao'), 0)
                    )['total']

                    # Verificar se nível atual foi concluído
                    respostas_nivel = progresso.respostas.filter(
                        pergunta__dificuldade=pergunta.dificuldade
                    ).count()
                    if respostas_nivel >= perguntas_por_nivel:
                        # Avançar para o próximo nível, se houver
                        if pergunta.dificuldade.nivel == 'facil':
                            progresso.nivel_atual = 'medio'
                        elif pergunta.dificuldade.nivel == 'medio':
                            progresso.nivel_atual = 'dificil'

                    # Verificar se a rodada foi concluída
                    total_respondidas = [
                        progresso.respostas.filter(pergunta__dificuldade__nivel=n).count()
                        for n in niveis_ordenados
                    ]
                    if all(qtd >= perguntas_por_nivel for qtd in total_respondidas):
                        if not progresso.rodada_completa:
                            progresso.rodada_completa = True
                            rodada_concluida_agora = True

                    progresso.save()

                    if rodada_concluida_agora:
                        # Criar estatística de progresso quando rodada é completada
                        try:
                            criar_estatistica_progresso(request.user)
                        except Exception as e:
                            logger.error(f"Erro ao criar estatística de progresso: {e}")
                        
                        rodadas_validas = Progresso.objects.filter(
                            usuario=request.user,
                            rodada_completa=True,
                            perguntas_respondidas__gte=total_perguntas_por_rodada
                        ).count()
                        pontos_totais = RespostaUsuario.objects.filter(usuario=request.user).aggregate(
                            total=Coalesce(Sum('pontuacao'), 0)
                        )['total']
                        perfil.rodadas_completas = rodadas_validas
                        perfil.pontos_totais = pontos_totais
                        perfil.save(update_fields=['rodadas_completas', 'pontos_totais'])
                    else:
                        # Atualiza pontos parciais mesmo durante a rodada
                        pontos_totais = RespostaUsuario.objects.filter(usuario=request.user).aggregate(
                            total=Coalesce(Sum('pontuacao'), 0)
                        )['total']
                        if perfil.pontos_totais != pontos_totais:
                            perfil.pontos_totais = pontos_totais
                            perfil.save(update_fields=['pontos_totais'])

                if correta:
                    if tempo_decorrido is not None:
                        if tempo_decorrido <= 15:
                            feedback = f"🚀 Resposta rápida! +{pontos_obtidos} pontos!"
                        elif tempo_decorrido <= 30:
                            feedback = f"✅ Resposta correta! +{pontos_obtidos} pontos."
                        elif tempo_decorrido <= 45:
                            feedback = f"👍 Correto! Tente ser mais rápido. +{pontos_obtidos} pontos."
                        else:
                            feedback = f"⏱️ Correto, mas muito lento. +{pontos_obtidos} pontos."
                    else:
                        feedback = f"✅ Resposta correta! +{pontos_obtidos} pontos."
                    feedback_tipo = "success"
                else:
                    feedback = "Resposta incorreta. Tente novamente na próxima!"
                    feedback_tipo = "error"
                    resposta_correta = pergunta.resposta_correta
            else:
                feedback = "Você já respondeu a esta pergunta nesta rodada."
                feedback_tipo = "warning"
                resposta_correta = resposta_existente.pergunta.resposta_correta

    # Atualizar referências após possível alteração
    progresso.refresh_from_db()

    respostas_por_nivel = {
        nivel: progresso.respostas.filter(pergunta__dificuldade__nivel=nivel).count()
        for nivel in niveis_ordenados
    }

    pergunta_atual = None
    if not progresso.rodada_completa:
        pergunta_atual = _obter_proxima_pergunta(progresso, perguntas_por_nivel)
        if not pergunta_atual:
            # Sem pergunta disponível, marcar rodada como completa
            if not progresso.rodada_completa:
                progresso.rodada_completa = True
                progresso.save(update_fields=['rodada_completa'])
                rodada_concluida_agora = True
                rodadas_validas = Progresso.objects.filter(
                    usuario=request.user,
                    rodada_completa=True,
                    perguntas_respondidas__gte=total_perguntas_por_rodada
                ).count()
                pontos_totais = RespostaUsuario.objects.filter(usuario=request.user).aggregate(
                    total=Coalesce(Sum('pontuacao'), 0)
                )['total']
                perfil.rodadas_completas = rodadas_validas
                perfil.pontos_totais = pontos_totais
                perfil.save(update_fields=['rodadas_completas', 'pontos_totais'])
                feedback = None
        else:
            if session_key:
                request.session[session_key] = timezone.now().isoformat()

    # Recalcular rodadas concluídas após possíveis alterações
    rodadas_concluidas = Progresso.objects.filter(
        usuario=request.user,
        tema=tema,
        rodada_completa=True,
        perguntas_respondidas__gte=total_perguntas_por_rodada
    ).count()

    respondidas_total = progresso.perguntas_respondidas
    progresso_percentual = min(100, int((respondidas_total / total_perguntas_por_rodada) * 100))
    nivel_atual_label = _obter_rotulo_dificuldade(progresso.nivel_atual)
    total_perguntas = total_perguntas_por_rodada
    numero_pergunta_atual = min(total_perguntas_por_rodada, respondidas_total + 1)

    if progresso.rodada_completa and session_key:
        request.session.pop(session_key, None)

    ranking_perfis = PerfilUsuario.objects.select_related('usuario').order_by(
        '-pontos_totais', '-rodadas_completas', 'usuario__username'
    )[:5]
    ranking = []
    usuario_presente = False
    for posicao, perfil_rank in enumerate(ranking_perfis, start=1):
        atual = perfil_rank.usuario_id == request.user.id
        if atual:
            usuario_presente = True
        ranking.append({
            'posicao': posicao,
            'usuario': perfil_rank.usuario.get_full_name() or perfil_rank.usuario.username,
            'pontos': perfil_rank.pontos_totais,
            'rodadas': perfil_rank.rodadas_completas,
            'atual': atual,
            'fora_ranking': False,
        })

    posicao_usuario = PerfilUsuario.objects.filter(
        pontos_totais__gt=perfil.pontos_totais
    ).count() + 1

    if not usuario_presente:
        ranking.append({
            'posicao': posicao_usuario,
            'usuario': perfil.usuario.get_full_name() or perfil.usuario.username,
            'pontos': perfil.pontos_totais,
            'rodadas': perfil.rodadas_completas,
            'atual': True,
            'fora_ranking': True,
        })

    feedback_para_exibir = feedback if not progresso.rodada_completa else None
    top_limite = len(ranking_perfis) or 5
    
    # Verificar se há perguntas erradas na rodada
    tem_perguntas_erradas = False
    if progresso.rodada_completa:
        total_erradas = progresso.respostas.filter(correta=False).count()
        tem_perguntas_erradas = total_erradas > 0

    context = {
        'tema': tema,
        'perfil': perfil,
        'progresso': progresso,
        'pergunta': pergunta_atual,
        'feedback': feedback_para_exibir,
        'feedback_tipo': feedback_tipo,
        'resposta_correta': resposta_correta,
        'rodadas_concluidas': rodadas_concluidas,
        'rodadas_totais': rodadas_totais,
        'perguntas_por_nivel': perguntas_por_nivel,
        'respostas_por_nivel': respostas_por_nivel,
        'respondidas_total': respondidas_total,
        'progresso_percentual': progresso_percentual,
        'nivel_atual_label': nivel_atual_label,
        'rodada_concluida': progresso.rodada_completa,
        'rodada_concluida_agora': rodada_concluida_agora,
        'tema_concluido': False,
        'total_perguntas': total_perguntas,
        'numero_pergunta_atual': numero_pergunta_atual,
        'rodada_pontuacao': progresso.pontuacao_total,
        'ranking': ranking,
        'posicao_usuario': posicao_usuario,
        'mostrar_nota_ranking': not usuario_presente,
        'ranking_top_limite': top_limite,
        'tem_perguntas_erradas': tem_perguntas_erradas,
    }
    return render(request, 'quiz/rodada.html', context)


def logout_view(request):
    """View para logout de usuários"""
    auto_logout = request.GET.get('auto') == '1' or request.POST.get('auto') == '1'
    logout(request)
    if auto_logout:
        return HttpResponse(status=204)
    messages.success(request, 'Você saiu com sucesso!')
    return redirect('quiz:home')


# =============================================
# VIEWS PARA QUIZ COM IA (OpenAI)
# =============================================

@login_required
def quiz_ia_escolher_tema(request):
    """
    View para escolher ou criar um tema personalizado para quiz com IA.
    """
    # Temas sugeridos para o usuário
    temas_sugeridos = [
        {'nome': 'Python', 'emoji': '🐍', 'descricao': 'Linguagem de programação Python'},
        {'nome': 'JavaScript', 'emoji': '💛', 'descricao': 'Linguagem de programação JavaScript'},
        {'nome': 'Redes de Computadores', 'emoji': '🌐', 'descricao': 'Redes, protocolos e infraestrutura'},
        {'nome': 'Banco de Dados', 'emoji': '💾', 'descricao': 'SQL, NoSQL e modelagem de dados'},
        {'nome': 'Segurança da Informação', 'emoji': '🔐', 'descricao': 'Cibersegurança e proteção de dados'},
        {'nome': 'Inteligência Artificial', 'emoji': '🤖', 'descricao': 'Machine Learning e Deep Learning'},
        {'nome': 'DevOps', 'emoji': '⚙️', 'descricao': 'CI/CD, Docker, Kubernetes'},
        {'nome': 'Cloud Computing', 'emoji': '☁️', 'descricao': 'AWS, Azure, Google Cloud'},
        {'nome': 'Linux', 'emoji': '🐧', 'descricao': 'Sistema operacional Linux e comandos'},
        {'nome': 'Git e Versionamento', 'emoji': '📂', 'descricao': 'Controle de versão com Git'},
        {'nome': 'HTML e CSS', 'emoji': '🎨', 'descricao': 'Desenvolvimento web front-end'},
        {'nome': 'React', 'emoji': '⚛️', 'descricao': 'Biblioteca JavaScript para interfaces'},
    ]
    
    # Ranking geral de Quiz IA - Top 10 por pontuação total
    from django.db.models import Sum, Count, F, FloatField, ExpressionWrapper
    from django.contrib.auth.models import User
    
    # Buscar estatísticas de cada usuário que fez quiz IA
    usuarios_com_quiz = QuizIAHistorico.objects.values('usuario').annotate(
        total_pontos=Sum('pontuacao'),
        total_quizzes=Count('id'),
        total_corretas=Sum('respostas_corretas'),
        total_perguntas=Sum('total_perguntas')
    )
    
    # Montar ranking com cálculo de porcentagem
    ranking_data = []
    for stats in usuarios_com_quiz:
        total_corretas = stats['total_corretas'] or 0
        total_perguntas = stats['total_perguntas'] or 1
        percentual = (total_corretas / total_perguntas) * 100
        
        ranking_data.append({
            'usuario_id': stats['usuario'],
            'pontos': stats['total_pontos'] or 0,
            'quizzes': stats['total_quizzes'] or 0,
            'percentual': percentual,
        })
    
    # Ordenar por: 1º pontos totais, 2º porcentagem de acertos
    ranking_data.sort(key=lambda x: (-x['pontos'], -x['percentual']))
    
    ranking = []
    usuario_no_ranking = False
    
    for posicao, stats in enumerate(ranking_data[:10], start=1):
        user = User.objects.get(id=stats['usuario_id'])
        is_current = user.id == request.user.id
        if is_current:
            usuario_no_ranking = True
        
        ranking.append({
            'posicao': posicao,
            'usuario': user.get_full_name() or user.username,
            'pontos': stats['pontos'],
            'quizzes': stats['quizzes'],
            'percentual': int(stats['percentual']),
            'atual': is_current,
        })
    
    # Se o usuário não está no top 10, adicionar sua posição
    if not usuario_no_ranking:
        user_stats = QuizIAHistorico.objects.filter(usuario=request.user).aggregate(
            total_pontos=Sum('pontuacao'),
            total_quizzes=Count('id'),
            total_corretas=Sum('respostas_corretas'),
            total_perguntas=Sum('total_perguntas')
        )
        
        if user_stats['total_pontos']:
            # Calcular porcentagem geral
            total_corretas = user_stats['total_corretas'] or 0
            total_perguntas = user_stats['total_perguntas'] or 1
            percentual_geral = int((total_corretas / total_perguntas) * 100)
            
            # Calcular posição do usuário
            user_pontos = user_stats['total_pontos']
            posicao_usuario = sum(1 for r in ranking_data if r['pontos'] > user_pontos) + 1
            
            ranking.append({
                'posicao': posicao_usuario,
                'usuario': request.user.get_full_name() or request.user.username,
                'pontos': user_stats['total_pontos'] or 0,
                'quizzes': user_stats['total_quizzes'] or 0,
                'percentual': percentual_geral,
                'atual': True,
                'fora_ranking': True,
            })
    
    context = {
        'temas_sugeridos': temas_sugeridos,
        'ranking_ia': ranking,
    }
    
    return render(request, 'quiz/quiz_ia_escolher_tema.html', context)


@login_required
def quiz_ia_gerar(request):
    """
    View para gerar perguntas de quiz usando IA.
    Recebe o tema via POST e gera as perguntas.
    """
    if request.method != 'POST':
        return redirect('quiz:quiz_ia_escolher_tema')
    
    tema_nome = request.POST.get('tema', '').strip()
    
    if not tema_nome:
        messages.error(request, 'Por favor, informe um tema para o quiz.')
        return redirect('quiz:quiz_ia_escolher_tema')
    
    # Verificar se a chave da API está configurada
    from django.conf import settings as django_settings
    if not getattr(django_settings, 'OPENAI_API_KEY', None):
        messages.error(
            request, 
            'A chave da API da OpenAI não está configurada. '
            'Verifique o arquivo .env e adicione OPENAI_API_KEY.'
        )
        return redirect('quiz:quiz_ia_escolher_tema')
    
    try:
        from .services.openai_service import OpenAIQuizService
        
        service = OpenAIQuizService()
        
        # Gerar uma rodada completa (15 perguntas: 5 fáceis + 5 médias + 5 difíceis)
        rodada = service.gerar_rodada_completa(tema_nome)
        
        # Armazenar as perguntas na sessão para uso posterior
        request.session['quiz_ia_tema'] = tema_nome
        request.session['quiz_ia_perguntas'] = rodada
        request.session['quiz_ia_indice'] = 0
        request.session['quiz_ia_nivel'] = 'facil'
        request.session['quiz_ia_pontuacao'] = 0
        request.session['quiz_ia_corretas'] = 0
        request.session['quiz_ia_total_respondidas'] = 0
        
        messages.success(request, f'Quiz sobre "{tema_nome}" gerado com sucesso! 🎉')
        return redirect('quiz:quiz_ia_jogar')
        
    except ImportError as e:
        messages.error(request, 'Erro ao importar o serviço de IA. Verifique se a biblioteca openai está instalada.')
        return redirect('quiz:quiz_ia_escolher_tema')
    except ValueError as e:
        messages.error(request, str(e))
        return redirect('quiz:quiz_ia_escolher_tema')
    except Exception as e:
        messages.error(request, f'Erro ao gerar quiz: {str(e)}')
        return redirect('quiz:quiz_ia_escolher_tema')


@login_required
def quiz_ia_jogar(request):
    """
    View para jogar o quiz gerado pela IA.
    As perguntas são armazenadas na sessão.
    """
    # Verificar se há um quiz ativo na sessão
    tema = request.session.get('quiz_ia_tema')
    perguntas = request.session.get('quiz_ia_perguntas')
    
    if not tema or not perguntas:
        messages.warning(request, 'Nenhum quiz ativo. Gere um novo quiz.')
        return redirect('quiz:quiz_ia_escolher_tema')
    
    # Obter estado atual do quiz
    nivel_atual = request.session.get('quiz_ia_nivel', 'facil')
    indice = request.session.get('quiz_ia_indice', 0)
    pontuacao = request.session.get('quiz_ia_pontuacao', 0)
    corretas = request.session.get('quiz_ia_corretas', 0)
    total_respondidas = request.session.get('quiz_ia_total_respondidas', 0)
    perguntas_erradas = request.session.get('quiz_ia_perguntas_erradas', [])
    
    feedback = None
    feedback_tipo = None
    resposta_correta = None
    
    # Chave para armazenar o tempo de início da pergunta
    session_key_tempo = 'quiz_ia_tempo_inicio'
    
    # Processar resposta do usuário
    if request.method == 'POST':
        resposta_escolhida = request.POST.get('resposta')
        pergunta_idx = int(request.POST.get('pergunta_idx', 0))
        nivel_pergunta = request.POST.get('nivel_pergunta', nivel_atual)
        
        if resposta_escolhida and nivel_pergunta in perguntas:
            pergunta_atual = perguntas[nivel_pergunta][pergunta_idx]
            correta = pergunta_atual['resposta_correta'] == resposta_escolhida.upper()
            
            # Calcular tempo decorrido
            tempo_decorrido = None
            tempo_inicio_iso = request.session.pop(session_key_tempo, None)
            if tempo_inicio_iso:
                try:
                    tempo_inicio = datetime.fromisoformat(tempo_inicio_iso)
                    if timezone.is_naive(tempo_inicio):
                        tempo_inicio = timezone.make_aware(tempo_inicio, timezone.get_current_timezone())
                    tempo_decorrido = (timezone.now() - tempo_inicio).total_seconds()
                    tempo_decorrido = max(0, tempo_decorrido)
                except ValueError:
                    tempo_decorrido = None
            
            # Pontuação base por nível
            pontos_base_por_nivel = {'facil': 5, 'medio': 10, 'dificil': 15}
            pontos_base = pontos_base_por_nivel.get(nivel_pergunta, 5)
            
            # Calcular pontos considerando tempo
            pontos = _calcular_pontos_pergunta(correta, tempo_decorrido, pontos_base)
            
            if correta:
                pontuacao += pontos
                corretas += 1
                
                # Feedback baseado no tempo
                if tempo_decorrido is not None:
                    if tempo_decorrido <= 15:
                        feedback = f'🚀 Resposta rápida e correta! +{pontos} pontos'
                    elif tempo_decorrido <= 30:
                        feedback = f'✅ Resposta correta! +{pontos} pontos'
                    elif tempo_decorrido <= 45:
                        feedback = f'👍 Correto, mas poderia ser mais rápido. +{pontos} pontos'
                    else:
                        feedback = f'⏱️ Correto! Tente ser mais rápido. +{pontos} pontos'
                else:
                    feedback = f'✅ Resposta correta! +{pontos} pontos'
                feedback_tipo = 'success'
            else:
                feedback = '❌ Resposta incorreta!'
                feedback_tipo = 'error'
                resposta_correta = pergunta_atual['resposta_correta']
                
                # Armazenar pergunta errada com informações
                pergunta_errada = {
                    'texto': pergunta_atual['texto'],
                    'alternativa_a': pergunta_atual['alternativa_a'],
                    'alternativa_b': pergunta_atual['alternativa_b'],
                    'alternativa_c': pergunta_atual['alternativa_c'],
                    'alternativa_d': pergunta_atual['alternativa_d'],
                    'resposta_correta': pergunta_atual['resposta_correta'],
                    'resposta_escolhida': resposta_escolhida.upper(),
                    'nivel': nivel_pergunta,
                }
                perguntas_erradas.append(pergunta_errada)
            
            total_respondidas += 1
            indice += 1
            
            # Verificar se precisa mudar de nível
            if indice >= len(perguntas[nivel_atual]):
                if nivel_atual == 'facil':
                    nivel_atual = 'medio'
                    indice = 0
                elif nivel_atual == 'medio':
                    nivel_atual = 'dificil'
                    indice = 0
                elif nivel_atual == 'dificil':
                    # Quiz completo!
                    request.session['quiz_ia_pontuacao'] = pontuacao
                    request.session['quiz_ia_corretas'] = corretas
                    request.session['quiz_ia_total_respondidas'] = total_respondidas
                    request.session['quiz_ia_perguntas_erradas'] = perguntas_erradas
                    return redirect('quiz:quiz_ia_resultado')
            
            # Atualizar sessão
            request.session['quiz_ia_nivel'] = nivel_atual
            request.session['quiz_ia_indice'] = indice
            request.session['quiz_ia_pontuacao'] = pontuacao
            request.session['quiz_ia_corretas'] = corretas
            request.session['quiz_ia_total_respondidas'] = total_respondidas
            request.session['quiz_ia_perguntas_erradas'] = perguntas_erradas
    
    # Obter pergunta atual
    perguntas_nivel = perguntas.get(nivel_atual, [])
    
    if indice >= len(perguntas_nivel):
        # Sem mais perguntas neste nível, avançar
        if nivel_atual == 'facil' and perguntas.get('medio'):
            nivel_atual = 'medio'
            indice = 0
        elif nivel_atual == 'medio' and perguntas.get('dificil'):
            nivel_atual = 'dificil'
            indice = 0
        else:
            # Quiz completo
            return redirect('quiz:quiz_ia_resultado')
        
        request.session['quiz_ia_nivel'] = nivel_atual
        request.session['quiz_ia_indice'] = indice
        perguntas_nivel = perguntas.get(nivel_atual, [])
    
    pergunta_atual = perguntas_nivel[indice] if perguntas_nivel else None
    
    # Salvar tempo de início da pergunta atual
    if pergunta_atual:
        request.session[session_key_tempo] = timezone.now().isoformat()
    
    # Calcular progresso
    total_perguntas = sum(len(perguntas.get(n, [])) for n in ['facil', 'medio', 'dificil'])
    progresso_percentual = int((total_respondidas / total_perguntas) * 100) if total_perguntas > 0 else 0
    
    # Labels para níveis
    nivel_labels = {'facil': 'Fácil', 'medio': 'Médio', 'dificil': 'Difícil'}
    
    context = {
        'tema': tema,
        'pergunta': pergunta_atual,
        'pergunta_idx': indice,
        'nivel_atual': nivel_atual,
        'nivel_label': nivel_labels.get(nivel_atual, nivel_atual),
        'pontuacao': pontuacao,
        'corretas': corretas,
        'total_respondidas': total_respondidas,
        'total_perguntas': total_perguntas,
        'progresso_percentual': progresso_percentual,
        'numero_pergunta_atual': total_respondidas + 1,
        'feedback': feedback,
        'feedback_tipo': feedback_tipo,
        'resposta_correta': resposta_correta,
    }
    
    return render(request, 'quiz/quiz_ia_jogar.html', context)


@login_required
def quiz_ia_resultado(request):
    """
    View para exibir o resultado do quiz gerado pela IA.
    """
    from .models import QuizIAHistorico
    
    tema = request.session.get('quiz_ia_tema')
    pontuacao = request.session.get('quiz_ia_pontuacao', 0)
    corretas = request.session.get('quiz_ia_corretas', 0)
    total_respondidas = request.session.get('quiz_ia_total_respondidas', 0)
    
    if not tema:
        messages.warning(request, 'Nenhum quiz encontrado.')
        return redirect('quiz:quiz_ia_escolher_tema')
    
    # Calcular porcentagem de acertos
    percentual_acertos = int((corretas / total_respondidas) * 100) if total_respondidas > 0 else 0
    
    # Salvar histórico no banco de dados
    QuizIAHistorico.objects.create(
        usuario=request.user,
        tema=tema,
        pontuacao=pontuacao,
        total_perguntas=total_respondidas,
        respostas_corretas=corretas,
        percentual_acertos=percentual_acertos
    )
    
    # Criar estatística de progresso após quiz IA
    try:
        criar_estatistica_progresso(request.user)
    except Exception as e:
        logger.error(f"Erro ao criar estatística de progresso: {e}")
    
    # Determinar mensagem de feedback
    if percentual_acertos >= 90:
        mensagem = '🏆 Excelente! Você é um mestre!'
        cor_mensagem = 'success'
    elif percentual_acertos >= 70:
        mensagem = '🎉 Muito bom! Continue assim!'
        cor_mensagem = 'success'
    elif percentual_acertos >= 50:
        mensagem = '👍 Bom trabalho! Pratique mais!'
        cor_mensagem = 'warning'
    else:
        mensagem = '📚 Continue estudando! Você vai melhorar!'
        cor_mensagem = 'info'
    
    # Obter perguntas erradas da sessão
    perguntas_erradas = request.session.get('quiz_ia_perguntas_erradas', [])
    
    # Limpar a sessão do quiz (mas manter perguntas erradas temporariamente)
    for key in ['quiz_ia_perguntas', 'quiz_ia_indice', 
                'quiz_ia_nivel', 'quiz_ia_pontuacao', 'quiz_ia_corretas',
                'quiz_ia_total_respondidas']:
        request.session.pop(key, None)
    
    # Calcular respostas erradas
    erradas = total_respondidas - corretas
    
    context = {
        'tema': tema,
        'pontuacao': pontuacao,
        'corretas': corretas,
        'erradas': erradas,
        'total_respondidas': total_respondidas,
        'percentual_acertos': percentual_acertos,
        'mensagem': mensagem,
        'cor_mensagem': cor_mensagem,
        'tem_perguntas_erradas': len(perguntas_erradas) > 0,
    }
    
    return render(request, 'quiz/quiz_ia_resultado.html', context)


@login_required
def quiz_ia_revisar_erradas(request):
    """
    View para revisar as perguntas erradas com dicas de estudo.
    """
    tema = request.session.get('quiz_ia_tema')
    perguntas_erradas = request.session.get('quiz_ia_perguntas_erradas', [])
    
    if not tema or not perguntas_erradas:
        messages.warning(request, 'Nenhuma pergunta errada para revisar.')
        return redirect('quiz:quiz_ia_escolher_tema')
    
    # Gerar dicas de estudo usando IA
    dicas_estudo = []
    try:
        from .services.openai_service import OpenAIQuizService
        service = OpenAIQuizService()
        
        # Criar prompt para gerar dicas
        perguntas_texto = []
        for i, pergunta in enumerate(perguntas_erradas, 1):
            perguntas_texto.append(f"{i}. {pergunta['texto']}")
        
        prompt_dicas = f"""Com base nas seguintes perguntas sobre "{tema}" que o usuário errou, forneça dicas de estudo concisas e práticas.

Perguntas erradas:
{chr(10).join(perguntas_texto)}

Forneça:
1. Um resumo geral dos conceitos que precisam ser revisados
2. Dicas específicas para cada pergunta (máximo 2-3 linhas por pergunta)
3. Recursos sugeridos para estudo (se aplicável)

Formato JSON:
{{
    "resumo_geral": "Resumo dos conceitos a revisar",
    "dicas_por_pergunta": [
        {{
            "pergunta": "Texto da pergunta",
            "dica": "Dica específica para esta pergunta"
        }}
    ],
    "recursos": ["Recurso 1", "Recurso 2"]
}}"""
        
        response = service.client.chat.completions.create(
            model=service.model,
            messages=[
                {"role": "system", "content": "Você é um tutor educacional especializado em fornecer dicas de estudo práticas e concisas."},
                {"role": "user", "content": prompt_dicas}
            ],
            temperature=0.7,
            max_tokens=2000,
            response_format={"type": "json_object"}
        )
        
        import json
        dicas_data = json.loads(response.choices[0].message.content)
        dicas_estudo = dicas_data
        
    except Exception as e:
        logger.error(f"Erro ao gerar dicas: {e}")
        # Dicas padrão caso a IA falhe
        dicas_estudo = {
            "resumo_geral": f"Revise os conceitos básicos sobre {tema}. Pratique mais exercícios relacionados às perguntas que você errou.",
            "dicas_por_pergunta": [],
            "recursos": [f"Pesquise mais sobre {tema}", "Pratique exercícios similares"]
        }
    
    # Combinar perguntas erradas com dicas
    perguntas_com_dicas = []
    dicas_por_pergunta = dicas_estudo.get('dicas_por_pergunta', [])
    
    for i, pergunta in enumerate(perguntas_erradas):
        dica = ""
        if i < len(dicas_por_pergunta):
            dica = dicas_por_pergunta[i].get('dica', '')
        elif dicas_por_pergunta:
            # Tentar encontrar dica por texto da pergunta
            for dica_item in dicas_por_pergunta:
                if pergunta['texto'] in dica_item.get('pergunta', ''):
                    dica = dica_item.get('dica', '')
                    break
        
        perguntas_com_dicas.append({
            **pergunta,
            'dica': dica or f"Revise os conceitos relacionados a esta pergunta sobre {tema}."
        })
    
    # Limpar perguntas erradas da sessão após mostrar
    if request.GET.get('limpar') == '1':
        request.session.pop('quiz_ia_perguntas_erradas', None)
        request.session.pop('quiz_ia_tema', None)
        return redirect('quiz:quiz_ia_escolher_tema')
    
    context = {
        'tema': tema,
        'perguntas_erradas': perguntas_com_dicas,
        'resumo_geral': dicas_estudo.get('resumo_geral', ''),
        'recursos': dicas_estudo.get('recursos', []),
        'total_erradas': len(perguntas_erradas),
    }
    
    return render(request, 'quiz/quiz_ia_revisar_erradas.html', context)


@login_required
def quiz_ia_salvar_tema(request):
    """
    View para salvar as perguntas geradas pela IA no banco de dados como um novo tema.
    """
    if request.method != 'POST':
        return redirect('quiz:quiz_ia_escolher_tema')
    
    tema_nome = request.session.get('quiz_ia_tema')
    perguntas = request.session.get('quiz_ia_perguntas')
    
    if not tema_nome or not perguntas:
        messages.error(request, 'Nenhum quiz para salvar.')
        return redirect('quiz:quiz_ia_escolher_tema')
    
    try:
        with transaction.atomic():
            # Criar ou obter o tema
            tema, created = Tema.objects.get_or_create(
                nome=tema_nome,
                defaults={'descricao': f'Tema gerado por IA: {tema_nome}'}
            )
            
            # Garantir que as dificuldades existem
            dificuldades = {}
            for nivel, nome, ordem in [('facil', 'Fácil', 1), ('medio', 'Médio', 2), ('dificil', 'Difícil', 3)]:
                dif, _ = Dificuldade.objects.get_or_create(
                    nivel=nivel,
                    defaults={'nome': nome, 'ordem': ordem}
                )
                dificuldades[nivel] = dif
            
            # Salvar as perguntas
            perguntas_salvas = 0
            for nivel, lista_perguntas in perguntas.items():
                dificuldade = dificuldades.get(nivel)
                if not dificuldade:
                    continue
                    
                for p in lista_perguntas:
                    # Verificar se a pergunta já existe
                    existe = Pergunta.objects.filter(
                        tema=tema,
                        dificuldade=dificuldade,
                        texto=p['texto']
                    ).exists()
                    
                    if not existe:
                        Pergunta.objects.create(
                            tema=tema,
                            dificuldade=dificuldade,
                            texto=p['texto'],
                            alternativa_a=p['alternativa_a'],
                            alternativa_b=p['alternativa_b'],
                            alternativa_c=p['alternativa_c'],
                            alternativa_d=p['alternativa_d'],
                            resposta_correta=p['resposta_correta']
                        )
                        perguntas_salvas += 1
            
            if created:
                messages.success(request, f'Tema "{tema_nome}" criado com {perguntas_salvas} perguntas!')
            else:
                messages.success(request, f'{perguntas_salvas} novas perguntas adicionadas ao tema "{tema_nome}"!')
                
    except Exception as e:
        messages.error(request, f'Erro ao salvar tema: {str(e)}')
    
    return redirect('quiz:escolher_tema')


@login_required
def progresso_alunos(request):
    """
    View para professores visualizarem o progresso dos alunos.
    Mostra dados de quando entraram, tempo jogando, progresso de acerto ao longo do tempo.
    """
    from django.contrib.auth.models import User
    from django.db.models import Count, Avg, Sum, Q, F
    from django.utils import timezone
    from datetime import timedelta
    import json
    
    # Verificar se o usuário é professor
    try:
        perfil = request.user.perfil
        if perfil.tipo_usuario != 'professor' and not request.user.is_superuser:
            messages.error(request, 'Acesso negado. Apenas professores podem visualizar esta página.')
            return redirect('quiz:dashboard')
    except PerfilUsuario.DoesNotExist:
        if not request.user.is_superuser:
            messages.error(request, 'Acesso negado. Apenas professores podem visualizar esta página.')
            return redirect('quiz:dashboard')
    
    # Obter todos os alunos
    alunos = User.objects.filter(perfil__tipo_usuario='aluno').select_related('perfil')
    
    # Filtros
    aluno_id = request.GET.get('aluno_id')
    tema_id = request.GET.get('tema_id')
    
    if aluno_id:
        alunos = alunos.filter(id=aluno_id)
    
    # Dados gerais
    dados_alunos = []
    
    for aluno in alunos:
        perfil_aluno = aluno.perfil
        
        # Calcular tempo total de jogo
        sessoes = SessaoJogo.objects.filter(usuario=aluno)
        tempo_total_segundos = sessoes.aggregate(total=Sum('tempo_total_segundos'))['total'] or 0
        
        # Calcular estatísticas de respostas
        respostas = RespostaUsuario.objects.filter(usuario=aluno)
        total_respostas = respostas.count()
        total_corretas = respostas.filter(correta=True).count()
        percentual_acerto = (total_corretas / total_respostas * 100) if total_respostas > 0 else 0
        
        # Progresso por tema
        progressos = Progresso.objects.filter(usuario=aluno)
        if tema_id:
            progressos = progressos.filter(tema_id=tema_id)
        
        temas_progresso = []
        for progresso in progressos:
            temas_progresso.append({
                'tema': progresso.tema.nome,
                'rodada': progresso.rodada_atual,
                'perguntas_respondidas': progresso.perguntas_respondidas,
                'perguntas_corretas': progresso.perguntas_corretas,
                'percentual': (progresso.perguntas_corretas / progresso.perguntas_respondidas * 100) if progresso.perguntas_respondidas > 0 else 0,
            })
        
        # Estatísticas ao longo do tempo (últimos 30 dias)
        data_inicio = timezone.now() - timedelta(days=30)
        estatisticas = EstatisticaProgresso.objects.filter(
            usuario=aluno,
            data_registro__gte=data_inicio
        ).order_by('data_registro')
        
        # Dados para gráfico de progresso ao longo do tempo
        dados_grafico_tempo = {
            'datas': [],
            'percentuais_acerto': [],
            'tempo_jogo': [],
            'xp_total': [],
        }
        
        for estat in estatisticas:
            dados_grafico_tempo['datas'].append(estat.data_registro.strftime('%d/%m'))
            dados_grafico_tempo['percentuais_acerto'].append(float(estat.percentual_acerto))
            dados_grafico_tempo['tempo_jogo'].append(estat.tempo_total_jogo_segundos / 3600)  # em horas
            dados_grafico_tempo['xp_total'].append(estat.xp_total)
        
        # Calcular melhoria (comparar primeira e última estatística)
        melhoria = 0
        if len(estatisticas) >= 2:
            primeira = estatisticas.first()
            ultima = estatisticas.last()
            melhoria = ultima.percentual_acerto - primeira.percentual_acerto
        
        # Tempo formatado
        horas = tempo_total_segundos // 3600
        minutos = (tempo_total_segundos % 3600) // 60
        tempo_formatado = f"{horas}h {minutos}m" if horas > 0 else f"{minutos}m"
        
        # Converter para JSON para uso seguro no template
        dados_grafico_tempo_json = json.dumps(dados_grafico_tempo)
        
        dados_alunos.append({
            'aluno': aluno,
            'perfil': perfil_aluno,
            'data_cadastro': aluno.date_joined.strftime('%d/%m/%Y'),
            'tempo_total_segundos': tempo_total_segundos,
            'tempo_formatado': tempo_formatado,
            'total_respostas': total_respostas,
            'total_corretas': total_corretas,
            'percentual_acerto': round(percentual_acerto, 1),
            'temas_progresso': temas_progresso,
            'melhoria': round(melhoria, 1),
            'dados_grafico_tempo': dados_grafico_tempo,
            'dados_grafico_tempo_json': dados_grafico_tempo_json,
            'nivel': perfil_aluno.nivel,
            'xp_total': perfil_aluno.xp_total,
            'rodadas_completas': perfil_aluno.rodadas_completas,
        })
    
    # Obter todos os temas para filtro
    temas = Tema.objects.all()
    
    # Estatísticas gerais (todos os alunos)
    total_alunos = User.objects.filter(perfil__tipo_usuario='aluno').count()
    tempo_medio = SessaoJogo.objects.aggregate(
        media=Avg('tempo_total_segundos')
    )['media'] or 0
    tempo_medio_horas = tempo_medio / 3600
    
    percentual_medio = RespostaUsuario.objects.filter(
        usuario__perfil__tipo_usuario='aluno'
    ).aggregate(
        total=Count('id'),
        corretas=Count('id', filter=Q(correta=True))
    )
    if percentual_medio['total'] > 0:
        percentual_medio_geral = (percentual_medio['corretas'] / percentual_medio['total']) * 100
    else:
        percentual_medio_geral = 0
    
    context = {
        'dados_alunos': dados_alunos,
        'temas': temas,
        'tema_selecionado': int(tema_id) if tema_id else None,
        'aluno_selecionado': int(aluno_id) if aluno_id else None,
        'total_alunos': total_alunos,
        'tempo_medio_horas': round(tempo_medio_horas, 2),
        'percentual_medio_geral': round(percentual_medio_geral, 1),
    }
    
    return render(request, 'quiz/progresso_alunos.html', context)


def _processar_texto_perguntas(texto):
    """
    Processa um texto e extrai perguntas com alternativas e respostas.
    Suporta vários formatos:
    - 1. Pergunta? a) ... b) ... c) ... d) ... Resposta: A
    - Pergunta 1: ... A) ... B) ... C) ... D) ... Gabarito: A
    - Q1: ... (A) ... (B) ... (C) ... (D) ... Resposta correta: A
    """
    import re
    
    perguntas_extraidas = []
    linhas = texto.split('\n')
    
    pergunta_atual = None
    alternativas = {}
    resposta_correta = None
    
    i = 0
    while i < len(linhas):
        linha = linhas[i].strip()
        
        if not linha:
            i += 1
            continue
        
        # Detectar início de nova pergunta (números, Q, Pergunta, etc.)
        padrao_pergunta = re.match(r'^(\d+)[\.\):]|^[Pp]ergunta\s*\d+|^[Qq]\d+[\.\):]', linha)
        if padrao_pergunta:
            # Se já havia uma pergunta anterior, salvar ela
            if pergunta_atual and len(alternativas) == 4 and resposta_correta:
                perguntas_extraidas.append({
                    'texto': pergunta_atual,
                    'alternativa_a': alternativas.get('A', ''),
                    'alternativa_b': alternativas.get('B', ''),
                    'alternativa_c': alternativas.get('C', ''),
                    'alternativa_d': alternativas.get('D', ''),
                    'resposta_correta': resposta_correta
                })
            
            # Iniciar nova pergunta
            pergunta_atual = re.sub(r'^(\d+)[\.\):]|^[Pp]ergunta\s*\d+[\.\):]|^[Qq]\d+[\.\):]', '', linha).strip()
            alternativas = {}
            resposta_correta = None
            i += 1
            continue
        
        # Detectar alternativas (a), b), c), d) ou A), B), C), D) ou (A), (B), etc.)
        padrao_alternativa = re.match(r'^([a-dA-D])[\.\)]\s*(.+)$', linha)
        if padrao_alternativa:
            letra = padrao_alternativa.group(1).upper()
            texto_alt = padrao_alternativa.group(2).strip()
            # Se já existe essa alternativa, pode ser continuação
            if letra in alternativas:
                alternativas[letra] += ' ' + texto_alt
            else:
                alternativas[letra] = texto_alt
            i += 1
            continue
        
        # Se não é alternativa e ainda não tem pergunta, pode ser continuação da pergunta
        if pergunta_atual and len(alternativas) < 4:
            # Verificar se é continuação da pergunta ou linha vazia
            if not re.match(r'^[a-dA-D][\.\)]', linha):
                pergunta_atual += ' ' + linha
            i += 1
            continue
        
        # Detectar resposta correta
        padrao_resposta = re.search(r'[Rr]esposta\s*[Cc]orreta?[:\s]+([A-D])|[Gg]abarito[:\s]+([A-D])|[Rr]esposta[:\s]+([A-D])', linha, re.IGNORECASE)
        if padrao_resposta:
            resposta_correta = (padrao_resposta.group(1) or padrao_resposta.group(2) or padrao_resposta.group(3)).upper()
            i += 1
            continue
        
        # Se já tem pergunta mas não tem alternativas completas, pode ser continuação
        if pergunta_atual:
            # Tentar detectar alternativa sem marcador claro
            if len(alternativas) < 4:
                # Verificar se a linha parece ser uma alternativa
                if linha and not resposta_correta:
                    # Adicionar como continuação da última alternativa ou nova
                    if alternativas:
                        ultima_letra = sorted(alternativas.keys())[-1]
                        alternativas[ultima_letra] += ' ' + linha
                    else:
                        # Tentar adivinhar qual alternativa
                        letras_faltando = [l for l in ['A', 'B', 'C', 'D'] if l not in alternativas]
                        if letras_faltando:
                            alternativas[letras_faltando[0]] = linha
        
        i += 1
    
    # Adicionar última pergunta se completa
    if pergunta_atual and len(alternativas) == 4 and resposta_correta:
        perguntas_extraidas.append({
            'texto': pergunta_atual,
            'alternativa_a': alternativas.get('A', ''),
            'alternativa_b': alternativas.get('B', ''),
            'alternativa_c': alternativas.get('C', ''),
            'alternativa_d': alternativas.get('D', ''),
            'resposta_correta': resposta_correta
        })
    
    return perguntas_extraidas


def _gerar_pin_unico():
    """Gera um PIN único de 6 dígitos para a sala"""
    while True:
        pin = ''.join(random.choices(string.digits, k=6))
        if not Sala.objects.filter(pin=pin).exists():
            return pin


@login_required
def importar_perguntas(request):
    """
    View para professores importarem perguntas a partir de texto e criar uma sala personalizada.
    """
    # Verificar autenticação
    if not request.user.is_authenticated:
        messages.error(request, 'Você precisa estar logado para acessar esta página.')
        return redirect('quiz:login')
    
    # Verificar se o usuário é professor
    try:
        perfil = request.user.perfil
        if perfil.tipo_usuario != 'professor' and not request.user.is_superuser:
            messages.error(request, 'Acesso negado. Apenas professores podem acessar esta página.')
            return redirect('quiz:dashboard')
    except PerfilUsuario.DoesNotExist:
        if not request.user.is_superuser:
            messages.error(request, 'Acesso negado. Apenas professores podem acessar esta página.')
            return redirect('quiz:dashboard')
    
    if request.method == 'POST':
        try:
            form = ImportarPerguntasForm(request.POST)
            if form.is_valid():
                tema_personalizado = form.cleaned_data.get('tema_personalizado', '').strip()
                texto_perguntas = form.cleaned_data.get('texto_perguntas', '').strip()
                
                # Validações básicas
                if not tema_personalizado:
                    messages.error(request, 'Erro: O tema não pode estar vazio.')
                    return render(request, 'quiz/importar_perguntas.html', {'form': form})
                
                if not texto_perguntas:
                    messages.error(request, 'Erro: O texto com perguntas não pode estar vazio.')
                    return render(request, 'quiz/importar_perguntas.html', {'form': form})
                
                try:
                    # Processar o texto e extrair perguntas
                    logger.info(f"Processando texto para professor {request.user.username}. Tema: {tema_personalizado}")
                    perguntas_extraidas = _processar_texto_perguntas(texto_perguntas)
                    logger.info(f"Perguntas extraídas: {len(perguntas_extraidas)}")
                    
                    if not perguntas_extraidas:
                        messages.error(request, 'Erro: Nenhuma pergunta foi encontrada no texto. Verifique o formato. Certifique-se de que cada pergunta tem: número, texto da pergunta, 4 alternativas (a, b, c, d) e uma resposta (Resposta: A, B, C ou D).')
                        return render(request, 'quiz/importar_perguntas.html', {'form': form})
                    
                    # Usar transação para garantir atomicidade
                    sala = None
                    try:
                        with transaction.atomic():
                            # Gerar PIN único para a sala
                            pin = _gerar_pin_unico()
                            logger.info(f"PIN gerado: {pin}")
                            
                            # Criar sala
                            sala = Sala.objects.create(
                                professor=request.user,
                                tema_personalizado=tema_personalizado,
                                pin=pin
                            )
                            logger.info(f"Sala criada: ID={sala.id}, PIN={sala.pin}")
                            
                            # Salvar perguntas na sala
                            perguntas_salvas = 0
                            erros = []
                            
                            for ordem, pergunta_data in enumerate(perguntas_extraidas, start=1):
                                try:
                                    # Validar estrutura da pergunta
                                    if not isinstance(pergunta_data, dict):
                                        erros.append(f"Erro na pergunta {ordem}: Formato inválido.")
                                        continue
                                    
                                    # Validar resposta correta
                                    resposta = pergunta_data.get('resposta_correta', '').strip().upper()
                                    if resposta not in ['A', 'B', 'C', 'D']:
                                        erros.append(f"Erro na pergunta {ordem}: Resposta inválida '{resposta}'. Deve ser A, B, C ou D.")
                                        continue
                                    
                                    # Validar alternativas
                                    alt_a = pergunta_data.get('alternativa_a', '').strip()
                                    alt_b = pergunta_data.get('alternativa_b', '').strip()
                                    alt_c = pergunta_data.get('alternativa_c', '').strip()
                                    alt_d = pergunta_data.get('alternativa_d', '').strip()
                                    
                                    if not all([alt_a, alt_b, alt_c, alt_d]):
                                        erros.append(f"Erro na pergunta {ordem}: Alternativas incompletas. Todas as 4 alternativas (A, B, C, D) são obrigatórias.")
                                        continue
                                    
                                    # Validar texto da pergunta
                                    texto = pergunta_data.get('texto', '').strip()
                                    if not texto:
                                        erros.append(f"Erro na pergunta {ordem}: Texto da pergunta está vazio.")
                                        continue
                                    
                                    # Criar pergunta na sala
                                    PerguntaSala.objects.create(
                                        sala=sala,
                                        texto=texto,
                                        alternativa_a=alt_a[:500],
                                        alternativa_b=alt_b[:500],
                                        alternativa_c=alt_c[:500],
                                        alternativa_d=alt_d[:500],
                                        resposta_correta=resposta,
                                        ordem=ordem
                                    )
                                    perguntas_salvas += 1
                                    logger.debug(f"Pergunta {ordem} salva com sucesso")
                                    
                                except Exception as e:
                                    logger.error(f"Erro ao salvar pergunta {ordem}: {e}", exc_info=True)
                                    erros.append(f"Erro ao processar pergunta {ordem}: {str(e)}")
                            
                            # Se nenhuma pergunta foi salva, fazer rollback da transação
                            if perguntas_salvas == 0:
                                raise ValueError(f"Nenhuma pergunta válida foi encontrada. A sala não foi criada. Erros encontrados: {len(erros)}")
                            
                            logger.info(f"Total de perguntas salvas: {perguntas_salvas}")
                            
                    except Exception as e:
                        logger.error(f"Erro na transação: {e}", exc_info=True)
                        if sala:
                            try:
                                sala.delete()
                            except:
                                pass
                        raise
                    
                    # Mensagens de resultado
                    if perguntas_salvas > 0:
                        messages.success(request, f'✅ Sala criada com sucesso! {perguntas_salvas} pergunta(s) importada(s).')
                        if erros:
                            messages.warning(request, f'⚠️ Algumas perguntas tiveram problemas: {len(erros)} erro(s).')
                            for erro in erros[:3]:  # Mostrar até 3 erros
                                messages.warning(request, erro)
                        
                        logger.info(f"Sala {sala.id} criada com sucesso pelo professor {request.user.username}. PIN: {sala.pin}")
                        
                        # Redirecionar para página de visualização do PIN
                        try:
                            return redirect('quiz:visualizar_pin_sala', sala_id=sala.id)
                        except Exception as e:
                            logger.error(f"Erro ao redirecionar: {e}", exc_info=True)
                            messages.error(request, f'Erro ao redirecionar: {str(e)}. A sala foi criada com sucesso. ID: {sala.id}, PIN: {sala.pin}')
                            return render(request, 'quiz/importar_perguntas.html', {'form': ImportarPerguntasForm()})
                    
                except ValueError as e:
                    # Erro de validação - não criar sala
                    logger.error(f"Erro de validação: {e}")
                    messages.error(request, f'❌ Erro de validação: {str(e)}')
                    return render(request, 'quiz/importar_perguntas.html', {'form': form})
                except Exception as e:
                    # Erro geral - log completo
                    logger.error(f"Erro ao processar texto: {e}", exc_info=True)
                    import traceback
                    error_trace = traceback.format_exc()
                    logger.error(error_trace)
                    messages.error(request, f'❌ Erro ao processar o texto: {str(e)}. Por favor, verifique o formato e tente novamente.')
                    # Manter os dados do formulário para o usuário não perder o que digitou
                    return render(request, 'quiz/importar_perguntas.html', {'form': form})
            else:
                # Formulário inválido
                logger.warning(f"Formulário inválido. Erros: {form.errors}")
                for field, errors in form.errors.items():
                    for error in errors:
                        messages.error(request, f'❌ Erro no campo "{field}": {error}')
        except Exception as e:
            # Capturar QUALQUER erro que possa ocorrer
            logger.error(f"Erro inesperado em importar_perguntas: {e}", exc_info=True)
            import traceback
            error_trace = traceback.format_exc()
            logger.error(error_trace)
            messages.error(request, f'❌ Erro inesperado: {str(e)}. Por favor, tente novamente ou entre em contato com o suporte.')
            form = ImportarPerguntasForm(request.POST if request.method == 'POST' else None)
            return render(request, 'quiz/importar_perguntas.html', {'form': form})
    else:
        form = ImportarPerguntasForm()
    
    return render(request, 'quiz/importar_perguntas.html', {'form': form})


@login_required
def visualizar_pin_sala(request, sala_id):
    """
    View para professor visualizar o PIN da sala criada.
    """
    try:
        sala = get_object_or_404(Sala, id=sala_id)
        
        # Verificar se o usuário está autenticado
        if not request.user.is_authenticated:
            messages.error(request, 'Você precisa estar logado para visualizar esta sala.')
            return redirect('quiz:login')
        
        # Verificar se o usuário é o professor que criou a sala
        if sala.professor != request.user and not request.user.is_superuser:
            messages.error(request, 'Acesso negado. Você não tem permissão para visualizar esta sala.')
            return redirect('quiz:dashboard')
        
        context = {
            'sala': sala,
            'total_perguntas': sala.perguntas.count()
        }
        
        return render(request, 'quiz/visualizar_pin_sala.html', context)
    except Exception as e:
        logger.error(f"Erro ao visualizar PIN da sala: {e}", exc_info=True)
        messages.error(request, 'Erro ao carregar informações da sala.')
        return redirect('quiz:dashboard')


@login_required
def entrar_sala(request):
    """
    View para alunos entrarem em uma sala usando o PIN.
    """
    # Verificar se o usuário é aluno
    try:
        perfil = request.user.perfil
        if perfil.tipo_usuario != 'aluno':
            messages.error(request, 'Apenas alunos podem entrar em salas.')
            return redirect('quiz:dashboard')
    except PerfilUsuario.DoesNotExist:
        messages.error(request, 'Perfil de usuário não encontrado.')
        return redirect('quiz:dashboard')
    
    if request.method == 'POST':
        pin = request.POST.get('pin', '').strip()
        
        if not pin:
            messages.error(request, 'Por favor, digite o PIN da sala.')
            return render(request, 'quiz/entrar_sala.html')
        
        try:
            sala = Sala.objects.get(pin=pin, ativa=True)
            
            # Verificar se o aluno já está na sala
            aluno_sala, created = AlunoSala.objects.get_or_create(
                sala=sala,
                aluno=request.user
            )
            
            if created:
                messages.success(request, f'Você entrou na sala "{sala.tema_personalizado}"!')
            else:
                messages.info(request, f'Você já está na sala "{sala.tema_personalizado}".')
            
            # Redirecionar para jogar o quiz da sala
            return redirect('quiz:jogar_sala', sala_id=sala.id)
            
        except Sala.DoesNotExist:
            messages.error(request, 'PIN inválido ou sala não encontrada.')
        except Exception as e:
            logger.error(f"Erro ao entrar na sala: {e}")
            messages.error(request, 'Erro ao entrar na sala. Tente novamente.')
    
    return render(request, 'quiz/entrar_sala.html')


@login_required
def jogar_sala(request, sala_id):
    """
    View para alunos jogarem o quiz de uma sala personalizada.
    Funciona igual ao quiz tradicional, pergunta por pergunta.
    """
    sala = get_object_or_404(Sala, id=sala_id, ativa=True)
    
    # Verificar se o aluno tem acesso à sala
    try:
        perfil = request.user.perfil
        if perfil.tipo_usuario != 'aluno':
            messages.error(request, 'Apenas alunos podem jogar quizzes de salas.')
            return redirect('quiz:dashboard')
    except PerfilUsuario.DoesNotExist:
        messages.error(request, 'Perfil de usuário não encontrado.')
        return redirect('quiz:dashboard')
    
    # Verificar se o aluno está na sala
    if not AlunoSala.objects.filter(sala=sala, aluno=request.user).exists():
        messages.error(request, 'Você precisa entrar na sala primeiro usando o PIN.')
        return redirect('quiz:entrar_sala')
    
    # Obter todas as perguntas da sala ordenadas
    todas_perguntas = sala.perguntas.all().order_by('ordem')
    
    if not todas_perguntas.exists():
        messages.error(request, 'Esta sala não possui perguntas.')
        return redirect('quiz:dashboard')
    
    total_perguntas = todas_perguntas.count()
    
    # Obter ou criar progresso do aluno na sala
    progresso_sala, _ = ProgressoSala.objects.get_or_create(
        aluno=request.user,
        sala=sala,
        defaults={
            'perguntas_respondidas': 0,
            'perguntas_corretas': 0,
            'pontuacao_total': 0,
            'quiz_completo': False
        }
    )
    
    # Verificar se o quiz já foi completado
    if progresso_sala.quiz_completo:
        context = {
            'sala': sala,
            'progresso': progresso_sala,
            'quiz_completo': True,
            'total_perguntas': total_perguntas,
            'perfil': perfil
        }
        return render(request, 'quiz/rodada_sala.html', context)
    
    feedback = None
    feedback_tipo = None
    resposta_correta = None
    
    session_key = f'sala_pergunta_inicio_{progresso_sala.pk}'
    
    # Processar resposta do usuário
    if request.method == 'POST' and not progresso_sala.quiz_completo:
        pergunta_id = request.POST.get('pergunta_id')
        resposta_escolhida = request.POST.get('resposta')
        
        if pergunta_id and resposta_escolhida:
            pergunta_sala = get_object_or_404(PerguntaSala, pk=pergunta_id, sala=sala)
            
            # Evitar respostas duplicadas
            resposta_existente = progresso_sala.respostas.filter(pergunta_sala=pergunta_sala).first()
            
            if not resposta_existente:
                correta = pergunta_sala.resposta_correta == resposta_escolhida.upper()
                agora = timezone.now()
                tempo_decorrido = None
                
                # Calcular tempo decorrido
                if session_key:
                    tempo_inicio_iso = request.session.pop(session_key, None)
                    if tempo_inicio_iso:
                        try:
                            tempo_inicio = datetime.fromisoformat(tempo_inicio_iso)
                            if timezone.is_naive(tempo_inicio):
                                tempo_inicio = timezone.make_aware(tempo_inicio, timezone.get_current_timezone())
                            tempo_decorrido = (agora - tempo_inicio).total_seconds()
                            tempo_decorrido = max(0, tempo_decorrido)
                        except ValueError:
                            tempo_decorrido = None
                
                # Pontuação base (10 pontos por pergunta)
                pontos_base = 10
                pontos_obtidos = _calcular_pontos_pergunta(correta, tempo_decorrido, pontos_base)
                
                with transaction.atomic():
                    # Criar resposta
                    RespostaSala.objects.create(
                        aluno=request.user,
                        pergunta_sala=pergunta_sala,
                        resposta_escolhida=resposta_escolhida.upper(),
                        correta=correta,
                        pontuacao=pontos_obtidos,
                        progresso_sala=progresso_sala
                    )
                    
                    # Atualizar progresso
                    progresso_sala.perguntas_respondidas = progresso_sala.respostas.count()
                    progresso_sala.perguntas_corretas = progresso_sala.respostas.filter(correta=True).count()
                    progresso_sala.pontuacao_total = progresso_sala.respostas.aggregate(
                        total=Coalesce(Sum('pontuacao'), 0)
                    )['total']
                    
                    # Verificar se o quiz foi completado
                    if progresso_sala.perguntas_respondidas >= total_perguntas:
                        progresso_sala.quiz_completo = True
                    
                    progresso_sala.save()
                    
                    # Atualizar perfil do aluno
                    pontos_totais = RespostaUsuario.objects.filter(usuario=request.user).aggregate(
                        total=Coalesce(Sum('pontuacao'), 0)
                    )['total']
                    if perfil.pontos_totais != pontos_totais:
                        perfil.pontos_totais = pontos_totais
                        perfil.save(update_fields=['pontos_totais'])
                
                # Feedback baseado na resposta
                if correta:
                    if tempo_decorrido is not None:
                        if tempo_decorrido <= 15:
                            feedback = f"🚀 Resposta rápida! +{pontos_obtidos} pontos!"
                        elif tempo_decorrido <= 30:
                            feedback = f"✅ Resposta correta! +{pontos_obtidos} pontos."
                        elif tempo_decorrido <= 45:
                            feedback = f"👍 Correto! Tente ser mais rápido. +{pontos_obtidos} pontos."
                        else:
                            feedback = f"⏱️ Correto, mas muito lento. +{pontos_obtidos} pontos."
                    else:
                        feedback = f"✅ Resposta correta! +{pontos_obtidos} pontos."
                    feedback_tipo = "success"
                else:
                    feedback = "❌ Resposta incorreta."
                    feedback_tipo = "error"
                    resposta_correta = pergunta_sala.resposta_correta
            else:
                feedback = "Você já respondeu a esta pergunta."
                feedback_tipo = "warning"
                resposta_correta = resposta_existente.pergunta_sala.resposta_correta
    
    # Atualizar referência após possível alteração
    progresso_sala.refresh_from_db()
    
    # Obter próxima pergunta não respondida
    perguntas_respondidas_ids = progresso_sala.respostas.values_list('pergunta_sala_id', flat=True)
    pergunta_atual = todas_perguntas.exclude(id__in=perguntas_respondidas_ids).first()
    
    # Se não há mais perguntas, marcar como completo
    if not pergunta_atual and not progresso_sala.quiz_completo:
        progresso_sala.quiz_completo = True
        progresso_sala.save(update_fields=['quiz_completo'])
    
    # Registrar tempo de início da pergunta atual
    if pergunta_atual and session_key:
        request.session[session_key] = timezone.now().isoformat()
    
    # Calcular progresso
    respondidas_total = progresso_sala.perguntas_respondidas
    progresso_percentual = min(100, int((respondidas_total / total_perguntas) * 100)) if total_perguntas > 0 else 0
    numero_pergunta_atual = min(total_perguntas, respondidas_total + 1)
    
    # Verificar se há perguntas erradas
    tem_perguntas_erradas = False
    if progresso_sala.quiz_completo:
        total_erradas = progresso_sala.respostas.filter(correta=False).count()
        tem_perguntas_erradas = total_erradas > 0
    
    context = {
        'sala': sala,
        'progresso': progresso_sala,
        'pergunta': pergunta_atual,
        'feedback': feedback if not progresso_sala.quiz_completo else None,
        'feedback_tipo': feedback_tipo,
        'resposta_correta': resposta_correta,
        'total_perguntas': total_perguntas,
        'respondidas_total': respondidas_total,
        'progresso_percentual': progresso_percentual,
        'numero_pergunta_atual': numero_pergunta_atual,
        'quiz_completo': progresso_sala.quiz_completo,
        'pontuacao_total': progresso_sala.pontuacao_total,
        'tem_perguntas_erradas': tem_perguntas_erradas,
        'perfil': perfil
    }
    
    return render(request, 'quiz/rodada_sala.html', context)