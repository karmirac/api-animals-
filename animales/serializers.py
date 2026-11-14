from rest_framework import serializers
from .models import Animal


class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')