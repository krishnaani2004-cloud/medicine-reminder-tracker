from django.db import models

class Medicine(models.Model):
    name = models.CharField(max_length=100,default="")
    dosage = models.CharField(max_length=50,default="")
    time = models.TimeField()

    def __str__(self):
        return self.name

class Patient(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username

class Caretaker(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    phone = models.CharField(max_length=15)
    certificate = models.FileField(upload_to="certificates/")

    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.username
    
class AdminUser(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username