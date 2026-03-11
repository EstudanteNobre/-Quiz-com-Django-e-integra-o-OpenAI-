from django.core.management.base import BaseCommand
from quiz.models import Tema, Dificuldade


class Command(BaseCommand):
    help = 'Popula o banco de dados com os temas e dificuldades iniciais do Info Quiz'

    def handle(self, *args, **options):
        # Criar dificuldades
        dificuldades_data = [
            {'nivel': 'facil', 'nome': 'Fácil', 'ordem': 1},
            {'nivel': 'medio', 'nome': 'Médio', 'ordem': 2},
            {'nivel': 'dificil', 'nome': 'Difícil', 'ordem': 3},
        ]
        
        for diff_data in dificuldades_data:
            dificuldade, created = Dificuldade.objects.get_or_create(
                nivel=diff_data['nivel'],
                defaults={'nome': diff_data['nome'], 'ordem': diff_data['ordem']}
            )
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f'[OK] Dificuldade "{dificuldade.nome}" criada com sucesso!')
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f'[AVISO] Dificuldade "{dificuldade.nome}" ja existe.')
                )
        
        # Criar temas
        temas_data = [
            {'nome': 'Python'},
            {'nome': 'Redes'},
            {'nome': 'Banco de Dados'},
            {'nome': 'Inglês'},
            {'nome': 'Informática'},
            {'nome': 'Análise de Projeto'},
            {'nome': 'Algoritmos'},
        ]
        
        for tema_data in temas_data:
            tema, created = Tema.objects.get_or_create(
                nome=tema_data['nome'],
                defaults={'descricao': f'Quiz sobre {tema_data["nome"]}'}
            )
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f'[OK] Tema "{tema.nome}" criado com sucesso!')
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f'[AVISO] Tema "{tema.nome}" ja existe.')
                )
        
        self.stdout.write(
            self.style.SUCCESS('\n[OK] Dados iniciais populados com sucesso!')
        )

