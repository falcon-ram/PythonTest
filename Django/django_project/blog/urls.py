from django.urls import path
from .views import (
    PostListView, 
    PostDetailView, 
    PostCreateView, 
    PostUpdateView,
    PostDeleteView,
    UserPostListView
)
from . import views
from users.views import profile_summary

urlpatterns = [
    #path('', views.home, name='blog-home'),
    # Using class view instead of function view
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<str:username>', UserPostListView.as_view(), name='post-user'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('users/<int:pk>/profile_summary', profile_summary, name='user-profile-summary'),
    path('about/', views.about, name='blog-about'),
]
