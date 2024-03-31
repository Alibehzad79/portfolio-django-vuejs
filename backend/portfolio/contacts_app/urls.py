from django.urls import path
from contacts_app.views import contacts_api

urlpatterns = [
    path("contacts/", contacts_api, name="contacts"),
]
