from django.shortcuts import render
from django.http import HttpResponse


def home(requests):
    return HttpResponse("hello vansh its home")


def templates(requests):
    person = [
        {'Name': 'vansh', 'Age': '19'},
        {'Name': 'harsh', 'Age': '29'},
        {'Name': 'suresh', 'Age': '21'},
        {'Name': 'dinesh', 'Age': '25'},
        {'Name': 'ramesh', 'Age': '56'},
    ]
    return render(requests, 'index.html', context={'persons': person})
