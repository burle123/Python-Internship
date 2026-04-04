from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from django.views.generic import TemplateView

from .forms import EmailAuthenticationForm, RegistrationForm


class UserLoginView(LoginView):
    authentication_form = EmailAuthenticationForm
    template_name = 'auth/login.html'
    redirect_authenticated_user = True

    def form_valid(self, form):
        messages.success(self.request, 'Welcome back.')
        return super().form_valid(form)


def signup_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard:home')

    form = RegistrationForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.save()
        login(request, user)
        messages.success(request, 'Your account has been created.')
        return redirect('dashboard:home')
    return render(request, 'auth/signup.html', {'form': form})


class TermsView(TemplateView):
    template_name = 'auth/terms.html'
