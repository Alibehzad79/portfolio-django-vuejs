from django.urls import path
from profile_app.views import profile_api

urlpatterns = [
    path("profile/", profile_api, name="profile"),
]
