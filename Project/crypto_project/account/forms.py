from django import forms
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.utils import timezone


User = get_user_model()


class RegistrationForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput, label='Password')
    password2 = forms.CharField(widget=forms.PasswordInput, label='Confirm Password')
    terms_accepted = forms.BooleanField(
        required=True,
        label='I agree to the Terms and Conditions',
        error_messages={'required': 'You must accept the Terms and Conditions.'},
    )

    class Meta:
        model = User
        fields = ('full_name', 'email', 'terms_accepted')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            if name == 'terms_accepted':
                field.widget.attrs.update({'class': 'mt-1 h-4 w-4 rounded border-slate-300 text-sky-600'})
            else:
                field.widget.attrs.update(
                    {
                        'class': 'w-full rounded-2xl border border-slate-300 bg-white px-4 py-3 text-sm outline-none ring-0 transition focus:border-sky-500 dark:border-slate-700 dark:bg-slate-950',
                    }
                )

    def clean_email(self):
        email = self.cleaned_data['email'].strip().lower()
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('An account with this email already exists.')
        return email

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get('password1') != cleaned_data.get('password2'):
            self.add_error('password2', 'Passwords do not match.')
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['email']
        user.email = self.cleaned_data['email']
        user.terms_accepted = self.cleaned_data['terms_accepted']
        user.terms_accepted_at = timezone.now()
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class EmailAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(label='Email')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update(
                {
                    'class': 'w-full rounded-2xl border border-slate-300 bg-white px-4 py-3 text-sm outline-none ring-0 transition focus:border-sky-500 dark:border-slate-700 dark:bg-slate-950',
                }
            )

    def clean(self):
        email = self.cleaned_data.get('username', '').strip().lower()
        password = self.cleaned_data.get('password')

        if email and password:
            user = User.objects.filter(email=email).first()
            username = user.username if user else email
            self.user_cache = authenticate(self.request, username=username, password=password)
            if self.user_cache is None:
                raise forms.ValidationError('Please enter a correct email and password.', code='invalid_login')
            self.confirm_login_allowed(self.user_cache)
        return self.cleaned_data
