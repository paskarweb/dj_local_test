# Generated by Django 2.2.6 on 2019-10-23 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lesson_fourth', '0004_article_publication'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'verbose_name': 'Автор', 'verbose_name_plural': 'Авторы'},
        ),
        migrations.AlterField(
            model_name='author',
            name='date_birth',
            field=models.DateField(verbose_name='Дата рождения'),
        ),
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='author',
            name='surname',
            field=models.CharField(max_length=50, verbose_name='Фамилия'),
        ),
    ]