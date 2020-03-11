from rest_framework import serializers
from .models import image
class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model=image
        fields='__all__'