from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):

    if 'title' in request.GET:
        result=request.GET['title']
    else:
        result="タイトルを指定してください"
    return HttpResponse(result)