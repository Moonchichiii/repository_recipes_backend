from rest_framework import viewsets
from .models import Post
from .serializers import PostSerializer
from utils.permissions import IsOwnerOrReadOnly

from utils.permissions import IsAuthenticatedOrReadOnlyForPost


# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnlyForPost]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)