from django.contrib.auth.models import User
from django.db import models
from adminapp.models import pet

class purchasepet(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    pe=models.ForeignKey(pet,on_delete=models.CASCADE)





