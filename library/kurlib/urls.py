from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('services', views.services),
    path('events', views.events),
    path('localHistory', views.local_history),
    path('questionAnswer', views.questions_answers),
    path('contacts', views.contacts),
    path('eventscard', views.events_card),
    path('whitecrown', views.white_crown),
]