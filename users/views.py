from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from .forms import UserRegisterForm

class UserRegisterView(CreateView):
    """
    Представление для регистрации пользователя.
    """
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('login')

class UserLoginView(LoginView):
    """
    Представление для входа пользователя.
    """
    template_name = 'users/login.html'
    redirect_authenticated_user = True  # Перенаправлять авторизованных пользователей

class UserLogoutView(LogoutView):
    """
    Представление для выхода пользователя.
    """
    template_name = 'users/logout.html'
    next_page = reverse_lazy('home')