from django.urls import path
from site_settings_app.views import site_settings_api

urlpatterns = [
    path("site-settings/", site_settings_api, name="site_settings"),
]
