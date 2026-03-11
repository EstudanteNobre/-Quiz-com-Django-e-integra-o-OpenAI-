from django.contrib import admin
from .models import Tema, Dificuldade, Pergunta, PerfilUsuario, Progresso, RespostaUsuario, Conquista, ConquistaUsuario, Sala, PerguntaSala, AlunoSala, ProgressoSala, RespostaSala


@admin.register(Tema)
class TemaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'descricao', 'criado_em']
    search_fields = ['nome', 'descricao']
    list_filter = ['criado_em']


@admin.register(Dificuldade)
class DificuldadeAdmin(admin.ModelAdmin):
    list_display = ['nome', 'nivel', 'ordem']
    list_editable = ['ordem']
    ordering = ['ordem']


@admin.register(Pergunta)
class PerguntaAdmin(admin.ModelAdmin):
    list_display = ['texto_curto', 'tema', 'dificuldade', 'resposta_correta', 'criado_em']
    list_filter = ['tema', 'dificuldade', 'criado_em']
    search_fields = ['texto', 'alternativa_a', 'alternativa_b', 'alternativa_c', 'alternativa_d']
    readonly_fields = ['criado_em', 'atualizado_em']
    
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('tema', 'dificuldade', 'texto')
        }),
        ('Alternativas', {
            'fields': ('alternativa_a', 'alternativa_b', 'alternativa_c', 'alternativa_d', 'resposta_correta')
        }),
        ('Metadados', {
            'fields': ('criado_em', 'atualizado_em'),
            'classes': ('collapse',)
        }),
    )
    
    def texto_curto(self, obj):
        return obj.texto[:50] + "..." if len(obj.texto) > 50 else obj.texto
    texto_curto.short_description = 'Pergunta'


@admin.register(PerfilUsuario)
class PerfilUsuarioAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'pontos_totais', 'rodadas_completas', 'xp_total', 'nivel', 'titulo', 'criado_em']
    search_fields = ['usuario__username', 'usuario__email']
    list_filter = ['criado_em', 'nivel']
    readonly_fields = ['criado_em', 'atualizado_em']


@admin.register(Conquista)
class ConquistaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'icone', 'condicao_tipo', 'condicao_valor', 'xp_recompensa']
    search_fields = ['nome', 'codigo', 'descricao']
    list_filter = ['condicao_tipo']


@admin.register(ConquistaUsuario)
class ConquistaUsuarioAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'conquista', 'desbloqueada_em']
    search_fields = ['usuario__username', 'conquista__nome']
    list_filter = ['desbloqueada_em', 'conquista']
    readonly_fields = ['desbloqueada_em']


@admin.register(Progresso)
class ProgressoAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'tema', 'rodada_atual', 'nivel_atual', 'perguntas_respondidas', 
                    'perguntas_corretas', 'rodada_completa', 'atualizado_em']
    list_filter = ['tema', 'rodada_atual', 'nivel_atual', 'rodada_completa', 'atualizado_em']
    search_fields = ['usuario__username', 'tema__nome']
    readonly_fields = ['criado_em', 'atualizado_em']
    ordering = ['usuario', 'tema', 'rodada_atual']


@admin.register(RespostaUsuario)
class RespostaUsuarioAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'pergunta_curta', 'resposta_escolhida', 'correta', 'respondida_em']
    list_filter = ['correta', 'respondida_em', 'pergunta__tema', 'pergunta__dificuldade']
    search_fields = ['usuario__username', 'pergunta__texto']
    readonly_fields = ['respondida_em']
    
    def pergunta_curta(self, obj):
        return obj.pergunta.texto[:50] + "..." if len(obj.pergunta.texto) > 50 else obj.pergunta.texto
    pergunta_curta.short_description = 'Pergunta'


@admin.register(Sala)
class SalaAdmin(admin.ModelAdmin):
    list_display = ['pin', 'tema_personalizado', 'professor', 'ativa', 'total_perguntas', 'criada_em']
    list_filter = ['ativa', 'criada_em']
    search_fields = ['pin', 'tema_personalizado', 'professor__username']
    readonly_fields = ['pin', 'criada_em', 'atualizada_em']
    
    def total_perguntas(self, obj):
        return obj.perguntas.count()
    total_perguntas.short_description = 'Total de Perguntas'


@admin.register(PerguntaSala)
class PerguntaSalaAdmin(admin.ModelAdmin):
    list_display = ['texto_curto', 'sala', 'ordem', 'resposta_correta', 'criada_em']
    list_filter = ['sala', 'criada_em']
    search_fields = ['texto', 'sala__tema_personalizado']
    readonly_fields = ['criada_em']
    ordering = ['sala', 'ordem']
    
    def texto_curto(self, obj):
        return obj.texto[:50] + "..." if len(obj.texto) > 50 else obj.texto
    texto_curto.short_description = 'Pergunta'


@admin.register(AlunoSala)
class AlunoSalaAdmin(admin.ModelAdmin):
    list_display = ['aluno', 'sala', 'entrou_em']
    list_filter = ['entrou_em', 'sala']
    search_fields = ['aluno__username', 'sala__pin', 'sala__tema_personalizado']
    readonly_fields = ['entrou_em']


@admin.register(ProgressoSala)
class ProgressoSalaAdmin(admin.ModelAdmin):
    list_display = ['aluno', 'sala', 'perguntas_respondidas', 'perguntas_corretas', 'pontuacao_total', 'quiz_completo', 'atualizado_em']
    list_filter = ['quiz_completo', 'atualizado_em', 'sala']
    search_fields = ['aluno__username', 'sala__pin', 'sala__tema_personalizado']
    readonly_fields = ['criado_em', 'atualizado_em']


@admin.register(RespostaSala)
class RespostaSalaAdmin(admin.ModelAdmin):
    list_display = ['aluno', 'pergunta_sala', 'resposta_escolhida', 'correta', 'pontuacao', 'respondida_em']
    list_filter = ['correta', 'respondida_em', 'pergunta_sala__sala']
    search_fields = ['aluno__username', 'pergunta_sala__texto', 'pergunta_sala__sala__pin']
    readonly_fields = ['respondida_em']
