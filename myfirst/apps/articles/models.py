import datetime

from django.db import models

from django.utils import timezone
from tags import models as m


# Create your models here.

class Article(models.Model):
    article_title = models.CharField('Название статьи', max_length=200)
    article_slug = models.SlugField(max_length=100)
    article_text = models.TextField('Текст статьи')
    pub_date = models.DateTimeField('Дата публикации')
    keywords = models.ManyToManyField(
        m.Keyword,
        through='Article_Keyword',
        related_name='tags',
        through_fields=[
        'article',
        'tag'
        ]
        )


    def __str__(self):
        return self.article_title

    def was_published_recently(self):
        return self.pub_date >= (timezone.now() - datetime.timedelta(days=7))

    def get_absolute_url(self):
        return reverse('articles/detail.html', kwargs={'slug': self.article_slug})

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
# Поля и класс промежуточной модели называть совмещённым названием соединяемых моделей.

class Article_Keyword(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    tag = models.ForeignKey(m.Keyword, on_delete=models.CASCADE)




class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author_name = models.CharField('Имя комментатора', max_length=60)
    comment_text = models.CharField('Текст комментария', max_length=200)
    is_moderate = models.BooleanField(default=False)

    def __str__(self):
        return self.author_name

    class Meta:
        verbose_name = 'комментарий'
        verbose_name_plural = 'комментарии'
