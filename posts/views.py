from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView

from posts.forms import PostForm
from posts.models import Post


class CreatePostView(LoginRequiredMixin, CreateView):
    template_name = "posts/new.html"
    form_class = PostForm
    success_url = reverse_lazy('posts:feed')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['profile'] = self.request.user.profile
        return context


class PostFeedView(LoginRequiredMixin, ListView):
    template_name = 'posts/feed.html'
    model = Post
    ordering = ('-created')
    paginate_by = 30
    context_object_name = 'posts'


class PostDetailView(DetailView):
    template_name = 'posts/detail.html'
    slug_field = 'pk'
    slug_url_kwarg = 'pk'
    queryset = Post.objects.all()
    context_object_name = 'post'
