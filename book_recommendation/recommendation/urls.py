from django.urls import path
from .views import BookListCreateView, UserPreferenceCreateView, BookRecommendationView

urlpatterns = [
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    path('preferences/', UserPreferenceCreateView.as_view(), name='user-preference-create'),
    path('recommendations/', BookRecommendationView.as_view(), name='book-recommendation'),
]