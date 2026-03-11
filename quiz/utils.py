"""
Utilitários para rastreamento de progresso e sessões de jogo.
"""
from django.utils import timezone
from django.db import transaction, models
from .models import SessaoJogo, EstatisticaProgresso, RespostaUsuario, PerfilUsuario
from datetime import timedelta


def iniciar_sessao_jogo(usuario, tema=None):
    """
    Inicia uma nova sessão de jogo para o usuário.
    Retorna a sessão criada.
    """
    sessao = SessaoJogo.objects.create(
        usuario=usuario,
        tema=tema
    )
    return sessao


def finalizar_sessao_jogo(sessao_id, tempo_total_segundos, perguntas_respondidas):
    """
    Finaliza uma sessão de jogo com o tempo total e número de perguntas.
    """
    try:
        sessao = SessaoJogo.objects.get(id=sessao_id)
        sessao.fim_sessao = timezone.now()
        sessao.tempo_total_segundos = tempo_total_segundos
        sessao.perguntas_respondidas = perguntas_respondidas
        sessao.save()
        return sessao
    except SessaoJogo.DoesNotExist:
        return None


def obter_ou_criar_sessao_ativa(usuario, tema=None):
    """
    Obtém a sessão ativa do usuário ou cria uma nova se não existir.
    Uma sessão é considerada ativa se foi iniciada nas últimas 2 horas.
    """
    duas_horas_atras = timezone.now() - timedelta(hours=2)
    
    sessao_ativa = SessaoJogo.objects.filter(
        usuario=usuario,
        fim_sessao__isnull=True,
        inicio_sessao__gte=duas_horas_atras
    ).first()
    
    if not sessao_ativa:
        sessao_ativa = iniciar_sessao_jogo(usuario, tema)
    
    return sessao_ativa


def criar_estatistica_progresso(usuario):
    """
    Cria uma estatística de progresso para o usuário com base nos dados atuais.
    """
    try:
        perfil = usuario.perfil
    except PerfilUsuario.DoesNotExist:
        perfil = PerfilUsuario.objects.create(usuario=usuario)
    
    # Calcular estatísticas de respostas
    respostas = RespostaUsuario.objects.filter(usuario=usuario)
    total_respostas = respostas.count()
    total_corretas = respostas.filter(correta=True).count()
    percentual_acerto = (total_corretas / total_respostas * 100) if total_respostas > 0 else 0.0
    
    # Calcular tempo total de jogo
    sessoes = SessaoJogo.objects.filter(usuario=usuario)
    tempo_total = sessoes.aggregate(
        total=models.Sum('tempo_total_segundos')
    )['total'] or 0
    
    # Criar estatística
    estatistica = EstatisticaProgresso.objects.create(
        usuario=usuario,
        total_perguntas_respondidas=total_respostas,
        total_perguntas_corretas=total_corretas,
        percentual_acerto=percentual_acerto,
        tempo_total_jogo_segundos=tempo_total,
        xp_total=perfil.xp_total,
        nivel_atual=perfil.nivel,
        rodadas_completas=perfil.rodadas_completas
    )
    
    return estatistica


def atualizar_tempo_sessao(sessao, tempo_adicional_segundos):
    """
    Atualiza o tempo total de uma sessão adicionando tempo adicional.
    """
    sessao.tempo_total_segundos += int(tempo_adicional_segundos)
    sessao.perguntas_respondidas += 1
    sessao.save(update_fields=['tempo_total_segundos', 'perguntas_respondidas'])

