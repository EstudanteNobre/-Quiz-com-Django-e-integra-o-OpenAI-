from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='progresso',
            name='pontuacao_total',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='respostausuario',
            name='pontuacao',
            field=models.IntegerField(default=0),
        ),
    ]

