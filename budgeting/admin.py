from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["email", "password", "is_logged_in", "is_active", "token", "access_token"]}),
    ]
    list_display = ["email", "password", "is_logged_in", "is_active", "token", "access_token"]
    list_filter = ["email", "token", "access_token"]
    search_fields = ["email", "token", "access_token"]

admin.site.register(User, UserAdmin)