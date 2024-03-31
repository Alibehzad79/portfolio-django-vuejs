from rest_framework import serializers
from site_settings_app.models import SiteSetting


class SiteSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteSetting
        exclude = ("id",)
