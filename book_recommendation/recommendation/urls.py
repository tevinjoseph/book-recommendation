from django.urls import path
from .views import BookListCreateView, UserListCreateView, UserDetailView, UserPreferenceCreateView, BookRecommendationView

urlpatterns = [
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    path('users/<int:id>/', UserDetailView.as_view(), name='user-detail'),
    path('users/', UserListCreateView.as_view(), name='user-list-create'),
    path('preferences/', UserPreferenceCreateView.as_view(), name='user-preference-create'),
    path('recommendations/', BookRecommendationView.as_view(), name='book-recommendation'),
]