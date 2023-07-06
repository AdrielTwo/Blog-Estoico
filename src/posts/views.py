from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView,DetailView,UpdateView
from .models import Post, User, PostView
from .forms import CommentForm

class PostListView(LoginRequiredMixin,ListView):
    model = Post
    
    def get_queryset(self):
        queryset = super().get_queryset()
        author = User.objects.get(username='Adriel')
        queryset = queryset.filter(author=author)
        return queryset
    
class PostDetailView(DetailView):
    model = Post
    
    def post(self, *args, **kwargs):
        form = CommentForm(self.request.POST)
        if form.is_valid():
            post = self.get_object()
            comment = form.instance
            comment.user = self.request.user
            comment.post = post
            comment.save()
            return redirect("detail", slug=post.slug)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'form': CommentForm(),
        })
        return context
    
    def get_object(self, **kwargs):
        object = super().get_object(**kwargs)
        if self.request.user.is_authenticated:
            PostView.objects.get_or_create(user=self.request.user, post=object)
        return object
    
