from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from site_settings_app.models import SiteSetting
from site_settings_app.serializers import SiteSettingsSerializer
from socials_app.models import Social
from socials_app.serializers import SocialSerializer
from contacts_app.models import ContactInfo
from contacts_app.serializers import ContactInfoSerializer

# Create your views here.


@api_view(["GET"])
def site_settings_api(request):
    site_settings = SiteSetting.objects.last()
    socials = Social.objects.last()
    contacts_info = ContactInfo.objects.last()
    site_settings_serializer = SiteSettingsSerializer(site_settings, many=False)
    socials_serializer = SocialSerializer(socials, many=False)
    contacts_info_serializer = ContactInfoSerializer(contacts_info, many=False)
    serializer = {
        "site_settings": site_settings_serializer.data,
        "socials": socials_serializer.data,
        "contacts_info": contacts_info_serializer.data,
    }
    return Response(serializer, status=status.HTTP_200_OK)
