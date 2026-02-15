from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from user.models import User


class UserAdmin(BaseUserAdmin):
    list_display = ("username", "email", "role", "is_staff")
    fieldsets = BaseUserAdmin.fieldsets + (
        ("Role", {"fields": ("role",)}),
    )


admin.site.register(User, UserAdmin)
