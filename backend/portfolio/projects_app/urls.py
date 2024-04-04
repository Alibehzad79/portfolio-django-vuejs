from django.urls import path
from projects_app.views import project_api, project_detail_api

urlpatterns = [
    path(
        "projects/",
        project_api,
        name="projects",
    ),
    path(
        "projects/<slug:slug>/",
        project_detail_api,
        name="project-detail",
    ),
]
