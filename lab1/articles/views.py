from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Article
from django.shortcuts import render, get_object_or_404
from .serializers import ArticleSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


def articles_by_author(request, username):
    user = User.objects.get(username=username)
    articles = Article.objects.filter(author=user)

    result = ""
    for article in articles:
        result += f"{article.title}<br>"

    return HttpResponse(result)

def article_list(request):
    articles = Article.objects.all()
    return render(request, 'articles/article_list.html', {'articles': articles})

def article_detail(request, id):
    article = get_object_or_404(Article, id=id)
    return render(request, 'articles/article_detail.html', {'article': article})

@api_view(['GET'])
def article_api(request):
    articles = Article.objects.all()
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data)