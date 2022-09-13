from django.urls import path

from .views import *


urlpatterns = [
        path('', AfricaView.as_view()),

        path('human', HumanView.as_view()),
    ]
