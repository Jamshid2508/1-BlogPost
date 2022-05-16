from django.urls import path

from .views import BlogPostView, DetailView, CreateViewBlog, BlogUpdateView, BlogDeleteView

urlpatterns = [
    path('post/<int:pk>/delete', BlogDeleteView.as_view(), name='delete'),
    path('post/<int:pk>/edit', BlogUpdateView.as_view(), name='post_edit'),
    path('post/new/', CreateViewBlog.as_view(), name='post_new'),
    path('', BlogPostView.as_view(), name='home'),
    path('post/<int:pk>', DetailView.as_view(), name='post_detail')
]
