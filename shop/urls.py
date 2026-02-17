from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    # Home/Product List
    path('', views.product_list, name='product_list'),
    
    # Static Content Pages
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('blog/', views.blog_detail, name='blog'),
    
    # Product Detail
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
    
    # Placeholder for Cart/Checkout (Abhi ke liye error rokne ke liye)
    path('cart/', views.product_list, name='cart'), 
    path('checkout/', views.product_list, name='checkout'),
]
