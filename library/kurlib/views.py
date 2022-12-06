from django.shortcuts import render
from .models import QuestionAnswer, Partners, Billboard
from django.apps import apps

def month_determination(month):
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

def index(request):
    model = apps.get_model('events', 'Event')
    events = model.objects.order_by('-date')[:3]
    for event in events:
        event.month = month_determination(event.date.month)
    event_1 = events[0]
    event_2 = events[1]
    event_3 = events[2]

    partners = Partners.objects.all()
    for i in range(len(partners)):
        partners[i].number = i%3

    billboard = Billboard.objects.all()
    return render(request, 'kurlib/index.html', {'event_1': event_1,
                                                 'event_2': event_2,
                                                 'event_3': event_3,
                                                 'partners': partners,
                                                 'billboard': billboard})


def services(request):
    return render(request, 'kurlib/services.html')


def questions_answers(request):
    qa = QuestionAnswer.objects.all()
    return render(request, 'kurlib/questions.html', {"qa": qa})


def contacts(request):
    return render(request, 'kurlib/contacts.html')

