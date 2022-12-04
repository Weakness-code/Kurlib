from django.urls import path
from . import views

urlpatterns = [
    path('', views.reader),
    path('new-books', views.book_novelties),
    path('prohorov', views.fund_prohorov),
    path('gnkk', views.gnnk),
    path('virtualperformance', views.virtual_performance),
    path('virtualcard', views.virtual_card),
    path('competitions', views.competitions),
]