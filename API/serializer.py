from rest_framework import serializers
from .models import *
class user_serializer(serializers.ModelSerializer):
    class Meta:
        model =User
        fields="__all__"