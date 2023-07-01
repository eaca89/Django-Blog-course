from .models import Post


def recent_posts(request):
    recent_posts = Post.objects.order_by('-date')[:5]
    return {'recent_posts': recent_posts}
