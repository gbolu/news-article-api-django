from django.contrib import admin

from .models.article import Article
from .models.author import Author
from .models.category import Category

# Register your models here.
admin.site.register(Article)
admin.site.register(Category)
admin.site.register(Author)
