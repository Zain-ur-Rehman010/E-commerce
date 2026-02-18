from django.shortcuts import render, get_object_or_404
from .models import Category, Product

# Cart form handler
try:
    from .cart.forms import CartAddProductForm
except ImportError:
    CartAddProductForm = None

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'shop/product/index.html', {
        'category': category, 
        'categories': categories, 
        'products': products
    })

def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    context = {'product': product}
    if CartAddProductForm:
        context['cart_product_form'] = CartAddProductForm()
    return render(request, 'shop/pages/shop/product.html', context)

def about(request):
    return render(request, 'shop/pages/content/about.html')

def contact(request):
    return render(request, 'shop/pages/content/contact.html')


def blog(request):
    return render(request, 'shop/pages/content/blog.html')

def product_list(request, category_slug=None):
    # ... baki code ...
    # Path ko GitHub folder structure ke mutabiq sahi karein
    return render(request, 'shop/pages/shop/index.html', {
        'category': category, 
        'categories': categories, 
        'products': products
    })
