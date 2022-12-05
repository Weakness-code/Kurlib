from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('services', views.services),
    path('questionAnswer', views.questions_answers),
    path('contacts', views.contacts),
    path('eventscard', views.events_card),
    path('whitecrown', views.white_crown),
]