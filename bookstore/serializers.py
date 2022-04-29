from rest_framework import serializers
from bookstore.models import Users


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('id', 'username', 'token', 'type')
