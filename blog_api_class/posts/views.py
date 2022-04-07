import imp
from rest_framework import generics
from .models import Post
from .serializers import PostSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from accounts.permissions import IsAuthorOrReadOnly
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [AllowAny]
    
    
    @method_decorator(cache_page(60*2))
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthorOrReadOnly]
