from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from socials_app.models import Social
from socials_app.serializers import SocialSerializer

# Create your views here.


@api_view()
def social_api(request):
    social = Social.objects.last()
    serializer = SocialSerializer(social, many=False)
    return Response(serializer.data, status=status.HTTP_200_OK)
