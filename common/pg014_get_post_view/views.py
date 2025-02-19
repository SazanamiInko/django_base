from django.shortcuts import render
from django.http import HttpResponse

#投稿ページ
def memory(request):
 if (request.method=='POST'):
  msg="前の思い出:"+request.POST['memory'];
  params={"msg":msg,};
 else:
  params={"msg":"",};
 return render(request,'pg014_get_post_view/memory.html',params);
