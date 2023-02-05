from django.db import models


class Category(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ['-created_at', 'name']
        managed = True

    def get_category_id(self) -> int:
        return self.id

    def __str__(self) -> str:
        return self.name
