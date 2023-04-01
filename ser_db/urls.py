"""ser_db URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from API.views import *
from knox import views as knox_views
urlpatterns = [
    #ymcho 
    path('admin/', admin.site.urls),
    path('api/register/',register.as_view()),
    path('api/login/',loginAPI.as_view()),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/pub/',get_create_pub.as_view()),
    path('api/pub/<int:id>',delete_update_pub.as_view()),
    path('api/themes/',get_themes.as_view()),
    path('api/questions/',get_questions.as_view()),
    path('api/postuler/<int:id>', postuler.as_view()),
    path('api/notification/<int:id>', notification_API.as_view()),
    path('api/envoyer-fiche-de-pfe/', generate_fiche_pfe.as_view(),name="generate_fiche_pfe"),
    path('api/validation_des_themes/<int:id>', themes_validation.as_view(),name="themes_validation"),
    path('api/accpete_refuse_themes/<int:id>', accpete_refuse_themes.as_view(),name="accpete_refuse_themes"),
    path('api/student_profile/',create_get_student_profile.as_view()),
    path('api/student_profile/<int:id>',profile_student_api.as_view()),
    path('api/ensignant_profile/',create_get_ensignant_profile.as_view()),
    path('api/ensignant_profile/<int:id>',profile_ensignats_api.as_view()),
    path('api/comapny_profile/',get_create_company_profile.as_view()),
    path('api/comapny_profile/<int:id>',delete_update_company_profile_api.as_view()),
    path('api/comments/<int:id',getposts_commentAPI.as_view()),
    path('api/comments/',create_commentAPI.as_view()) #id ta3 pub ytb3at m3a el data 
]