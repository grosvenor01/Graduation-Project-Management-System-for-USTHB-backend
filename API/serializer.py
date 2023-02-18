from rest_framework import serializers
from .models import *
class user_serializer(serializers.ModelSerializer):
    class Meta:
        model =user
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
class comment_serializer(serializers.ModelSerializer):
    class Meta:
        model=comment
        fields = "__all__"
class message_serializer(serializers.ModelSerializer):
    class Meta:
        model=message
        fields="__all__"