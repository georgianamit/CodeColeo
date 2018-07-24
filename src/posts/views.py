from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Post

# Create your views here.

def check(request):
    return render(request, "posts/check.html", {'sidebar': False})

