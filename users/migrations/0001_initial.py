# Generated by Django 2.2.4 on 2019-12-30 06:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=12)),
                ('name', models.CharField(max_length=20)),
                ('dob', models.DateField(default=django.utils.timezone.now)),
                ('gender', models.CharField(choices=[('MALE', 'Male'), ('FEMALE', 'Female'), ('OTHERS', 'Rather Not Say')], default=1, max_length=6)),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=20)),
                ('city_circle', models.IntegerField(default=0)),
                ('qualifier', models.IntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
