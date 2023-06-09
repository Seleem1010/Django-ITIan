from django.shortcuts import render ,redirect
from django.http import HttpResponse, HttpResponseRedirect
from account.models import *
from django.contrib.auth.models import *
from django.contrib.auth import login,authenticate,logout

from .models import *
#from .form import *

# Create your views here.
def Login(req):
    context = {}
    if req.method == "POST":
        myuser = SUser.objects.filter(
            username=req.POST["name"], password=req.POST["password"]
        )
        userobj = authenticate(username=req.POST['name'],password=req.POST['password'])
        print(userobj)

        if len(myuser) != 0:
            req.session["username"] = myuser[0].username

            if userobj is not None:
                login(req,userobj)
                return HttpResponseRedirect("/admin")
                
            else :    
                return HttpResponseRedirect("/Trainees")
        else:
            context["msg"] = "Wrong Email or Password"
    return render(req, "login.html", context=context)


def Logout(req):
    # req.session.clear()
    # return HttpResponse("Logout")
    logout(req)
    return redirect("/")




def Registeration(req):
    context = {}
    if req.method == "POST":
        username = req.POST["username"]
        password = req.POST["password"]
        email = req.POST["email"]
        SUser.objects.create(
            username=username, password=password, email=email
        )
    return render(req, "register.html", context)


# def List(req):
#     context = {}
#     for myuser in SUser.objects.all():
#         print(myuser.id, myuser.username)
#     context["users"] = myuser.objects.all()
#     context["user2"] = myuser.objects.filter(id=1)
#     return render(req, "listusers.html", context)
