from django.shortcuts import render

# Create your views here
from django.http import HttpResponse

# Главная страница
def index(request):
    return HttpResponse('Главная страница')


# Страница со списком мороженого
def posts_list(request):
    return HttpResponse('Список постов')


# Страница с информацией об одном сорте мороженого;
# view-функция принимает параметр pk из path()
def group_posts(request, slug):
    return HttpResponse(f'Пост: {slug}')