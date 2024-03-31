from rest_framework import serializers
from socials_app.models import Social, SocialItem


class SocialItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialItem
        exclude = ("id", "social")


class SocialSerializer(serializers.ModelSerializer):
    social_item = serializers.SerializerMethodField()

    class Meta:
        model = Social
        fields = ("title", "social_item")

    def get_social_item(self, obj):
        return [
            SocialItemSerializer(social_item).data for social_item in obj.socials.all()
        ]
