from rest_framework import serializers
from .models import *
from django.db.models import fields

class Traineeselizer(serializers.ModelSerializer):
    class Meta:
        model = Trainee
        fields = '__all__'