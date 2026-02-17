from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('about/', views.about, name='about'),           # About Page
    path('blog/', views.blog_detail, name='blog_detail'), # Blog Page
    path('contact/', views.contact, name='contact'),     # Contact Page
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
]
