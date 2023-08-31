from api.views import BookReviewViewsSet
from rest_framework.routers import DefaultRouter

app_name = "api"

router = DefaultRouter()
router.register('reviews', BookReviewViewsSet, basename='review')
urlpatterns = router.urls
