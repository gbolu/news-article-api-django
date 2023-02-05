from re import S
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import api_view
from rest_framework import status

from ..serializers.article import ArticleSerializer

from ..utils import Paginate, composeResponse

from ..repositories.article import ArticleRepository

# These contain the response to the HTTP requests.

# Returns all the articles.


@api_view(['GET'])
def getArticles(request: Request):
    pagination = Paginate()

    page = request.GET.get('page', 1)
    limit = request.GET.get('limit', 10)

    pagination.set_page(int(page))
    pagination.set_limit(int(limit))

    articles = ArticleRepository().get_all(pagination)
    return composeResponse(articles, 'articles fetched successfully')


@api_view(['GET'])
def getSingleArticle(_, id):
    article = ArticleRepository().get_one(id)
    if article is None:
        return composeResponse(None, 'no such article was found', status.HTTP_404_NOT_FOUND)
    return composeResponse(article, 'article fetched successfully')


@api_view(['POST'])
def createArticle(request: Request):
    serializer = ArticleSerializer(data=request.data)
    if not serializer.is_valid():
        return composeResponse(None, 'invalid request', status.HTTP_400_BAD_REQUEST, serializer.errors)
    serializer.save()
    article = serializer.data
    return composeResponse(article, 'article created successfully', status.HTTP_201_CREATED)
