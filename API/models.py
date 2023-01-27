from django.db import models
from django.contrib.auth import get_user_model
import datetime
# Create your models here.
types=(('question','question'),('theme','theme'))
User = get_user_model()
class pub(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    text=models.TextField()
    pub_type=models.CharField(max_length =30 ,choices=types)
    date=models.DateField(default=datetime.date.today)
class profile(models.Model):
    user=models.OneToOneField(User , on_delete=models.CASCADE)
    speciality=models.CharField(max_length=300)
    interested =models.CharField(max_length=400)
    university_name=models.CharField(max_length=200)
class skill(models.Model):
    user=models.ForeignKey(User , on_delete=models.CASCADE)
    skill_name=models.CharField(max_length=200)
class student_profile(profile):
    binome=models.ForeignKey(User , on_delete=models.CASCADE,default=None)
    CV=models.FileField(upload_to="CVs", max_length=1999999)
    study_level=models.CharField( max_length =30 ,choices=(('L3','L3'),('M2','M2'),("doctorate","doctorate")))
    github_link=models.URLField(max_length=300)
    linkedin_link =models.URLField(max_length=300)
class ensignant_profile(profile):
    grade=models.CharField(max_length=200)
    rating =models.IntegerField()
    departement=models.CharField(max_length=300)
class company_profile(models.Model):
    name=models.CharField(max_length=130)
    desription = models.TextField()
    post_needed = models.CharField(max_length=250)
    validation = models.CharField(max_length =30 ,choices=(("true","true"),("false","false")))
class comment(models.Model):
    comment_by= models.ForeignKey(User , on_delete=models.CASCADE)
    pub = models.ForeignKey(pub , on_delete=models.CASCADE)
    text= models.TextField()
    date = models.DateField(default=datetime.date.today)
    
    