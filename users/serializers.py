from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    """
    Сериализатор пользователя
    """
    class Meta:
        model = User
        fields = '__all__'


class UserDetailSerializer(serializers.ModelSerializer):
    """
    Cериализатор пользователя с полями для просмотра
    """
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'tg_chat_id']


class UserUpdateSerializer(serializers.ModelSerializer):
    """
    Cериализатор пользователя с полями для редактирования
    """
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'tg_chat_id']
