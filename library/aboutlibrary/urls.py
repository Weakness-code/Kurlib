from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.about_library),
    path('library_history', views.library_history),
    path('documents', views.documents),
    path('reports', views.reports),
    path('kuraginsky', views.kuraginskiy, ),
    path('branches/', include('branches.urls')),
]