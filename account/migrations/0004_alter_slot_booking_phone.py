# Generated by Django 4.1.2 on 2022-11-28 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_slot_booking_end_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slot_booking',
            name='phone',
            field=models.CharField(max_length=10),
        ),
    ]