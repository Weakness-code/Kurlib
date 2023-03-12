from django.shortcuts import render
from django.views.generic import DetailView

from .models import Rules, Competition, NewWork

def reader(request):
    rules = Rules.objects.all()
    return render(request, 'reader/reader.html', {'rules': rules})


def book_novelties(request):
    works = NewWork.objects.all()
    return render(request, 'reader/bookNovelties.html', {'works': works})


def fund_prohorov(request):
    return render(request, 'reader/fund_Prohorov.html')


def gnnk(request):
    return render(request, 'reader/partnersNKK.html')

def virtual_performance(request):
    virtualcards = NewWork.objects.all()
    return render(request, 'reader/virtualExhibitionSlider.html',{'virtualcards':virtualcards})

class VirtualCardDetailView(DetailView):
    model = NewWork
    template_name = 'reader/virtualExhibitionCard.html'
    context_object_name = "virtualcard"
    def get_object(self, queryset=None):
        obj = super(VirtualCardDetailView, self).get_object(queryset=queryset)
        obj.edited_description = info_editor(obj.description)
        return obj

def competitions(request):
    comps = Competition.objects.order_by('date_end')
    return render(request, 'reader/competitions.html', {'competitions': comps})

def info_editor(info: str):
    text = info.split("\n")
    for _ in text:
        _ = '<p class="eventCard__text">' + _ + '</p>'
    return text