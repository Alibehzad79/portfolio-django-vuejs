from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from services_app.models import Service, RequestToWork
from services_app.serializers import ServiceSerializer, RequestToWorkSerializer
from django.utils import timezone
from datetime import datetime

# Create your views here.


@api_view(["GET"])
def service_api(request):
    service = Service.objects.all()
    serializer = ServiceSerializer(service, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["POST"])
def request_to_work_api(request):
    if request.method == "POST":
        request.data["date_recive"] = datetime.today().strftime("%Y-%m-%d")
        serializer = RequestToWorkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
