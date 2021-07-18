from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist


class Profile(AbstractUser):
    username = models.EmailField(_('email address'), unique=True)
    created = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    group = models.ForeignKey('Groups', on_delete=models.DO_NOTHING, null=True, blank=True)
    password = models.CharField(max_length=128, verbose_name='password', default='')

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return str(self.username)


class Groups(models.Model):
    group_name = models.CharField(max_length=100)
    group_description = models.CharField(max_length=100)

    def __str__(self):
        return self.group_name

