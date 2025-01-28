from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request,left,right):
    ans=left+right
    result=str(left)+" + "+str(right)+" = "+str(ans)
    return HttpResponse(result)
