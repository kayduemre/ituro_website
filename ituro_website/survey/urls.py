from django.conf.urls import url
from django.urls import path
from survey.views import SurveyCreateView

urlpatterns = [
    path('<slug:slug>/$', SurveyCreateView.as_view(),
        name="survey_create"),
]
