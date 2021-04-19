# Generated by Django 3.1.7 on 2021-04-19 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0003_auto_20210418_1156'),
        ('articles', '0004_auto_20210418_1222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='keywords',
            field=models.ManyToManyField(related_name='tags', through='articles.Article_Keyword', to='tags.Keyword'),
        ),
    ]