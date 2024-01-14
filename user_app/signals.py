from .models import UserProfile
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save


@receiver(post_save, sender=User)
def create_user(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
