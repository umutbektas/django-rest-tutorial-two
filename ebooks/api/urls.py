from django.urls import path
from ebooks.api.views import EbookListCreateAPIView, EbookDetailAPIView, ReviewCreateAPIView, ReviewDetailAPIView


urlpatterns = [
    path('', EbookListCreateAPIView.as_view(), name="ebooks-list"),
    path('<int:pk>/', EbookDetailAPIView.as_view(), name="ebooks-detail"),
    path('<int:ebook_pk>/review/', ReviewCreateAPIView.as_view(), name="ebooks-review"),
    path('review/<int:ebook_pk>/', ReviewDetailAPIView.as_view(), name="ebooks-review-detail"),
]