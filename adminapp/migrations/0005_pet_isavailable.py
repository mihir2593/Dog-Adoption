# Generated by Django 5.0 on 2024-02-28 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0004_alter_pet_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='isavailable',
            field=models.BooleanField(default=True),
        ),
    ]
