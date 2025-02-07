from django.db import models

# Create your models here.

class city(models.Model):
    name  = models.CharField(max_length=100)
    
    def _str_(self):
        return self.name
