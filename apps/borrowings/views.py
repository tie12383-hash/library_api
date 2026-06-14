from rest_framework import viewsets, status, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils import timezone
from .models import BorrowRecord
from .serializers import BorrowRecordSerializer
from .permissions import IsLibrarian

class BorrowRecordViewSet(viewsets.ModelViewSet):
    queryset = BorrowRecord.objects.all()
    serializer_class = BorrowRecordSerializer

    def get_permissions(self):
        if self.action in ['create', 'return_book']:
            # Создавать запись может любой аутентифицированный, возвращать – владелец или библиотекарь
            return [permissions.IsAuthenticated()]
        # Просмотр и изменение – только библиотекарь
        return [permissions.IsAuthenticated(), IsLibrarian()]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'librarian':
            return BorrowRecord.objects.all()
        # Читатель видит только свои записи
        return BorrowRecord.objects.filter(user=user)

    def perform_create(self, serializer):
        # Автоматически проставляем пользователя и уменьшаем available_copies
        book = serializer.validated_data['book']
        book.available_copies -= 1
        book.save()
        serializer.save(user=self.request.user)

    @action(detail=True, methods=['post'])
    def return_book(self, request, pk=None):
        record = self.get_object()
        if record.status == 'returned':
            return Response({'detail': 'Книга уже возвращена.'}, status=status.HTTP_400_BAD_REQUEST)
        if request.user != record.user and request.user.role != 'librarian':
            return Response({'detail': 'Недостаточно прав.'}, status=status.HTTP_403_FORBIDDEN)

        record.status = 'returned'
        record.return_date = timezone.now()
        record.save()
        # Увеличиваем количество доступных экземпляров
        record.book.available_copies += 1
        record.book.save()
        return Response({'detail': 'Книга успешно возвращена.'})