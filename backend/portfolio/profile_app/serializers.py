from rest_framework import serializers
from profile_app.models import MyProfile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyProfile
        fields = ["full_name", "whate_am_i", "my_description", "img"]
