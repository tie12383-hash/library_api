from rest_framework import serializers
from .models import BorrowRecord
from apps.books.models import Book

class BorrowRecordSerializer(serializers.ModelSerializer):
    book_title = serializers.ReadOnlyField(source='book.title')
    user_name = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = BorrowRecord
        fields = [
            'id', 'user', 'user_name', 'book', 'book_title',
            'issued_date', 'due_date', 'return_date', 'status'
        ]
        read_only_fields = ['issued_date', 'return_date', 'status']

    def validate(self, data):
        # Проверка наличия доступных экземпляров при создании
        if self.instance is None:  # создание
            book = data['book']
            if book.available_copies < 1:
                raise serializers.ValidationError("Нет доступных экземпляров книги.")
        return data