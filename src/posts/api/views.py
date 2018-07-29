from rest_framework import generics
from .serializers import PostModelSerializer
from posts.models import Post


class PostListAPIView(generics.ListAPIView):
    serializer_class = PostModelSerializer

    def get_queryset(self):
        return Post.objects.all()
    