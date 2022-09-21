
from django.shortcuts import render
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication

from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser

# Create your views here.

# class StudentViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset= Student.objects.all()
#     serializer_class= StudentSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset= Student.objects.all()
    serializer_class= StudentSerializer
    # authentication_classes= [BasicAuthentication]
    # permission_classes= [IsAuthenticated]
    # permission_classes= [AllowAny]
    # permission_classes= [IsAdminUser]
