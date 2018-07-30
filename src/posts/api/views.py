from rest_framework import generics
from rest_framework import permissions
from .serializers import PostModelSerializer
from django.db.models import Q
from posts.models import Post

class PostCreateAPIView(generics.CreateAPIView):
    serializer_class = PostModelSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class PostListAPIView(generics.ListAPIView):
    serializer_class = PostModelSerializer

    def get_queryset(self, *args, **kwargs):
        qs = Post.objects.all().order_by('-timestamp')
        query = self.request.GET.get('q', None)
        if query is not None:
            qs = qs.filter(
                Q(content__icontains = query) |
                Q(user__username__icontains = query))
        return qs
    