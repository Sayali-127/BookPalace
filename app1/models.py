<<<<<<< HEAD
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
=======
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.utils import timezone
from django import forms

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
    
class NewBook(models.Model):  
    
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    cover_image = models.ImageField(upload_to="book_covers")

    def __str__(self):
        return self.title

    def __str__(self):
        return self.title

class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s Wishlist"
    
# class SavedAddress(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     full_name = models.CharField(max_length=100)
#     phone_number = models.CharField(max_length=15, default='')  # Set a default value here
#     address = models.TextField()
#     city = models.CharField(max_length=100)
#     zip_code = models.CharField(max_length=10)
#     country = models.CharField(max_length=100)

#     def __str__(self):
#         return f"{self.full_name} - {self.address}, {self.city}, {self.zip_code}, {self.country}"
    
class Address(models.Model):
    address = models.TextField()
    pincode = models.IntegerField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    razorpay_order_id = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
>>>>>>> 2c9025f (Initial commit with requirements.txt)
