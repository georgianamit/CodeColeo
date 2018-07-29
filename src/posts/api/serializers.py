from rest_framework import serializers
from posts.models import Post
from accounts.api.serializers import UserDisplaySerializer
class PostModelSerializer(serializers.ModelSerializer):
    user = UserDisplaySerializer()
    class Meta:
        model = Post
        fields =[
            'user',
            'content'
        ]
