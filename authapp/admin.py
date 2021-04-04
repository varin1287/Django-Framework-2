from django.contrib import admin

from authapp.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'id')
    list_display_links = ('username',)


admin.site.register(User, UserAdmin)
