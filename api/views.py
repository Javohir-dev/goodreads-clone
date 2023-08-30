from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from books.models import BookReview

from api.serializers import BookReviewSerializer


class BookReviewDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        book_review = BookReview.objects.get(id=id)
        serializer = BookReviewSerializer(book_review)

        return Response(data=serializer.data)
    
    def delete(self, request, id):
        book_review = BookReview.objects.get(id=id)
        book_review.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, id):
        book_review = BookReview.objects.get(id=id)
        serializer = BookReviewSerializer(instance=book_review, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id):
        book_review = BookReview.objects.get(id=id)
        serializer = BookReviewSerializer(instance=book_review, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookReviewsAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        book_reviews = BookReview.objects.all().order_by('-created_at')

        paginator = PageNumberPagination()
        page_obj = paginator.paginate_queryset(book_reviews, request)
        serializer = BookReviewSerializer(page_obj, many=True)

        return paginator.get_paginated_response(serializer.data)
    
    def post(self, request):
        serializer = BookReviewSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
