from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .models import Shop

#店舗一覧
class ShopView(TemplateView):
  #初期化 
  def dispatch(self, request, *args, **kwargs):
    data=Shop.objects.using('pokapoka').all();
    self.params={'data':data,
         'title':'店舗一覧'};
    return super().dispatch(request, *args, **kwargs)
  
  #get
  def get(self,request):
    
    return render(request,'pg036_mysql_connect/index.html',self.params);
   