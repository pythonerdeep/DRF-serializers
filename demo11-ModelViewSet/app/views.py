
from django.shortcuts import render
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets

# Create your views here.

class StudentViewSet(viewsets.ModelViewSet):
    queryset= Student.objects.all()
    serializer_class= StudentSerializer