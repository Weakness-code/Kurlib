from django.shortcuts import render
from .models import Rules, Competition, NewWork, VirtualCard

def reader(request):
    rules = Rules.objects.all()
    return render(request, 'reader/reader.html', {'rules': rules})


def book_novelties(request):
    return render(request, 'reader/bookNovelties.html')


def fund_prohorov(request):
    return render(request, 'reader/fund_Prohorov.html')


def gnnk(request):
    return render(request, 'reader/partnersNKK.html')

def virtual_performance(request):
    return render(request, 'reader/virtualExhibitionSlider.html')

def virtual_card(request):
    return render(request, 'reader/virtualExhibitionCard.html')

def competitions(request):
    comps = Competition.objects.order_by('date_end')
    return render(request, 'reader/competitions.html', {'competitions': comps})