# Generated by Django 3.0.6 on 2020-05-30 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200, verbose_name='Nome')),
                ('nascimento', models.DateField(verbose_name='Nascimento')),
                ('cpf', models.CharField(max_length=14, verbose_name='CPF')),
            ],
        ),
    ]
