from functools import partial
from django.shortcuts import render
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets

# Create your views here.

class StudentViewSet(viewsets.ViewSet):
    def list(self,request):
        print("********List**********")
        print("Basename:", self.basename)
        print("Action:", self.action)
        print("Detail:", self.detail)
        print("Suffix:", self.suffix)
        print("Name:", self.name)
        print("Description:", self.description)

        stu= Student.objects.all()
        serializer= StudentSerializer(stu, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        print("********List**********")
        print("Basename:", self.basename)
        print("Action:", self.action)
        print("Detail:", self.detail)
        print("Suffix:", self.suffix)
        print("Name:", self.name)
        print("Description:", self.description)

        id= pk
        if id is not None:
            stu= Student.objects.get(id=id)
            serializer= StudentSerializer(stu)
            return Response(serializer.data)

    def create(self, request):
        print("********Create**********")
        print("Basename:", self.basename)
        print("Action:", self.action)
        print("Detail:", self.detail)
        print("Suffix:", self.suffix)
        print("Name:", self.name)
        print("Description:", self.description)

        serializer= StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created.', 'success':True})
        return Response({'error':serializer.errors, 'success':False})

    
    def update(self, request,pk):
        print("********Update**********")
        print("Basename:", self.basename)
        print("Action:", self.action)
        print("Detail:", self.detail)
        print("Suffix:", self.suffix)
        print("Name:", self.name)
        print("Description:", self.description)

        id= pk
        stu= Student.objects.get(pk=id)
        serializer= StudentSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete data update.', 'success':True})
        return Response({'error':serializer.errors, 'success':False})

    def partial_update(self,request,pk):
        print("********Partial Update**********")
        print("Basename:", self.basename)
        print("Action:", self.action)
        print("Detail:", self.detail)
        print("Suffix:", self.suffix)
        print("Name:", self.name)
        print("Description:", self.description)

        id= pk
        stu= Student.objects.get(pk=id)
        serializer= StudentSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Partial data update.', 'success':True})
        return Response({'error':serializer.errors, 'success':False})


    def destroy(self,request,pk):
        print("********Destroy**********")
        print("Basename:", self.basename)
        print("Action:", self.action)
        print("Detail:", self.detail)
        print("Suffix:", self.suffix)
        print("Name:", self.name)
        print("Description:", self.description)

        id= pk
        stu= Student.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'Data deleted.', 'success':True})