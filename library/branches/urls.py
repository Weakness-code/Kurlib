from django.urls import path
from . import views

urlpatterns = [
    path('', views.branches),
    path('<int:pk>', views.BranchDetailView.as_view(), name='branch_detail'),
]