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

    form=self.params['form'];
    
    form.fields['name'].initial= request.session.get('name');
    form.fields['kind'].initial= request.session.get('kind');
    form.fields['address'].initial= request.session.get('address');
    form.fields['phone'].initial= request.session.get('phone');
    form.fields['age'].initial= request.session.get('age');
    form.fields['sex'].initial= request.session.get('sex');

    return render(request,'pg032_middleware/input.html',self.params);
    
  #post
  def post(self,request):
   
   nameline="氏名:"+request.POST['name']+"<br>"; 
   kindline="会員種別:"+request.POST['kind']+"<br>";
   adddressline="住所:"+request.POST['address']+"<br>";
   phoneline="電話番号:"+request.POST['phone']+"<br>";
   ageline="年齢:"+request.POST['age']+"<br>";
   sex=request.POST['sex'];
   sexline='性別:男性<br>'; 
   
   if sex=='2':
     sexline='性別:女性<br>';
   msg=nameline+kindline+adddressline+phoneline+ageline+sexline;
 
   self.params['msg']=msg;
   self.params['form']=MemberForm(request.POST);
   self.params['title']="会員登録:入力確認";
   
   #セッションにデータを詰める
   request.session['name']=request.POST['name'];
   request.session['kind']=request.POST['kind'];
   request.session['address']=request.POST['address'];
   request.session['phone']=request.POST['phone'];
   request.session['age']=request.POST['age'];
   request.session['sex']=request.POST['sex'];
   return render(request,'pg032_middleware/input.html',self.params);

def member_middleware(get_response):

  def middleWare(request):
    count=request.session.get('count',0);
    count=count+1;
    request.session['count']=count;
    response=get_response(request);
    print("あなたのアクセス回数:"+str(count));
    return response
  return middleWare
