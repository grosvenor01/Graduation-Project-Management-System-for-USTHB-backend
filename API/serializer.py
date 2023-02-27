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
class comment_serializer(serializers.ModelSerializer):
    class Meta:
        model=comment
        fields = "__all__"
class message_serializer(serializers.ModelSerializer):
    class Meta:
        model=message
        fields="__all__"
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}} # the field will only be used for deserialization (when creating or updating an object

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
        return user