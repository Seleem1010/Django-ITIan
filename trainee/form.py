from django import forms
from django.contrib.auth.models import *
from .models import *
from course.models import *

class AddForm(forms.Form):

    trainee_name=forms.CharField()
    course=forms.ModelChoiceField(queryset=Course.objects.all())


class UpdateModelForm(forms.ModelForm):
    class Meta:
        model=Trainee
        fields='__all__'