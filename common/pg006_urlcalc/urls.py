from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:left>/<int:right>', views.index, name='index')
]