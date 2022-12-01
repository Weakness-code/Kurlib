from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('reader', views.reader),
    path('services', views.services),
    path('events', views.events),
    path('localHistory', views.local_history),
    path('questionAnswer', views.questions_answers),
    path('contacts', views.contacts),
    path('new-books', views.book_novelties),
    path('prohorov', views.fund_prohorov),
    path('gnkk', views.gnnk),
]