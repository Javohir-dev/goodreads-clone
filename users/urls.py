from django.urls import path

from .views import RegisterView, LoginView, ProfileView

app_name = "users"
urlpatterns = [
    path('dashboard/', ProfileView.as_view(), name='profile'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
]