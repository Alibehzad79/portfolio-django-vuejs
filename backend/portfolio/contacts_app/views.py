from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from contacts_app.models import Contact, ContactInfo
from contacts_app.serializers import ContactInfoSerializer, ContactSerializer
from datetime import datetime

# Create your views here.


@api_view(["GET", "POST"])
def contacts_api(request):
    if request.method == "GET":
        contact_info = ContactInfo.objects.last()
        serializer = ContactInfoSerializer(contact_info, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == "POST":
        request.data["date_recive"] = datetime.today().strftime("%Y-%m-%d")
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
