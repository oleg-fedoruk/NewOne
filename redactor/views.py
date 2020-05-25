from django.shortcuts import render
from django.views.generic import ListView,  DetailView
from django.views.generic.edit import CreateView, UpdateView
from . models import Post


class RedListView(ListView):
    model = Post
    template_name = 'home.html'


class RedDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


class RedCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = '__all__'


class RedUpdateView(UpdateView):
    model = Post
    fields = ['title', 'body']
    template_name = 'post_edit.html'
