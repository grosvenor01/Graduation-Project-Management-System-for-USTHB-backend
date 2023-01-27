from django.shortcuts import render
from rest_framework import mixins , generics 
from rest_framework.parsers import JSONParser
from django.http import HttpResponse , JsonResponse
from .models import * 
from .serializer import user_serializer
# Create your views here.
class userAPI(generics.GenericAPIView , mixins.CreateModelMixin , mixins.ListModelMixin):
    serializer_class = user_serializer
    queryset=User.objects.all()
    lookup_field="id"
    def get(self,request):
        return self.list(request)
    def post(self,request):
        return self.create(request)
class delete_update_user_api(generics.GenericAPIView , mixins.DestroyModelMixin , mixins.UpdateModelMixin):
    serializer_class = user_serializer
    queryset=User.objects.all()
    lookup_field="id"
    def delete(self, request,id):
        return self.destroy(request,id)
    def put(self,request,id):
        return self.update(request,id)
class pubAPI():
    pass 
def profileAPI(request):
    pass 
