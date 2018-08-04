from rest_framework import serializers
from posts.models import Post
from accounts.api.serializers import UserDisplaySerializer
from django.utils.timesince import timesince


class PostModelSerializer(serializers.ModelSerializer):
    user = UserDisplaySerializer(read_only=True)
    date_display = serializers.SerializerMethodField()
    timesince = serializers.SerializerMethodField()
    class Meta:
        model = Post
        fields =[
            'user',
            'content',
            'timestamp',
            'date_display',
            'timesince'
        ]
    
    def get_date_display(self,obj):
        return obj.timestamp.strftime("%b %d %I:%M %p")

    def get_timesince(self, obj):
        if timesince(obj.timestamp)[0] is '0':
            return "Just Now"
        else:
            return timesince(obj.timestamp) + " ago"
