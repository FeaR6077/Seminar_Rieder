from django.shortcuts import render



posts = [
    {
        'author': 'kevin',
        'title': 'Moin Moin',
        'content': 'gerade aufgestanden, erstmal ne Runde Fortnite',
        'date_posted': '27.Oktober.2020'
    },
    {
        'author': 'bastian',
        'title': 'Anker lichten!',
        'content': 'AHOOOOOOOOOOOOOOOIIIIIIIIIIII IHR LANDRATTEN!',
        'date_posted': '27.Oktober.2020'
    },
    {
        'author': 'julian',
        'title': 'Motiviert',
        'content': 'richtig Bock auf Kosten',
        'date_posted': '12.Oktober.2020'
    },
    { 
        'author': 'torben',
        'title': 'Hello World',
        'content': '\N{winking face}',
        'date_posted': '06.Oktober.2020'
    }
    
]


# Create your views here.
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

