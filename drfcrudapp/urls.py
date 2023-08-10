from rest_framework import routers
from .api import *

router = routers.DefaultRouter()

router.register('api/productos', ProductoViewSet, 'productos')
router.register('api/posts', PostViewSet, 'posts')
router.register('api/cursos', CursoViewSet, 'cursos')

urlpatterns = router.urls

