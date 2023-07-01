from django.urls import path
from .views import HomeView, PostNewView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('post/new', PostNewView.as_view(), name='newpost')
]
