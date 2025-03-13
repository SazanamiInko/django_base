from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .forms import MesureForm

#登録ページ
class CheckoutView(TemplateView):
  #初期化
  def __init__(self):
     self.params={'form':MesureForm(),
         'title':'身体測定'};
  #get
  def get(self,request):
    return render(request,'pg024_strtofloat/input.html',self.params);
    
  #post
  def post(self,request):
   self.params["form"]=MesureForm(request.POST);
   weight_str=request.POST['weight'];
   tall_str=request.POST['tall'];
   weightline="体重:"+weight_str+"<br>"; 
   tallline="身長:"+tall_str+"<br>";
   weight_value=float(weight_str);
   tall_value=float(tall_str);
   bmi=int((weight_value/(tall_value*tall_value))*10000);
   bmiline="BMI値:"+str(bmi)+"<br>";
    
   msg=weightline+tallline+bmiline;
   self.params["title"]="測定結果";
   self.params["msg"]=msg;
   return render(request,'pg024_strtofloat/input.html',self.params);