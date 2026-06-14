from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth import get_user_model
from .serializers import UserRegistrationSerializer, UserSerializer
from .permissions import IsLibrarian

User = get_user_model()

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action == 'create':
            # Регистрация доступна всем
            return [permissions.AllowAny()]
        # Остальные действия только библиотекарям
        return [permissions.IsAuthenticated(), IsLibrarian()]

    def get_serializer_class(self):
        if self.action == 'create':
            return UserRegistrationSerializer
        return UserSerializer