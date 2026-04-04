from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.core import mail
from django.test import TestCase
from django.urls import reverse
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes


class AuthenticationFlowTests(TestCase):
    def setUp(self):
        self.user_model = get_user_model()
        self.password = 'StrongPass123!'
        self.user = self.user_model.objects.create_user(
            username='existing@example.com',
            email='existing@example.com',
            full_name='Existing User',
            password=self.password,
            terms_accepted=True,
        )

    def test_signup_requires_terms_acceptance(self):
        response = self.client.post(
            reverse('account:signup'),
            {
                'full_name': 'Test User',
                'email': 'tester@example.com',
                'password1': self.password,
                'password2': self.password,
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertFalse(self.user_model.objects.filter(email='tester@example.com').exists())
        self.assertContains(response, 'You must accept the Terms and Conditions.')

    def test_signup_logs_user_in_and_stores_terms(self):
        response = self.client.post(
            reverse('account:signup'),
            {
                'full_name': 'Test User',
                'email': 'tester@example.com',
                'password1': self.password,
                'password2': self.password,
                'terms_accepted': 'on',
            },
        )

        self.assertRedirects(response, reverse('dashboard:home'))
        user = self.user_model.objects.get(email='tester@example.com')
        self.assertTrue(user.terms_accepted)
        self.assertIsNotNone(user.terms_accepted_at)

    def test_dashboard_requires_login(self):
        response = self.client.get(reverse('dashboard:home'))
        self.assertRedirects(response, f"{reverse('account:login')}?next={reverse('dashboard:home')}")

    def test_login_accepts_email(self):
        response = self.client.post(
            reverse('account:login'),
            {'username': 'existing@example.com', 'password': self.password},
        )

        self.assertRedirects(response, reverse('dashboard:home'))

    def test_login_rejects_invalid_credentials(self):
        response = self.client.post(
            reverse('account:login'),
            {'username': 'existing@example.com', 'password': 'wrong-password'},
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Please enter a correct email and password.')

    def test_signup_rejects_duplicate_email(self):
        response = self.client.post(
            reverse('account:signup'),
            {
                'full_name': 'Another User',
                'email': 'existing@example.com',
                'password1': self.password,
                'password2': self.password,
                'terms_accepted': 'on',
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'An account with this email already exists.')

    def test_signup_rejects_password_mismatch(self):
        response = self.client.post(
            reverse('account:signup'),
            {
                'full_name': 'Mismatch User',
                'email': 'mismatch@example.com',
                'password1': self.password,
                'password2': 'DifferentPass123!',
                'terms_accepted': 'on',
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Passwords do not match.')

    def test_authenticated_user_is_redirected_from_signup(self):
        self.client.login(username='existing@example.com', password=self.password)

        response = self.client.get(reverse('account:signup'))

        self.assertRedirects(response, reverse('dashboard:home'))

    def test_terms_page_is_public(self):
        response = self.client.get(reverse('account:terms'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Terms &amp; Conditions')

    def test_logout_ends_authenticated_session(self):
        self.client.login(username='existing@example.com', password=self.password)

        response = self.client.post(reverse('account:logout'))

        self.assertRedirects(response, reverse('account:login'))
        dashboard_response = self.client.get(reverse('dashboard:home'))
        self.assertRedirects(dashboard_response, f"{reverse('account:login')}?next={reverse('dashboard:home')}")

    def test_password_reset_sends_email_for_known_user(self):
        response = self.client.post(
            reverse('account:password_reset'),
            {'email': 'existing@example.com'},
        )

        self.assertRedirects(response, reverse('account:password_reset_done'))
        self.assertEqual(len(mail.outbox), 1)
        self.assertIn('reset', mail.outbox[0].subject.lower())
        self.assertIn('/accounts/reset/', mail.outbox[0].body)

    def test_password_reset_does_not_send_email_for_unknown_user(self):
        response = self.client.post(
            reverse('account:password_reset'),
            {'email': 'missing@example.com'},
        )

        self.assertRedirects(response, reverse('account:password_reset_done'))
        self.assertEqual(len(mail.outbox), 0)

    def test_password_reset_confirm_page_loads_with_valid_token(self):
        uid = urlsafe_base64_encode(force_bytes(self.user.pk))
        token = default_token_generator.make_token(self.user)

        response = self.client.get(
            reverse('account:password_reset_confirm', args=[uid, token]),
            follow=True,
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Choose a secure password')

    def test_password_reset_confirm_updates_password(self):
        uid = urlsafe_base64_encode(force_bytes(self.user.pk))
        token = default_token_generator.make_token(self.user)
        confirm_url = reverse('account:password_reset_confirm', args=[uid, token])
        priming_response = self.client.get(confirm_url, follow=True)

        response = self.client.post(
            priming_response.request['PATH_INFO'],
            {
                'new_password1': 'BrandNewPass123!',
                'new_password2': 'BrandNewPass123!',
            },
        )

        self.assertRedirects(response, reverse('account:password_reset_complete'))
        self.user.refresh_from_db()
        self.assertTrue(self.user.check_password('BrandNewPass123!'))

    def test_dashboard_renders_prd_sections_for_authenticated_user(self):
        self.client.login(username='existing@example.com', password=self.password)

        response = self.client.get(reverse('dashboard:home'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Welcome, Existing User')
        self.assertContains(response, 'Notifications')
        self.assertContains(response, 'Quick Links')
        self.assertContains(response, 'data-sidebar-open', html=False)
        self.assertContains(response, 'data-theme-toggle', html=False)
