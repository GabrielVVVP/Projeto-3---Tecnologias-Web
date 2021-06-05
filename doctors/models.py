from django.db import models

class User(models.Model):
    encryptid = models.CharField(max_length=200, null=True)
    name = models.CharField(max_length=200, null=True)
    age = models.CharField(max_length=200, null=True)
    sex = models.CharField(max_length=200)
    #image = models.ImageField(upload_to="images/",default='images/default.png')
    email = models.CharField(max_length=200) 
    password = models.CharField(max_length=200)
    def __str__(self):
        return str(self.id)+"."+self.name

class Patient(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    job = models.CharField(max_length=200)
    def __str__(self):
        return str(self.id)+"."+self.user.name

class Doctor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    spec = models.CharField(max_length=200)
    diseases = models.CharField(max_length=500,null=True,blank=True)
    nota = models.CharField(max_length=10,null=True,blank=True)
    def __str__(self):
        return str(self.id)+"."+self.user.name

class Event(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.CharField(max_length=200)
    eventtype = models.CharField(max_length=200)
    calendartype = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    def __str__(self):
        return str(self.id)+"."+self.eventtype+"."+self.patient.user.name+"."+self.doctor.user.name+"."+self.date

class Instance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200)
    date = models.CharField(max_length=200)
    status = models.CharField(max_length=200, null=True)
    def __str__(self):
        return str(self.id)+"."+self.name

class Symptom(models.Model):
    instance = models.ForeignKey(Instance, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200)
    value = models.CharField(max_length=200)
    def __str__(self):
        return str(self.id)+"."+self.name

class Diagnostic(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    instance = models.ForeignKey(Instance, on_delete=models.CASCADE, null=True)
    date = models.CharField(max_length=200)
    mainname = models.CharField(max_length=200, null=True)
    mainprob = models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.instance.name+"."+"Date:"+str(self.date)

class Disease(models.Model):
    diagnostic = models.ForeignKey(Diagnostic, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200)
    probability = models.CharField(max_length=200)
    alert = models.CharField(max_length=200, null=True) 
    def __str__(self):
        return str(self.id)+"."+self.name

class Feature(models.Model):
    features = models.TextField(blank=True, null=True)
    def __str__(self):
        return "Allfeatures"+"."+str(self.id)

class Reference(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, null=True)
    date = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
    def __str__(self):
        return self.patient.user.name+"."+self.doctor.user.name        
                         
