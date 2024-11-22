from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
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

    def get(self, request, id, *args, **kwargs):
        try:
            # Fetch the user by ID
            user = User.objects.get(id=id)
            serializer = UserSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response(
                {"error": "User not found"},
                status=status.HTTP_404_NOT_FOUND
            )


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
