from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from datetime import datetime, timedelta
import jwt


class Profile(AbstractUser):
    username = models.EmailField(_('email address'), unique=True)
    created = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    group = models.ForeignKey('Groups', on_delete=models.SET_NULL, null=True, blank=True)
    password = models.CharField(max_length=128, verbose_name='password', default='')

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    # token is dynamic property
    @property
    def token(self):
        return self._generate_jwt_token()

    def _generate_jwt_token(self):
        dt = datetime.now() + timedelta(days=1)
        token = jwt.encode({'id': self.pk, 'exp': int(dt.strftime('%s'))}, 'secret', algorithm='HS256')
        return token.decode('utf-8')

    def __str__(self):
        return str(self.username)


class Groups(models.Model):
    group_name = models.CharField(max_length=100, unique=True)
    group_description = models.CharField(max_length=100)

    def __str__(self):
        return self.group_name

