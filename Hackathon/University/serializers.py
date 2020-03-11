from rest_framework import serializers
from .models import Profile,Application
class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model=Profile
        fields=["Name","Address","Website","Conteact_no","Type","University","AICTE_college_code","Email"]

class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Application
        fields=["proposal_text"]