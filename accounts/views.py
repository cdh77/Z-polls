from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import RegistrationForm


class UserRegistrationView(CreateView):
    template_name = 'accounts/register.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('polls:index')


class UserLoginView(auth_views.LoginView):
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('polls:index')


class UserLogoutView(auth_views.LogoutView):
    template_name = 'accounts/logout.html'
