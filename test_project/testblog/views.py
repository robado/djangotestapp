from django.shortcuts import render

# from django.http import HttpResponse

# Create your views here.

posts = [
    {
        'author': 'Robert',
        'title': 'Robertin Blogi',
        'content': 'Test Blog Post',
        'date_posted': 'Syyskuuta 22, 1994'
    },
    {
        'author': 'Sinkki',
        'title': 'Sinkin Blogi',
        'content': 'Test Blog Post Toinen',
        'date_posted': 'Uusikuusi 22, 1991'
    }
]

'''def home(request):
    return HttpResponse('<H1>First View - Home</h1>')'''


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


'''When I tried to do \'blog/home.html\' it said template does not exist so I had to just type \'home.html\'. But I 
was missing a \"blog\" directory from templates'''


def about(request):
    return render(request, 'blog/about.html')


def third(request):
    return render(request, 'blog/third.html')
