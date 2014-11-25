from django.contrib import admin

from .models import Product, ProductPicture


admin.site.register(Product, admin.ModelAdmin)
admin.site.register(ProductPicture, admin.ModelAdmin)
