from django.core.management.base import BaseCommand
from quiz.models import Tema, Dificuldade, Pergunta
import re


class Command(BaseCommand):
    help = 'Popula o banco de dados com todas as perguntas do Info Quiz'

    def add_arguments(self, parser):
        parser.add_argument(
            '--limpar',
            action='store_true',
            help='Limpa todas as perguntas existentes antes de popular',
        )

    def handle(self, *args, **options):
        if options['limpar']:
            Pergunta.objects.all().delete()
            self.stdout.write(self.style.WARNING('[AVISO] Todas as perguntas foram removidas.'))

        # Obter temas e dificuldades
        temas_dict = {tema.nome: tema for tema in Tema.objects.all()}
        dificuldades_dict = {
            'facil': Dificuldade.objects.get(nivel='facil'),
            'medio': Dificuldade.objects.get(nivel='medio'),
            'dificil': Dificuldade.objects.get(nivel='dificil'),
        }

        # Importar todas as perguntas
        from quiz.data.perguntas_completas import PERGUNTAS_DATA

        total_criadas = 0
        total_ja_existiam = 0
        total_erros = 0

        for tema_nome, rodadas in PERGUNTAS_DATA.items():
            if tema_nome not in temas_dict:
                self.stdout.write(
                    self.style.ERROR(f'[ERRO] Tema "{tema_nome}" nao encontrado no banco de dados.')
                )
                total_erros += 1
                continue

            tema = temas_dict[tema_nome]

            for rodada_num, dificuldades in rodadas.items():
                for dificuldade_nome, perguntas in dificuldades.items():
                    if dificuldade_nome not in dificuldades_dict:
                        self.stdout.write(
                            self.style.ERROR(f'[ERRO] Dificuldade "{dificuldade_nome}" nao encontrada.')
                        )
                        total_erros += 1
                        continue

                    dificuldade = dificuldades_dict[dificuldade_nome]

                    for pergunta_data in perguntas:
                        try:
                            pergunta, created = Pergunta.objects.get_or_create(
                                tema=tema,
                                dificuldade=dificuldade,
                                texto=pergunta_data['texto'],
                                defaults={
                                    'alternativa_a': pergunta_data['alternativa_a'],
                                    'alternativa_b': pergunta_data['alternativa_b'],
                                    'alternativa_c': pergunta_data['alternativa_c'],
                                    'alternativa_d': pergunta_data['alternativa_d'],
                                    'resposta_correta': pergunta_data['resposta_correta'],
                                }
                            )

                            if created:
                                total_criadas += 1
                            else:
                                total_ja_existiam += 1
                        except Exception as e:
                            self.stdout.write(
                                self.style.ERROR(f'[ERRO] Erro ao criar pergunta: {e}')
                            )
                            total_erros += 1

        self.stdout.write(
            self.style.SUCCESS(
                f'\n[OK] Processo concluido!\n'
                f'  - Perguntas criadas: {total_criadas}\n'
                f'  - Perguntas que ja existiam: {total_ja_existiam}\n'
                f'  - Erros: {total_erros}\n'
                f'  - Total processado: {total_criadas + total_ja_existiam}'
            )
        )
