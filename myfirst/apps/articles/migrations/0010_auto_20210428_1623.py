# Generated by Django 3.2 on 2021-04-28 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0009_rename_comment_text_comment_text'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='articlekeyword',
            unique_together=set(),
        ),
        migrations.AddConstraint(
            model_name='articlekeyword',
            constraint=models.UniqueConstraint(fields=('article', 'tag'), name='article_tag_relation'),
        ),
    ]
