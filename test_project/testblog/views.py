from django.shortcuts import render

# from django.http import HttpResponse

# Create your views here.


'''def home(request):
    return HttpResponse('<H1>First View - Home</h1>')'''


def home(request):
    return render(request, 'blog/home.html')


'''When I tried to do \'blog/home.html\' it said template does not exist so I had to just type \'home.html\'. But I 
was missing a \"blog\" directory from templates'''


def about(request):
    return render(request, 'blog/about.html')


def third(request):
    return render(request, 'blog/third.html')
