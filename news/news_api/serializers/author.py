from rest_framework import serializers
from ..models.author import Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'name', 'surname', 'created_at',
                  'updated_at', 'job_description')
