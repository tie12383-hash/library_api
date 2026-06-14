from rest_framework import viewsets, filters
from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer
from .permissions import IsLibrarianOrReadOnly

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsLibrarianOrReadOnly]

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsLibrarianOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'author__first_name', 'author__last_name', 'genre']
    ordering_fields = ['title', 'published_year']