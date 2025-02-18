from django.shortcuts import render
from django.http import HttpResponse

#投稿ページ
def post(request):
 return render(request,'pg013_makeview/post.html');

#受信ページ
def recieve(request):
 
 name=request.POST['name'];
 address=request.POST['address']; 
 age=request.POST['age'];

 msg="氏名:"+name+"<br>住所:"+address+"<br>年齢:"+age

 params={"msg":msg,}

 return render(request,'pg013_makeview/recieve.html',params);