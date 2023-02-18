from rest_framework import mixins , generics ,status
from rest_framework.views import APIView 
from rest_framework.parsers import JSONParser
from django.http import HttpResponse , JsonResponse
from rest_framework.response import Response
from .models import * 
from .serializer import *
#USER delete ,update aw ghalet 
class get_create_user(generics.GenericAPIView , mixins.CreateModelMixin , mixins.ListModelMixin):
    serializer_class = user_serializer
    queryset=user.objects.all()
    def get(self,request):
        return self.list(request)
    def post(self,request):
        return self.create(request)
class delete_update_user_api(generics.GenericAPIView , mixins.DestroyModelMixin , mixins.UpdateModelMixin):
    serializer_class = user_serializer
    queryset=user.objects.all()
    lookup_field="pk"
    def delete(self, request,pk):
        return self.destroy(request,username="dady")
    def put(self,request,pk):
        return self.update(request,_id=pk)
#PUBS
class get_create_pub(generics.GenericAPIView , mixins.CreateModelMixin , mixins.ListModelMixin):
    serializer_class = pub_serializer
    queryset=pub.objects.all()
    def get(self,request):
        return self.list(request)
    def post(self,request):
        return self.create(request)
class delete_update_pub(generics.GenericAPIView , mixins.DestroyModelMixin , mixins.UpdateModelMixin):
    serializer_class = pub_serializer
    queryset=pub.objects.all()
    lookup_field="id"
    def get(self,request,id):
        serializer = pub_serializer(pub.objects.get(id=id))
        return JsonResponse(serializer.data)
    def delete(self, request,id):
        return self.destroy(request,id)
    def put(self,request,id):
        return self.update(request,id)
class get_themes(generics.GenericAPIView , mixins.ListModelMixin):
    serializer_class = pub_serializer
    queryset=pub.objects.filter(type = "theme")
    def get(self,request):
        return self.list(request)
class get_questions(generics.GenericAPIView , mixins.ListModelMixin):
    serializer_class = pub_serializer
    queryset=pub.objects.filter(type ="question")
    def get(self,request):
        return self.list(request)
#PROFILES _Students 
class profile_student_api(APIView):
    def get(self,request, id):
        try:
            snippets = student_profile.objects.get(id=id)
            serializer = student_profile_serializer(snippets)
            return JsonResponse(serializer.data)
        except :
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self ,request, id):
        snippets = student_profile.objects.get(id=id)
        snippets.delete()
        serializer=student_profile_serializer(snippets)
        return JsonResponse(serializer.data, status=201)
    def put(self , request , id ):
        altred_obj=student_profile.objects.get(id=id)
        serializer = student_profile_serializer(altred_obj , data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data , status=200,safe=False)
        return JsonResponse(serializer.data , status=404,safe=False)
class create_get_student_profile(APIView):#hna kayen ghelta fel post 
    def get( self , request ):
        all_profiles= student_profile.objects.all()
        serializer=student_profile_serializer(all_profiles,many=True)
        return JsonResponse(serializer.data,safe=False, status=200)
    def post(self, request, format=None):
        serializer = student_profile_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#PROFILES_ensignants
class profile_ensignats_api(APIView):
    def get(self,request, id):
        try:
            snippets = ensignant_profile.objects.get(id=id)
            serializer = ensignant_profile_serializer(snippets)
            return JsonResponse(serializer.data)
        except :
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self ,request, id ):
        snippets = ensignant_profile.objects.get(id=id)
        snippets.delete()
        serializer=ensignant_profile_serializer(snippets)
        return JsonResponse(serializer.data, status=201)
    def put(self , request , id ):
        altred_profile= ensignant_profile.objects.get(id=id)
        serializer = ensignant_profile_serializer(altred_profile , data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data , status=200)
        return JsonResponse(serializer.data , status=404)
class create_get_ensignant_profile(APIView):
    def get(self , request):
        all_profiles= ensignant_profile.objects.all()
        serializer=ensignant_profile_serializer(all_profiles,many=True)
        return JsonResponse(serializer.data,safe=False, status=200)
    def post(self, request, format=None):
        serializer = ensignant_profile_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#PROFILES_company
class get_create_company_profile(generics.GenericAPIView , mixins.CreateModelMixin , mixins.ListModelMixin):
    serializer_class = company_profile_serializer
    queryset=company_profile.objects.all()
    def get(self,request):
        return self.list(request)
    def post(self,request):
        return self.create(request)
class delete_update_company_profile_api(generics.GenericAPIView , mixins.DestroyModelMixin , mixins.UpdateModelMixin):
    serializer_class = company_profile_serializer
    queryset=company_profile.objects.all()
    lookup_field="id"
    def get(self , request , id ):#hadi jsp wchbiha 
        try:
            snippets = company_profile.objects.get(id=id)
            serializer = company_profile_serializer(snippets)
            return JsonResponse(serializer.data)
        except :
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request,id):
        return self.destroy(request,id)
    def put(self,request,id):
        return self.update(request,id)
#COMMENT 
class create_commentAPI(generics.GenericAPIView , mixins.CreateModelMixin):
    serializer_class=comment_serializer
    queryset=comment.objects.all()
    def post(self,request,id):
        return self.create(request)
class getposts_commentAPI(APIView):
    def get(self,request, id):
        try:
            comments = comment.objects.filter(post=id)
            serializer = comment_serializer(comments)
            return JsonResponse(serializer.data)
        except :
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id ):
        try:
            comment_to_delete = comment.objects.filter(id=id)
            serializer = comment_serializer(comment_to_delete)
            if serializer.is_valid():
                serializer.delete()
            return JsonResponse(serializer.data)
        except :
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#MESSAGES
class send_recieve_messageAPI(generics.GenericAPIView, mixins.CreateModelMixin ,mixins.ListModelMixin):
    serializer_class = message_serializer
    queryset = message.objects.all()
    def get(self,request):
        return self.list(request)
    def post(self,request):
        return self.create(request)