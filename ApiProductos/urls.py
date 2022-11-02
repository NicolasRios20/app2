from rest_framework import routers
from .api import ProductoviewSet 

router = routers.DefaultRouter()
router.register('api/ApiProductos',ProductoviewSet,'ApiProductos')

urlpatterns = router.urls