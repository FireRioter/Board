# Generated by Django 5.0.7 on 2024-07-31 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='category',
            field=models.CharField(choices=[('TANK', 'Танки'), ('HEALER', 'Хилы'), ('DPS', 'ДД'), ('MERCHANT', 'Торговцы'), ('GUILDMASTER', 'Гилдмастеры'), ('QUESTGIVER', 'Квестгиверы'), ('BLACKSMITH', 'Кузнецы'), ('LEATHERWORKER', 'Кожевники'), ('POTION_MASTER', 'Зельевары'), ('SPELLMASTER', 'Мастера заклинаний')], max_length=20),
        ),
    ]