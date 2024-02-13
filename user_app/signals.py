from .models import UserProfile
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
import random


@receiver(post_save, sender=User)
def create_user(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(pre_save, sender=User)
def set_username(sender, instance, **kwargs):
    if not instance.username:
        counter = random.randint(1000, 9999)
        username = f"{instance.first_name}_{counter}".lower()
        while User.objects.filter(username=username):
            counter = random.randint(10000, 99999)
            username = f"{instance.first_name}_{instance.last_name}_{counter}".lower()
        instance.username = username
