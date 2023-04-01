from django.db import models
from django.contrib.auth import get_user_model
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
User = get_user_model() 
class pub(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)   #user that post this pub 
    user_type = models.CharField(max_length =30,choices=(('etudiant','etudiant'),('ensignant','ensignant'),('entreprise','entreprise')))
    main_text=models.CharField(max_length=300)
    description_text=models.TextField()
    type=models.CharField(max_length =30 ,choices=(('question','question'),('theme','theme')))
    keywords = models.CharField(max_length=400) #converting the keywords into a string and store it 
    date=models.DateField(default=datetime.date.today)
    comission=models.ForeignKey("comission_validation",on_delete=models.CASCADE, blank=True , null = True )
    def __str__(self):
        return self.main_text
class themes_to_validate(models.Model):
    file = models.FileField(blank=True, null =True )
    specialite = models.CharField(max_length=200 , choices=(('sepcialité1','sepcialité1'),('sepcialité2','sepcialité2'),('sepcialité3','sepcialité3')))
class validated_themes(models.Model):
    file = models.FileField(blank=True, null =True )
    specialite = models.CharField(max_length=200 , choices=(('sepcialité1','sepcialité1'),('sepcialité2','sepcialité2'),('sepcialité3','sepcialité3')))
    status=models.CharField(choices=(('Accepted','Accepted'),('Rejected','Rejected')),max_length=20)
class skill(models.Model):
    user=models.ForeignKey(User , on_delete=models.CASCADE)
    skill_name=models.CharField(max_length=200)
    description=models.TextField()
    pourcentage = models.IntegerField(validators=[MaxValueValidator(100),MinValueValidator(10)])
    def __str__(self):
        return self.skill_name
class student(models.Model):
    user=models.OneToOneField(User , on_delete=models.CASCADE,related_name="owner")
    speciality=models.CharField(max_length=300)
    interested =models.CharField(max_length=400)
    CV=models.FileField(upload_to="CVs", max_length=1999999,blank=True)
    study_level=models.CharField( max_length =30 ,choices=(('L3','L3'),('M2','M2'),("doctorate","doctorate")))
    github_link=models.URLField(max_length=300)
    linkedin_link =models.URLField(max_length=300)
    Role = models.CharField(choices = (('Binome','Binome'),('monome','monome'),('None','None')), default="None", max_length = 20)
    binome=models.ForeignKey(User , on_delete=models.CASCADE,related_name="binome",blank =True ,  null=True)
    def __str__(self):
        return self.user.username
class jury(models.Model):
    m_jury_st=models.ForeignKey(User, on_delete=models.CASCADE,related_name="m_jury1")
    jury_nd=models.ForeignKey(User , on_delete = models.CASCADE,related_name="m_jury2")
    president = models.ForeignKey(User , on_delete = models.CASCADE,related_name="president")
    themes = models.ForeignKey(pub, on_delete=models.CASCADE,related_name="themes")
class ensignant(models.Model):
    user=models.OneToOneField(User , on_delete=models.CASCADE)
    themes_proposed=models.ForeignKey(pub, on_delete=models.CASCADE)
    grade=models.CharField(max_length=200)
    rating =models.IntegerField(validators=[MaxValueValidator(5),MinValueValidator(0)])
    def __str__(self):
        return self.user.username
class resp_epcialit(models.Model):
    ensignant_re=models.ForeignKey(ensignant, on_delete=models.CASCADE, blank =True , null =True)
    specialite = models.CharField(max_length=200 , choices=(('sepcialité1','sepcialité1'),('sepcialité2','sepcialité2'),('sepcialité3','sepcialité3')),blank =True , null =True)
class comission_validation(models.Model):
    ensignant1=models.ForeignKey(ensignant, on_delete=models.CASCADE,related_name="m_comission1")
    ensignant2=models.ForeignKey(ensignant , on_delete = models.CASCADE,related_name="m_comission2")
    ensignant3 = models.ForeignKey(ensignant , on_delete = models.CASCADE,related_name="m_comission3")
    theme = models.ForeignKey(themes_to_validate, on_delete=models.CASCADE)
    #khsna liste ta3 les themes
class company(models.Model):
    name=models.CharField(max_length=130)
    desription = models.TextField()
    post_needed = models.CharField(max_length=250)
    validation = models.CharField(max_length =30 ,choices=(("True","True"),("False","False")))
    def __str__(self):
        return self.name
class comment(models.Model):
    comment_by= models.ForeignKey(User , on_delete=models.CASCADE)
    pub = models.ForeignKey(pub , on_delete=models.CASCADE)
    text= models.TextField()
    date = models.DateField(default=datetime.date.today)
    def __str__(self):
        return self.text
class message(models.Model):
    pass
class notification(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name="user")
    id_pub = models.ForeignKey(pub, on_delete=models.CASCADE, blank=True , null = True)
    titel = models.CharField(max_length=200)
    decription = models.TextField()
    date = models.DateTimeField(default=datetime.date.today)
    notification_type = models.CharField(choices=(('notification_binome','notification_binome'),('notification_ensignant','notification_ensignant'),('notification_responsable','notification_responsable')),max_length=100)
    send_from=models.ForeignKey(User,on_delete=models.CASCADE, blank=True , null =True,related_name="send_from")