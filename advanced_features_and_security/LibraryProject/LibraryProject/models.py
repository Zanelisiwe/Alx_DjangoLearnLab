from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.core.validators import FileExtensionValidator
from django.db import models


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, username, email=None, password=None, **extra_fields):
        if not username:
            raise ValueError("The username must be set")
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        if password:
            user.set_password(password)
        else:
            user.set_unusable_password()
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        return self.create_user(username, email=email, password=password, **extra_fields)


class User(AbstractUser):
    # ✅ Your custom fields:
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(
        upload_to="profile_photos/",
        null=True, blank=True,
        validators=[FileExtensionValidator(allowed_extensions=["jpg", "jpeg", "png", "gif"])],
        help_text="Optional profile image."
    )

    objects = UserManager()  # plug in the custom manager

    def __str__(self):
        return self.username
