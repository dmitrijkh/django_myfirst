# Переделать на классы

from django.http import Http404, HttpResponseRedirect



from django.shortcuts import render

from django.urls import reverse

from .models import Article

from rest_framework import viewsets
from .serializers import ArticleSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all().order_by('title')
    serializer_class = ArticleSerializer

def index(request):
    latest_articles_list = Article.objects.order_by('-pub_date')[:5]
    return render(request, 'articles/list.html',
                  {'latest_articles_list': latest_articles_list})


def detail(request, article_id):
    try:
        a = Article.objects.get(id=article_id)
    except BaseException:
        raise Http404('Статья не найдена')

    latest_comment_list = a.comment_set.filter(is_moderate=True).order_by('-id')[:10]

    return render(request, 'articles/detail.html',
                  {'article': a, 'latest_comment_list': latest_comment_list})


def leave_comment(request, article_id):
    try:
        a = Article.objects.get(id=article_id)
    except BaseException:
        raise Http404('Статья не найдена')

    a.comment_set.create(
        author_name=request.POST['name'], comment_text=request.POST['text'])

    return HttpResponseRedirect(reverse('articles:detail', args=(a.id,)))
