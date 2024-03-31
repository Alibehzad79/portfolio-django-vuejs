from rest_framework import serializers
from services_app.models import Service, ServiceOption, ServicePlan, RequestToWork


class ServicePlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServicePlan
        exclude = ("id", "service")


class ServiceOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceOption
        exclude = ("id", "service")


class ServiceSerializer(serializers.ModelSerializer):
    service_option = serializers.SerializerMethodField()
    service_plan = serializers.SerializerMethodField()

    class Meta:
        model = Service
        fields = ("title", "slug", "content", "service_option", "service_plan")

    def get_service_option(self, obj):
        return (
            ServicePlanSerializer(option).data for option in obj.service_options.all()
        )

    def get_service_plan(self, obj):
        return (ServiceOptionSerializer(plan).data for plan in obj.service_plans.all())


class RequestToWorkSerializer(serializers.ModelSerializer):
    date_recive = serializers.DateField()

    class Meta:
        model = RequestToWork
        fields = ("service", "name", "email", "subject", "message", "date_recive")
