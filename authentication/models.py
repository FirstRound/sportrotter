from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models

# TODO custom auth backend
# TODO create method in serializ
class SportrotterUser(AbstractBaseUser):
    avatar = models.FileField(upload_to='avatars', blank=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(unique=True)

    # username = models.CharField(
    #     blank=True,se
    #     max_length=12
    # )
    # EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'

    def get_short_name(self):
        return self.email

    def get_full_name(self):
        return self.email
        # payments = None
