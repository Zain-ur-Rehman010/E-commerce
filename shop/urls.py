from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    # 1. Landing Page (Jab website open ho)
    # Yeh views.home ko call karega jo 'shop/product/index.html' render karta hai
    path('', views.home, name='home'),

    # 2. Shop Page (Jab Shop link par click ho)
    # Yeh 'shop/pages/shop/index.html' render karega
    path('shop/', views.product_list, name='product_list'),
    
    # Category Filter Support
    path('category/<slug:category_slug>/', views.product_list, name='product_list_by_category'),

    # Static Content Pages
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('blog/', views.blog, name='blog'),

    # Product Detail
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),

    # Placeholders
    path('cart/', views.product_list, name='cart'), 
    path('checkout/', views.product_list, name='checkout'),
]
