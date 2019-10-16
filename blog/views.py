from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView


# def home(request):
#     posts = Post.objects.all()
#     context = {
#         "posts": posts
#     }
#     return render(request, "blog/home.html", context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    ordering = ['-date_posted']
    context_object_name = 'posts'


class PostDetailView(DetailView):
    model = Post


def about(request):
    return render(request, "blog/about.html")
