from typing import Any, Dict
from django.views.generic import View, CreateView, DetailView, FormView
from django.views.generic.edit import UpdateView, DeleteView
from .models import Post
from .forms import PostForm, CommentForm
from django.urls import reverse_lazy, reverse
from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.generic.detail import SingleObjectMixin


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


class CommentGet(DetailView):
    model = Post
    template_name = 'post_single.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        return context


class CommentPost(SingleObjectMixin, FormView):
    model = Post
    form_class = CommentForm
    template_name = "post_single.html"

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.post = self.object
        comment.author = self.request.user
        comment.save()
        return super().form_valid(form)

    def get_success_url(self):
        post = self.get_object()
        return reverse("post_detail", kwargs={'pk': post.pk})


class PostDetailView(View):

    def get(self, request, *args, **kwargs):
        view = CommentGet.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = CommentPost.as_view()
        return view(request, *args, **kwargs)


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
