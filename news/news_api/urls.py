from django.urls import path
from .views import articles
from .views import categories
from .views import authors
from django.conf import settings

urlpatterns = [
    # Register article routes
    path('articles/', articles.getArticles),
    path('articles/create', articles.createArticle),
    path('articles/<int:id>/', articles.getSingleArticle),

    # Register category routes
    path('categories/', categories.getCategories),
    path('categories/create', categories.createCategory),
    path('categories/<int:id>/', categories.getSingleCategory),

    # Register author routes
    path('authors/', authors.getAuthors),
    path('authors/create', authors.createAuthor),
    path('authors/<int:id>/', authors.getSingleAuthor),
]
