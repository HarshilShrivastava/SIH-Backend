from rest_framework import serializers
from .models import Company,Jobs
class companyserializer(serializers.ModelSerializer):
    class Meta:
        model=Company
        fields=["Name","Address","Email","City","State","Registration_no","website"]
class jobserializer(serializers.ModelSerializer):
    class Meta:
        model=Jobs
        fields='__all__'