from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from .models import Book, UserPreference
from .serializers import BookSerializer, UserPreferenceSerializer

class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class UserPreferenceCreateView(APIView):
    def post(self, request):
        serializer = UserPreferenceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookRecommendationView(APIView):
    def get(self, request):
        user = request.user
        liked_books = UserPreference.objects.filter(user=user, preference=UserPreference.LIKE).values_list('book__genre', flat=True)
        recommendations = Book.objects.filter(genre__in=liked_books).exclude(userpreference__user=user)
        serializer = BookSerializer(recommendations, many=True)
        return Response(serializer.data)
