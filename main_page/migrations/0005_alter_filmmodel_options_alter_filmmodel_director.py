# Generated by Django 4.2.7 on 2023-11-21 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0004_alter_filmmodel_genre'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='filmmodel',
            options={'verbose_name': 'Авто', 'verbose_name_plural': 'Авто'},
        ),
        migrations.AlterField(
            model_name='filmmodel',
            name='director',
            field=models.CharField(max_length=100, verbose_name='Укажите цену'),
        ),
    ]
