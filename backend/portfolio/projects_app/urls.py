from django.urls import path
from projects_app.views import project_api

urlpatterns = [
    path(
        "projects/",
        project_api,
        name="projects",
    ),
]
