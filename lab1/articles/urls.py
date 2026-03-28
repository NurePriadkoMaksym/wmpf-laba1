from django.urls import path
from .views import articles_by_author
from .views import article_list, article_detail, article_api

urlpatterns = [
    path('author/<str:username>/', articles_by_author),
    path('', article_list, name='article_list'),
    path('<int:id>/', article_detail, name='article_detail'),
    path('api/articles/', article_api, name='article_api'),
]