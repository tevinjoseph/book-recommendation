from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):
    title = models.CharField(max_length=200, help_text="Enter the title of the book")
    author = models.CharField(max_length=100, help_text="Enter the author's name")
    genre = models.CharField(max_length=50, help_text="Enter the genre of the book")
    published_date = models.DateField(help_text="Enter the publication date of the book")

    def __str__(self):
        return self.title
    
class UserPreference(models.Model):
    LIKE = 'like'
    DISLIKE = 'dislike'
    PREFERENCE_CHOICES = [
        (LIKE, 'Like'),
        (DISLIKE, 'Dislike'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    preference = models.CharField(max_length=10, choices=PREFERENCE_CHOICES)

    def __str__(self):
        return f"{self.user.username} - {self.book.title} - {self.preference}"