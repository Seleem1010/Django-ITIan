
from django.urls import path
from trainee.views import *

urlpatterns = [
    #new for api
    path("", traineelist,name='traineelist'),
    path("<int:id>", traineelist,name='traineelist'),
    path("Add", traineeadd,name='traineeadd'),
    path("Update/<int:id>", traineeupdate,name='traineeupdate'),
    path("Delete/<int:id>", traineedelete,name='traineedelete')
    

    
    #old before api
    # path("", traineelist,name='traineelist'),
    # path("Add", traineeadd,name='traineeadd'),
    # path("Update/<int:id>", traineeupdate,name='traineeupdate'),
    # path("Delete/<int:id>", traineedelete,name='traineedelete'),


    
]
