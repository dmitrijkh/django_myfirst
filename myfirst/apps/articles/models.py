import datetime

from django.db import models

from django.utils import timezone
from tags import models as m


# Create your models here.

class Article(models.Model):
    # Переделать имена title, slug и т.д
    title = models.CharField('Название статьи', max_length=200)
    slug = models.SlugField(max_length=100)
    text = models.TextField('Текст статьи')
    pub_date = models.DateTimeField('Дата публикации')
    keywords = models.ManyToManyField(
        m.Keyword,
        through='ArticleKeyword',
        related_name='tags',
        through_fields=[
            'article',
            'tag'
        ]
        )


    def __str__(self):
        return self.title

    def was_published_recently(self):
        return self.pub_date >= (timezone.now() - datetime.timedelta(days=7))

    def get_absolute_url(self):
        # reverse принимает вьюху. Пишем сюда index
        return reverse('index', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
# Поля и класс промежуточной модели называть совмещённым названием соединяемых моделей.

class ArticleKeyword(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    tag = models.ForeignKey(m.Keyword, on_delete=models.CASCADE)

    class Meta:
        # unique_together = ('article', 'tag')
        constraints = [
            models.UniqueConstraint(fields=['article', 'tag'], name='article_tag_relation')
        ]



class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    # Это, в идеале, отдельная модель автор, и там уже поле name
    author_name = models.CharField('Имя комментатора', max_length=60)
    text = models.CharField('Текст комментария', max_length=200)
    is_moderate = models.BooleanField(default=False)

    def __str__(self):
        return self.author_name

    class Meta:
        verbose_name = 'комментарий'
        verbose_name_plural = 'комментарии'
