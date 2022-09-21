from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializr
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
import io
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def student_create(request):
    if request.method == 'POST':
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