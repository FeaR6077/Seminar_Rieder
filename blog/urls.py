from django.urls import path
from . import views

#returns views.home when opens that path
urlpatterns = [
    #path = blog/'' "/" is important
    path('', views.home, name='blog-home'),
    #path = blog/about/ "/" is important
    path('', views.home, name='blog-home'),#name = name for path pattern (f.e NAV-BAR)
    path('about/', views.about, name='blog-about'),
    path('register/', views.about, name='blog-register'),
]
