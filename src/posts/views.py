from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.views import View
from .models import Post
from .forms import PostModelForm
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class ShareView(View):
    def get(self, request, pk, *args, **kwargs):
        post = get_object_or_404(Post, pk=pk)
        if request.user.is_authenticated():
            new_post = Post.objects.share(request.user, post)
            return HttpResponseRedirect("/")
        return HttpResponseRedirect(post.get_absolute_url())

class PostCreateView(CreateView):
    form_class = PostModelForm
    template_name = 'posts/post_create.html'
    # success_url = "/post/list/"

    def form_valid(self,form):
        form.instance.user = self.request.user
        return super(PostCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["sidebar"] = True
        return context
    
class PostUpdateView(UpdateView):
    queryset = Post.objects.all()
    form_class = PostModelForm
    template_name = 'posts/post_update.html'
    success_url = "/post/list/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["sidebar"] = False
        return context

class PostDeleteView(DeleteView):
    model = Post
    template_name = "posts/post_delete.html"
    success_url = reverse_lazy('post:List')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["sidebar"] = False
        return context
    

class PostDetailView(DetailView):
    template_name = "posts/post_detail.html"
    # queryset = Post.objects.all()

    def get_object(self):
        pk = self.kwargs.get('pk')
        return Post.objects.get(id=pk)

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context["sidebar"] = False
        return context
    

class PostListView(LoginRequiredMixin, ListView):
    template_name = "posts/post_list.html"

    def get_queryset(self, *args, **kwargs):
        qs = Post.objects.all().order_by('-timestamp')
        query = self.request.GET.get('q', None)
        if query is not None:
            qs = qs.filter(
                Q(content__icontains = query) |
                Q(user__username__icontains = query))
        return qs

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        context["sidebar"] = False
        context['form'] = PostModelForm()
        context['post_url'] = reverse_lazy("post:create")
        return context



