from django.shortcuts import render, get_object_or_404
#from django.http import HttpResponse
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post
from django.contrib.auth.models import User

# Create your views here.

# Dummy data
# posts = [
#     {
#         'author': 'Reghu',
#         'title': 'Blog Post 1',
#         'content': 'First post content',
#         'date_posted': 'March 10, 2020'
#     },
#     {
#         'author': 'Ram',
#         'title': 'Postit',
#         'content': 'I won Toto',
#         'date_posted': 'March 9, 2020'
#     }
# ]

# Home page
def home(request):
    #return HttpResponse('<h1>Blog Home</h1>')
    
    # this returns the home.html template in the templates dir
    # django automatically looks for the template in the app's templates dir
    # return render(request, 'blog/home.html')

    # Passing data into the template using a dictionary
    # context = {
    #     'posts': posts
    # }

    # Now query posts from the database
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

# New Home page using class views
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    # this is used to change the ordering of the posts
    # so that the newest post (by date) is displayed on top.
    ordering = ['-date_posted']
    paginate_by = 5  # this does pagination automatically in class views

class UserPostListView(ListView):
    model = Post
    template_name = 'blog/posts_user.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5  # this does pagination automatically in class views

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# The class UserPassesTestMixin is used to verify that the user updating the post
# in the same user that created the post by overring the test_func() member
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object() # get the post that we are currently trying to update
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object() # get the post that we are currently trying to update
        if self.request.user == post.author:
            return True
        return False

# About page
def about(request):
    #return HttpResponse('<h1>Blog About</h1>')
    return render(request, 'blog/about.html', {'title': 'About'})