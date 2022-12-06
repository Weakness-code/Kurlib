from django.urls import path
from . import views

urlpatterns = [
    path('', views.local_history),
    path('/<int:pk>', views.LocalHistoryDetailView.as_view(), name="localhistory_info")
]