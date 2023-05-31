from django.shortcuts import render
from django.http import HttpResponse ,HttpResponseRedirect
from trainee.models import *
from course.models import *

# Create your views here.

def traineelist(req):
    if( 'username' in req.session):
        trainees = Trainee.objects.all()
        context={}
        context['trainees'] = trainees
        return  render(req,'trainee/list.html',context)
    else:
        return HttpResponseRedirect('/')



def traineeadd(req):
    if( 'username' in req.session):
        context={}
        context['courses'] = Course.objects.all()
        if(req.method=='POST'):
            mycourse=Course.objects.get(id=req.POST['course'])
            Trainee.objects.create(name=req.POST['trainee_name'],course_id=mycourse)
        return render(req,'trainee/add.html',context)
    else:
        return HttpResponseRedirect('/')


def traineeupdate(req,id):
    context={}
    context['courses'] = Course.objects.all()
    context['trainee_data']=Trainee.objects.get(id = id)
    if(req.method == 'POST'):
        # name = req.POST['trainee_name']
        Trainee.objects.filter(id = id).update(name = req.POST['trainee_name'],course_id = Course.objects.get(id= req.POST['course']) )
        return HttpResponseRedirect('/Trainees')
    return render(req,'trainee/update.html',context)


def traineedelete(req,id):
    Trainee.objects.filter(id = id).delete()
    return  HttpResponseRedirect('/Trainees')

