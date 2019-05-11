from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home(request):
    return HttpResponse('<H1>First View - Home</h1>')


def about(request):
    return HttpResponse('<H1>Second View - About</h1>')


def third(request):
    return HttpResponse('<H1>This is my Third view</h1>')
