from django.urls import path, include
from rest_framework.routers import SimpleRouter, DefaultRouter
from product.views import ProductViewSet, CategoryViewSet

# router = SimpleRouter()
router = DefaultRouter()
router.register('products', ProductViewSet)
router.register('categories', CategoryViewSet)

# urlpatterns = router.urls

urlpatterns = [
    path('', include(router.urls)),
    # rest of urls 
    # path('contact/', ),
]