from typing import Tuple
from ..models.article import Article
from django.core.paginator import Paginator
from ..serializers.article import ArticleSerializer

from ..utils import Paginate


class ArticleRepository:
    def get_all(self, paginate: Paginate):
        articles = Paginator(Article.objects.all().select_related('author'), paginate.limit).page(
            paginate.page).object_list
        serializer = ArticleSerializer(articles, many=True)
        return serializer.data

    def update_one(self, article: Article):
        id = article.get_article_id()
        Article.objects.filter(id=id).update(article=article)
        return None

    def get_one(self, article_id: int) -> Article:
        article = Article.objects.filter(id=article_id).first()
        if article is None:
            return None
        serializer = ArticleSerializer(article, many=False)
        return serializer.data
