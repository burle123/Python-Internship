from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def dashboard_home(request):
    user_model = get_user_model()
    context = {
        'stats': [
            {'label': 'Users', 'value': user_model.objects.count(), 'detail': 'Registered members'},
            {'label': 'Activity', 'value': 128, 'detail': 'Actions this week'},
            {'label': 'Alerts', 'value': 3, 'detail': 'Items needing review'},
            {'label': 'Messages', 'value': 14, 'detail': 'Unread updates'},
        ],
        'activities': [
            'New user registrations are flowing through the custom onboarding form.',
            'Password reset emails are configured with the console backend for local development.',
            'Theme preferences persist with system, dark, and light support.',
        ],
        'notifications': [
            'Two password reset requests were generated in the last 24 hours.',
            'Dashboard sidebar is optimized for mobile-first navigation.',
            'Terms acceptance is stored on each user profile.',
        ],
        'quick_links': [
            {'label': 'Manage users', 'url': '/admin/account/user/'},
            {'label': 'Open terms page', 'url': '/accounts/terms/'},
            {'label': 'Reset password', 'url': '/accounts/password-reset/'},
        ],
    }
    return render(request, 'dashboard/home.html', context)
