from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
 return render(request,'pg011_boot_strap/index.html');