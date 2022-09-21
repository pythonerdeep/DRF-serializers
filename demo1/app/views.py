from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializr
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
# Create your views here.


def student_detail(request, pk):
    stu= Student.objects.get(id=pk)
    seralizer= StudentSerializr(stu)
    json_data=JSONRenderer().render(seralizer.data)
    return HttpResponse(json_data, content_type='application/json')
    #return JsonResponse(serializer.data)


def student_list(request):
    stu= Student.objects.all()
    seralizer= StudentSerializr(stu, many=True)
    json_data=JSONRenderer().render(seralizer.data)
    return HttpResponse(json_data, content_type='application/json')