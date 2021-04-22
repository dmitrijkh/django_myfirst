from django.contrib import admin

# Register your models here.
from .models import Article, Comment

class ArticleAdmin(admin.ModelAdmin):
    # list_display = ('article_title', 'article_text')
    read_only_fields = ['article_slug']

admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
