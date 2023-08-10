from .models import *
from rest_framework import viewsets, permissions, filters
from .serializers import *

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProductoSerializer
    filter_backends = [filters.OrderingFilter]
    ordering = ['id']
    
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PostSerializer
    filter_backends = [filters.OrderingFilter]
    ordering = ['id']
    
class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CursoSerializer
    filter_backends = [filters.OrderingFilter]
    ordering = ['id']