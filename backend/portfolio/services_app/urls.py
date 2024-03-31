from django.urls import path
from services_app.views import service_api, request_to_work_api

urlpatterns = [
    path("services/", service_api, name="services"),
    path("request-to-work/", request_to_work_api, name="request_to_work"),
]
