from django.urls import path
from .views import BookListCreateView, UserListCreateView, UserDetailView, UserPreferenceView, BookRecommendationView

urlpatterns = [
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    path('users/<int:user_id>/', UserDetailView.as_view(), name='user-detail'),
    path('users/<int:user_id>/preferences/', UserPreferenceView.as_view(), name='user-preference'),
    path('users/', UserListCreateView.as_view(), name='user-list-create'),
    path('recommendations/', BookRecommendationView.as_view(), name='book-recommendation'),
]