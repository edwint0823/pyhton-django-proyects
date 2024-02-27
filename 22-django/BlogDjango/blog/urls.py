from django.urls import path
from . import views

urlpatterns = [
    path('articulos', views.list_articles, name="list_articles"),
    path('categoria/<int:category_id>', views.get_category, name="category"),
    path('articulo/<int:article_id>', views.get_article, name="article")
]
