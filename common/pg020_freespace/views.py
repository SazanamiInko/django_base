from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .forms import QuestionnaireForm
from .forms import AnswerForm

#アンケート回答
# ページ
class questionnaireView(TemplateView):
  #初期化
  def __init__(self):
     self.params={'form':QuestionnaireForm(),
         'title':'アンケート'};
  #get
  def get(self,request):
    return render(request,'pg020_freespace/questionnaire.html',self.params);
  
  #post
  def post(self,request):
    ansf=AnswerForm();
    ansf.fields["userbility"].initial=request.POST["userbility"];
    ansf.fields["price"].initial=request.POST["price"];
    ansf.fields["desighn"].initial=request.POST["desighn"];
    ansf.fields["opinion"].initial=request.POST["opinion"];
    self.params['form']=ansf;
    self.params['title']="回答確認";
    return render(request,'pg020_freespace/questionnaire.html',self.params);