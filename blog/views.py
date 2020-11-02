from django.shortcuts import render

#fakeposts
posts =[
    {
        'author': 'user1',
        'title': 'Blog Post 1',
        'content': 'Hello world',
        'date': 'August 12 2002'
    },
    {
        'author': 'user2',
        'title': 'Blog Post 2',
        'content': 'Fortnite <3',
        'date': 'August 13 2002'
    }
]


def home(request): #request is always needed
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)# subdirectory in templates folder
                                            #render returns httpresponse !!!
def about(request):
    return render(request, 'blog/about.html', {'title': 'Seminar Blog'})

