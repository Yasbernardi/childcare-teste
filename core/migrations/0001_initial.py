# Generated by Django 4.1 on 2022-08-29 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('endereco', models.CharField(max_length=250)),
                ('telefone', models.CharField(max_length=14)),
                ('nome', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=250)),
                ('data_nasc', models.DateField()),
                ('cpf', models.CharField(max_length=14)),
            ],
        ),
    ]
