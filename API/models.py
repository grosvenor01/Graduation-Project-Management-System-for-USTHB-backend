import datetime
from djongo import models
# Create your models here.
class user(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
class pub(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    user=models.EmbeddedField(user)
    text=models.TextField()
    pub_type=models.CharField(max_length =30 ,choices=(('question','question'),('theme','theme')))
    date=models.DateField(default=datetime.date.today)
    type=models.CharField(max_length=10,choices=(("theme","theme"),("question","question")))
class profile(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    user=models.EmbeddedField(user)
    speciality=models.CharField(max_length=300)
    interested =models.CharField(max_length=400)
    university_name=models.CharField(max_length=200)
class skill(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    user=models.EmbeddedField(user)
    skill_name=models.CharField(max_length=200)
class student_profile(profile):
    binome=models.EmbeddedField(user)
    CV=models.FileField(upload_to="CVs", max_length=1999999,blank=True)
    study_level=models.CharField( max_length =30 ,choices=(('L3','L3'),('M2','M2'),("doctorate","doctorate")))
    github_link=models.URLField(max_length=300)
    linkedin_link =models.URLField(max_length=300)
class ensignant_profile(profile):
    grade=models.CharField(max_length=200)
    rating =models.IntegerField()
    departement=models.CharField(max_length=300)
class company_profile(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    name=models.CharField(max_length=130)
    description = models.TextField()
    post_needed = models.CharField(max_length=250)
    validation = models.CharField(max_length =30 ,choices=(("true","true"),("false","false")))
class comment(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    comment_by=models.EmbeddedField(user)
    post=models.EmbeddedField(pub)
    text=models.TextField()
    date = models.DateField(auto_now=True)
class message(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    sender=models.EmbeddedField(user)
    date=date=models.DateField(default=datetime.date.today)
    message_text=models.TextField()
    
    