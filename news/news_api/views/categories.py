from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import api_view
from rest_framework import status

from ..serializers.category import CategorySerializer

from ..utils import Paginate, composeResponse

from ..repositories.category import CategoryRepository


@api_view(['GET'])
def getCategories(request: Request):
    pagination = Paginate()

    page = request.GET.get('page', 1)
    limit = request.GET.get('limit', 10)

    pagination.set_page(int(page))
    pagination.set_limit(int(limit))

    articles = CategoryRepository().get_all(pagination)
    return composeResponse(articles, 'categories fetched successfully')


@api_view(['GET'])
def getSingleCategory(_, id):
    category = CategoryRepository().get_one(id)
    if category is None:
        return composeResponse(None, 'no such category was found', status.HTTP_404_NOT_FOUND)
    return composeResponse(category, 'category fetched successfully')


@api_view(['POST'])
def createCategory(request: Request):
    serializer = CategorySerializer(data=request.data)
    if not serializer.is_valid():
        return composeResponse(None, 'invalid request', status.HTTP_400_BAD_REQUEST, serializer.errors)
    serializer.save()
    article = serializer.data
    return composeResponse(article, 'article created successfully', status.HTTP_201_CREATED)
