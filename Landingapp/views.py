from django.shortcuts import render
from Landingapp import models
from Landingapp.models import Teacher
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail

#login user
def userLogin(request):
    data={}
    user=0
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        print(username,password)
        user=authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            request.session['username']=username
            return HttpResponseRedirect('profile',user)
        else:
            messages.error(request, 'Invalid Crudentials!!')
            return HttpResponseRedirect("/",data)
    else:
        data={}
        res=render(request,'Landingapp/firstpage.html')
        return res

#user Registration
def register(request):
    data={}
    if request.method=="POST":
       first_name=request.POST['namesignup']
       username=request.POST['usernamesignup']
       password=request.POST['passwordsignup']
       passwords_confirm=request.POST['passwordsignup_confirm']
       mail=request.POST['emailsignup']
       if User.objects.filter(username=username).exists():
           messages.error(request, 'Membership teken already')
           return HttpResponseRedirect("/",data)
           print("username is taken")
       elif User.objects.filter(email=mail).exists():
           messages.error(request, 'Email already exists!!')
           return HttpResponseRedirect("/",data)
           print("email exists already")

       elif  password != passwords_confirm:
            messages.error(request, 'Password not matched!!')
            return HttpResponseRedirect("/",data)
       else:
          user = User.objects.create_user(
          username=username,
          password=password,
          email=mail,
          first_name=first_name,
          )
          #user.save()
          print("shi hai")
          messages.error(request, 'Secssefully signuped go for Login')
          return HttpResponseRedirect("/",data)
    else:
        return HttpResponse("<h1> out </h1>");

#homepage
def firstpage(request):
         res=render(request,'Landingapp/firstpage.html')
         return res

#contact page
@login_required(login_url="/login/")
def contact(request):
    res=render(request,'Landingapp/contact.html')
    return res
#about page
def about(request):
    res=render(request,'Landingapp/about.html')
    return res
def teacherData(request):
    data={}
    if request.method=="POST":
        tname=request.POST['tname']
        temail=request.POST['temail']
        tphone=request.POST['tphone']
        print(tname,temail,tphone)
        if  Teacher.objects.filter(email=temail).exists():
            messages.error(request, 'Email already exists!!')
            return HttpResponseRedirect("/",data)
        else:
            teacher =models.Teacher()
            teacher.name=tname
            teacher.email=temail
            teacher.phone=tphone
            teacher.save();
            messages.error(request,'Thank you for join !!')
            return HttpResponseRedirect('/',data)
    else:
        return HttpResponse("<h2>Inavalid request</h2>")
def ChangePassword(request):
    data={};
    if request.method=="POST":
        username=request.POST['username']
        print(username)
        if User.objects.filter(username=username).exists():
            print("user exists");
            usr = User.objects.get(username=username)
            print(usr.email)
            send_mail(
                     'Eklavya',
                     '''We heard that you lost your Eklavya password. Sorry about that!
But dont worry! You can use the following link to reset your password
http://localhost:8000/Generate-password?username='''+usr.username,

                     'mishraa.prabhat@gmail.com',
                     ['golumishra311@gmail.com'],
                     fail_silently=False,
                     )
            messages.error(request, "Email has been sent check your email.")
            return HttpResponseRedirect('/',data)
        else:
            messages.error(request, "Email does not exists")
            return HttpResponseRedirect('/',data)
    else:
        return render(request,'Landingapp/Resetpassword.html');


def GeneratePassword(request):
    data={};
    if request.method=="POST":
        username=request.POST['username']
        createpassword=request.POST['createpassword']
        confirmpassword=request.POST['confirmpassword']
        print(createpassword,username,confirmpassword)
        user=User.objects.get(username=username)
        user.set_password(createpassword)
        user.save()
        messages.error(request, "Password has been changed.")
        return HttpResponseRedirect('/',data)
    else:
        return render(request,'Landingapp/generatePass.html');
