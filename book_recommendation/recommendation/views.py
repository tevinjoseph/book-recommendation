from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from itertools import chain
from .models import Book, UserPreference
from .serializers import BookSerializer, UserSerializer, UserPreferenceSerializer


class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(APIView):
    """
    API View to fetch user details by ID.
    """

    def get(self, request, user_id):
        try:
            # Fetch the user by ID
            user = User.objects.get(id=user_id)
            serializer = UserSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response(
                {"error": "User not found"},
                status=status.HTTP_404_NOT_FOUND
            )


class UserPreferenceView(APIView):
    def post(self, request, user_id):
        request.data["user"] = user_id
        # Prevent duplicate preferences (a user cannot "like" and "dislike" the same book)
        book = request.data["book"]
        user_preference = UserPreference.objects.filter(user=user_id, book=book)
        if user_preference:
            return Response(["A user cannot 'like' and 'dislike' the same book"], status=status.HTTP_400_BAD_REQUEST)

        serializer = UserPreferenceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, user_id):
        book = request.data["book"]
        UserPreference.objects.filter(user=user_id, book=book).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class BookRecommendationView(APIView):
    def get(self, request, user_id):
        liked_books = UserPreference.objects.filter(user=user_id, preference=UserPreference.LIKE).values_list('book__genre', flat=True)
        recommendations = Book.objects.filter(genre__in=liked_books).exclude(userpreference__user=user_id)
        random_recommendation = Book.objects.exclude(genre__in=liked_books).first()
        recommendations = list(chain(recommendations, [random_recommendation]))
        serializer = BookSerializer(recommendations, many=True)
        return Response(serializer.data)
