from django.db import models
from django.contrib.auth.models import AbstractUser

ROLES = (
    ('admin', 'Admin'),
    ('user', 'User'),
)

# Create your models here.
class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=150, unique=True, blank=True)
    email = models.EmailField(unique=True, db_index=True) # db_index=True for search optimization
    password = models.CharField(max_length=128)
    role = models.CharField(choices = ROLES, max_length=10, default='user')