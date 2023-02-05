from rest_framework import serializers
from ..models.article import Article


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'content', 'created_at', 'updated_at',
                  'summary', 'published', 'published_date', 'author', 'category')
