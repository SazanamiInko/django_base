from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .forms import CheckOutForm

#連絡先登録ページ
class CheckoutView(TemplateView):
  #初期化
  def __init__(self):
     self.params={'form':CheckOutForm(),
         'title':'手動チェックアウト'};
  #get
  def get(self,request):
    return render(request,'pg023_date/CheckOut.html',self.params);
    
  #post
  def post(self,request):
    self.params["form"]=CheckOutForm(request.POST);
   
    dateline="日付:"+request.POST['Date']+"<br>"; 
    timeline="時刻:"+request.POST['Time']+"<br>";
    
    msg=dateline+timeline;
    self.params["title"]="手動チェックアウト:入力確認";
    self.params["msg"]=msg;
    return render(request,'pg023_date/CheckOut.html',self.params);