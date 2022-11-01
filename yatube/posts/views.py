from django.shortcuts import render
from django.http import HttpResponse

def index(request):    
    return HttpResponse('Главнейшая страница')


def group_posts(request):
    return HttpResponse('Отфильтрованные посты')

# Create your views here.
