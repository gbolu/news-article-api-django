from django.db import models


class Author(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    job_description = models.TextField()

    class Meta:
        ordering = ['-created_at', 'name']

    def get_author_id(self) -> int:
        return self.id

    def __str__(self) -> str:
        return f'{self.name} {self.surname}'
