from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import User
from users.permissions import IsUser
from users.serializers import UserSerializer, UserUpdateSerializer, UserDetailSerializer


class UserCreateAPIView(CreateAPIView):
    """
    Регистрация пользователя
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        """
        Устанавливает пользователя активным
        """
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class UserAPIView(APIView):
    """
    Просмотр профиля пользователя
    """
    permission_classes = (IsAuthenticated, IsUser)

    def get(self, request):
        user = request.user
        serializer = UserDetailSerializer(user)
        return Response(serializer.data)

    def patch(self, request):
        user = request.user
        serializer = UserUpdateSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
