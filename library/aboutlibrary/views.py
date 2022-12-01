from django.shortcuts import render
from .models import Documents, Reports

def about_library(request):
    return render(request, 'aboutlibrary/aboutLibrary.html')


def library_history(request):
    return render(request, 'aboutlibrary/aboutLibraryHistory.html')


def documents(request):
    docs = Documents.objects.all()
    return render(request, 'aboutlibrary/documents.html', {'documents': docs})


def reports(request):
    reps = Reports.objects.all()
    return render(request, 'aboutlibrary/reports.html', {'reports': reps})


def kuraginskiy(request):
    return render(request, 'aboutlibrary/citesKuraginskiy.html')
