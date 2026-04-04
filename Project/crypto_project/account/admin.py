from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ('email', 'full_name', 'role', 'terms_accepted', 'is_staff')
    search_fields = ('email', 'full_name', 'username')
    ordering = ('email',)
    fieldsets = BaseUserAdmin.fieldsets + (
        ('MVP Profile', {'fields': ('full_name', 'role', 'terms_accepted', 'terms_accepted_at')}),
    )
