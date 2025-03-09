from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView
from django.contrib.auth.views import LoginView, LogoutView
from .forms import UserRegisterForm, ProfileEditForm
from .models import CustomUser
from django.contrib.auth.mixins import LoginRequiredMixin


class ProfileView(LoginRequiredMixin, DetailView):
    """
    Представление просмотра профиля.
    """

    model = CustomUser
    template_name = "users/profile.html"
    context_object_name = "user_profile"

    def get_object(self):
        return self.request.user


class ProfileEditView(LoginRequiredMixin, UpdateView):
    """
    Представление редактирования профиля.
    """

    model = CustomUser
    form_class = ProfileEditForm
    template_name = "users/profile_edit.html"
    success_url = reverse_lazy("profile")

    def get_object(self):
        return self.request.user


class UserRegisterView(CreateView):
    """
    Представление для регистрации пользователя.
    """

    form_class = UserRegisterForm
    template_name = "users/register.html"
    success_url = reverse_lazy("login")


class UserLoginView(LoginView):
    """
    Представление для входа пользователя.
    """

    template_name = "users/login.html"
    redirect_authenticated_user = True  # Перенаправлять авторизованных пользователей


class UserLogoutView(LogoutView):
    """
    Представление для выхода пользователя.
    """

    template_name = "users/logout.html"
    next_page = reverse_lazy("logout")
