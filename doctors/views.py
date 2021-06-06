from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Feature, User, Patient, Doctor, Event, Instance, Symptom, Diagnostic, Disease, Reference
from datetime import datetime
from random import randint
import requests
import json
import hashlib

base_url = "http://api.endlessmedical.com/v1/dx"
url_ext = "/InitSession"
url_ext2 = "/AcceptTermsOfUse"
url_ext3 = "/UpdateFeature"
url_ext4 = "/Analyze"
url = base_url+url_ext
url2 = base_url+url_ext2
url3 = base_url+url_ext3
url4 = base_url+url_ext4
headers = {
    'x-rapidapi-key': "b663bf0fbbmshdedd777ff7e87c8p12da5bjsn9e348029b6f7",
    'x-rapidapi-host': "endlessmedicalapi1.p.rapidapi.com"
    }

def analyze(symptoms):
    # Pegar o Session ID
    response = requests.request("GET", url, headers=headers)
    resp = json.loads(response.text)
    session_ID = resp["SessionID"]
    # Pegar os Termos de Uso
    querystring = {"passphrase":"I have read, understood and I accept and agree to comply with the Terms of Use of EndlessMedicalAPI and Endless Medical services. The Terms of Use are available on endlessmedical.com","SessionID":session_ID}
    requests.request("POST", url2, headers=headers, params=querystring)
    # Fazer POST dos sintomas
    for symptom in symptoms:
        querystring2 = {"SessionID":session_ID,"value":symptom.value,"name":symptom.name}
        requests.request("POST", url3, headers=headers, params=querystring2)  
    # Fazer a análise
    querystring3 = {"SessionID":session_ID}
    response_final = requests.request("GET", url4, headers=headers, params=querystring3)
    diseases = json.loads(response_final.text)
    return diseases

def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end) 

def encrypt_string(hash_string):
    sha_signature = \
        hashlib.sha256(hash_string.encode()).hexdigest()
    return sha_signature

def load_instances(user_id):
    all_instances = Instance.objects.all().filter(user=user_id)
    symptoms = Symptom.objects.all()
    all_symptoms = []
    for instance in all_instances:
        for symptom in symptoms:
            if int(instance.id) == int(symptom.instance.id):
                all_symptoms.append(symptom)       
    features = Feature.objects.all().filter(id=1).first().features
    all_features = features.split(",")
    all_features = sorted(all_features, key=str.lower)
    print(all_symptoms)
    return all_instances, all_symptoms, all_features

def load_doc(user_id,diag_id):
    querydiag = Diagnostic.objects.all().filter(id=diag_id).first()
    diseases = Disease.objects.all().filter(diagnostic=querydiag)
    main_disease_val = 0.0
    main_disease = 0
    for disease in diseases:
        if float(disease.probability) > float(main_disease_val):
            main_disease = disease.name
            main_disease_val = disease.probability
    all_doctors = []
    doctors = Doctor.objects.all()
    for doctor in doctors:
        especialidades = doctor.diseases.split(",")
        for spec in especialidades:
            if main_disease==spec:
                all_doctors.append(doctor)
    return all_doctors

def index(request, login=False):
    if request.method == 'POST':
        if login==False:
            usertype = request.POST.get('usertype')
            name = request.POST.get('nome')
            age = request.POST.get('idade')
            sex = request.POST.get('sexo')
            email = request.POST.get('email')
            password = request.POST.get('senha')
            if usertype == "Médico":
                spec = request.POST.get('especialidade')
                additional = request.POST.get('adicional')
            else:
                job = request.POST.get('profissao')
            #try:
            #    print(request.FILES['filename'].name)
            #    image_check = True
            #except:
            #    image_check = False
            if name == "":
                alert = "warning"
                alert_message = "Favor Preencher o Campo de Nome" 
                return render(request, 'doctors/index.html', {'alert':alert,'alertmessage':alert_message})  
            elif age == "":
                alert = "warning"
                alert_message = "Favor Preencher o Campo de Idade" 
                return render(request, 'doctors/index.html', {'alert':alert,'alertmessage':alert_message})
            elif sex == "":
                alert = "warning"
                alert_message = "Favor Preencher o Campo de Sexo" 
                return render(request, 'doctors/index.html', {'alert':alert,'alertmessage':alert_message}) 
            elif usertype == "Médico" and  spec =="":
                alert = "warning"
                alert_message = "Favor Preencher o Campo de Especialidade" 
                return render(request, 'doctors/index.html', {'alert':alert,'alertmessage':alert_message})
            elif usertype == "Médico" and  additional =="":
                alert = "warning"
                alert_message = "Favor Preencher o Campo de Doenças" 
                return render(request, 'doctors/index.html', {'alert':alert,'alertmessage':alert_message}) 
            elif usertype == "Paciente" and  job =="":
                alert = "warning"
                alert_message = "Favor Preencher o Campo de Profissão" 
                return render(request, 'doctors/index.html', {'alert':alert,'alertmessage':alert_message}) 
            elif email == "":
                alert = "warning"
                alert_message = "Favor Preencher o Campo de Email" 
                return render(request, 'doctors/index.html', {'alert':alert,'alertmessage':alert_message}) 
            elif password == "":
                alert = "warning"
                alert_message = "Favor Preencher o Campo de Senha" 
                return render(request, 'doctors/index.html', {'alert':alert,'alertmessage':alert_message})               
            if (User.objects.all().filter(name=name).exists()==False):
                if (User.objects.all().filter(email=email).exists()==False):
                    if len(password)>=8:
                        passencrypted = encrypt_string(password)
                        #if image_check == True:
                            #image = request.FILES['filename']
                        newuser = User(name=name,age=age,sex=sex,email=email,password=passencrypted)
                        newuser.save()
                        newuser.encryptid = encrypt_string(str(newuser.id))
                        #else:
                        #    newuser = User(name=name,age=age,sex=sex,email=email,password=password)
                        newuser.save()
                        if usertype == "Médico":
                            spec = request.POST.get('especialidade')
                            additional = request.POST.get('adicional')
                            newdoc = Doctor(user=newuser,spec=spec,diseases=additional,nota="5")
                            newdoc.save()
                        else:
                            job = request.POST.get('profissao')
                            newpatient = Patient(user=newuser,job=job)
                            newpatient.save()
                        newuser.save()
                        return redirect(reverse('menu', kwargs={"user_id": str(newuser.encryptid)}))
                    else:
                        alert = "warning"
                        alert_message = "Senha Possui Menos de 8 Caracteres" 
                        return render(request, 'doctors/index.html', {'alert':alert,'alertmessage':alert_message})          
                else:
                    alert = "warning"
                    alert_message = "Email Já Utilizado" 
                    return render(request, 'doctors/index.html', {'alert':alert,'alertmessage':alert_message})  
            else:
                alert = "warning"
                alert_message = "Usuário Já Existe" 
                return render(request, 'doctors/index.html', {'alert':alert,'alertmessage':alert_message})
        else:
            email = request.POST.get('email')
            pass_receive = request.POST.get('senha')
            if (User.objects.all().filter(email=email).exists()):
                passencrypted = encrypt_string(pass_receive)
                password_full = User.objects.all().filter(email=email).first().password 
                if (passencrypted==str(password_full)):
                    return redirect(reverse('menu', kwargs={"user_id": str(User.objects.all().filter(email=email).first().encryptid)}))
                else:
                    alert = "warning"
                    alert_message = "Senha Incorreta" 
                    return render(request, 'doctors/index.html', {'alert':alert,'alertmessage':alert_message})
            else:
                alert = "warning"
                alert_message = "Usuário Inválido" 
                return render(request, 'doctors/index.html', {'alert':alert,'alertmessage':alert_message})                 
    else:
        alert = "default"
        alert_message = "" 
        return render(request, 'doctors/index.html', {'alert':alert,'alertmessage':alert_message})

def about(request,login=False): 
    if request.method == 'POST':
        if login==False:
            usertype = request.POST.get('usertype')
            name = request.POST.get('nome')
            age = request.POST.get('idade')
            sex = request.POST.get('sexo')
            email = request.POST.get('email')
            password = request.POST.get('senha')
            if usertype == "Médico":
                spec = request.POST.get('especialidade')
                additional = request.POST.get('adicional')
            else:
                job = request.POST.get('profissao')
            #try:
            #    print(request.FILES['filename'].name)
            #    image_check = True
            #except:
            #    image_check = False
            if name == "":
                alert = "warning"
                alert_message = "Favor Preencher o Campo de Nome" 
                return render(request, 'doctors/about.html', {'alert':alert,'alertmessage':alert_message})  
            elif age == "":
                alert = "warning"
                alert_message = "Favor Preencher o Campo de Idade" 
                return render(request, 'doctors/about.html', {'alert':alert,'alertmessage':alert_message})
            elif sex == "":
                alert = "warning"
                alert_message = "Favor Preencher o Campo de Sexo" 
                return render(request, 'doctors/about.html', {'alert':alert,'alertmessage':alert_message}) 
            elif usertype == "Médico" and  spec =="":
                alert = "warning"
                alert_message = "Favor Preencher o Campo de Especialidade" 
                return render(request, 'doctors/about.html', {'alert':alert,'alertmessage':alert_message})
            elif usertype == "Médico" and  additional =="":
                alert = "warning"
                alert_message = "Favor Preencher o Campo de Doenças" 
                return render(request, 'doctors/about.html', {'alert':alert,'alertmessage':alert_message}) 
            elif usertype == "Paciente" and  job =="":
                alert = "warning"
                alert_message = "Favor Preencher o Campo de Profissão" 
                return render(request, 'doctors/about.html', {'alert':alert,'alertmessage':alert_message}) 
            elif email == "":
                alert = "warning"
                alert_message = "Favor Preencher o Campo de Email" 
                return render(request, 'doctors/about.html', {'alert':alert,'alertmessage':alert_message}) 
            elif password == "":
                alert = "warning"
                alert_message = "Favor Preencher o Campo de Senha" 
                return render(request, 'doctors/about.html', {'alert':alert,'alertmessage':alert_message})               
            if (User.objects.all().filter(name=name).exists()==False):
                if (User.objects.all().filter(email=email).exists()==False):
                    if len(password)>=8:
                        #if image_check == True:
                        #image = request.FILES['filename']
                        passencrypted = encrypt_string(password)
                        newuser = User(name=name,age=age,sex=sex,email=email,password=passencrypted)
                        newuser.save()
                        newuser.encryptid = encrypt_string(str(newuser.id))
                        #else:
                        #    newuser = User(name=name,age=age,sex=sex,email=email,password=password)
                        newuser.save()
                        if usertype == "Médico":
                            spec = request.POST.get('especialidade')
                            additional = request.POST.get('adicional')
                            newdoc = Doctor(user=newuser,spec=spec,diseases=additional,nota="5")
                            newdoc.save()
                        else:
                            job = request.POST.get('profissao')
                            newpatient = Patient(user=newuser,job=job)
                            newpatient.save()
                        newuser.save()
                        return redirect(reverse('menu', kwargs={"user_id": str(newuser.encryptid)}))
                    else:
                        alert = "warning"
                        alert_message = "Senha Possui Menos de 8 Caracteres" 
                        return render(request, 'doctors/about.html', {'alert':alert,'alertmessage':alert_message})                 
                else:
                    alert = "warning"
                    alert_message = "Usuário Inválido" 
                    return render(request, 'doctors/about.html', {'alert':alert,'alertmessage':alert_message})          
            else:
                alert = "warning"
                alert_message = "Usuário Já Existe" 
                return render(request, 'doctors/about.html', {'alert':alert,'alertmessage':alert_message})
        else:
            email = request.POST.get('email')
            pass_receive = request.POST.get('senha')
            if (User.objects.all().filter(email=email).exists()):
                passencrypted = encrypt_string(pass_receive)
                password_full = User.objects.all().filter(email=email).first().password 
                if (passencrypted==str(password_full)):
                    return redirect(reverse('menu', kwargs={"user_id": str(User.objects.all().filter(email=email).first().encryptid)}))
                else:
                    alert = "warning"
                    alert_message = "Senha Incorreta" 
                    return render(request, 'doctors/about.html', {'alert':alert,'alertmessage':alert_message})
            else:
                alert = "warning"
                alert_message = "Usuário Inválido"                      
                return render(request, 'doctors/about.html', {'alert':alert,'alertmessage':alert_message})
    else:
        alert = "default"
        alert_message = ""     
        return render(request, 'doctors/about.html', {'alert':alert,'alertmessage':alert_message})
        
def menu(request,user_id,type=""):
    if request.method == 'GET':
        usertype = None
        user = User.objects.all().filter(encryptid=user_id).first()
        thisuser = Doctor.objects.all().filter(user=user).first()
        usertype = "Doctor"
        if thisuser == None:
            thisuser = Patient.objects.all().filter(user=user).first()
            usertype = "Patient"
        if usertype == "Patient":
            return render(request, 'doctors/patient/menu.html', {'patient':thisuser,'id':user_id})
        else:
            return render(request, 'doctors/doctor/menu.html', {'doctor':thisuser,'id':user_id})
    else:
        usertype = None
        user = User.objects.all().filter(encryptid=user_id).first()
        thisuser = Doctor.objects.all().filter(user=user).first()
        usertype = "Doctor"
        if thisuser == None:
            thisuser = Patient.objects.all().filter(user=user).first()
            usertype = "Patient"
        if type == "user":
            name = request.POST.get('nome')
            age = request.POST.get('idade')
            sex = request.POST.get('sexo')
            email = request.POST.get('email')
            if (name != "") and (user.name != name):
                user.name = name
            if (age != "") and (str(user.age) != str(age)):
                user.age = age
            if (sex != "") and (user.sex != sex):
                user.sex = sex
            if (email != "") and (user.email != email):
                user.email = email
            user.save() 
        else: 
            oldpass = request.POST.get('senha')
            newpass1 = request.POST.get('senha2')
            newpass2 = request.POST.get('senha3')
            oldencrypt = encrypt_string(oldpass)
            if (user.password != oldencrypt)or(oldpass==""):
                alert = "warning"
                alert_message = "Senha Antiga Incorreta"
            elif (newpass1 =="")or(newpass2 ==""):
                alert = "warning"
                alert_message = "Favor Preencher Senha Nova"     
            elif (newpass1!=newpass2):
                alert = "warning"
                alert_message = "Valores Diferentes da Senha Nova"     
            else:
                newencrypt = encrypt_string(newpass1)
                user.password = newencrypt 
                user.save()
                alert = "default"
                alert_message = ""
            if usertype == "Patient":     
                return render(request, 'doctors/patient/menu.html', {'patient':thisuser,'id':user_id,'alert':alert,'alertmessage':alert_message})
            else:
                return render(request, 'doctors/doctor/menu.html', {'doctor':thisuser,'id':user_id,'alert':alert,'alertmessage':alert_message})            
        if usertype == "Patient":
            job = request.POST.get('profissao')
            if (job!="")and(job!=None) and (thisuser.job != job):
                thisuser.job = job   
                thisuser.save()
            return render(request, 'doctors/patient/menu.html', {'patient':thisuser,'id':user_id})
        else:
            spec = request.POST.get('especialidade')
            diseases = request.POST.get('adicional')
            if thisuser.spec != spec:
                thisuser.spec = spec
            if thisuser.diseases != diseases:
                thisuser.diseases = diseases    
            thisuser.save() 
            return render(request, 'doctors/doctor/menu.html', {'doctor':thisuser,'id':user_id})        

def diagnostic(request,user_id,instance_id=0,diag_id=0,check=False,patient_id=""):
    if request.method == 'GET':
        if check == False:
            usertype = None
            user = User.objects.all().filter(encryptid=user_id).first()
            thisuser = Doctor.objects.all().filter(user=user).first()
            usertype = "Doctor"
            if thisuser == None:
                thisuser = Patient.objects.all().filter(user=user).first()
                usertype = "Patient"     
            queryinstances = Instance.objects.all().filter(user=user)     
            return render(request, 'doctors/patient/diagnostic.html', {'patient':thisuser,'id':user_id, 'instances':queryinstances})
        else:
            usertype = None
            user = User.objects.all().filter(encryptid=user_id).first()
            thisuser = Doctor.objects.all().filter(user=user).first()
            usertype = "Doctor"
            if thisuser == None:
                thisuser = Patient.objects.all().filter(user=user).first()
                usertype = "Patient"
            diag = Diagnostic.objects.all().filter(id=int(diag_id)).first()
            all_symptoms = Symptom.objects.all().filter(instance=diag.instance)     
            diseases_all = Disease.objects.all().filter(diagnostic=diag)    
            if patient_id == "":       
                return render(request, 'doctors/patient/diagnosticshow.html', {'patient':thisuser,'id':user_id, 'diseases':diseases_all, 'instance':diag.instance, 'symptoms':all_symptoms})
            else:
                thispatient = Patient.objects.all().filter(id=patient_id).first()
                return render(request, 'doctors/doctor/diagnosticshow.html', {'doctor':thisuser,'patient':thispatient,'id':user_id, 'diseases':diseases_all, 'instance':diag.instance, 'symptoms':all_symptoms})    
    else:       
        usertype = None
        user = User.objects.all().filter(encryptid=user_id).first()
        thisuser = Doctor.objects.all().filter(user=user).first()
        usertype = "Doctor"
        if thisuser == None:
            thisuser = Patient.objects.all().filter(user=user).first()
            usertype = "Patient"      
        queryinstance = Instance.objects.all().filter(id=instance_id).first()
        all_symptoms = Symptom.objects.all().filter(instance=queryinstance)
        datenow = datetime.today().strftime('%d/%m/%Y-%H:%M:%S')          
        diseases = analyze(all_symptoms)
        count = 0
        for i in range(len(diseases["Diseases"])):
            key = list(diseases["Diseases"][i].keys())[0]
            value = "{:.2f}".format(float(list(diseases["Diseases"][i].values())[0])*100)
            if count <=4:
                if count == 0:
                    diag = Diagnostic(user=thisuser.user,instance=queryinstance,date=datenow,mainname=key,mainprob=value)
                    diag.save()
                    disease = Disease(diagnostic=diag,name=key,probability=value,alert="red")
                    disease.save()
                elif count < 2:
                    disease = Disease(diagnostic=diag,name=key,probability=value,alert="red")
                    disease.save()
                elif count >= 2 and count < 4:  
                    disease = Disease(diagnostic=diag,name=key,probability=value,alert="yellow")
                    disease.save()
                else:
                    disease = Disease(diagnostic=diag,name=key,probability=value,alert="green")
                    disease.save()    
            count += 1
        diseases_all = Disease.objects.all().filter(diagnostic=diag)
        queryinstance.status = "Closed"
        queryinstance.save()                
        return render(request, 'doctors/patient/diagnosticshow.html', {'patient':thisuser,'id':user_id, 'diseases':diseases_all, 'instance':queryinstance, 'symptoms':all_symptoms})

def instances(request,user_id, patient_id=""):
    if request.method == 'GET':
        usertype = None
        user = User.objects.all().filter(encryptid=user_id).first()
        thisuser = Doctor.objects.all().filter(user=user).first()
        usertype = "Doctor"
        if thisuser == None:
            thisuser = Patient.objects.all().filter(user=user).first()
            usertype = "Patient"
        if patient_id == "":        
            all_instances = Instance.objects.all().filter(user=user)    
            features = Feature.objects.all().filter(id=1).first().features
            all_features = features.split(",")
            all_features = sorted(all_features, key=str.lower)
            return render(request, 'doctors/patient/instances.html', {'patient':thisuser, 'id':user_id, 'features': all_features,'listinst':all_instances})
        else:
            thispatient = Patient.objects.all().filter(id=patient_id).first()
            all_instances = Instance.objects.all().filter(user=thispatient.user)    
            return render(request, 'doctors/doctor/allinstances.html', {'doctor':thisuser, 'id':user_id, 'patient': thispatient,'listinst':all_instances})
    else:
        usertype = None
        user = User.objects.all().filter(encryptid=user_id).first()
        thisuser = Doctor.objects.all().filter(user=user).first()
        usertype = "Doctor"
        if thisuser == None:
            thisuser = Patient.objects.all().filter(user=user).first()
            usertype = "Patient"
        # Criar nova instancia
        datenow = datetime.today().strftime('%d/%m/%Y-%H:%M:%S')
        instname = "ID"+str(random_with_N_digits(8))
        newinstance = Instance(user=thisuser.user,name=instname,date=datenow,status="Open")
        newinstance.save()
        # Adicionando os sintomas
        feature = request.POST.get('default-select')
        value = request.POST.get('valor')
        newsymptom = Symptom(instance=newinstance,name=feature,value=value)
        newsymptom.save()
        feature = request.POST.get('default-select2')
        value = request.POST.get('valor2')
        newsymptom = Symptom(instance=newinstance,name=feature,value=value)
        newsymptom.save()
        feature = request.POST.get('default-select3')
        value = request.POST.get('valor3')
        newsymptom = Symptom(instance=newinstance,name=feature,value=value)
        newsymptom.save()
        all_instances = Instance.objects.all().filter(user=user)    
        features = Feature.objects.all().filter(id=1).first().features
        all_features = features.split(",")
        all_features = sorted(all_features, key=str.lower)
        return render(request, 'doctors/patient/instances.html', {'patient':thisuser, 'id':user_id, 'features': all_features,'listinst':all_instances})

def editinstance(request,user_id,instance,symptom="",type=0,patient_id=""):
    if request.method == "GET":
        usertype = None
        user = User.objects.all().filter(encryptid=user_id).first()
        thisuser = Doctor.objects.all().filter(user=user).first()
        usertype = "Doctor"
        if thisuser == None:
            thisuser = Patient.objects.all().filter(user=user).first()
            usertype = "Patient"
        thisinstance = Instance.objects.all().filter(id=int(instance)).first()
        symptoms = Symptom.objects.all().filter(instance=int(instance))
        if patient_id=="":
            features = Feature.objects.all().filter(id=1).first().features
            all_features = features.split(",")
            all_features = sorted(all_features, key=str.lower)      
            return render(request, 'doctors/patient/instancesedit.html', {'patient':thisuser, 'id':user_id, 'instance':thisinstance,'features': all_features,'symptoms':symptoms})
        else:
            thispatient = Patient.objects.all().filter(user=patient_id).first()
            return render(request, 'doctors/doctor/instanceshow.html', {'doctor':thisuser, 'patient':thispatient, 'id':user_id, 'instance':thisinstance,'symptoms':symptoms})    
    else:
        if type == "1": #Novo Sintoma
            usertype = None
            user = User.objects.all().filter(encryptid=user_id).first()
            thisuser = Doctor.objects.all().filter(user=user).first()
            usertype = "Doctor"
            if thisuser == None:
                thisuser = Patient.objects.all().filter(user=user).first()
                usertype = "Patient"     
            
            thisinstance = Instance.objects.all().filter(id=int(instance)).first() 
            feature = request.POST.get('default-select')
            value = request.POST.get('valor')
            newsymptom = Symptom(instance=thisinstance,name=feature,value=value)
            newsymptom.save()        
            symptoms = Symptom.objects.all().filter(instance=int(instance))
            features = Feature.objects.all().filter(id=1).first().features
            all_features = features.split(",")
            all_features = sorted(all_features, key=str.lower)            
            return render(request, 'doctors/patient/instancesedit.html', {'patient':thisuser, 'id':user_id, 'instance':thisinstance,'features': all_features,'symptoms':symptoms})
        elif type == "2": #Deletar sintoma
            usertype = None
            user = User.objects.all().filter(encryptid=user_id).first()
            thisuser = Doctor.objects.all().filter(user=user).first()
            usertype = "Doctor"
            if thisuser == None:
                thisuser = Patient.objects.all().filter(user=user).first()
                usertype = "Patient"
            thisinstance = Instance.objects.all().filter(id=int(instance)).first()
            thissymptom =  Symptom.objects.all().filter(id=int(symptom)).first()
            thissymptom.delete()
            symptoms = Symptom.objects.all().filter(instance=int(instance))
            features = Feature.objects.all().filter(id=1).first().features
            all_features = features.split(",")
            all_features = sorted(all_features, key=str.lower)            
            return render(request, 'doctors/patient/instancesedit.html', {'patient':thisuser, 'id':user_id, 'instance':thisinstance,'features': all_features,'symptoms':symptoms})
        elif type == "3": #Deletar Instância
            usertype = None
            user = User.objects.all().filter(encryptid=user_id).first()
            thisuser = Doctor.objects.all().filter(user=user).first()
            usertype = "Doctor"
            if thisuser == None:
                thisuser = Patient.objects.all().filter(user=user).first()
                usertype = "Patient"
            delinstance = Instance.objects.all().filter(id=instance).first()
            delinstance.delete()
            all_instances = Instance.objects.all().filter(user=user)    
            features = Feature.objects.all().filter(id=1).first().features
            all_features = features.split(",")
            all_features = sorted(all_features, key=str.lower)
            return render(request, 'doctors/patient/instances.html', {'patient':thisuser, 'id':user_id, 'features': all_features,'listinst':all_instances})
        else:        
            return redirect('editinstance') 

def history(request,user_id,patient_id=""):
    if request.method == 'GET':
        usertype = None
        user = User.objects.all().filter(encryptid=user_id).first()
        thisuser = Doctor.objects.all().filter(user=user).first()
        usertype = "Doctor"
        if thisuser == None:
            thisuser = Patient.objects.all().filter(user=user).first()
            usertype = "Patient"
        if patient_id == "":    
            all_diagnostics = Diagnostic.objects.all().filter(user=user)
            return render(request, 'doctors/patient/history.html', {'patient':thisuser, 'id':user_id, 'diagnostics':all_diagnostics})
        else:
            thispatient = Patient.objects.all().filter(id=patient_id).first()
            all_diagnostics = Diagnostic.objects.all().filter(user=thispatient.user.id)
            return render(request, 'doctors/doctor/alldiagnostic.html', {'doctor':thisuser, 'patient':thispatient, 'id':user_id,  'diagnostics':all_diagnostics})

def doctors(request,user_id,diag_id="-1"):
    if request.method == 'GET':
        if diag_id=="-1":
            usertype = None
            user = User.objects.all().filter(encryptid=user_id).first()
            thisuser = Doctor.objects.all().filter(user=user).first()
            usertype = "Doctor"
            if thisuser == None:
                thisuser = Patient.objects.all().filter(user=user).first()
                usertype = "Patient"
            all_diagnostics = Diagnostic.objects.all().filter(user=user)
            return render(request, 'doctors/patient/historydoctors.html', {'patient':thisuser, 'id':user_id, 'diagnostics':all_diagnostics})
        else:
            usertype = None
            user = User.objects.all().filter(encryptid=user_id).first()
            thisuser = Doctor.objects.all().filter(user=user).first()
            usertype = "Doctor"
            if thisuser == None:
                thisuser = Patient.objects.all().filter(user=user).first()
                usertype = "Patient"
            doctors = load_doc(user_id,int(diag_id))
            all_doctors = []
            for doc in doctors:
                all_doctors.append(doc)     
            if len(all_doctors)>0: 
                return render(request, 'doctors/patient/doctors.html', {'patient':thisuser, 'id':user_id, 'alldoc':all_doctors})
            else:
                return render(request, 'doctors/patient/nodoctor.html', {'patient':thisuser, 'id':user_id})    

def docshow(request,user_id,doc_id):
    if request.method == 'GET':
        usertype = None
        user = User.objects.all().filter(encryptid=user_id).first()
        thisuser = Doctor.objects.all().filter(user=user).first()
        usertype = "Doctor"
        if thisuser == None:
            thisuser = Patient.objects.all().filter(user=user).first()
            usertype = "Patient"
        thisdoctor = Doctor.objects.all().filter(id=doc_id).first()
        thisnota = thisdoctor.nota
        notas = []
        for i in range(int(thisnota)):
            notas.append("1")
        if len(notas) < 5:
            diff = 5 - len(notas)
            for j in range(diff):
                notas.append("0")
        newref = Reference.objects.all().filter(patient=thisuser,doctor=thisdoctor).first()
        if newref == None:
            return render(request, 'doctors/patient/doctorcheck.html', {'patient':thisuser, 'id':user_id, 'medico':thisdoctor, 'notas':notas})
        else:                    
            return render(request, 'doctors/patient/doctorcheckdone.html', {'patient':thisuser, 'id':user_id, 'medico':thisdoctor, 'notas':notas})
    else: 
        usertype = None
        user = User.objects.all().filter(encryptid=user_id).first()
        thisuser = Patient.objects.all().filter(user=user).first()
        usertype = "Patient"   
        thisdoctor = Doctor.objects.all().filter(id=doc_id).first()
        thisnota = thisdoctor.nota
        notas = []
        for i in range(int(thisnota)):
            notas.append("1")
        if len(notas) < 5:
            diff = 5 - len(notas)
            for j in range(diff):
                notas.append("0")
        newref = Reference.objects.all().filter(patient=thisuser,doctor=thisdoctor).first()
        if newref == None:
            newref = Reference(patient=thisuser,doctor=thisdoctor,date=datetime.today().strftime('%d/%m/%Y-%H:%M:%S'),status="Open")
            newref.save()        
            return render(request, 'doctors/patient/doctorcheckdone.html', {'patient':thisuser, 'id':user_id, 'medico':thisdoctor, 'notas':notas})
        else:
            return render(request, 'doctors/patient/doctorcheckdone.html', {'patient':thisuser, 'id':user_id, 'medico':thisdoctor, 'notas':notas})

def send_message(api_key,api_dom,api_send,user_mail,subject,param,thres,valor,site):
    from_origin = 'Aries Micro-Estações <{}>'.format(api_send)
    return requests.post(
        api_dom,
        auth=("api", api_key),
        data={"from": from_origin,
              "to": [user_mail],
              "subject": subject,
              "template": "alert",
			  "v:parametro": param,
              "v:threshold": thres,
              "v:valor": valor,
              "v:site": site
              })       

def calendar(request,user_id,type="1"):
    if request.method == 'GET':
        if type=="1":
            usertype = None
            user = User.objects.all().filter(encryptid=user_id).first()
            thisuser = Doctor.objects.all().filter(user=user).first()
            usertype = "Doctor"
            if thisuser == None:
                thisuser = Patient.objects.all().filter(user=user).first()
                usertype = "Patient"
            consultas = Event.objects.all().filter(patient=thisuser)
            return render(request, 'doctors/patient/calendar.html', {'patient':thisuser,'id':user_id, 'consultas':consultas})
        else:
            usertype = None
            user = User.objects.all().filter(encryptid=user_id).first()
            thisuser = Doctor.objects.all().filter(user=user).first()
            usertype = "Doctor"
            if thisuser == None:
                thisuser = Patient.objects.all().filter(user=user).first()
                usertype = "Patient"
            consultas = Event.objects.all().filter(doctor=thisuser)
            return render(request, 'doctors/doctor/calendar.html', {'doctor':thisuser,'id':user_id, 'consultas':consultas})


def patients(request,user_id,patient_id=None,type=None):
    if request.method == 'GET':
        usertype = None
        user = User.objects.all().filter(encryptid=user_id).first()
        thisuser = Doctor.objects.all().filter(user=user).first()
        usertype = "Doctor"
        if thisuser == None:
            thisuser = Patient.objects.all().filter(user=user).first()
            usertype = "Patient"
        closedrequests = Reference.objects.all().filter(doctor=thisuser, status="Closed")    
        if type=="3":
            return render(request, 'doctors/doctor/instances.html', {'doctor':thisuser,'id':user_id, 'closedrequests':closedrequests})
        elif type =="4":
            return render(request, 'doctors/doctor/diagnostic.html', {'doctor':thisuser,'id':user_id, 'closedrequests':closedrequests})
        elif type == "5":
            return render(request, 'doctors/doctor/events.html', {'doctor':thisuser,'id':user_id, 'closedrequests':closedrequests})
        else:            
            openrequests = Reference.objects.all().filter(doctor=thisuser, status="Open")
            return render(request, 'doctors/doctor/requisições.html', {'doctor':thisuser,'id':user_id, 'openrequests':openrequests, 'closedrequests':closedrequests})
    if request.method == 'POST':
        if type=="1":
            usertype = None
            thisuser = Doctor.objects.all().filter(user=user_id).first()
            usertype = "Doctor"
            if thisuser == None:
                thisuser = Patient.objects.all().filter(user=user_id).first()
                usertype = "Patient"
            thispat = Patient.objects.all().filter(id=patient_id).first()
            thisreq = Reference.objects.all().filter(doctor=thisuser,patient=thispat).first()
            thisreq.status = "Closed"
            thisreq.save()
            openrequests = Reference.objects.all().filter(doctor=thisuser, status="Open")
            closedrequests = Reference.objects.all().filter(doctor=thisuser, status="Closed")
            return render(request, 'doctors/doctor/requisições.html', {'doctor':thisuser,'id':user_id, 'openrequests':openrequests, 'closedrequests':closedrequests})
        if type=="2":
            usertype = None
            user = User.objects.all().filter(encryptid=user_id).first()
            thisuser = Doctor.objects.all().filter(user=user).first()
            usertype = "Doctor"
            if thisuser == None:
                thisuser = Patient.objects.all().filter(user=user).first()
                usertype = "Patient"
            thispat = Patient.objects.all().filter(id=patient_id).first()
            thisreq = Reference.objects.all().filter(doctor=thisuser,patient=thispat).first()
            thisreq.delete()
            openrequests = Reference.objects.all().filter(doctor=thisuser, status="Open")
            closedrequests = Reference.objects.all().filter(doctor=thisuser, status="Closed")
            return render(request, 'doctors/doctor/requisições.html', {'doctor':thisuser,'id':user_id, 'openrequests':openrequests, 'closedrequests':closedrequests})

def event(request,user_id,patient_id):
    if request.method == 'GET':
        usertype = None
        user = User.objects.all().filter(encryptid=user_id).first()
        thisuser = Doctor.objects.all().filter(user=user).first()
        usertype = "Doctor"
        if thisuser == None:
            thisuser = Patient.objects.all().filter(user=user).first()
            usertype = "Patient"
        thispatient = Patient.objects.all().filter(id=patient_id).first()
        events = Event.objects.all().filter(doctor=thisuser,patient=thispatient)
        eventtypes = ["Consulta","Cirurgia"]  
        return render(request, 'doctors/doctor/patientevent.html', {'doctor':thisuser,'id':user_id, 'patient':thispatient, 'events':events, 'eventtypes':eventtypes})
    
    else:
        usertype = None
        user = User.objects.all().filter(encryptid=user_id).first()
        thisuser = Doctor.objects.all().filter(user=user).first()
        usertype = "Doctor"
        if thisuser == None:
            thisuser = Patient.objects.all().filter(user=user).first()
            usertype = "Patient"
        thispatient = Patient.objects.all().filter(id=patient_id).first()
        typeevent = request.POST.get('default-select')
        if typeevent == "Cirurgia":
            hiddenval = "event"
        else:
            hiddenval = "holiday"    
        date = request.POST.get('data')
        description = request.POST.get('descricao')
        newevent = Event(patient=thispatient,doctor=thisuser,eventtype=typeevent,date=date,description=description,calendartype=hiddenval)
        newevent.save() 
        events = Event.objects.all().filter(doctor=thisuser,patient=thispatient)
        eventtypes = ["Consulta","Cirurgia"]  
        return render(request, 'doctors/doctor/patientevent.html', {'doctor':thisuser,'id':user_id, 'patient':thispatient, 'events':events, 'eventtypes':eventtypes})    
