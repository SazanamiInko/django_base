from django.urls import path
from .views import MemberView
from .views import ListView
from .views import SettingTimeoutView

urlpatterns = [
    path('', MemberView.as_view(), name='input'),
    path('list', ListView.as_view(), name='list'),
    path('setting_session', SettingTimeoutView.as_view(), name='setting_session')
]
