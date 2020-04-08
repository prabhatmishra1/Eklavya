from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Course(models.Model):
    coursename=models.CharField(max_length=40)
    courseduration=models.CharField(max_length=30)
    coursefee=models.FloatField()
    teachername=models.CharField(max_length=45)
    courseimage=models.ImageField(upload_to="courseimg",default='SOME STRING')
    def __str__(self):
      return str(self.coursename)
class CourseEntry(models.Model):
    course=models.ForeignKey(Course, on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    score=models.IntegerField()
    status=models.CharField(max_length=30)
    result=models.BooleanField()
    def __str__(self):
        x = str(self.course)
        return x
