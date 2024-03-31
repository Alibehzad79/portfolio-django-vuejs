from django.urls import path
from resume_app.views import resume_api

urlpatterns = [
    path("resume/", resume_api, name="resume"),
]
