# from django.contrib.auth.views import LogoutView, LoginView
# from django.urls import reverse_lazy, reverse
# from django.views import View
#
# from .apps import UsersConfig
# from .forms import CustomUserCreationForm
# from django.core.mail import send_mail
# import secrets
# from config.settings import EMAIL_HOST_USER
# from .models import CustomUser
# from django.shortcuts import get_object_or_404, redirect
#
#
# class CustomLoginView(LoginView):
#     template_name = 'login.html'
#     success_url = reverse_lazy('/')
#
# class CustomLogoutView(LogoutView):
#     next_page = reverse_lazy('/')  # Перенаправление на другую страницу после выхода
#
# from django.urls import reverse_lazy
# from django.views.generic.edit import CreateView
#
#
# class RegisterView(CreateView):
#     model = CustomUser
#     template_name = 'register.html'
#     form_class = CustomUserCreationForm
#     success_url = reverse_lazy('users:login')
#
#     def form_valid(self, form):
#         user = form.save()
#         user.is_active = False
#         token = secrets.token_hex(16)
#         user.token = token
#         user.save()
#         host = self.request.get_host()
#         url = f'http://{host}/users/email-confirm/{token}/'
#         send_mail(
#             subject="Подтверждение почты",
#             message=f"Привет, перейди по ссылке для подтверждения почты {url}",
#             from_email=EMAIL_HOST_USER,
#             recipient_list=[user.email],
#         )
#         return super().form_valid(form)
#
# def email_verefication(request, token):
#     user = get_object_or_404(CustomUser, token = token)
#     user.is_active = True
#     user.save()
#     return redirect(reverse("users:login"))
#
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def profile(request):
    return render(request, 'users/profile.html', {'user': request.user})


from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import ProfileForm

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=request.user)
    return render(request, 'users/edit_profile.html', {'form': form})


from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render
from django.contrib.auth.models import User

@login_required
@user_passes_test(lambda u: u.groups.filter(name='Менеджеры').exists())
def user_list(request):
    users = User.objects.all()
    return render(request, 'users/user_list.html', {'users': users})

