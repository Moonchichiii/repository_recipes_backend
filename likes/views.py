from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Like
from .serializers import LikeSerializer, PostSerializer

class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

    def perform_create(self, serializer):
        if Like.objects.filter(profile=self.request.user.profile, post_id=self.request.data['post']).exists():
            return Response(status=status.HTTP_409_CONFLICT)
        serializer.save(profile=self.request.user.profile)

    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated])
    def user_likes(self, request):
        user_profile = request.user.profile
        likes = Like.objects.filter(profile=user_profile)
        liked_posts = [like.post for like in likes]
        serializer = PostSerializer(liked_posts, many=True)
        return Response(serializer.data)
        
        