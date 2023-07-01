from django.views.generic import View, CreateView, DetailView
from django.views.generic.edit import UpdateView, DeleteView
from .models import Post
from .forms import PostForm
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.shortcuts import render


class HomeView(View):
    # model = Post
    template_name = 'home.html'
    paginate_by = 1

    def get(self, request):
        posts = Post.objects.all()
        paginator = Paginator(posts, self.paginate_by)

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context = {
            'post_list': page_obj
        }

        return render(request, self.template_name, context)


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_single.html'


class PostNewView(CreateView):
    model = Post
    template_name = 'post_new.html'
    form_class = PostForm
    success_url = reverse_lazy('home')
    # fields = ['title', 'excerpt', 'body', 'author', 'date', 'photo']


class PostUpdateView(UpdateView):
    model = Post
    template_name = 'post_update.html'
    fields = ['title', 'excerpt', 'body', 'photo']


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')
