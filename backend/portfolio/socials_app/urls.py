from django.urls import path
from socials_app.views import social_api

urlpatterns = [
    path("socials/", social_api, name="socials"),
]
