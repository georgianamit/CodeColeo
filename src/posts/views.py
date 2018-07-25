from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Post

# Create your views here.

class PostDetailView(DetailView):
    template_name = "posts/post_detail.html"
    queryset = Post.objects.all()

    def get_object(self):
        return Post.objects.get(id=1)

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context["sidebar"] = True 
        return context
    

class PostListView(ListView):
    template_name = "posts/post_list.html"
    queryset = Post.objects.all()

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        context["sidebar"] = True 
        return context



