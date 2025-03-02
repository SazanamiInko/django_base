from django.shortcuts import render
from django.http import HttpResponse
from .forms import MemberForm

#会員登録ページ
def member(request):
 params={'form':MemberForm(),
         'title':'会員登録'};
 return render(request,'pg017_form_bootstrap/member.html',params);
