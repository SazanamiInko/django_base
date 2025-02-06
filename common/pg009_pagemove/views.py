from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
 return render(request,'pg009_pagemove/index.html');

def detail(request):
  return render(request,'pg009_pagemove/detail.html');