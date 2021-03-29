from django.contrib import admin

from ordersapp.models import Order, OrderItem


class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'updated', 'status', 'is_active')
    list_display_links = ('user',)


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity')
    list_display_links = ('order', 'product')


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
