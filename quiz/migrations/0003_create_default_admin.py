from django.conf import settings
from django.db import migrations


APP_LABEL, MODEL_NAME = settings.AUTH_USER_MODEL.split('.')


def create_default_admin(apps, schema_editor):
    User = apps.get_model(APP_LABEL, MODEL_NAME)
    username = 'admin'
    password = 'admin123456'
    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username=username, email='', password=password)


def remove_default_admin(apps, schema_editor):
    User = apps.get_model(APP_LABEL, MODEL_NAME)
    User.objects.filter(username='admin').delete()


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_respostausuario_pontuacao_progresso_pontuacao_total'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RunPython(create_default_admin, remove_default_admin),
    ]

