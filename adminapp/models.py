from django.db import models

# Create your models here.
class pet(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField()
    type = models.CharField(max_length=30)
    color = models.CharField(max_length=30)
    gender = models.CharField(max_length=30,null=True)
    image = models.ImageField(upload_to='dog_photo')
    isavailable = models.BooleanField(default=True)

