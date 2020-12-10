from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
 ListView,
 DetailView,
 CreateView,
 UpdateView, 
 DeleteView
)
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

class PostListView(ListView):
        model = Post
        template_name = 'blog/home.html'
        context_object_name = 'posts'
        ordering = ['-date_posted']  ### den ältesten Post als erstes anzeigen

class PostDetailView(DetailView):
        model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
        model = Post
        fields = ['title', 'content']

        def form_valid(self, form):
                form.instance.author = self.request.user
                return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
        model = Post
        fields = ['title', 'content']

        def form_valid(self, form):
                form.instance.author = self.request.user
                return super().form_valid(form)

        def test_func(self):
                post = self.get_object()
                if self.request.user == post.author:
                        return True
                return False

## success-url: damit es zu keinem fehler kommt und der Post gelöscht wird

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
        model = Post
        success_url = '/' 


        def test_func(self):
                post = self.get_object()
                if self.request.user == post.author:
                        return True
                return False


def about(request):
    return render(request, "blog/about.html", {"title": "About"})
