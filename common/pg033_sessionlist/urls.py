from django.urls import path
from .views import MemberView
from .views import ListView

urlpatterns = [
    path('', MemberView.as_view(), name='input'),
    path('list', ListView.as_view(), name='list')
]