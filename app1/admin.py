<<<<<<< HEAD
from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price')  # Columns to display in the list view
    search_fields = ('title', 'author')  # Searchable fields in the admin interface
    list_filter = ('author',)  # Filters to add to the list view
    ordering = ('title',)  # Default ordering of books in the list view
    fields = ('title', 'author', 'description', 'price', 'cover_image')  # Fields to display in the form
=======
from django.contrib import admin
from .models import Book , NewBook

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price')  
    search_fields = ('title', 'author')  
    list_filter = ('author',) 
    ordering = ('title',)  
    fields = ('title', 'author', 'description', 'price', 'cover_image')  

@admin.register(NewBook)
class newBookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price')  
    search_fields = ('title', 'author') 
    list_filter = ('author',)  
    ordering = ('title',)  
    fields = ('title', 'author', 'description', 'price', 'cover_image')  

    

  

>>>>>>> 2c9025f (Initial commit with requirements.txt)
