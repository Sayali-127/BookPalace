from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    cover_image = models.ImageField(upload_to="book_covers")

    def __str__(self):
        return self.title
    
class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added_on = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.quantity} x {self.book.title}'
