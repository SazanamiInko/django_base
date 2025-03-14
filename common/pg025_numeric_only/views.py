from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .forms import MemberForm

#登録ページ
class MemberView(TemplateView):
  #初期化
  def __init__(self):
     self.params={'form':MemberForm(),
         'title':'会員登録'};
  #get
  def get(self,request):
    return render(request,'pg025_numeric_only/input.html',self.params);
    
  #post
  def post(self,request):
   nameline="氏名:"+request.POST['name']+"<br>"; 
   adddressline="住所:"+request.POST['address']+"<br>";
   phoneline="電話番号:"+request.POST['phone']+"<br>";
   ageline="年齢:"+request.POST['age']+"<br>";
   msg=nameline+adddressline+phoneline+ageline;
   self.params['msg']=msg;
   self.params['form']=MemberForm(request.POST);
   self.params['title']="会員登録:入力確認";
   return render(request,'pg025_numeric_only/input.html',self.params);