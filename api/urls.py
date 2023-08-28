from django.urls import path
from api.views import BookReviewDetailAPIView, BookReviewsAPIView

app_name = "api"
urlpatterns = [
    path("review/<int:id>/", BookReviewDetailAPIView.as_view(), name="review_detail"),
    path("reviews/", BookReviewsAPIView.as_view(), name="reviews"),
]
