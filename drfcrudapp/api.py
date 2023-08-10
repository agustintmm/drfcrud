from .models import *
from rest_framework import viewsets, permissions
from .serializers import *

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProductoSerializer
    
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PostSerializer
    
class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CursoSerializer