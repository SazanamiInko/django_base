from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .models import Score

#結果発表
class ScoreListView(TemplateView):
  #初期化 
  def dispatch(self, request, *args, **kwargs):
    data=Score.objects.using('test_result').all();
    self.params={'data':data,
         'title':'試験結果'};
    return super().dispatch(request, *args, **kwargs)
  
  #get
  def get(self,request):

    
    return render(request,'pg035_sqlite_connect/index.html',self.params);
   