from django.shortcuts import render, redirect
from .models import Post
from .forms import Post_forms
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# Create your views here.


class PostList(ListView):  # need query , all is default
    model = Post
    # template_name :app/model_list.html
    # context_object_name  : object_list or model_list


class PostDetail(DetailView):
    model = Post
    # Optional: defaults to blog/post_detail.html
    # Optional: defaults to 'object'


class PostCreate(CreateView):
    model = Post
    fields = '__all__'
    success_url = '/blog'  # Optional: defaults to blog/post_form.html


class PostUpdata(UpdateView):
    model = Post
    fields = '__all__'
    success_url = '/blog'  # the same file template
    # template_name = 'blog/post_edit.html'


class PostDelete(DeleteView):
    model = Post
    success_url = '/blog'
