from django.shortcuts import render
from django.http import HttpResponse

#投稿ページ
def post(request):
 return render(request,'pg012_post/post.html');

#受信ページ
def recieve(request):
 
 msg=request.POST['msg'];

 params={"msg":msg,}

 return render(request,'pg012_post/recieve.html',params);