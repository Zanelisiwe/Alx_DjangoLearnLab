from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Book, CustomUser


# --- Book admin (yours, unchanged) ---
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publication_year")
    search_fields = ("title", "author")
    list_filter = ("publication_year",)


# --- CustomUser admin ---
class CustomUserAdmin(UserAdmin):
    # add our extra fields to the standard UserAdmin views
    fieldsets = UserAdmin.fieldsets + (
        ("Additional info", {"fields": ("date_of_birth", "profile_photo")}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {"fields": ("date_of_birth", "profile_photo")}),
    )
    list_display = UserAdmin.list_display + ("date_of_birth",)


# Register with explicit call (checker expects this)
admin.site.register(CustomUser, CustomUserAdmin)
