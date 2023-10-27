from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    phone=models.CharField(max_length=12)
    desc=models.TextField()
    date=models.DateField()
    def __str__(self):
        return self.name
class Register(models.Model):
    name1=models.CharField(max_length=122)
    email1=models.CharField(max_length=122)
    phone1=models.CharField(max_length=12)
    password=models.CharField(max_length=12)
    enrol=models.CharField(max_length=20)
    add=models.TextField()
    city=models.CharField(max_length=122)
    pin=models.CharField(max_length=122)
    date=models.DateField()
    def __str__(self):
        return self.name1
class Usname(models.Model):
    usname=models.CharField(max_length=122)
    email2=models.CharField(max_length=122)
    password1=models.CharField(max_length=122)
    def __str__(self):
        return self.usname
class Password_Configuration(models.Model):
    usname1=models.CharField(max_length=122)
    op=models.CharField(max_length=20)
    np=models.CharField(max_length=20)
    def __str__(self):
        return self.usname1

# makemigrations --> create changes and store in a file 
# migration -->apply the pending changes made by the make migrations 
