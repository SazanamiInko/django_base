from django.urls import path
from . import views

urlpatterns = [
    path('<str:title>/<str:start>/<str:end>/', views.index, name='index'),
]