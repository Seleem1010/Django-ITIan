from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from account.models import *


# Create your views here.
def Login(req):
    context = {}
    if req.method == "POST":
        myuser = SUser.objects.filter(
            email=req.POST["email"], password=req.POST["password"]
        )
        if len(myuser) != 0:
            req.session["username"] = myuser[0].username
            return HttpResponseRedirect("/Trainees")
        else:
            context["msg"] = "Wrong Email or Password"
    return render(req, "login.html", context=context)


def Logout(req):
    req.session.clear()
    return HttpResponse("Logout")


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
