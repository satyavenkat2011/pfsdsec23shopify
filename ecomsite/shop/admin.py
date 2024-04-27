from django.contrib import admin
from .models import Products
from .models import Order
# Register your models here.

admin.site.site_header = "E-Commerce Site"
admin.site.site_title = "Shpping"
admin.site.index_title = "Manage Shopping"

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title','price','discount_price','category')
    search_fields= ( 'title',)
    list_editable = ('price','discount_price',)
admin.site.register(Products,ProductAdmin)
admin.site.register(Order)