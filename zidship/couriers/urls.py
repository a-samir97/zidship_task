from email.mime import base
from rest_framework.routers import DefaultRouter
from .views import ShipmentViewSet
router = DefaultRouter()

router.register("shipments", ShipmentViewSet, basename="shipment-viewset")

urlpatterns = router.urls