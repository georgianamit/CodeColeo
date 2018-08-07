from django.contrib.auth.models import User
from rest_framework import serializers
from django.urls import reverse_lazy

class UserDisplaySerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'url'
        ]
    
    def get_url(self, obj):
        return reverse_lazy("profiles:detail",kwargs={"username":obj.username})