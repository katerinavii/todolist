from django.contrib import admin
from core.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    readonly_fields = ('last_login', 'date_joined')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (
            'Personal Info',
            {'fields': ('email', 'first_name', 'last_name')}
        ),
        (
            'Permission',
            {'fields': ('is_active', 'is_superuser', 'is_staff')}
        ),
        (
            'Important dates',
            {'fields': ('last_login', 'date_joined')}
        )
    )
