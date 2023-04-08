from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from .models import Post
from .permissions import IsAuthOrReadOnly
from .serializers import PostSerializer, UserSerializer

User = get_user_model()


class PostViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAdminUser,)
    queryset = User.objects.all()
    serializer_class = UserSerializer
