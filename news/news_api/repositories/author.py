from typing import Tuple
from ..models.author import Author
from django.core.paginator import Paginator
from ..serializers.author import AuthorSerializer

from ..utils import Paginate


class AuthorRepository:
    def get_all(self, paginate: Paginate):
        authors = Paginator(Author.objects.all(), paginate.limit).page(
            paginate.page).object_list
        serializer = AuthorSerializer(authors, many=True)
        return serializer.data

    def update_one(self, author: Author):
        id = author.get_author_id()
        Author.objects.filter(id=id).update(author=author)
        return None

    def get_one(self, author_id: int) -> Author:
        author = Author.objects.filter(id=author_id).first()
        if author is None:
            return None
        serializer = AuthorSerializer(author, many=False)
        return serializer.data
