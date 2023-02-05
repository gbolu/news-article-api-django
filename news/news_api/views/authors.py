from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import api_view
from rest_framework import status

from ..serializers.author import AuthorSerializer

from ..utils import Paginate, composeResponse

from ..repositories.author import AuthorRepository


@api_view(['GET'])
def getAuthors(request: Request):
    pagination = Paginate()

    page = request.GET.get('page', 1)
    limit = request.GET.get('limit', 10)

    pagination.set_page(int(page))
    pagination.set_limit(int(limit))

    authors = AuthorRepository().get_all(pagination)
    return composeResponse(authors, 'authors fetched successfully')


@api_view(['GET'])
def getSingleAuthor(_, id):
    author = AuthorRepository().get_one(id)
    if author is None:
        return composeResponse(None, 'no such author was found', status.HTTP_404_NOT_FOUND)
    return composeResponse(author, 'author fetched successfully')


@api_view(['POST'])
def createAuthor(request: Request):
    serializer = AuthorSerializer(data=request.data)
    if not serializer.is_valid():
        return composeResponse(None, 'invalid request', status.HTTP_400_BAD_REQUEST, serializer.errors)
    serializer.save()
    author = serializer.data
    return composeResponse(author, 'author created successfully', status.HTTP_201_CREATED)
