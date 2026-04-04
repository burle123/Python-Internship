from django.contrib.auth.views import LogoutView, PasswordResetCompleteView, PasswordResetConfirmView, PasswordResetDoneView, PasswordResetView
from django.urls import path, reverse_lazy

from .views import TermsView, UserLoginView, signup_view


app_name = 'account'

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('terms/', TermsView.as_view(), name='terms'),
    path(
        'password-reset/',
        PasswordResetView.as_view(
            template_name='auth/password_reset_form.html',
            email_template_name='auth/password_reset_email.txt',
            subject_template_name='auth/password_reset_subject.txt',
            success_url=reverse_lazy('account:password_reset_done'),
        ),
        name='password_reset',
    ),
    path(
        'password-reset/done/',
        PasswordResetDoneView.as_view(template_name='auth/password_reset_done.html'),
        name='password_reset_done',
    ),
    path(
        'reset/<uidb64>/<token>/',
        PasswordResetConfirmView.as_view(
            template_name='auth/password_reset_confirm.html',
            success_url=reverse_lazy('account:password_reset_complete'),
        ),
        name='password_reset_confirm',
    ),
    path(
        'reset/done/',
        PasswordResetCompleteView.as_view(template_name='auth/password_reset_complete.html'),
        name='password_reset_complete',
    ),
]
