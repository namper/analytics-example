from rest_framework.routers import SimpleRouter
from facebook_statistics import viewsets

router = SimpleRouter()
router.register('posts', viewsets.PostViewSet)

urlpatterns = router.urls
