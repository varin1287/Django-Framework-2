from django.contrib import admin

from mainapp.models import ProductCategory, Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity', 'price', 'id')
    list_display_links = ('name',)


admin.site.register(ProductCategory)
admin.site.register(Product, ProductAdmin)
