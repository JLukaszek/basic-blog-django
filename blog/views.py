from django.views.generic import ListView, TemplateView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Post


class HomePageView(ListView):
    model = Post
    paginate_by = 4
    template_name = 'blog/blog.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'body']
    template_name = 'blog/post_create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'body']
    template_name = 'blog/post_edit.html'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('blog:home')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class AboutPageView(TemplateView):
    template_name = 'blog/about.html'



