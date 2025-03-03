from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User, AnonymousUser
from django.http import HttpResponse
from .models import Book
from django.contrib.auth.decorators import login_required
from .models import Book, CartItem
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def Home(request):
    return render(request,"index.html")


def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if password == password2:
            if User.objects.filter(username=username).exists():
                return HttpResponse("Username already exists")
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                auth_login(request, user)
                return redirect('login')  # Redirect to a home page after registration
        else:
            return HttpResponse("Passwords do not match")
    return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('Home')  # Redirect to a home page after login
        else:
            return HttpResponse("Invalid login credentials")
    return render(request,'login.html')


def logout(request):
    auth_logout(request)
    return redirect('Home')

def book_list(request):
    books = Book.objects.all()
    context={'books':books}
    return render(request, 'book_list.html', context)

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'book_detail.html', {'book': book})

def purchase(request, pk):
    # Add your purchase logic here
    return render(request, 'purchase_success.html')


def add_to_cart(request, book_id):

    if isinstance(request.user, AnonymousUser):
        return redirect('/login/?next=/cart/') 
    book = get_object_or_404(Book, id=book_id)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, book=book)
    
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    
    return redirect('cart')  # Redirect to the cart page

def cart(request):
    if not request.user.is_authenticated:
        return render(request, 'login.html', {'login_message': 'Please log in to view your cart.'})

    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.book.price * item.quantity for item in cart_items)
    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})

    



def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id)
    cart_item.delete()
    return redirect('cart')

def update_cart_quantity(request, item_id):
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        cart_item = get_object_or_404(CartItem, id=item_id)
        
        if quantity > 0:
            cart_item.quantity = quantity
            cart_item.save()
        else:
            cart_item.delete()
        
    return redirect('cart')

def contact_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Example of sending an email (adjust as needed)
        send_mail(
            f'Contact Us Form Submission from {name}',
            message,
            email,
            [settings.CONTACT_EMAIL],  # Set this in your settings
            fail_silently=False,
        )

        messages.success(request, 'Your message has been sent successfully!')
        return redirect('contact_us')

    return render(request, 'contact.html')