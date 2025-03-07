from django.urls import path
from .views import WeighttView

urlpatterns = [
    path('', WeighttView.as_view(), name='weight')
]