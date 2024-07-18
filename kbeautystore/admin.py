from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', ]  # Customize the fields displayed in the admin list view

admin.site.register(Product, ProductAdmin)
from .models import Category

from django.contrib import admin
from .models import Category, Product

class ProductInline(admin.TabularInline):
    model = Product
    extra = 0  # To display only existing products by default
    fields = ['name', 'price']  # Customize the fields displayed in the inline form

class CategoryAdmin(admin.ModelAdmin):
    inlines = [ProductInline]
    list_display = ['name']  # Customize the fields displayed in the category admin list view

admin.site.register(Category, CategoryAdmin)

# admin.py

from django.contrib import admin
from .models import FAQ

class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer')
    search_fields = ['question']  # Add search functionality by question

admin.site.register(FAQ, FAQAdmin)


# admin.py

from django.contrib import admin
from .models import Notification

class NotificationAdmin(admin.ModelAdmin):
    list_display = ('message', 'created_at')
    search_fields = ('message',)
    readonly_fields = ('created_at',)

admin.site.register(Notification, NotificationAdmin)

from django.contrib import admin
from .models import Subscription


from django.contrib import admin
from .models import Subscription

class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('email', 'date_subscribed')
    search_fields = ('email',)
    list_filter = ('date_subscribed',)

# Register the model with the admin site
admin.site.register(Subscription, SubscriptionAdmin)


