from django.urls import path
from rest_framework import routers
from .views import RetseptAPIViewSet,ProductViewSet,DeliverViewSet




router = routers.DefaultRouter()
router.register(r'retsept', RetseptAPIViewSet,basename='food')
router.register(r'product',ProductViewSet,basename='product')
router.register(r'deliver',DeliverViewSet,basename='deliver')
urlpatterns = router.urls