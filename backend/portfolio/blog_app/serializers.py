from rest_framework import serializers
from blog_app.models import Article


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        exclude = ("id",)
