from django.urls import path
from .views import upload_resume, CnabView


urlpatterns = [
    path("data/", CnabView.as_view()),
    path('',upload_resume),
]