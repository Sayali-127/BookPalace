<<<<<<< HEAD
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
=======
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User, AnonymousUser
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Book, CartItem,  NewBook, Wishlist, Order , Address
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.db import IntegrityError
from django.http import Http404



import razorpay


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

@login_required
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

def new_arrivals(request):
   
    new_books = NewBook.objects.all().order_by('title')  
    return render(request, 'new_arrivals.html', {'new_books': new_books})

def blog(request):
    return render(request, 'blog.html')

def search(request):
    query = request.GET.get('query', '')  
    books = Book.objects.filter(title__icontains=query)  
    context = {'books': books}  
    return render(request, 'search.html', context) 
   


def new_bookdetail(request, pk):
    newbook = get_object_or_404(NewBook, pk=pk)  
    return render(request, 'new_bookdetail.html', {'newbook': newbook})


@login_required
def add_to_wishlist(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    Wishlist.objects.get_or_create(user=request.user, book=book)
    return redirect('wishlist')  

@login_required
def remove_from_wishlist(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    Wishlist.objects.filter(user=request.user, book=book).delete()
    return redirect('wishlist')  

@login_required
def wishlist(request):
    wishlist_books = Wishlist.objects.filter(user=request.user)
    return render(request, 'wishlist.html', {'wishlist_books': wishlist_books})

@login_required
def buy_now(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if request.method == 'POST':
        
        order_data = {
            'book_id': book.id,
            'amount': int(book.price * 100),  
            'currency': 'INR',
        }
        request.session['order'] = order_data  
        return redirect('address', book_id=book.id)  

    return render(request, 'buy_now.html', {'book': book})

# def address(request):
#     if request.user.is_authenticated:
#         if request.method=="POST":
#             new_address = request.POST['address']
#             new_pincode = request.POST['pincode']
#             total_addresses = Address.objects.filter(user = request.user)
#             if len(total_addresses) < 3:
#                 add_address = Address.objects.create(user=request.user,address=new_address,pincode=new_pincode)
#                 add_address.save()
#                 return redirect('address')
#             else:
#                 address = Address.objects.filter(user = request.user)
#                 return render(request,"address.html",{'address':address})
#         else:
#             address = Address.objects.filter(user = request.user)
#             return render(request,"address.html",{'address':address})
#     else:
#         return redirect('login')
@login_required
def address(request):
    book_id = request.GET.get('book_id')  # Get the book_id from query parameters
    book = get_object_or_404(Book, id=book_id) if book_id else None
    existing_addresses = Address.objects.filter(user=request.user)
    
    return render(request, "address.html", {'address': existing_addresses, 'book': book})
    
def delete_address(request,id):
    if request.user.is_authenticated:
        address = Address.objects.filter(user=request.user,id=id)
        address.delete()
        return redirect('address')
    
def update_address(request,id):
    if request.user.is_authenticated:
        address = Address.objects.filter(user=request.user)
        update_address = get_object_or_404(Address,user=request.user,id = id)
        if request.method =="POST":
            update_address.address=request.POST.get('address')
            update_address.pincode=request.POST.get('pincode')
            update_address.save()
            return redirect('address')
        else:
            return render(request,"address.html",{'update_address':update_address,'address':address})
    else:
        return redirect('signin')


# def confirm_order(request,id):
#     if request.user.is_authenticated:
        
#         address = Address.objects.get(id=id,user=request.user)
#     else:
#         return redirect('signin')
#     context = {}
    
#     context['address'] = address
#     list=[]
#     total_price = 0
    
#     return render(request,"confirm_order.html",context)



@login_required
def confirm_order(request, address_id, book_id=None):
    cart_item = CartItem.objects.filter(user=request.user)
    address = get_object_or_404(Address, id=address_id, user=request.user)

    if book_id and book_id != '0':  # Ensure that book_id is not '0'
        book = get_object_or_404(Book, id=book_id)
        total_price = book.price
        items = None
        total_quantity = 1
    else:
        # Handle cart ordering when no valid book_id is provided
        cart_items = CartItem.objects.filter(user=request.user)
        items = cart_items
        total_price = sum(item.book.price * item.quantity for item in cart_items)
        total_quantity = len(cart_items)

    context = {
        'address': address,
        'book': book if book_id and book_id != '0' else None,
        'items': items,
        'total_price': total_price,
        'total_quantity': total_quantity,
    }

    return render(request, 'payment.html', context)


# @login_required
# def payment_view(request, book_id, address_id):
#     book = get_object_or_404(Book, id=book_id)
#     address = get_object_or_404(Address, id=address_id, user=request.user)

#     client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
#     amount = int(float(book.price) * 100)

#     try:
#         order_data = {
#             'amount': amount,
#             'currency': 'INR',
#             'receipt': f'order_rcptid_{book.id}_{address.id}',
#             'payment_capture': '1',
#         }
#         order = client.order.create(data=order_data)

#         new_order = Order(
#             user=request.user,
#             book=book,
#             address=address,
#             razorpay_order_id=order['id'],
#             amount=book.price  
#         )
#         new_order.save()

#     except Exception as e:
#         return render(request, 'error.html', {'error': str(e)})

#     context = {
#         'order_id': order['id'],
#         'amount': book.price,
#         'razorpay_key': settings.RAZORPAY_KEY_ID,
#         'address': address,
#         'book': book,
#     }

#     return render(request, 'payment.html', context)

@login_required
def payment_view(request, book_id, address_id):
    # Get book and address based on IDs
    book = get_object_or_404(Book, id=book_id)
    address = get_object_or_404(Address, id=address_id, user=request.user)

    # Initialize Razorpay client
    client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

    # Calculate the amount in paisa
    amount = int(float(book.price) * 100) 

    try:
        # Create Razorpay order
        order_data = {
            'amount': amount,
            'currency': 'INR',
            'receipt': f'order_rcptid_{book.id}_{address.id}',
            # 'payment_capture': '1',  # Auto capture payment
        }
        order = client.order.create(data=order_data)

        # Save the order in your database
        new_order = Order(
            user=request.user,
            book=book,
            address=address,
            razorpay_order_id=order['id'],
            amount=book.price
        )
        new_order.save()

    except Exception as e:
        # Handle errors during Razorpay order creation
        return render(request, 'error.html', {'error': str(e)})

    # Pass order details and Razorpay keys to the template
    context = {
        'order_id': order['id'],
        'amount': book.price,
        'razorpay_key': settings.RAZORPAY_KEY_ID,
        'address': address,
        'book': book,
    }

    return render(request, 'payment.html', context)


@login_required
def payment_success(request):
    
    return render(request, 'success.html', {'message': 'Thank you for your order! Your order will be delivered within 7-8 days.'})

@login_required
def my_orders(request):

    orders = Order.objects.filter(user=request.user)
    
    context = {
        'orders': orders
    }
    return render(request, 'my_orders.html', context) 
>>>>>>> 2c9025f (Initial commit with requirements.txt)
