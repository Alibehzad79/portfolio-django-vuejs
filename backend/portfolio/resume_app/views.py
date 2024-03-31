from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from resume_app.models import Resume
from resume_app.serializers import ResumeSerializer

# Create your views here.


@api_view(["GET"])
def resume_api(request):
    resume = Resume.objects.last()
    serializer = ResumeSerializer(resume, many=False)
    return Response(serializer.data, status=status.HTTP_200_OK)
