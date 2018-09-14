from rest_framework import generics
from rest_framework import permissions
from .serializers import PostModelSerializer
from django.db.models import Q
from posts.models import Post
from .pagination import StandardResultsPagination
from rest_framework.views import APIView
from rest_framework.response import Response

class LikeToggleAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, pk, format=None):
        post_qs = Post.objects.filter(pk=pk)
        message = "Not Allowed"
        if request.user.is_authenticated():
            is_liked = Post.objects.like_toggle(request.user, post_qs.first())
            return Response({"liked": is_liked})
        return Response({"message": message}, status=400)

class ShareAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, pk, format=None):
        post_qs = Post.objects.filter(pk=pk)
        if post_qs.exists() and post_qs.count() == 1:
            # if request.user.is_authenticated():
            new_post = Post.objects.share(request.user, post_qs.first())
            if new_post is not None:
                data = PostModelSerializer(new_post).data
                return Response(data)
        return Response(None, status=400)

class PostCreateAPIView(generics.CreateAPIView):
    serializer_class = PostModelSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class PostListAPIView(generics.ListAPIView):
    serializer_class = PostModelSerializer
    pagination_class = StandardResultsPagination

    def get_serializer_context(self, *args, **kwargs):
            context = super(PostListAPIView, self).get_serializer_context(*args, **kwargs)
            context['request'] = self.request
            return context

    def get_queryset(self, *args, **kwargs):
        requested_user = self.kwargs.get("username")
        if requested_user:
            qs = Post.objects.filter(user__username=requested_user).order_by('-timestamp')
        else:
            im_following = self.request.user.profile.get_following()
            qs1 = Post.objects.filter(user__in=im_following)
            qs2 = Post.objects.filter(user=self.request.user)
            qs = (qs1 | qs2).distinct().order_by('-timestamp')
        query = self.request.GET.get('q', None)
        if query is not None:
            qs = qs.filter(
                Q(content__icontains = query) |
                Q(user__username__icontains = query))
        return qs
    