
from django.db import models

# from articles import models as art_m
# Create your models here.

class Keyword(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'





# class Tag(models.Model):
#   tag_article = models.ManyToManyField(m.Article)
#   tag_name = models.CharField(max_length=20)

#   def __str__(self):
#       return self.tag_name

#   class Meta:
#       verbose_name = 'Тег'
#       verbose_name_plural = 'Теги'