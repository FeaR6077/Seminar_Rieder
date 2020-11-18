from django.shortcuts import render
from .models import Post  # import Postclass


# Create your views here.
def home(request):
        from django.utils import translation
                #set a language key!
                # user_language = 'de'
                # translation.activate(user_language)
                # request.session[translation.LANGUAGE_SESSION_KEY] = user_language
        if translation.LANGUAGE_SESSION_KEY in request.session:
                del request.session[translation.LANGUAGE_SESSION_KEY]

        context = {"posts": Post.objects.all()}
        return render(request, "blog/home.html", context)


def about(request):
    return render(request, "blog/about.html", {"title": "About"})
