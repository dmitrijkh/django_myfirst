# Generated by Django 3.1.7 on 2021-04-20 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_auto_20210419_1957'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_slug',
            field=models.SlugField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
