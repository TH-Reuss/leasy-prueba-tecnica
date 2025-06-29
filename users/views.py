from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from .forms import EmailAuthenticationForm

class UserLoginView(LoginView):
    form_class = EmailAuthenticationForm
    template_name = 'users/login.html'
    redirect_authenticated_user = True

class UserLogoutView(LogoutView):
    next_page = reverse_lazy('users:login')
