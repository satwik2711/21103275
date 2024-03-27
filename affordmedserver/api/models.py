from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone


class Product(models.Model):
    category_name = models.CharField(max_length=255)
    product_id = models.CharField(max_length=255, unique=True)
    product_data = models.JSONField()
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-last_updated']
        indexes = [
            models.Index(fields=['category_name', 'product_id']),
        ]

    def __str__(self):
        return self.product_data.get('name', 'Unnamed Product')


# class UniversityUserManager(BaseUserManager):
#     def create_user(self, email, roll_number, password=None, **extra_fields):
#         if not email:
#             raise ValueError('The Email field must be set')
#         if not roll_number:
#             raise ValueError('The Roll Number field must be set')

#         email = self.normalize_email(email)
#         user = self.model(email=email, roll_number=roll_number, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, roll_number, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)

#         if extra_fields.get('is_staff') is not True:
#             raise ValueError('Superuser must have is_staff=True.')
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError('Superuser must have is_superuser=True.')

#         return self.create_user(email, roll_number, password, **extra_fields)

# class UniversityUser(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField(unique=True)
#     roll_number = models.CharField(max_length=15, unique=True)
#     is_staff = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=True)
#     date_joined = models.DateTimeField(default=timezone.now)

#     objects = UniversityUserManager()

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['roll_number']

#     def __str__(self):
#         return self.email


class AccessToken(models.Model):
    company_name = models.CharField(max_length=100)
    client_id = models.CharField(max_length=100)
    client_secret = models.CharField(max_length=100)
    access_token = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.company_name
