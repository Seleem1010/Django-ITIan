from django.shortcuts import render
from django.http import HttpResponse ,HttpResponseRedirect

# Create your views here.

def traineelist(req):
    trainees=[(1,'trainee1'),(2,'trainee2'),(3,'trainee3')]
    context={}
    context['trainees']=trainees
    return  render(req,'trainee/list.html',context)


def traineeadd(req):
    return render(req,'trainee/add.html')


def traineeupdate(req,id):
    return HttpResponseRedirect('/Trainees')


def traineedelete(req,id):
    return HttpResponse('hi id ='+str(id)+' deleted')
