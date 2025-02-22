from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'owner')
    search_fields = ('name', 'owner__username')
    list_filter = ('price', 'owner')
