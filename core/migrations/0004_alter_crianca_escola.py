# Generated by Django 4.1 on 2022-08-29 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_escola_alter_crianca_escola'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crianca',
            name='escola',
            field=models.CharField(max_length=150),
        ),
    ]