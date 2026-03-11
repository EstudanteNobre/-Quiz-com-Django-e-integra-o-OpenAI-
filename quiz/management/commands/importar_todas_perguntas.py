"""
Script para importar todas as perguntas baseadas nos arquivos
`quiz/data/perguntas-*-completas.py` diretamente para o banco de dados.
"""
from importlib import util as importlib_util
from pathlib import Path

from django.core.management.base import BaseCommand
from django.db import transaction

from quiz.models import Dificuldade, Pergunta, Tema


class Command(BaseCommand):
    help = 'Importa todas as perguntas dos arquivos em quiz/data/ diretamente para o banco de dados.'

    def add_arguments(self, parser):
        parser.add_argument(
            '--limpar',
            action='store_true',
            help='Limpa todas as perguntas existentes antes de popular.',
        )

    def _carregar_modulo(self, caminho_arquivo: Path):
        """
        Carrega dinamicamente um módulo Python a partir de um arquivo e retorna o objeto de módulo.
        """
        module_name = f"quiz.data.{caminho_arquivo.stem.replace('-', '_')}"
        spec = importlib_util.spec_from_file_location(module_name, caminho_arquivo)
        if spec is None or spec.loader is None:
            raise ImportError(f'Não foi possível carregar o módulo do arquivo {caminho_arquivo.name}')
        module = importlib_util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module

    def handle(self, *args, **options):
        data_dir = Path(__file__).resolve().parents[2] / 'data'
        arquivos_perguntas = sorted(data_dir.glob('perguntas-*-completas.py'))

        if not arquivos_perguntas:
            self.stdout.write(self.style.ERROR('Nenhum arquivo de perguntas encontrado em quiz/data/.'))
            return

        if options['limpar']:
            Pergunta.objects.all().delete()
            self.stdout.write(self.style.WARNING('[AVISO] Todas as perguntas foram removidas.'))

        # Garante que as dificuldades padrão existam
        dificuldades_padrao = [
            ('facil', 'Fácil', 1),
            ('medio', 'Médio', 2),
            ('dificil', 'Difícil', 3),
        ]
        for nivel, nome, ordem in dificuldades_padrao:
            Dificuldade.objects.get_or_create(
                nivel=nivel,
                defaults={'nome': nome, 'ordem': ordem}
            )

        dificuldades_dict = {d.nivel: d for d in Dificuldade.objects.all()}

        total_criadas = 0
        total_ja_existiam = 0
        total_erros = 0
        total_arquivos = 0

        for arquivo in arquivos_perguntas:
            total_arquivos += 1
            try:
                modulo = self._carregar_modulo(arquivo)
                perguntas_data = getattr(modulo, 'PERGUNTAS_DATA', None)
                if perguntas_data is None:
                    self.stdout.write(
                        self.style.WARNING(f'[AVISO] Arquivo {arquivo.name} não possui PERGUNTAS_DATA. Ignorado.')
                    )
                    continue
            except Exception as exc:
                self.stdout.write(
                    self.style.ERROR(f'[ERRO] Falha ao carregar {arquivo.name}: {exc}')
                )
                total_erros += 1
                continue

            for tema_nome, rodadas in perguntas_data.items():
                tema, _ = Tema.objects.get_or_create(nome=tema_nome)

                for dificuldades in rodadas.values():
                    for dificuldade_nome, perguntas in dificuldades.items():
                        dificuldade = dificuldades_dict.get(dificuldade_nome)
                        if dificuldade is None:
                            self.stdout.write(
                                self.style.ERROR(
                                    f'[ERRO] Dificuldade "{dificuldade_nome}" não registrada no banco de dados.'
                                )
                            )
                            total_erros += 1
                            continue

                        for pergunta_data in perguntas:
                            try:
                                with transaction.atomic():
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
                            except Exception as exc:
                                self.stdout.write(
                                    self.style.ERROR(f'[ERRO] Problema ao criar pergunta "{pergunta_data.get("texto")}": {exc}')
                                )
                                total_erros += 1

        self.stdout.write(
            self.style.SUCCESS(
                '\n[OK] Processo concluído!\n'
                f'  - Arquivos processados: {total_arquivos}\n'
                f'  - Perguntas criadas: {total_criadas}\n'
                f'  - Perguntas que já existiam: {total_ja_existiam}\n'
                f'  - Erros: {total_erros}\n'
                f'  - Total processado: {total_criadas + total_ja_existiam}'
            )
        )
