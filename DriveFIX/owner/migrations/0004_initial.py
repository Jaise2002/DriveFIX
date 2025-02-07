# Generated by Django 5.1.1 on 2024-10-07 06:41

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('owner', '0003_delete_teach_request'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('service_center_name', models.CharField(max_length=255)),
                ('operating_hours', models.CharField(max_length=100)),
                ('available_services', models.TextField()),
                ('pricing', models.TextField()),
                ('ratings_reviews', models.TextField()),
                ('service_center_type', models.CharField(max_length=100)),
                ('facilities', models.TextField()),
                ('manager_name', models.CharField(max_length=100)),
                ('booking_availability', models.IntegerField()),
                ('payment_methods', models.CharField(max_length=255)),
                ('service_center_image', models.ImageField(blank=True, null=True, upload_to='service_center_images/')),
                ('user', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
