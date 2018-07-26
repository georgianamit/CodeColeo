from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView
from .models import Post
from .forms import PostModelForm
# Create your views here.

class PostCreateView(CreateView):
    form_class = PostModelForm
    template_name = 'posts/post_create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["sidebar"] = True
        return context
    


class PostDetailView(DetailView):
    template_name = "posts/post_detail.html"
    # queryset = Post.objects.all()

    def get_object(self):
        pk = self.kwargs.get('pk')
        return Post.objects.get(id=pk)

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



