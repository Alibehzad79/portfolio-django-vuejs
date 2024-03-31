from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from profile_app.models import MyProfile
from profile_app.serializers import ProfileSerializer
from socials_app.models import Social
from socials_app.serializers import SocialSerializer

# Create your views here.


@api_view()
def profile_api(request):
    profile = MyProfile.objects.last()
    social = Social.objects.last()
    profile_serializer = ProfileSerializer(profile, many=False)
    social_serializer = SocialSerializer(social, many=False)
    data = {"profile": profile_serializer.data, "socials": social_serializer.data}
    return Response(data, status=status.HTTP_200_OK)
