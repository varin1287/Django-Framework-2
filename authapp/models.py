from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import timedelta
from django.utils.timezone import now
from django.db.models.signals import post_save
from django.dispatch import receiver


class User(AbstractUser):
    avatar = models.ImageField(upload_to='users_avatar', blank=True)
    age = models.PositiveSmallIntegerField(blank=True, null=True, default=18)

    activation_key = models.ImageField(max_length=64, blank=True, null=True)
    activation_key_expires = models.DateTimeField(default=now() + timedelta(hours=48))

    def is_activation_key_current(self):
        return now() <= self.activation_key_expires


class ShopUserProfile(models.Model):
    MALE = 'M'
    FEMALE = 'W'

    GENDER_CHOICES = (
        (MALE, 'Мужской'),
        (FEMALE, 'Женский')
    )

    user = models.OneToOneField(User, unique=True, null=False, db_index=True, on_delete=models.CASCADE)
    tagline = models.CharField(verbose_name='теги', max_length=128, blank=True)
    about_me = models.TextField(verbose_name='о себе', max_length=512, blank=True)
    gender = models.CharField(verbose_name='пол', max_length=1, choices=GENDER_CHOICES, blank=True)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            ShopUserProfile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.shopuserprofile.save()
