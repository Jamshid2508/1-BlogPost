from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Post
from django.urls import reverse_lazy

# Create your views here.


class BlogPostView(ListView):
  model = Post
  template_name = 'home.html'


class DetailView(DetailView):
  model = Post
  template_name = 'post_detail.html'


class CreateViewBlog(CreateView):
  model = Post
  template_name = 'post_new.html'

  fields = [
    'title',
    'author',
    'body'
  ]

class BlogUpdateView(UpdateView):
  model = Post

  template_name = 'post_edit.html'

  fields = ['title', 'body']


class BlogDeleteView(DeleteView):
   model = Post

   template_name = 'delete.html'
   success_url = reverse_lazy('home')