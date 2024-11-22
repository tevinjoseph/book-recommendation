from django.contrib.auth.models import User
from .models import Book
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse

class UserDetailViewTests(APITestCase):
    """
    Test cases for UserDetailView API.
    """

    def setUp(self):
        """
        Set up initial test data.
        """
        # Create test users
        self.user1 = User.objects.create_user(
            username='john_doe',
            email='john@example.com',
            first_name='John',
            last_name='Doe'
        )
        self.user2 = User.objects.create_user(
            username='jane_doe',
            email='jane@example.com',
            first_name='Jane',
            last_name='Doe'
        )
        self.client = APIClient()

    def test_fetch_user_details_success(self):
        """
        Test fetching user details with a valid ID.
        """
        url = reverse('user-detail', args=[self.user1.id])  # URL for user1
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], self.user1.id)
        self.assertEqual(response.data['username'], self.user1.username)
        self.assertEqual(response.data['email'], self.user1.email)
        self.assertEqual(response.data['first_name'], self.user1.first_name)
        self.assertEqual(response.data['last_name'], self.user1.last_name)

    def test_fetch_user_details_not_found(self):
        """
        Test fetching user details with an invalid ID.
        """
        url = reverse('user-detail', args=[999])  # Non-existent user ID
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data['error'], 'User not found')


class BookListCreateView(APITestCase):
    """
    Test cases for BookListCreateView API.
    """

    def setUp(self):
        """
        Set up initial test data.
        """
        # Create test users
        self.book1 = Book(
            title='Lets Talk Money',
            author='Monika Halan',
            genre='Finance',
            published_date='2018-07-05'
        ).save()
        self.client = APIClient()

    def test_fetch_books_success(self):
        """
        Test fetching list of books
        """
        url = reverse('book-list-create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [{'id': 1, 'title': 'Lets Talk Money', 'author': 'Monika Halan', 'genre': 'Finance', 'published_date': '2018-07-05'}])