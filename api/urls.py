from django.urls import path
from api.views import BookReviewDetailAPIView, BookListAPIView

app_name = "api"
urlpatterns = [
    path("review/<int:id>/", BookReviewDetailAPIView.as_view(), name="review_detail"),
    path("reviews/", BookListAPIView.as_view(), name="reviews"),
]
