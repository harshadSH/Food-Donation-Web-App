# Generated by Django 4.0.3 on 2024-03-11 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donation', '0002_donation_donationarea_volunteer_gallery_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='donation',
            name='updationdate',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='donor',
            name='contact',
            field=models.CharField(max_length=115, null=True),
        ),
    ]
