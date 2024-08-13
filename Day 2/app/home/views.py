from django.shortcuts import render
from django.http import HttpResponse


def home(requests):
    return HttpResponse("Hey its Vansh Server chimchapak dam dam")
  
def templates(requests):
  return render(requests,'index.html')
