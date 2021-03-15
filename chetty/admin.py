from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Customer)
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('name',)}

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('name',)}

admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)