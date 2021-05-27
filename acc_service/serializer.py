from django.contrib.auth.models import User
from rest_framework import serializers

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class AccountLoginSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=255)