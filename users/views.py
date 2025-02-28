import secrets
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from config.settings import EMAIL_HOST_USER
from .models import CustomUser
from .forms import ProfileForm, CustomUserCreationForm

from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from .forms import UserRegistrationForm

class UserLoginView(LoginView):
    template_name = 'users/login.html'

class UserLogoutView(LogoutView):
    next_page = '/'

class UserRegisterView(CreateView):
    form_class = UserRegistrationForm
    template_name = 'users/register.html'
    success_url = '/login/'


class UserViewSet:
    def list(self, request):
        users = CustomUser.objects.all()
        return render(request, 'users/list.html', {'users': users})

@login_required
def profile(request):
    return render(request, 'users/profile.html', {'user': request.user})

@login_required
def edit_profile(request):
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('users:profile')
    else:
        form = ProfileForm(instance=request.user)
    return render(request, 'users/edit_profile.html', {'form': form})

def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            token = secrets.token_hex(16)
            user.token = token
            user.save()
            host = request.get_host()
            url = f'http://{host}/users/email-confirm/{token}/'
            send_mail(
                subject="Подтверждение почты",
                message=f"Привет, перейди по ссылке для подтверждения почты {url}",
                from_email=EMAIL_HOST_USER,
                recipient_list=[user.email],
            )
            return redirect('users:login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})

def email_verification(request, token):
    user = CustomUser.objects.get(token=token)
    user.is_active = True
    user.save()
    return redirect('users:login')