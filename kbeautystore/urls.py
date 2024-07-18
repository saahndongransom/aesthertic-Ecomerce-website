from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views
from django.conf.urls.static import static
from django.conf import settings
from .views import subscribe, send_message_to_all,send_message_page

urlpatterns = [
    path('', views.index, name='index'), 
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('shop/', views.shop, name='shop'),
    path('shop-single/<int:product_id>/', views.shop_single, name='shop_single'),
    #path('shop-single/', views.shop_single, name='shop_single'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('products/<int:category_id>/', views.products_by_category, name='products_by_category'),
    path('paypal/process-payment/', views.paypal_process_payment, name='paypal_process_payment'),
    path('return/', views.return_page, name='return'),
    path('cancel/', views.cancel_page, name='cancel'),
    path('paypal/checkout/', views.paypal_checkout, name='paypal_checkout'),
    path('contact/success/', views.success_page, name='success_page'),
    path('faq/', views.faq, name='faq'),
    path('add_faq/', views.add_faq, name='add_faq'),
    path('simulate_notification/', views.simulate_notification, name='simulate_notification'),
    path('notifications/', views.notifications, name='notifications'),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('send_message_to_all/', send_message_to_all, name='send_message_to_all'),
    path('send_message/', send_message_page, name='send_message_page'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


