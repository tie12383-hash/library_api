from rest_framework import serializers
from .models import Author, Book

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source='author.__str__')

    class Meta:
        model = Book
        fields = [
            'id', 'title', 'author', 'author_name', 'genre',
            'published_year', 'isbn', 'total_copies', 'available_copies'
        ]
        read_only_fields = ['available_copies']