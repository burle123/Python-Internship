from django.db import models
from django.contrib.auth.models import AbstractUser

ROLES = (
    ('admin', 'Admin'),
    ('user', 'User'),
)

class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True, db_index=True)
    full_name = models.CharField(max_length=255)
    terms_accepted = models.BooleanField(default=False)
    terms_accepted_at = models.DateTimeField(blank=True, null=True)
    role = models.CharField(choices=ROLES, max_length=10, default='user')

    def __str__(self):
        return self.full_name or self.email
