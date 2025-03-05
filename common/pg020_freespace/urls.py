from django.urls import path
from .views import questionnaireView

urlpatterns = [
    path('', questionnaireView.as_view(), name='questionnaire')
]