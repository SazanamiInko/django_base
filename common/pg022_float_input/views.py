from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .forms import WeightForm

#連絡先登録ページ
class WeighttView(TemplateView):
  #初期化
  def __init__(self):
     self.params={'form':WeightForm(),
         'title':'体重測定'};
  #get
  def get(self,request):
    return render(request,'pg022_floart_input/weight.html',self.params);
    
  #post
  def post(self,request):
    self.params["form"]=WeightForm(request.POST);
   
    weightline="体重:"+request.POST['weight']+"<br>"; 
    tallline="身長:"+request.POST['tall']+"<br>";
    
    msg=weightline+tallline;
    self.params["title"]="体重測定:入力確認";
    self.params["msg"]=msg;
    return render(request,'pg022_floart_input/weight.html',self.params);