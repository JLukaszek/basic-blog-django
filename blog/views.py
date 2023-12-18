from django.views.generic import ListView, TemplateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Post


class HomePageView(ListView):
    model = Post
    template_name = 'blog/blog.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'


class PostUpdateView(UpdateView):
    model = Post
    fields = ['title', 'body']
    template_name = 'blog/post_edit.html'


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('blog:home')


class AboutPageView(TemplateView):
    template_name = 'blog/about.html'



