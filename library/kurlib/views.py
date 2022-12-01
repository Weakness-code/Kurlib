from django.shortcuts import render


def index(request):
    return render(request, 'kurlib/index.html')


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


def book_novelties(request):
    return render(request, 'kurlib/bookNovelties.html')


def fund_prohorov(request):
    return render(request, 'kurlib/fund_Prohorov.html')


def gnnk(request):
    return render(request, 'kurlib/partnersNKK.html')
