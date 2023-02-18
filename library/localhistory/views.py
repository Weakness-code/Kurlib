from django.shortcuts import render
from django.views.generic import DetailView
from .models import LocalHistoryModel


def local_history(request):
    articles = LocalHistoryModel.objects.order_by('title')
    kuraginsky_district = list()
    kuragino = list()
    villages_towns = list()
    memorial_plaques = list()
    kuragintsy_ww2 = list()
    literary_map = list()
    cult_art_lib = list()
    history_names = list()
    for article in articles:
        if article.chapter == 1:
            kuraginsky_district.append(article)
        elif article.chapter == 2:
            kuragino.append(article)
        elif article.chapter == 3:
            villages_towns.append(article)
        elif article.chapter == 4:
            memorial_plaques.append(article)
        elif article.chapter == 5:
            kuragintsy_ww2.append(article)
        elif article.chapter == 6:
            literary_map.append(article)
        elif article.chapter == 7:
            cult_art_lib.append(article)
        elif article.chapter == 8:
            history_names.append(article)
    return render(request, 'localhistory/localHistory.html', {'articles': articles,
                                                              'kuraginsky_district': kuraginsky_district,
                                                              'kuragino': kuragino,
                                                              'villages_towns': villages_towns,
                                                              'memorial_plaques': memorial_plaques,
                                                              'kuragintsy_ww2': kuragintsy_ww2,
                                                              'literary_map': literary_map,
                                                              'cult_art_lib': cult_art_lib,
                                                              'history_names': history_names})

class LocalHistoryDetailView(DetailView):
    model = LocalHistoryModel
    template_name = 'localhistory/localhistory_layout.html'
    context_object_name = "localhistory_layout"

    def get_object(self, queryset=None):
        obj = super(LocalHistoryDetailView, self).get_object(queryset=queryset)
        obj.edited_description = info_editor(obj.description)
        obj.images = []
        for i in range(20):
            try:
                eval(f"obj.images.append(obj.image_{i}.url)")
            except ValueError:
                break
        return obj

def info_editor(info: str):
    text = info.split("\n")
    return text