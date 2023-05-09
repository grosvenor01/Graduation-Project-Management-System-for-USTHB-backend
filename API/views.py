from rest_framework import mixins , generics ,status
from rest_framework.views import APIView 
from rest_framework.parsers import JSONParser
from django.http import HttpResponse , JsonResponse
from rest_framework.response import Response
from .models import * 
from .serializer import *
from knox.models import AuthToken
from rest_framework.authtoken.serializers import AuthTokenSerializer
from django.contrib.auth import login
from rest_framework import permissions , authentication
from knox.views import LoginView as KnoxLoginView
import gspread
#USER
class register(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": user_serializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })
class loginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(loginAPI, self).post(request, format=None)
#PUBS
class get_create_pub(generics.GenericAPIView , mixins.CreateModelMixin , mixins.ListModelMixin):
    serializer_class = pub_serializer
    queryset=pub.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    def get(self,request):
        return self.list(request)
    def post(self,request):
        if request.data["user_type"]!= "ensignant" and request.data["user_type"]!= "entreprise" and request.data["type"]=="theme":
            return Response({"error":"this type of users can't create a theme"})
        return self.create(request)
    
class get_recomanded_post(APIView):
    def get(self , request):
        import numpy as np
        # Load the similarity matrix
        similarity_matrix = np.load('models/similarity_matrix.pkl',allow_pickle=True)
        index = 0
        # Sort the similarity scores in descending order
        similarity_scores = list(enumerate(similarity_matrix[index]))
        sorted_sim_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)
        # Get the top 5 most similar documents
        top = sorted_sim_scores[1:]
        #get all objects 
        objects=[]
        for index, score in top:
            try : 
                objects.append(pub.objects.get(id=index))
            except pub.DoesNotExist :
                pass
        serializer= pub_serializer(objects , many=True )
        return JsonResponse(serializer.data , status = 200, safe=False)
class delete_update_pub(generics.GenericAPIView , mixins.DestroyModelMixin , mixins.UpdateModelMixin):
    permission_classes = [permissions.IsAuthenticated]
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
    permission_classes = [permissions.IsAuthenticated]
    def get(self,request):
        return self.list(request)
class get_questions(generics.GenericAPIView , mixins.ListModelMixin):
    serializer_class = pub_serializer
    permission_classes = [permissions.IsAuthenticated]
    queryset=pub.objects.filter(type ="question")
    def get(self,request):
        return self.list(request)
class postuler(APIView):#send the id of the pub 
    def post(self, request , id):
        try :
            user_ineracted = student.objects.get(user = request.data['user'])
            if user_ineracted.Role == "None":
                return Response({"error":"il faut etre un monome ou un binome pour postuler"})
            elif user_ineracted.Role == "monome":
                ensignant_notified = ensignant.objects.get(user= pub.objects.get(id=id).user)
                titel =  user_ineracted.user.username+" a postuler au theme intituler "+ pub.objects.get(id=id).main_text 
                new_notification =  notification.objects.create(user = ensignant_notified.user,id_pub=pub.objects.get(id=id) , titel = titel ,notification_type = "notification_ensignant" , send_from=user_ineracted.user )
                new_notification.save()
                return HttpResponse(status = 200)
            elif user_ineracted.Role == "Binome":
                binome_notified = student.objects.get(user=student.objects.get(user=user_ineracted.user).binome)
                titel =  user_ineracted.user.username+" a demender de postuler au theme intituler "+ pub.objects.get(id=id).main_text 
                new_notification =  notification.objects.create(user = binome_notified.user ,id_pub = pub.objects.get(id=id) , titel = titel,notification_type = "notification_binome" )
                new_notification.save()
                return HttpResponse(status = 200)
        except Exception as e : 
            return Response({"error":"error occured"})
class notification_API(APIView):
    def get(self , request,id):
        user = User.objects.get(id=id)
        notifications =  notification.objects.filter(user = user).order_by('date')
        serializer = notification_serializer(notifications, many =True )
        return JsonResponse(serializer.data , safe= False ,status = 200)
    def post(self , request, id ):  #send the id of a notification 
        notif =  notification.objects.get(id=id)
        pub_sep = pub.objects.get(id = request.data['id_pub'])
        
        if(notif.notification_type == "notification_binome"):
            if request.data['status']=="Accepted":
                titel =  User.objects.get(id=request.data['user']).username +  " and "+ User.objects.get(id=request.data['binome']).username + "a demender de postuler au theme intituler "+ pub_sep.main_text
                new_notification = notification.objects.create(user = pub_sep.user ,id_pub=pub_sep, titel = titel ,notification_type = "notification_ensignant", send_from = User.objects.get(id=request.data['user']) )
                new_notification.save()
                notif.delete()
                return HttpResponse("la demende a etait envoyer", status =200)
        elif(notif.notification_type == "notification_ensignant"):
            if request.data['status']=="Accepted":
                titel = notif.user.username + " a accepter votre demende de postuler au theme intituler "+ pub_sep.main_text
                new_notification1 = notification.objects.create(user =notif.send_from  ,id_pub=pub_sep, titel = titel ,notification_type = "notification_ensignant", send_from =notif.user )
                new_notification1.save()
                binome= student.objects.get(user=notif.send_from)
                new_notification2 = notification.objects.create(user = binome.binome ,id_pub=pub_sep, titel = titel ,notification_type = "notification_ensignant", send_from =notif.user)
                new_notification2.save()
                user_=notif.user   #used to get the other notification after deleting
                notif.delete()
                #deleting all other same pub notification 
                notification.objects.filter(id_pub=pub_sep,user=pub_sep.user).delete()
                #get all other notification 
                notifications = notification.objects.filter(user=user_)
                return JsonResponse(data = notifications, safe=False , status = 204)
#PROFILES _Students 
class profile_student_api(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self,request, id):
        try:
            snippets = student.objects.get(id=id)
            serializer = student_serializer(snippets)
            return JsonResponse(serializer.data)
        except :
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self ,request, id):
        snippets = student.objects.get(id=id)
        snippets.delete()
        serializer=student_serializer(snippets)
        return JsonResponse(serializer.data, status=201)
    def put(self , request , id ):
        altred_obj=student.objects.get(id=id)
        serializer = student_serializer(altred_obj , data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data , status=200,safe=False)
        return JsonResponse(serializer.data , status=404,safe=False)
class create_get_student_profile(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get( self , request ):
        all_profiles= student.objects.all()
        serializer=student_serializer(all_profiles,many=True)
        return JsonResponse(serializer.data,safe=False, status=200)
    def post(self, request, format=None):
        if request.data['Role']== "Binome" and request.data['user'] == request.data['binome']:
            return Response({"error":"vous devez choisire un autre binome"},status=404)
        serializer = student_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#PROFILES_ensignants
class profile_ensignats_api(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self,request, id):
        try:
            snippets = ensignant.objects.get(id=id)
            serializer = ensignant_serializer(snippets)
            return JsonResponse(serializer.data)
        except :
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self ,request, id ):
        snippets = ensignant.objects.get(id=id)
        snippets.delete()
        serializer=ensignant_serializer(snippets)
        return JsonResponse(serializer.data, status=201)
    def put(self , request , id ):
        altred_profile= ensignant.objects.get(id=id)
        serializer = ensignant_serializer(altred_profile , data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data , status=200)
        return JsonResponse(serializer.data , status=404)
class create_get_ensignant_profile(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self , request):
        all_profiles= ensignant.objects.all()
        serializer=ensignant_serializer(all_profiles,many=True)
        return JsonResponse(serializer.data,safe=False, status=200)
    def post(self, request, format=None):
        serializer = ensignant_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#PROFILES_company
class get_create_company_profile(generics.GenericAPIView , mixins.CreateModelMixin , mixins.ListModelMixin):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = company_serializer
    queryset=company.objects.all()
    def get(self,request):
        return self.list(request)
    def post(self,request):
        return self.create(request)
class delete_update_company_profile_api(generics.GenericAPIView , mixins.DestroyModelMixin , mixins.UpdateModelMixin):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = company_serializer
    queryset=company.objects.all()
    lookup_field="id"
    def get(self , request , id ):#hadi jsp wchbiha 
        try:
            snippets = company.objects.get(id=id)
            serializer = company_serializer(snippets)
            return JsonResponse(serializer.data)
        except :
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request,id):
        return self.destroy(request,id)
    def put(self,request,id):
        return self.update(request,id)
#COMMENT 
class create_commentAPI(generics.GenericAPIView , mixins.CreateModelMixin):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class=comment_serializer
    queryset=comment.objects.all()
    def post(self,request,id):
        return self.create(request)
class getposts_commentAPI(APIView):
    permission_classes = [permissions.IsAuthenticated]
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
    pass
#pdf sending
from fillpdf import fillpdfs
class generate_fiche_pfe(APIView):
    def post(self , request):
        if(request.data['niveau']=="L3"):
            if request.data['choix']=="ACAD":
                choix = "Choix4"
            elif request.data['choix']=="ISIL":
                choix = "Choix5"
            elif request.data['choix']=="GTR":
                choix = "Choix6"
            data_dict = {'Groupe112': choix, 'Case à cocher104': request.data['gl'],
                     'Case à cocher108': request.data['archi'],'Case à cocher105': request.data['reseau'],
                     'Case à cocher109': request.data['computer_vision'], 'Case à cocher106': request.data['ai'],
                     'Case à cocher110': request.data['info_th'], 'Case à cocher107': request.data['web'],
                     
                     'Texte86': request.data['nom1'], 'Texte87': request.data['nom1_matricule'],
                     'Texte88': request.data['nom1_email'], 'Texte89': request.data['nom1_tel'],
                     
                     'Texte90': request.data['nom2'],'Texte91': request.data['nom2_matricule'],
                     'Texte92': request.data['nom2_email'], 'Texte93': request.data['nom2_tel'],
                     
                     'Texte94': request.data['nom1_encadreur'], 'Texte95': request.data['nom1_encGrade'],
                     'Texte96': request.data['nom1_encemail'],
                     
                     'Texte97': request.data['nom2_encadreur'], 'Texte98':  request.data['nom2_encGrade'],
                     'Texte99': request.data['nom2_encemail'],
                     
                     'Texte100': '',
                     'Texte101': '', 'Texte102': '', 'Texte85': request.data['titre'], 'Texte81': request.data['resume'],
                     'Texte82': request.data['mot_cle'], 'Texte83': request.data['plan']}
            fillpdfs.write_fillable_pdf("fiches/fiche_PFE.pdf","fiches/temp.pdf",data_dict)
            themes=themes_to_validate.objects.create(file="fiches/temp.pdf",specialite=request.data['specialite'])
            themes.save()
            return HttpResponse("fichier envoyer a le responsable pour le valider")
        
        elif request.data['niveau']=="M2":
            if request.data['choix']=="RSD":
                choix = "Choix1"
            elif request.data['choix']=="IL":
                choix = "Choix2"
            elif request.data['choix']=="IV":
                choix = "Choix3"
            elif request.data['choix']=="MIND":
                choix = "Choix4"
            elif request.data['choix']=="SII":
                choix = "Choix5"
            elif request.data['choix']=="SSI":
                choix = "Choix6"
            elif request.data['choix']=="BioInfo":
                choix = "Choix7"
            if request.data['organisme']=="Interne":
                organisme ="Choix1"
            if request.data['organisme']=="Externe":
                organisme ="Choix2"
            data_dict= {'Groupe103': choix, 'Case à cocher104': request.data['gl'], 'Case à cocher108': request.data['archi'], 
             'Case à cocher105': request.data['reseau'], 'Case à cocher109': request.data['computer_vision'],
             'Case à cocher106':request.data['ai'] ,
             'Case à cocher110': request.data['info_th'], 'Case à cocher107': request.data['web/app'],
             'Case à cocher111': request.data['BioInfo'],
             
             'Texte86': request.data['nom1'], 'Texte87': request.data['nom1_matricule'],
             'Texte88': request.data['nom1_email'],'Texte89': request.data['nom1_tel'],
             
             'Texte90': request.data['nom2'], 'Texte91':  request.data['nom2_matricule'],
             'Texte92': request.data['nom2_email'], 'Texte93': request.data['nom2_tel'],
             
             'Texte94': request.data['nom1_encadreur'], 'Texte95': request.data['nom1_encGrade'], 
             'Texte96': request.data['nom1_encemail'],
             
             'Texte97': request.data['nom2_encadreur'],'Texte98':  request.data['nom2_encGrade'],
             'Texte99': request.data['nom1_encemail'],
             
             'Groupe112': organisme , 'Texte100': request.data['raison_social'], 
             'Texte101': request.data['service'], 'Texte102':"informatique",
             'Texte85': request.data['titre'], 'Texte81': request.data['resume'],
             'Texte82': request.data['mot_cle'], 'Texte83': request.data['plan'],
             'Texte84': request.data['bibliotheques']}
            fillpdfs.write_fillable_pdf("fiches/fiche_PFE_Matser.pdf","fiches/temp2.pdf",data_dict)
            themes=themes_to_validate.objects.create(file="fiches/temp2.pdf",specialite=request.data['specialite'])
            themes.save()
            return HttpResponse("fichier envoyer a le responsable pour le valider")
class themes_validation(APIView): #hna tatkhdam el comission
    def get(self , request , id): #lazm yb3at el id ta3 el responsable hna 
        try: 
            the_user = resp_epcialit.objects.get(id=id)
            all_themes= themes_to_validate.objects.filter(specialite=the_user.specialite)
            serializer = themes_ToValidate_serializer(all_themes,many=True)
            return JsonResponse(serializer.data, safe=False , status = 200)
        except User.DoesNotExist : 
            return Response({"error":"cette utilisateur n'exist pas"})
    def post(self , request , id ): #cree une comission / hna yb3at el id ta3 theme to validate
        theme =  themes_to_validate.objects.get(id=id)
        if request.data['ens1']== request.data['ens2'] or request.data['ens1']==request.data['ens3'] or request.data['ens2']==request.data['ens3']:
            return Response({"error":"les ensignant doivent etre different"})
        comission =comission_validation.objects.create(ensignant1=ensignant.objects.get(id=request.data['ens1']),ensignant2=ensignant.objects.get(id=request.data['ens2']),ensignant3=ensignant.objects.get(id=request.data['ens3']), theme = theme)
        comission.save()
        serializer = comission_serializer(comission)
        return JsonResponse(serializer.data , safe = False , status =200) 
class accpete_refuse_themes(APIView):
    def post(self , request, id  ): #hna yb3at el id ta3 el theme to validate
        try :  
            theme = themes_to_validate.objects.get(id=id)
            if request.data["status"]=="Accepted":
                validated_theme=validated_themes.objects.create(file =  theme.file , specialite=request.data["specialite"], status = "Accepted")
                validated_theme.save()
                theme.delete()
                
            elif request.data["status"]=="Refused":
                validated_theme=validated_themes.objects.create(file =  theme.file , specialite=request.data["specialite"], status = "Rejected")
                validated_theme.save()
                theme.delete()

            add_theme_to_sheet(theme.file,request.data['status'],request.data['niveau'])
            return HttpResponse("theme added")
        except themes_to_validate.DoesNotExist:
            return Response({"error":"cette theme n'existe pas"})
def add_theme_to_sheet(file,status,niveau):
        sa=gspread.service_account(filename='service_account.json')
        sh = sa.open("List PFEs")
        wks = sh.worksheet("IA")
        data = fillpdfs.get_form_fields(file)
        choix =  ''
        type = ''
        nom_prenom1= data.get('Texte86')
        nom_prenom2= data.get('Texte90')
        titre = data.get('Texte85')
        promoteur1= data.get('Texte94')
        promoteur2 = data.get('Texte97')
        organisme ='jsp'
        validation = status
        n_commssion='idk'
        com_suiv='idk'
        Email ='idk'
        matricule1 =data.get('Texte87')
        email1 =data.get('Texte88')
        matricule2=data.get('Texte91')
        email2=data.get('Texte92')
        
        if niveau == "M2":
            organisme = data.get("Groupe112")
            choix = data.get("Groupe103")
            if choix == "Choix4" or choix == "Choix2" or choix == "Choix5" or choix == "Choix1":
                wks = sh.worksheet("SIQ")
        elif data.get("Groupe112") == "Choix6" or data.get("Groupe103")=="Choix5":
            wks = sh.worksheet("SIQ")
        
        values = [choix,1,type, nom_prenom1,nom_prenom2,titre,promoteur1,promoteur2, organisme,validation,
              n_commssion,com_suiv,Email,matricule1,email1,matricule2,email2] #nbdal el data (jbd data mal file)
        wks.insert_row(values,2)
class jury_managing(APIView):
    def post(slef , request, id): #id ta3 theme
        try:
            memeber1=ensignant.objects.get(user=User.objects.get(username=request.data['memeber1']))
            memeber2=ensignant.objects.get(user=User.objects.get(username=request.data['memeber2']))
            president=ensignant.objects.get(user=User.objects.get(username=request.data['president']))
            theme = validated_themes.objects.get(id=id)
            nom_encadreur = fillpdfs.get_form_fields(theme.file)["Texte95"]
            if memeber1 == memeber2 or memeber1 == president or memeber2 == president:
                return Response({"error":"vous devez choisire des differents ensignants"})
            elif jury.objects.get(themes=theme):
                return Response({"error":"ce theme a deja une jury"})
            elif memeber1.user.username == nom_encadreur  or memeber2.user.username == nom_encadreur or president.user.username == nom_encadreur:
                return Response({"error":"un memebre de jury doit pas etre un encadreur de meme theme"})
            
            la_jury = jury.objects.create(m_jury_st=memeber1,jury_nd=memeber2,president=president,themes=theme)
            la_jury.save()
            serializer=jury_serializer(la_jury,many=False) 
            return JsonResponse(data=serializer.data,status=200)
        except ensignant.DoesNotExist or User.DoesNotExist:
            return Response({"error":"cette utilisateur n'existe pas"})
    def get(self, request , id ): #id ta3 theme / naffichiw la jury ta3 had el theme
        theme=validated_themes.objects.get(id=id)
        jury_of_theme = jury.objects.get(themes=theme)
        titre = fillpdfs.get_form_fields(theme.file)["Texte85"]
        response = {
           "theme": titre,
           "jury 1 ":{"username":jury_of_theme.m_jury_st.user.get_username() , "email":jury_of_theme.m_jury_st.user.get_email_field_name()},
           "jury 2 ":{"username":jury_of_theme.jury_nd.user.get_username() , "email":jury_of_theme.jury_nd.user.get_email_field_name()},
           "president":{"username":jury_of_theme.president.user.get_username() , "email":jury_of_theme.president.user.get_email_field_name()},
        }
        return JsonResponse(response , safe=False, status = 200)
        