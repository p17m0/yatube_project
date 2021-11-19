from . import views
from django.urls import path

urlpatterns = [
    # Главная страница
    path('', views.index),
    # Страница со списком мороженого
    path('posts/', views.posts_list),
    # Страница с информацией об одном сорте мороженого;
    # в качестве параметра ожидает целое положительное число или 0
    path('posts/<slug:slug>/', views.group_posts),
]