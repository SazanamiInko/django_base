from django.shortcuts import render
from django.http import HttpResponse
from pg015_form_class.forms import MemberForm

#会員登録ページ
def member(request):
 params={'form':MemberForm(),
         'title':'会員登録'};
 return render(request,'pg015_form_class/member.html',params);
