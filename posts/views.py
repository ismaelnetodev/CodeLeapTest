from django.shortcuts import render
from rest_framework import viewsets
from .models import Post
from .serializers import PostSerializer
# Create your views here.

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_datetime')
    serializer_class = PostSerializer

    def create(self, request, *args, **kwargs):
        request.data['username'] = request.data.get('username', 'anonymous')
        return super().create(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        for field in ['id', 'username', 'created_datetime']:
            if field in request.data:
                request.data.pop(field)
        return super().partial_update(request, *args, **kwargs)