from rest_framework import serializers
from .models import *
class user_serializer(serializers.ModelSerializer):
    class Meta:
        model =User
        fields="__all__"
class pub_serializer(serializers.ModelSerializer):
    class Meta:
        model=pub
        fields ="__all__"
class student_profile_serializer(serializers.ModelSerializer):
    class Meta:
        model=student_profile
        fields ="__all__"
class ensignant_profile_serializer(serializers.ModelSerializer):
    class Meta:
        model=ensignant_profile
        fields ="__all__"
class company_profile_serializer(serializers.ModelSerializer):
    class Meta: 
        model = company_profile
        fields ="__all__"