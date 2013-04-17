from django.db import models
from django.forms import ModelForm

class SimpleModel(models.Model):
    message = models.CharField(max_length=80)
    def __unicode__(self):
        return self.SimpleModel
    
