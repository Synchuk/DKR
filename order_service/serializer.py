from .models import Good
from rest_framework import serializers

class GoodModelSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    class Meta:
        model = Good
        fields = '__all__'