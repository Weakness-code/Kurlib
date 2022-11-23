from django.shortcuts import render


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
