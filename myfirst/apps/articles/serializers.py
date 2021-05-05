from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta: 
        model = Article
        fields = ('title', 'text', 'pub_date', 'key_words')