from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.utils.translation import gettext_lazy as _
from django.utils.html import format_html

from .models import Book, CustomUser


# -------------------- Book admin (unchanged) --------------------
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publication_year")
    search_fields = ("title", "author")
    list_filter = ("publication_year",)


# -------------------- Custom admin forms --------------------
class CustomUserCreationAdminForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        # Include your required extras so the add form saves them
        fields = ("username", "email", "date_of_birth", "profile_photo")

class CustomUserChangeAdminForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = CustomUser
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
            "date_of_birth",
            "profile_photo",
            "is_active",
            "is_staff",
            "is_superuser",
            "groups",
            "user_permissions",
        )


# -------------------- CustomUser admin --------------------
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationAdminForm
    form = CustomUserChangeAdminForm

    # Show a small preview of the profile photo on the change page
    def profile_photo_preview(self, obj):
        if obj.profile_photo:
            return format_html('<img src="{}" style="height:40px; width:40px; object-fit:cover; border-radius:4px;" />', obj.profile_photo.url)
        return "—"
    profile_photo_preview.short_description = "Photo"

    # Add our extra fields to the standard sections
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email", "date_of_birth", "profile_photo", "profile_photo_preview")}),
        (_("Permissions"), {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )

    # Make preview read-only
    readonly_fields = ("profile_photo_preview",)

    # Add form (creation) should include your custom fields
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("username", "email", "password1", "password2", "date_of_birth", "profile_photo"),
        }),
    )

    # Nice list view & search
    list_display = ("username", "email", "first_name", "last_name", "date_of_birth", "is_staff")
    search_fields = ("username", "email", "first_name", "last_name")
    list_filter = ("is_staff", "is_superuser", "is_active", "groups")
    ordering = ("username",)
