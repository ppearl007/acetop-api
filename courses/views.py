from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request, 'index.html')

def hello(request):
    return HttpResponse("Hello courses page.")

def test(request):
    return HttpResponse("You're at the test page.")