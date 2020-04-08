from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from course.models import Course,CourseEntry
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url="/login/")
def courseprofile(request):
    if request.method=="GET":
        data=[1,2]
        user=User.objects.get(id=request.GET['userid'])
        obj=user.courseentry_set.all().exists()
        if(False==obj):
         messages.error(request, 'You have not purched any course')
         return HttpResponseRedirect("/",data)

        else:
         obj=user.courseentry_set.all()
         for i in obj:
             print(i.course)
         res=render(request,"course/Course.html",{'userobj':obj})
         return res
@login_required(login_url="/login/")
def test(request):
    res=render(request,"base.html")
    return res

def c(request):
 if request.method=="GET":
     return render(request,"course/c.html")
def python(request):
 if request.method=="GET":
     return render(request,"course/python.html")
def java(request):
 if request.method=="GET":
     return render(request,"course/java.html")

def Payment(request):
  user=None
  if request.method=="POST":
     try:
       username=request.POST['username']
       courseid=request.POST['courseid']
       user=User.objects.get(username=username)
       c=Course.objects.get(id=courseid)
       obj=user.courseentry_set.filter(course=c).exists()
       if(obj==True):
            messages.error(request, 'You have Already purched this course!')
            return redirect("/")
       else:
           student=CourseEntry(course=c,user=user,score=0,status='Running',result=False)
           student.save()
           return render(request,'course/payment.html')
     except:
        messages.error(request, 'Login Please!')
        return redirect("/")


@login_required(login_url="/login/")
def FinalPayment(request):
 if request.method=="GET":
     return render(request,"course/final.html")

@login_required(login_url="/login/")
def profile(request):
 if request.method=="GET":
     data={}
     return HttpResponseRedirect("/",data)

@login_required(login_url="/login/")
def Video(request):
 if request.method=="GET":
     return render(request,"course/video.html")
