# Generated by Django 5.1.1 on 2024-10-07 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0006_alter_serviceprofile_booking_availability'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serviceprofile',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='serviceprofile',
            name='available_services',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='serviceprofile',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='serviceprofile',
            name='facilities',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='serviceprofile',
            name='manager_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='serviceprofile',
            name='operating_hours',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='serviceprofile',
            name='payment_methods',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='serviceprofile',
            name='phone',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='serviceprofile',
            name='pricing',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='serviceprofile',
            name='ratings_reviews',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='serviceprofile',
            name='service_center_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='serviceprofile',
            name='service_center_type',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
