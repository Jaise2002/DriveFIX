# Generated by Django 4.2.7 on 2024-02-05 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teach_request',
            name='Subject',
            field=models.CharField(default='none', max_length=30),
        ),
    ]