from django.views.generic import TemplateView, CreateView
from .models import Post
from .forms import PostForm
from django.urls import reverse_lazy


class HomeView(TemplateView):
    template_name = 'home.html'


class PostNewView(CreateView):
    model = Post
    template_name = 'post_new.html'
    form_class = PostForm
    success_url = reverse_lazy('home')
    # fields = ['title', 'excerpt', 'body', 'author', 'date', 'photo']
