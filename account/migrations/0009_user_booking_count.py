# Generated by Django 4.1.2 on 2023-01-03 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_slot_booking_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='booking_count',
            field=models.IntegerField(default=0),
        ),
    ]
