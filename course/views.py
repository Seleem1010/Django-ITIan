from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from course.models import *

# Create your views here.

def courselist(req):
    if( 'username' in req.session):
        courses = Course.objects.all()
        context={}
        context['courses'] = courses
        return  render(req,'course/list.html',context)
    else:
        return HttpResponseRedirect('/')


def courseadd(req):
    if( 'username' in req.session):
        context={}
        if(req.method == 'POST'):
            name=req.POST['course_name']
            Course.objects.create(name=name)
        return render(req,'course/add.html',context)
    else:
        return HttpResponseRedirect('/')


def courseupdate(req,id):
    return HttpResponseRedirect('Courseupdate')


def coursedelete(req,id):
    return HttpResponse('Coursedelete')
