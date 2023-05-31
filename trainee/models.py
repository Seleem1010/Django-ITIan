from django.db import models
from course.models import *


# Create your models here.
class Trainee(models.Model):
    id=models.AutoField(primary_key=True,db_column='id')
    name=models.TextField(max_length=20)
    course_id=models.ForeignKey('course.Course',on_delete=models.CASCADE)