from rest_framework.routers import DefaultRouter
from .views import PriceIndexViewset


router = DefaultRouter()
router.register('price/', PriceIndexViewset, basename='price')


urlpatterns = [
    
] + router.urls