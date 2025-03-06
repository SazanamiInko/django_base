from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .forms import ContactForm

#連絡先登録ページ
class ContactView(TemplateView):
  #初期化
  def __init__(self):
     self.params={'form':ContactForm(),
         'title':'連絡先登録'};
  #get
  def get(self,request):
    return render(request,'pg021_email_input/contact.html',self.params);
    
  #post
  def post(self,request):
    self.params["form"]=ContactForm(request.POST);
    nameline="法人名:"+request.POST['name']+"<br>"; 
    adddressline="住所:"+request.POST['address']+"<br>";
    phoneline="電話番号:"+request.POST['phone']+"<br>";
    urlline="URL:"+request.POST['url']+"<br>";
    emailline="email:"+request.POST['email']+"<br>";
    msg=nameline+adddressline+phoneline+urlline+emailline;
    self.params["title"]="連絡先:入力確認";
    self.params["msg"]=msg;
    return render(request,'pg021_email_input/contact.html',self.params);