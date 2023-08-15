from django.urls import path

from .views import (
    RegisterView,
    LoginView,
    ProfileView,
    LogoutView,
    ProfileUpdateView,
)

app_name = "users"
urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('dashboard/', ProfileView.as_view(), name='profile'),
    path('dashboard/edit/', ProfileUpdateView.as_view(), name='profile_edit'),
]
