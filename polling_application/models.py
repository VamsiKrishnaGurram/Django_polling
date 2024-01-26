from django.db import models

# Create your models here.
class logindetails(models.Model):
	username =  models.CharField(max_length=15)
	password =  models.CharField(max_length=10)
	email = models.CharField(max_length=30,primary_key=True)