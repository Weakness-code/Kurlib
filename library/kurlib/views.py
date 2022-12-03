from django.shortcuts import render
from django.views.generic import DetailView
from .models import Branches


class BranchDetailView(DetailView):
    model = Branches
    template_name = 'kurlib/branch_template.html'
    context_object_name = "branch"


def index(request):
    return render(request, 'kurlib/index.html')


def about_library(request):
    return render(request, 'kurlib/aboutLibrary.html')


def reader(request):
    return render(request, 'kurlib/reader.html')


def services(request):
    return render(request, 'kurlib/services.html')


def events(request):
    return render(request, 'kurlib/events.html')


def local_history(request):
    return render(request, 'kurlib/localHistory.html')


def questions_answers(request):
    return render(request, 'kurlib/questions.html')


def contacts(request):
    return render(request, 'kurlib/contacts.html')


def library_history(request):
    return render(request, 'kurlib/aboutLibraryHistory.html')


def documents(request):
    return render(request, 'kurlib/documents.html')


def reports(request):
    return render(request, 'kurlib/reports.html')


def branches(request):
    branches_objects = Branches.objects.all()
    return render(request, 'kurlib/branchesAbout.html', {'branches': branches_objects})


def kuraginskiy(request):
    return render(request, 'kurlib/citesKuraginskiy.html')


def book_novelties(request):
    return render(request, 'kurlib/bookNovelties.html')


def fund_prohorov(request):
    return render(request, 'kurlib/fund_Prohorov.html')


def gnnk(request):
    return render(request, 'kurlib/partnersNKK.html')
