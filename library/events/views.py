from django.shortcuts import render
from django.views.generic import DetailView
from .models import Event
def events(request):
    events_all = Event.objects.all()
    return render(request, 'events/events.html', {'events': events_all})

class EventDetailView(DetailView):
    model = Event
    template_name = 'events/eventsCard.html'
    context_object_name = "event"
