
from django.urls import path
from course.views import *

urlpatterns = [
    path("", courselist,name='courselist'),
    path("Add", courseadd,name='courseadd'),
    path("Update/<int:id>", courseupdate,name='courseupdate'),
    path("Delete/<int:id>", coursedelete,name='coursedelete'),

]
