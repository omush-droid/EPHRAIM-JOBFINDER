from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from accounts.models import User
from .models import Follow, Notification
from .serializers import FollowSerializer, NotificationSerializer

class FollowViewSet(viewsets.ModelViewSet):
    serializer_class = FollowSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return Follow.objects.filter(follower=self.request.user)
    
    @action(detail=False, methods=['post'])
    def follow_user(self, request):
        user_id = request.data.get('user_id')
        user_to_follow = get_object_or_404(User, id=user_id)
        
        if user_to_follow == request.user:
            return Response({'error': 'Cannot follow yourself'}, status=status.HTTP_400_BAD_REQUEST)
        
        follow, created = Follow.objects.get_or_create(
            follower=request.user,
            following=user_to_follow
        )
        
        if created:
            Notification.objects.create(
                user=user_to_follow,
                type='follow',
                message=f'{request.user.username} started following you'
            )
            return Response({'message': 'Successfully followed user'}, status=status.HTTP_201_CREATED)
        return Response({'message': 'Already following this user'}, status=status.HTTP_200_OK)
    
    @action(detail=False, methods=['post'])
    def unfollow_user(self, request):
        user_id = request.data.get('user_id')
        user_to_unfollow = get_object_or_404(User, id=user_id)
        
        try:
            follow = Follow.objects.get(follower=request.user, following=user_to_unfollow)
            follow.delete()
            
            Notification.objects.create(
                user=user_to_unfollow,
                type='unfollow',
                message=f'{request.user.username} unfollowed you'
            )
            return Response({'message': 'Successfully unfollowed user'}, status=status.HTTP_200_OK)
        except Follow.DoesNotExist:
            return Response({'error': 'Not following this user'}, status=status.HTTP_400_BAD_REQUEST)

class NotificationViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return Notification.objects.filter(user=self.request.user)
    
    @action(detail=True, methods=['patch'])
    def mark_read(self, request, pk=None):
        notification = self.get_object()
        notification.is_read = True
        notification.save()
        return Response({'message': 'Notification marked as read'})