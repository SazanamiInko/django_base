from django.urls import path
from .views import ScoreListView

urlpatterns = [
    path('', ScoreListView.as_view(), name='index'),
 ]
