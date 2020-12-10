from django.urls import path
from .views import (
 PostListView,
 PostDetailView, 
 PostCreateView,
 PostUpdateView,
 PostDeleteView
)
from . import views

#returns views.home when opens that path
urlpatterns = [
    #path = blog/'' "/" is important
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'), ## pk = Primary Key
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    #path = blog/about/ "/" is important
    path('', views.home, name='blog-home'),#name = name for path pattern (f.e NAV-BAR)
    path('about/', views.about, name='blog-about'),
    path('register/', views.about, name='blog-register'),
]
