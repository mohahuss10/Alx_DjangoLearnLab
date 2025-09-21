from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet

# Create a router and register the BookViewSet
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # Old endpoint from Task 1 (list only)
    path('books/', BookList.as_view(), name='book-list'),

    # Router endpoints (CRUD)
    path('', include(router.urls)),
]
