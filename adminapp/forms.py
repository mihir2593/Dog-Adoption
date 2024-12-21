from  django import forms
from . import models

class petform(forms.ModelForm):
    class Meta:
        model = models.pet
        fields = "__all__"