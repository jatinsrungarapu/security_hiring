# Generated by Django 3.1.3 on 2022-12-26 12:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('securityapp', '0021_remove_booking_guardname'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='guardname',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='securityapp.guard'),
        ),
    ]
