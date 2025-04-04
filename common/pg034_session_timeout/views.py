from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .forms import MemberForm
from .forms import SessionTimeOutSettingForm

#登録ページ
class MemberView(TemplateView):
  #初期化 
  def dispatch(self, request, *args, **kwargs):
    self.params={'form':MemberForm(),
         'title':'会員登録'};
    return super().dispatch(request, *args, **kwargs)
  
  #get
  def get(self,request):

    request.GET.get('next', '/')
    form=self.params['form'];
    
    form.fields['pg034_name'].initial= request.session.get('pg034_name');
    form.fields['pg034_kind'].initial= request.session.get('pg034_kind');
    form.fields['pg034_address'].initial= request.session.get('pg034_address');
    form.fields['pg034_phone'].initial= request.session.get('pg034_phone');
    form.fields['pg034_age'].initial= request.session.get('pg034_age');
    form.fields['pg034_sex'].initial= request.session.get('pg034_sex');

    return render(request,'pg034_session_timeout/input.html',self.params);
    
  #post
  def post(self,request):
   
   nameline="氏名:"+request.POST['pg034_name']+"<br>"; 
   kindline="会員種別:"+request.POST['pg034_kind']+"<br>";
   adddressline="住所:"+request.POST['pg034_address']+"<br>";
   phoneline="電話番号:"+request.POST['pg034_phone']+"<br>";
   ageline="年齢:"+request.POST['pg034_age']+"<br>";
   sex=request.POST['pg034_sex'];
   sexline='性別:男性<br>'; 
   
   if sex=='2':
     sexline='性別:女性<br>';
   msg=nameline+kindline+adddressline+phoneline+ageline+sexline;
 
   self.params['msg']=msg;
   self.params['form']=MemberForm(request.POST);
   self.params['title']="会員登録:入力確認";
   
   #セッションにデータを詰める
   request.session['pg034_name']=request.POST['pg034_name'];
   request.session['pg034_kind']=request.POST['pg034_kind'];
   request.session['pg034_address']=request.POST['pg034_address'];
   request.session['pg034_phone']=request.POST['pg034_phone'];
   request.session['pg034_age']=request.POST['pg034_age'];
   request.session['pg034_sex']=request.POST['pg034_sex'];
   return render(request,'pg034_session_timeout/input.html',self.params);

#セッションリストビュー
class ListView(TemplateView):
  def dispatch(self, request, *args, **kwargs):
    
    sessions=list(request.session.items());
    self.params={'title':'セッションリスト',
                 'sessions':sessions
                 };

    return super().dispatch(request, *args, **kwargs)
  
  def get(self,request):
   

    return render(request,'pg034_session_timeout/list.html',self.params);

  def post(self,request):
  
    return render(request,'pg034_session_timeout/list.html',self.params);

#セッション設定View
class SettingTimeoutView(TemplateView):
  def dispatch(self, request, *args, **kwargs):
      form=SessionTimeOutSettingForm();
      form.fields['pg034_timeout_setting'].initial=request.session.get_expiry_age();
      self.params={'title':'タイムアウト設定',
                 'form':form};
      return super().dispatch(request, *args, **kwargs)
  
  def get(self,request):
    return render(request,'pg034_session_timeout/input.html',self.params);
  
  def post(self,request):
        new_timeout=int(request.POST['pg034_timeout_setting']);
        request.session.set_expiry(new_timeout);
        self.params['msg']="タイムアウトが設定されました。";
        self.params['title']="タイムアウト設定";
        return render(request,'pg034_session_timeout/input.html',self.params);