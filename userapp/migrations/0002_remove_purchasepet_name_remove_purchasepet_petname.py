# Generated by Django 5.0 on 2024-02-27 12:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchasepet',
            name='name',
        ),
        migrations.RemoveField(
            model_name='purchasepet',
            name='petname',
        ),
    ]
