from django.shortcuts import render
from django.views.generic import DetailView
from .models import LocalHistoryModel


def local_history(request):
    return render(request, 'localhistory/localHistory.html')


class LocalHistoryDetailView(DetailView):
    model = LocalHistoryModel
    template_name = 'localhistory/localhistory_layout.html'
    context_object_name = "localhistory_layout"