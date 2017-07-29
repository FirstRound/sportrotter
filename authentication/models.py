from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models


# TODO custom auth backend
# TODO create method in serializ
class Gender:
    MALE = 'MALE'
    FEMALE = 'FEMALE'
    OTHER = 'OTHER'
    GENDER_TYPE_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHER, 'Other'),
    )


class SportrotterUser(AbstractBaseUser):
    avatar = models.FileField(upload_to='avatars', blank=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=20,
                              choices=Gender.GENDER_TYPE_CHOICES,
                              default=Gender.MALE, blank=True)
    # TODO fb access?

    # TODO add address
    # address = AddressField(related_name="+", blank=True)
    # address = models.CharField(max_length=50)
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
