from rest_framework import serializers
from resume_app.models import Resume, Education, Experiance, Skill


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        exclude = ("id", "resume")


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        exclude = ("id", "resume")


class ExperianceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experiance
        exclude = ("id", "resume")


class ResumeSerializer(serializers.ModelSerializer):
    educations = serializers.SerializerMethodField()
    experiances = serializers.SerializerMethodField()
    skills = serializers.SerializerMethodField()

    class Meta:
        model = Resume
        fields = ("educations", "experiances", "skills")

    def get_educations(self, obj):
        return (
            EducationSerializer(education).data for education in obj.educations.all()
        )

    def get_experiances(self, obj):
        return (
            ExperianceSerializer(experiance).data
            for experiance in obj.experiances.all()
        )

    def get_skills(self, obj):
        return (SkillSerializer(skill).data for skill in obj.skills.all())
