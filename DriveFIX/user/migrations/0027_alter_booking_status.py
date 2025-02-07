# Generated by Django 5.1.1 on 2024-10-08 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0026_alter_booking_customer_alter_booking_service_center'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='status',
            field=models.CharField(blank=True, choices=[('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Billing..', 'Billing..'), ('Completed', 'Completed')], default='Pending', max_length=10, null=True),
        ),
    ]
