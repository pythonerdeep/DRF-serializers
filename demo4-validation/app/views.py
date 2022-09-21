from functools import partial
import json
import re
from django import views
from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializr
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
import io
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
# Create your views here.

@method_decorator(csrf_exempt, name='dispatch')
class StudentApi(View):
    def get(self, request, *args, **kwargs):
        json_data= request.body
        stream= io.BytesIO(json_data)
        pythodata= JSONParser().parse(stream)
        id= pythodata.get('id', None)
        if id is not None:
            stu= Student.objects.get(id=id)
            serializer= StudentSerializr(stu)
            json_data= JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type='application/json')
        stu= Student.objects.all()
        serializer= StudentSerializr(stu, many=True)
        json_data= JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type='application/json')

    def post(self, request, *args, **kwargs):
        json_data= request.body
        stream= io.BytesIO(json_data)
        pytho_data= JSONParser().parse(stream)
        serializer= StudentSerializr(data=pytho_data)
        if serializer.is_valid():
            serializer.save()
            res= {'msg': 'Data created'}
            json_data= JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        json_data= JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')

    def put(self, request, *args, **kwargs):
        json_data= request.body
        stream= io.BytesIO(json_data)
        pytho_data= JSONParser().parse(stream)
        id= pytho_data.get('id')
        stu= Student.objects.get(id=id)  
        serializer= StudentSerializr(stu, data=pytho_data, partial=True)
        if serializer.is_valid(): 
            serializer.save()
            res= {'mgg':'Data uploaded'}
            json_data= JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        json_data= JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')

    def delete(self, request, *args, **kwargs):
        json_data=request.body
        stream= io.BytesIO(json_data)
        pytho_data= JSONParser().parse(stream)
        id= pytho_data.get('id')
        stu= Student.objects.get(id=id) 
        stu.delete()
        res= {'mgg':'Data deleted'}
        json_data= JSONRenderer().render(res)
        return HttpResponse(json_data, content_type='application/json')
