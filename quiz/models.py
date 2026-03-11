from django.db import models
from django.contrib.auth.models import User


class Tema(models.Model):
    """Modelo para representar os temas do quiz"""
    nome = models.CharField(max_length=100, unique=True)
    descricao = models.TextField(blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Tema"
        verbose_name_plural = "Temas"
        ordering = ['nome']
    
    def __str__(self):
        return self.nome


class Dificuldade(models.Model):
    """Modelo para representar os níveis de dificuldade"""
    NIVEL_CHOICES = [
        ('facil', 'Fácil'),
        ('medio', 'Médio'),
        ('dificil', 'Difícil'),
    ]
    
    nivel = models.CharField(max_length=10, choices=NIVEL_CHOICES, unique=True)
    nome = models.CharField(max_length=50)
    ordem = models.IntegerField(default=0)  # Para ordenar: 1=Fácil, 2=Médio, 3=Difícil
    
    class Meta:
        verbose_name = "Dificuldade"
        verbose_name_plural = "Dificuldades"
        ordering = ['ordem']
    
    def __str__(self):
        return self.nome


class Pergunta(models.Model):
    """Modelo para representar as perguntas do quiz"""
    RESPOSTA_CHOICES = [
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
    ]
    
    tema = models.ForeignKey(Tema, on_delete=models.CASCADE, related_name='perguntas')
    dificuldade = models.ForeignKey(Dificuldade, on_delete=models.CASCADE, related_name='perguntas')
    texto = models.TextField()
    alternativa_a = models.CharField(max_length=500)
    alternativa_b = models.CharField(max_length=500)
    alternativa_c = models.CharField(max_length=500)
    alternativa_d = models.CharField(max_length=500)
    resposta_correta = models.CharField(max_length=1, choices=RESPOSTA_CHOICES)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Pergunta"
        verbose_name_plural = "Perguntas"
        ordering = ['tema', 'dificuldade__ordem']
        unique_together = [['tema', 'dificuldade', 'texto']]  # Evita perguntas duplicadas
    
    def __str__(self):
        return f"{self.tema.nome} - {self.dificuldade.nome}: {self.texto[:50]}..."


class PerfilUsuario(models.Model):
    """Modelo para estender o perfil do usuário"""
    TIPO_USUARIO_CHOICES = [
        ('aluno', 'Aluno'),
        ('professor', 'Professor'),
    ]
    
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    tipo_usuario = models.CharField(
        max_length=10,
        choices=TIPO_USUARIO_CHOICES,
        default='aluno',
        verbose_name='Tipo de Usuário'
    )
    pontos_totais = models.IntegerField(default=0)
    rodadas_completas = models.IntegerField(default=0)
    xp_total = models.IntegerField(default=0)  # Pontos de experiência (XP)
    nivel = models.IntegerField(default=1)  # Nível do jogador
    titulo = models.CharField(max_length=100, default="Iniciante", blank=True)  # Título do jogador
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Perfil de Usuário"
        verbose_name_plural = "Perfis de Usuários"
    
    def calcular_nivel(self):
        """Calcula o nível baseado no XP total"""
        # Fórmula: nível = sqrt(XP / 100) + 1
        import math
        if self.xp_total <= 0:
            return 1
        nivel_calculado = int(math.sqrt(self.xp_total / 100)) + 1
        return max(1, nivel_calculado)
    
    def xp_para_proximo_nivel(self):
        """Retorna o XP total necessário para alcançar o próximo nível"""
        # XP total necessário = (nível atual)² * 100
        return (self.nivel ** 2) * 100
    
    def xp_no_nivel_atual(self):
        """Retorna o XP no nível atual (desde o início do nível)"""
        if self.nivel <= 1:
            return self.xp_total
        xp_nivel_anterior = ((self.nivel - 1) ** 2) * 100
        return self.xp_total - xp_nivel_anterior
    
    def xp_necessario_proximo_nivel(self):
        """Retorna o XP necessário para passar do nível atual para o próximo"""
        xp_total_proximo = (self.nivel ** 2) * 100
        xp_total_atual = ((self.nivel - 1) ** 2) * 100 if self.nivel > 1 else 0
        return xp_total_proximo - xp_total_atual
    
    def progresso_nivel_percentual(self):
        """Retorna o progresso percentual para o próximo nível"""
        xp_necessario = self.xp_necessario_proximo_nivel()
        xp_atual = self.xp_no_nivel_atual()
        if xp_necessario == 0:
            return 100
        return min(100, int((xp_atual / xp_necessario) * 100))
    
    def obter_titulo(self):
        """Retorna o título baseado no nível"""
        titulos = {
            1: "Iniciante",
            2: "Aprendiz",
            3: "Estudante",
            4: "Conhecido",
            5: "Especialista",
            6: "Mestre",
            7: "Lenda",
            8: "Ídolo",
            9: "Gênio",
            10: "Lendário"
        }
        if self.nivel >= 10:
            return "Lendário"
        return titulos.get(self.nivel, "Iniciante")
    
    def __str__(self):
        return f"Perfil de {self.usuario.username}"


class Progresso(models.Model):
    """Modelo para rastrear o progresso do usuário por tema e rodada"""
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='progressos')
    tema = models.ForeignKey(Tema, on_delete=models.CASCADE, related_name='progressos')
    rodada_atual = models.IntegerField(default=1)  # Rodada atual (1, 2 ou 3)
    perguntas_respondidas = models.IntegerField(default=0)  # Quantas perguntas foram respondidas nesta rodada
    perguntas_corretas = models.IntegerField(default=0)  # Quantas perguntas foram acertadas nesta rodada
    pontuacao_total = models.IntegerField(default=0)  # Pontuação acumulada na rodada
    nivel_atual = models.CharField(
        max_length=10,
        choices=[('facil', 'Fácil'), ('medio', 'Médio'), ('dificil', 'Difícil')],
        default='facil'
    )  # Nível atual na rodada (fácil -> médio -> difícil)
    rodada_completa = models.BooleanField(default=False)  # Se a rodada foi completada
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Progresso"
        verbose_name_plural = "Progressos"
        unique_together = [['usuario', 'tema', 'rodada_atual']]  # Um progresso por usuário/tema/rodada
        ordering = ['usuario', 'tema', 'rodada_atual']
    
    def __str__(self):
        return f"{self.usuario.username} - {self.tema.nome} - Rodada {self.rodada_atual}"


class RespostaUsuario(models.Model):
    """Modelo para armazenar as respostas dadas pelos usuários"""
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='respostas')
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE, related_name='respostas_usuarios')
    resposta_escolhida = models.CharField(max_length=1, choices=Pergunta.RESPOSTA_CHOICES)
    correta = models.BooleanField(default=False)
    pontuacao = models.IntegerField(default=0)
    progresso = models.ForeignKey(Progresso, on_delete=models.CASCADE, related_name='respostas', null=True, blank=True)
    respondida_em = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Resposta do Usuário"
        verbose_name_plural = "Respostas dos Usuários"
        ordering = ['-respondida_em']
    
    def __str__(self):
        status = "[OK]" if self.correta else "[ERR]"
        return f"{status} {self.usuario.username} - {self.pergunta.tema.nome}"


class Conquista(models.Model):
    """Modelo para representar conquistas/achievements"""
    codigo = models.CharField(max_length=50, unique=True)  # Código único da conquista
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    icone = models.CharField(max_length=50, default="🏆")  # Emoji ou nome do ícone
    xp_recompensa = models.IntegerField(default=0)  # XP ganho ao desbloquear
    condicao_tipo = models.CharField(
        max_length=50,
        choices=[
            ('pontos_totais', 'Pontos Totais'),
            ('rodadas_completas', 'Rodadas Completas'),
            ('tema_completo', 'Tema Completo'),
            ('nivel_atingido', 'Nível Atingido'),
        ],
        default='pontos_totais'
    )
    condicao_valor = models.IntegerField(default=0)  # Valor necessário para desbloquear
    
    class Meta:
        verbose_name = "Conquista"
        verbose_name_plural = "Conquistas"
        ordering = ['condicao_valor']
    
    def __str__(self):
        return self.nome


class ConquistaUsuario(models.Model):
    """Modelo para relacionar usuários com conquistas desbloqueadas"""
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='conquistas')
    conquista = models.ForeignKey(Conquista, on_delete=models.CASCADE, related_name='usuarios')
    desbloqueada_em = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Conquista do Usuário"
        verbose_name_plural = "Conquistas dos Usuários"
        unique_together = [['usuario', 'conquista']]
        ordering = ['-desbloqueada_em']
    
    def __str__(self):
        return f"{self.usuario.username} - {self.conquista.nome}"


class QuizIAHistorico(models.Model):
    """Modelo para armazenar o histórico de quizzes gerados por IA"""
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='quizzes_ia')
    tema = models.CharField(max_length=200)  # Tema pode ser personalizado, não precisa ser FK
    pontuacao = models.IntegerField(default=0)
    total_perguntas = models.IntegerField(default=15)
    respostas_corretas = models.IntegerField(default=0)
    percentual_acertos = models.IntegerField(default=0)
    concluido_em = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Quiz IA - Histórico"
        verbose_name_plural = "Quiz IA - Históricos"
        ordering = ['-concluido_em']
    
    def __str__(self):
        return f"{self.usuario.username} - {self.tema} - {self.pontuacao} pts"


class SessaoJogo(models.Model):
    """Modelo para rastrear sessões de jogo e tempo gasto"""
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sessoes_jogo')
    inicio_sessao = models.DateTimeField(auto_now_add=True)
    fim_sessao = models.DateTimeField(null=True, blank=True)
    tempo_total_segundos = models.IntegerField(default=0)  # Tempo total em segundos
    perguntas_respondidas = models.IntegerField(default=0)
    tema = models.ForeignKey(Tema, on_delete=models.SET_NULL, null=True, blank=True, related_name='sessoes')
    
    class Meta:
        verbose_name = "Sessão de Jogo"
        verbose_name_plural = "Sessões de Jogo"
        ordering = ['-inicio_sessao']
    
    def tempo_formatado(self):
        """Retorna o tempo formatado em horas:minutos:segundos"""
        horas = self.tempo_total_segundos // 3600
        minutos = (self.tempo_total_segundos % 3600) // 60
        segundos = self.tempo_total_segundos % 60
        if horas > 0:
            return f"{horas}h {minutos}m {segundos}s"
        elif minutos > 0:
            return f"{minutos}m {segundos}s"
        return f"{segundos}s"
    
    def __str__(self):
        return f"{self.usuario.username} - {self.inicio_sessao.strftime('%d/%m/%Y %H:%M')} - {self.tempo_formatado()}"


class EstatisticaProgresso(models.Model):
    """Modelo para armazenar estatísticas de progresso ao longo do tempo"""
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='estatisticas_progresso')
    data_registro = models.DateTimeField(auto_now_add=True)
    total_perguntas_respondidas = models.IntegerField(default=0)
    total_perguntas_corretas = models.IntegerField(default=0)
    percentual_acerto = models.FloatField(default=0.0)
    tempo_total_jogo_segundos = models.IntegerField(default=0)
    xp_total = models.IntegerField(default=0)
    nivel_atual = models.IntegerField(default=1)
    rodadas_completas = models.IntegerField(default=0)
    
    class Meta:
        verbose_name = "Estatística de Progresso"
        verbose_name_plural = "Estatísticas de Progresso"
        ordering = ['-data_registro']
        indexes = [
            models.Index(fields=['usuario', '-data_registro']),
        ]
    
    def percentual_acerto_formatado(self):
        """Retorna o percentual formatado"""
        return f"{self.percentual_acerto:.1f}%"
    
    def tempo_formatado(self):
        """Retorna o tempo formatado"""
        horas = self.tempo_total_jogo_segundos // 3600
        minutos = (self.tempo_total_jogo_segundos % 3600) // 60
        if horas > 0:
            return f"{horas}h {minutos}m"
        return f"{minutos}m"
    
    def __str__(self):
        return f"{self.usuario.username} - {self.data_registro.strftime('%d/%m/%Y')} - {self.percentual_acerto_formatado()}"


class Sala(models.Model):
    """Modelo para representar salas de quiz personalizadas criadas por professores"""
    professor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='salas_criadas')
    tema_personalizado = models.CharField(max_length=200, verbose_name='Tema Personalizado')
    pin = models.CharField(max_length=6, unique=True, verbose_name='PIN da Sala')
    ativa = models.BooleanField(default=True, verbose_name='Sala Ativa')
    criada_em = models.DateTimeField(auto_now_add=True)
    atualizada_em = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Sala"
        verbose_name_plural = "Salas"
        ordering = ['-criada_em']
    
    def __str__(self):
        return f"Sala {self.pin} - {self.tema_personalizado} (Prof: {self.professor.username})"


class PerguntaSala(models.Model):
    """Modelo para perguntas específicas de uma sala personalizada"""
    RESPOSTA_CHOICES = [
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
    ]
    
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE, related_name='perguntas')
    texto = models.TextField()
    alternativa_a = models.CharField(max_length=500)
    alternativa_b = models.CharField(max_length=500)
    alternativa_c = models.CharField(max_length=500)
    alternativa_d = models.CharField(max_length=500)
    resposta_correta = models.CharField(max_length=1, choices=RESPOSTA_CHOICES)
    ordem = models.IntegerField(default=0, help_text='Ordem da pergunta no quiz')
    criada_em = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Pergunta da Sala"
        verbose_name_plural = "Perguntas da Sala"
        ordering = ['sala', 'ordem']
    
    def __str__(self):
        return f"{self.sala.tema_personalizado} - Pergunta {self.ordem}: {self.texto[:50]}..."


class AlunoSala(models.Model):
    """Modelo para relacionar alunos com salas que podem acessar"""
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE, related_name='alunos')
    aluno = models.ForeignKey(User, on_delete=models.CASCADE, related_name='salas_acesso')
    entrou_em = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Aluno na Sala"
        verbose_name_plural = "Alunos nas Salas"
        unique_together = [['sala', 'aluno']]
        ordering = ['-entrou_em']
    
    def __str__(self):
        return f"{self.aluno.username} - Sala {self.sala.pin}"


class ProgressoSala(models.Model):
    """Modelo para rastrear o progresso do aluno em uma sala"""
    aluno = models.ForeignKey(User, on_delete=models.CASCADE, related_name='progressos_sala')
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE, related_name='progressos')
    perguntas_respondidas = models.IntegerField(default=0)
    perguntas_corretas = models.IntegerField(default=0)
    pontuacao_total = models.IntegerField(default=0)
    quiz_completo = models.BooleanField(default=False)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Progresso na Sala"
        verbose_name_plural = "Progressos nas Salas"
        unique_together = [['aluno', 'sala']]
        ordering = ['-atualizado_em']
    
    def __str__(self):
        return f"{self.aluno.username} - Sala {self.sala.pin} - {self.perguntas_respondidas} perguntas"


class RespostaSala(models.Model):
    """Modelo para armazenar as respostas dos alunos nas salas"""
    RESPOSTA_CHOICES = [
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
    ]
    
    aluno = models.ForeignKey(User, on_delete=models.CASCADE, related_name='respostas_sala')
    pergunta_sala = models.ForeignKey(PerguntaSala, on_delete=models.CASCADE, related_name='respostas')
    resposta_escolhida = models.CharField(max_length=1, choices=RESPOSTA_CHOICES)
    correta = models.BooleanField(default=False)
    pontuacao = models.IntegerField(default=0)
    progresso_sala = models.ForeignKey(ProgressoSala, on_delete=models.CASCADE, related_name='respostas', null=True, blank=True)
    respondida_em = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Resposta na Sala"
        verbose_name_plural = "Respostas nas Salas"
        unique_together = [['aluno', 'pergunta_sala']]
        ordering = ['-respondida_em']
    
    def __str__(self):
        status = "[OK]" if self.correta else "[ERR]"
        return f"{status} {self.aluno.username} - Pergunta {self.pergunta_sala.ordem}"