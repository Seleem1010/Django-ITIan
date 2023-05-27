from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect

# Create your views here.

def courselist(req):
    courses=[(1,'course1'),(2,'course2'),(3,'course3')]
    context={}
    context['courses']=courses
    return  render(req,'course/list.html',context)


def courseadd(req):
    return render(req,'course/add.html')


def courseupdate(req,id):
    return HttpResponseRedirect('/Courses')


def coursedelete(req,id):
    return HttpResponse('hi id ='+str(id)+' deleted')
