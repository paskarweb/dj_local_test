# Generated by Django 2.2.6 on 2019-11-07 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lesson_fifth', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='text',
            field=models.TextField(max_length=500, verbose_name='Текст статьи'),
        ),
    ]