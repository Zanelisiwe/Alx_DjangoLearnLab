from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from .views import register_view, profile_view

urlpatterns = [
    # home page (works with LOGIN_REDIRECT_URL = "/")
    path('',TemplateView.as_view(template_name='blog/base.html'), name='home'),

    # Auth routes
    path('login/', auth_views.LoginView.as_view(
        template_name='registration/login.html'
    ), name='login'),
    path('logout/', auth_views.LogoutView.as_view(
        template_name='registration/logout.html'
    ), name='logout'),
    path('register/', register_view, name='register'),
    path('profile/', profile_view, name='profile'),
]
