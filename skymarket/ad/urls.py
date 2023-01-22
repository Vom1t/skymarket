
from rest_framework import routers
from ad.views import AdViewSet

router = routers.SimpleRouter()
router.register('Ad', AdViewSet)
router.register('Comment', AdViewSet)

urlpatterns = [
]

urlpatterns += router.urls