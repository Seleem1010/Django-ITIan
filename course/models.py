from django.db import models

# Create your models here.
class Course(models.Model):
    id=models.AutoField(primary_key=True,db_column='id')
    name=models.TextField(max_length=50)
    def __str__(self):
        return str(self.id) +" "+self.name