from django.shortcuts import render
from .models import QuestionAnswer

def index(request):
    return render(request, 'kurlib/index.html')


def services(request):
    return render(request, 'kurlib/services.html')


def questions_answers(request):
    qa = QuestionAnswer.objects.all()
    return render(request, 'kurlib/questions.html', {"qa": qa})


def contacts(request):
    return render(request, 'kurlib/contacts.html')

