from django.db import models

# Create your models here.



class Patient(models.Model):
    n = models.CharField(max_length=50)
    m = models.IntegerField(null=True)
    ag=models.IntegerField(null=True)
    g = models.CharField(max_length=10)
    p=models.CharField(max_length=10)
    s = models.CharField(max_length=10)

    def __str__(self):
       return self.name;



class Contact(models.Model):
    name = models.CharField(max_length=100, null=True)
    contact = models.CharField(max_length=15, null=True)
    email = models.CharField(max_length=50, null=True)
    subject = models.CharField(max_length=100, null=True)
    message = models.CharField(max_length=300, null=True)
    msgdate = models.DateField(null=True)
    isread = models.CharField(max_length=10,null=True)

    def __str__(self):
        return self.id
