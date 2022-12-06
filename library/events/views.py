from django.shortcuts import render
from django.views.generic import DetailView
from .models import Event


def events(request):
    events_all = Event.objects.order_by('date')
    return render(request, 'events/events.html', {'events': events_all})

class EventDetailView(DetailView):
    model = Event
    template_name = 'events/eventsCard.html'
    context_object_name = "event"
    def get_object(self, queryset=None):
        obj = super(EventDetailView, self).get_object(queryset=queryset)
        obj.month = month_determination(obj.date.month)
        obj.edited_info = info_editor(obj.main_info)
        return obj


def month_determination(month: int):
    months = {1: "Января",
             2: "Февраля",
             3: "Марта",
             4: "Апреля",
             5: "Мая",
             6: "Июня",
             7: "Июля",
             8: "Августа",
             9: "Сентября",
             10: "Октября",
             11: "Ноября",
             12: "Декабря",
             }
    return months[month]

def info_editor(info: str):
    text = info.split("\n")
    for _ in text:
        _ = '<p class="eventCard__text">' + _ + '</p>'
    return text