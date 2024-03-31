from rest_framework import serializers
from projects_app.models import Project, ProjectGallery


class ProjectGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectGallery
        exclude = ("id", "project")


class ProjectSerializer(serializers.ModelSerializer):
    project_gallery = serializers.SerializerMethodField()
    category = serializers.CharField()

    class Meta:
        model = Project
        exclude = ("id",)

    def get_project_gallery(self, obj):
        return (
            ProjectGallerySerializer(gallery).data for gallery in obj.galleries.all()
        )

    def get_category(self, obj):
        return obj.category.name
