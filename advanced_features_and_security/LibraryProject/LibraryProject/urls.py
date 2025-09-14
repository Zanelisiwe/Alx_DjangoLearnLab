from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path("admin/", admin.site.urls),

    # Built-in auth views: /accounts/login/, /accounts/logout/, password reset, etc.
    path("accounts/", include("django.contrib.auth.urls")),

    # Bookshelf app routes
    path("books/", include("bookshelf.urls")),

    # A tiny home page so login redirects have somewhere to land (optional)
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
]

# Serve uploaded media (e.g., profile photos) during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
