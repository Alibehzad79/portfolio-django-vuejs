from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from projects_app.models import Project
from projects_app.serializers import ProjectSerializer

# Create your views here.


@api_view(["GET"])
def project_api(request):
    item_limit = request.GET.get("limit")
    if item_limit:
        projects = Project.objects.all()[: int(item_limit)]
    else:
        projects = Project.objects.all()
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
