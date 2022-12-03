from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('about', views.about_library),
    path('reader', views.reader),
    path('services', views.services),
    path('events', views.events),
    path('localHistory', views.local_history),
    path('questionAnswer', views.questions_answers),
    path('contacts', views.contacts),
    path('library_history', views.library_history),
    path('documents', views.documents),
    path('reports', views.reports),
    path('branches', views.branches),
    path('kuraginsky', views.kuraginskiy,),
    path('new-books', views.book_novelties),
    path('prohorov', views.fund_prohorov),
    path('gnkk', views.gnnk),
    path('<int:pk>', views.BranchDetailView.as_view(), name='branch_detail'),
]
