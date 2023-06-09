from django.shortcuts import render
from django.http import HttpResponse ,HttpResponseRedirect
from trainee.models import *
from course.models import *
from trainee.form import *
from rest_framework.response import Response
from  rest_framework.decorators import  api_view
from .serliazers import *
from rest_framework.status import *
from django.shortcuts import  get_object_or_404


# Lab 4 api
#view
@api_view(['GET'])
def traineelist(req,id=None):
    #if id is provided then get 1 trainee or 404 code
    if(id is not None):
        data=get_object_or_404(Trainee,id=id)
    #else get all trainee
    else:
        data=Trainee.objects.all()

    #if data is returned change it from objects to json
    if(data):
        if(id is not None):
            trainee_json = Traineeselizer(data)
            return Response(status=HTTP_202_ACCEPTED, data={'Trainee': trainee_json.data})
        else:
            trainee_json=Traineeselizer(data,many=True)
            return Response(status=HTTP_207_MULTI_STATUS, data={'Trainees':trainee_json.data})
    #else return status code 404 not found
    else:
        return  Response(status=HTTP_404_NOT_FOUND)


#add
@api_view(['POST'])
def traineeadd(req):
    
    trainee = Traineeselizer(data=req.data)
    print(req.data)
    if(trainee.is_valid()):
        trainee.save()
        return  Response(status=HTTP_200_OK,data=trainee.data)
    else:
        return Response(HTTP_406_NOT_ACCEPTABLE,data={'error':'Wrong values for trainee'})


#update
@api_view(['PUT'])
def traineeupdate(req,id):
    if(len(Trainee.objects.filter(id=id))!=0):
        obj = Trainee.objects.get(id=id)
        
        updated_obj = Traineeselizer(instance=obj,data=req.data)
        if(updated_obj.is_valid()):
            updated_obj.save()
            return Response(status=HTTP_202_ACCEPTED,data=updated_obj.data)
    else:
        return  Response(status=HTTP_404_NOT_FOUND,data={'error':'Trainee not found'})


#delete
@api_view(['DELETE'])
def traineedelete(req,id):
    if(len(Trainee.objects.filter(id=id))!=0):
        obj = Trainee.objects.get(id=id)
        obj.delete()
        return Response(status=HTTP_200_OK,data={'error':'Trainee Deleted'})
    else:
        return  Response(status=HTTP_404_NOT_FOUND,data={'error':'Trainee not found'})

##### old labs

# # Create your views here.
# def traineelist(req):
#     if( 'username' in req.session):
#         trainees = Trainee.objects.all()
#         context={}
#         context['trainees'] = trainees
#         return  render(req,'trainee/list.html',context)
#     else:
#         return HttpResponseRedirect('/')



# def traineeadd(req):
#     if( 'username' in req.session):
#         f=AddForm()
#         context={}
#         context['form']=f
#         context['courses'] = Course.objects.all()
#         if(req.method=='POST'):
#             mycourse=Course.objects.get(id=req.POST['course'])
#             Trainee.objects.create(name=req.POST['trainee_name'],course_id=mycourse)
#         # return render(req,'trainee/add.html',context)
#         return render(req,'trainee/addform.html',context)
#     else:
#         return HttpResponseRedirect('/')


# def traineeupdate(req,id):
#     f=UpdateModelForm(instance=Trainee.objects.get(id = id))
#     context={}
#     context['form']=f
#     context['courses'] = Course.objects.all()
#     context['trainee_data']=Trainee.objects.get(id = id)
#     if(req.method == 'POST'):
#         form = UpdateModelForm(req.POST, instance=Trainee.objects.get(id = id))
#         if form.is_valid():
#             form.save()

#         # Trainee.objects.filter(id = id).update(name = req.POST['trainee_name'],course_id = Course.objects.get(id= req.POST['course']) )
#         return HttpResponseRedirect('/Trainees')
#     # return render(req,'trainee/update.html',context)
#     return render(req,'trainee/updatemodelform.html',context)


# def traineedelete(req,id):
#     Trainee.objects.filter(id = id).delete()
#     return  HttpResponseRedirect('/Trainees')

