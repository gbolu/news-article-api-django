from typing import Tuple

from ..serializers.category import CategorySerializer
from ..models.category import Category
from django.core.paginator import Paginator

from ..utils import Paginate


class CategoryRepository:
    def get_all(self, paginate: Paginate):
        categories = Paginator(Category.objects.all(), paginate.limit).page(
            paginate.page).object_list
        serializer = CategorySerializer(categories, many=True)
        return serializer.data

    def update_one(self, category: Category):
        id = category.get_category_id()
        Category.objects.filter(id=id).update(category=category)
        return None

    def get_one(self, category_id: int) -> Category:
        category = Category.objects.filter(id=category_id).first()
        if category is None:
            return None
        serializer = CategorySerializer(category, many=False)
        return serializer.data
