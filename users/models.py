from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils import timezone
from django.urls import reverse

sex_choices = [('MALE', 'Male'), ('FEMALE', 'Female'), ('OTHERS', 'Rather Not Say'),]

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    uid = models.CharField(max_length=12)
    name = models.CharField(max_length = 20)
    dob = models.DateField(default = timezone.now)
    gender = models.CharField(max_length = 6, choices = sex_choices, default = 1)
    city = models.CharField(max_length = 20)
    state = models.CharField(max_length = 20)

    city_circle = models.IntegerField(default=0)
    qualifier = models.IntegerField(default = 0) # 1 - Staff   0 - DBer

    def profile_create_url(self):
        return reverse('create_profile', kwargs={'pk': self.pk})

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.qualifier == 0:
            self.city_circle = ord(upper(self.city[0])) - 64
