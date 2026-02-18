from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Shop app ka rasta
    path('', include('shop.urls', namespace='shop')),
    path('', include('shop.urls')),
    
    # Cart aur Orders ke raste badal kar 'shop.cart' aur 'shop.orders' karein
    path('cart/', include('shop.cart.urls', namespace='cart')),
    path('orders/', include('shop.orders.urls', namespace='orders')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
