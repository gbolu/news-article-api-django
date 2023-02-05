from django.db import models

from ..models.author import Author

from ..models.category import Category


class Article(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.TextField()
    summary = models.TextField()
    content = models.TextField()
    published = models.BooleanField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-published_date', '-created_at', 'title']
        managed = True

    def get_article_id(self):
        return self.id

    def __str__(self) -> str:
        return self.title
