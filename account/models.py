from django.db import models

# Create your models here.
class SUser(models.Model):
    #int auto pk
    id=models.AutoField(primary_key=True,db_column='id')
    username=models.TextField(max_length=20)
    email=models.EmailField(max_length=75)
    password=models.CharField(max_length=8)
