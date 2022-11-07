# Generated by Django 4.1 on 2022-09-17 19:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0004_remove_userprofilemodel_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofilemodel',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='profile_image/'),
        ),
        migrations.AlterField(
            model_name='userprofilemodel',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='profile', serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]