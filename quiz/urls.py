from django.urls import path
from . import views

app_name = 'quiz'

urlpatterns = [
    path('', views.home, name='home'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('painel-admin/', views.admin_dashboard, name='admin_dashboard'),
    path('escolher-tema/', views.escolher_tema, name='escolher_tema'),
    path('tema/<int:tema_id>/rodada/', views.jogar_tema, name='jogar_tema'),
    path('tema/<int:tema_id>/revisar-erradas/', views.revisar_perguntas_erradas, name='revisar_perguntas_erradas'),
    
    # URLs para Quiz com IA (OpenAI)
    path('quiz-ia/', views.quiz_ia_escolher_tema, name='quiz_ia_escolher_tema'),
    path('quiz-ia/gerar/', views.quiz_ia_gerar, name='quiz_ia_gerar'),
    path('quiz-ia/jogar/', views.quiz_ia_jogar, name='quiz_ia_jogar'),
    path('quiz-ia/resultado/', views.quiz_ia_resultado, name='quiz_ia_resultado'),
    path('quiz-ia/revisar-erradas/', views.quiz_ia_revisar_erradas, name='quiz_ia_revisar_erradas'),
    path('quiz-ia/salvar/', views.quiz_ia_salvar_tema, name='quiz_ia_salvar_tema'),
    
    # Progresso dos alunos
    path('progresso-alunos/', views.progresso_alunos, name='progresso_alunos'),
    
    # Importar perguntas (apenas professores)
    path('importar-perguntas/', views.importar_perguntas, name='importar_perguntas'),
    
    # Salas personalizadas
    path('sala/<int:sala_id>/pin/', views.visualizar_pin_sala, name='visualizar_pin_sala'),
    path('entrar-sala/', views.entrar_sala, name='entrar_sala'),
    path('sala/<int:sala_id>/jogar/', views.jogar_sala, name='jogar_sala'),
]

