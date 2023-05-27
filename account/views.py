from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def Login(req):
    return render(req,'login.html')


def Logout(req):
    return HttpResponse('Logout')


def Registration(req):
    context={}
    return  render(req,'register.html',context)