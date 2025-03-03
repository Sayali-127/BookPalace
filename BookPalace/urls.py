<<<<<<< HEAD
"""
URL configuration for BookPalace project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Home, name='Home'),
    path('signup',views.signup,name='signup'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('book_list', views.book_list, name='book_list'),
    path('book/<int:pk>/', views.book_detail, name='book_detail'),
    path('book/<int:pk>/purchase/', views.purchase, name='purchase'),
    path('cart/', views.cart, name='cart'),
    path('cart/add/<int:book_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:cart_item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('update_quantity/<int:item_id>/', views.update_cart_quantity, name='update_cart_quantity'),
    path('contact/', views.contact_form, name='contact')


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
=======
"""
URL configuration for BookPalace project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from app1 import views




urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Home, name='Home'),
    path('signup',views.signup,name='signup'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('book_list', views.book_list, name='book_list'),
    path('book/<int:pk>/', views.book_detail, name='book_detail'),
    path('book/<int:pk>/purchase/', views.purchase, name='purchase'),
    path('cart/', views.cart, name='cart'),
    path('cart/add/<int:book_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:cart_item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('update_quantity/<int:item_id>/', views.update_cart_quantity, name='update_cart_quantity'),
    path('contact/', views.contact_form, name='contact'),
    path('new_arrivals/', views.new_arrivals, name='new_arrivals'),
    path('newbook/<int:pk>/', views.new_bookdetail, name='new_bookdetail'),
    path('blog/',views.blog, name='blog'),
    path('search/',views.search,name='search'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('wishlist/add/<int:book_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('wishlist/remove/<int:book_id>/', views.remove_from_wishlist, name='remove_from_wishlist'),
    path('buy-now/<int:book_id>/', views.buy_now, name='buy_now'),
    path('address',views.address,name="address"),
    path('delete_address/<int:id>',views.delete_address,name="delete_address"),
    path('update_address/<int:id>',views.update_address,name="update_address"),
    path('confirm_order/<int:address_id>/<int:book_id>/', views.confirm_order, name="confirm_order"),
    path('payment/<int:book_id>/<int:address_id>/', views.payment_view, name='payment'),  
    path('payment/success/', views.payment_success, name='payment_success'),
    path('my-orders/', views.my_orders, name='my_orders'),
  


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
>>>>>>> 2c9025f (Initial commit with requirements.txt)
