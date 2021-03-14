from django.contrib import admin

from basketapp.models import Basket

class BasketAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product', 'quantity')

admin.site.register(Basket, BasketAdmin)






