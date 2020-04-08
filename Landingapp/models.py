from django.db import models

# Create your models here.
class Teacher(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField(max_length=100,primary_key=True)
    phone=models.CharField(max_length=20)
    def __str__(self):
        return self.name 
