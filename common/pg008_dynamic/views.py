from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request,title,start,end):

    params={'title':title,
        'start':str(start),
        'end':str(end)};
    return render(request,'pg008_dynamic/index.html',params)