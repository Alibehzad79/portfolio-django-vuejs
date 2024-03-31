from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from blog_app.models import Article
from blog_app.serializers import ArticleSerializer


# Create your views here.


@api_view(["GET"])
def article_list_api(request):
    articles = Article.objects.filter(is_active=True).all()
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def article_detail_api(request, *args, **kwargs):
    article_slug = kwargs["slug"]
    try:
        article = Article.objects.get(slug=article_slug, is_active=True)
    except:
        article = None

    if article is not None:
        serializer = ArticleSerializer(article, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response({"status": "Not Found"}, status.HTTP_404_NOT_FOUND)