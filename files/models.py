from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils import timezone
from django.urls import reverse
from users.models import Profile

class File(models.Model):

    staff = models.ForeignKey(Profile, on_delete = models.CASCADE)
    fname = models.CharField(max_length=20)
    doc = models.FileField(upload_to='files_dir/', blank=True)
    up_date = models.DateField(default = timezone.now)

    def __str__(self):
        return f'{self.fname}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
