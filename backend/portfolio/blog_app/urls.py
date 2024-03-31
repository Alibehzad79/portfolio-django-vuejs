from django.urls import path
from blog_app.views import article_list_api, article_detail_api

urlpatterns = [
    path("articles/", article_list_api, name="article_list_api"),
    path("<slug:slug>/", article_detail_api, name="article_detail_api"),
]
