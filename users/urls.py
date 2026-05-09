from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users.apps import UsersConfig
from users.views import LogoutConfirmView, UserCreateView, email_verification

app_name = UsersConfig.name

urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutConfirmView.as_view(), name='logout'),
    path('logout/confirm/', LogoutView.as_view(), name='logout_confirm'),
    path('register/', UserCreateView.as_view(), name='register'),
    path('confirm/<str:token>/', email_verification, name='confirm_email'),
]

