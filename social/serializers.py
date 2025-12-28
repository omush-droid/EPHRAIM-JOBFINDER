from rest_framework import serializers
from .models import Follow, Notification

class FollowSerializer(serializers.ModelSerializer):
    follower_name = serializers.CharField(source='follower.username', read_only=True)
    following_name = serializers.CharField(source='following.username', read_only=True)
    
    class Meta:
        model = Follow
        fields = ['id', 'follower', 'follower_name', 'following', 'following_name', 'created_at']
        read_only_fields = ['follower', 'created_at']

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['id', 'type', 'message', 'is_read', 'created_at']
        read_only_fields = ['type', 'message', 'created_at']