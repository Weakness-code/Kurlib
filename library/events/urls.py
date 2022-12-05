from django.urls import path
from . import views

urlpatterns = [
    path('', views.events),
    path('<int:pk>', views.EventDetailView.as_view(), name="event_detail"),
]