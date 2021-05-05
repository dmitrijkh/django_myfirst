from django.urls import path, include

from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'articles', views.ArticleViewSet)
app_name = 'articles'

urlpatterns = [

    path('', views.index, name='index'),
    path('<int:article_id>/', views.detail, name='detail'),
    path('<int:article_id>/leave_comment',
         views.leave_comment, name='leave_comment'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    # path('test/', views.test, name='test')
]
