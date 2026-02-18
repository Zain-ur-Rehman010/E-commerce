from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    # Home/Product List
    path('', views.product_list, name='product_list'),
    
    # Static Content Pages
    path('about/', views.about, name='about'),
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    # Yahan 'blog' rakhein kyunke views mein hum 'blog' function banayenge
    path('blog/', views.blog, name='blog'),
    
    # Product Detail
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
    
    # Placeholders takay crash na ho
    path('cart/', views.product_list, name='cart'), 
    path('checkout/', views.product_list, name='checkout'),
]
