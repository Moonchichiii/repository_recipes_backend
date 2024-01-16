from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from followers.models import Follow  
from .serializers import FollowSerializer



# Create your views here.

class FollowViewSet(viewsets.ModelViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        if serializer.validated_data['follower'] == serializer.validated_data['following']:
            return Response({"detail": "You cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)
        serializer.save(follower=self.request.user.profile)

    @action(detail=False, methods=['get'])
    def following(self, request):
        user_profile = request.user.profile
        following = user_profile.following.all()
        serializer = self.get_serializer(following, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def followers(self, request):
        user_profile = request.user.profile
        followers = user_profile.followers.all()
        serializer = self.get_serializer(followers, many=True)
        return Response(serializer.data)
