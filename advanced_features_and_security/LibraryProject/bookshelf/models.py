from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError
from django.utils import timezone


# ---------- helpers / validators ----------
def profile_upload_path(instance, filename):
    return f"profile_photos/{instance.pk or 'new'}/{filename}"


def validate_file_size(value, max_mb: int = 5):
    if value and value.size > max_mb * 1024 * 1024:
        raise ValidationError(f"File too large. Max size is {max_mb}MB.")


# ---------- Custom User ----------
class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not username:
            raise ValueError("The username must be set")
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        # set_password(None) makes an unusable password, which is acceptable if you ever create passwordless users.
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email=None, password=None, **extra_fields):
        """
        Create and save a regular user.
        """
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        """
        Create and save a superuser.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(username, email, password, **extra_fields)


class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(
        upload_to=profile_upload_path,
        null=True,
        blank=True,
        validators=[
            FileExtensionValidator(allowed_extensions=["jpg", "jpeg", "png", "gif"]),
            validate_file_size,  # optional size cap
        ],
    )

    REQUIRED_FIELDS = ["email", "date_of_birth"]
    objects = CustomUserManager()

    def clean(self):
        super().clean()
        if self.date_of_birth and self.date_of_birth > timezone.now().date():
            raise ValidationError({"date_of_birth": "Date of birth cannot be in the future."})

    def __str__(self):
        return self.username


# ---------- Book model ----------
class Book(models.Model):
    title = models.CharField(max_length=200, db_index=True)
    author = models.CharField(max_length=100, db_index=True)
    publication_year = models.IntegerField()

    class Meta:
        permissions = [
            ("can_create", "Can create a book"),
            ("can_delete", "Can delete a book"),
        ]

    def __str__(self):
        return f"{self.title} by {self.author} ({self.publication_year})"
