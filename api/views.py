from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Task
from .serializers import TaskSerializer

# Create your views here.
@api_view(["GET"])
def ApiOverview(request):
    return Response({
        "Create": "/task-create/",
        "Read": "/task-read/",
        "Update": "/task-update/<str:pk>/",
        "Delete": "/task-delete/<str:pk>/"
    })

@api_view(["GET"])
def TaskRead(request, pk):
    try:
        if pk == 'all':
            tasks = Task.objects.all()
        else:
            tasks = Task.objects.all().filter(id=pk)

        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)
    except Exception as error:
        print(error)