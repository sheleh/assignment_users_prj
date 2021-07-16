

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist


class Profile(models.Model):
    username_p = models.OneToOneField(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    group = models.ForeignKey('Groups', on_delete=models.DO_NOTHING, null=True, blank=True)

    def __str__(self):
        return str(self.username_p)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    try:
        instance.profile.save()
    except ObjectDoesNotExist:
        Profile.objects.create(user=instance)


class Groups(models.Model):
    group_name = models.CharField(max_length=100)
    group_description = models.CharField(max_length=100)

    def __str__(self):
        return self.group_name

