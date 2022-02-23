from tokenize import blank_re
from django.db import models
from django.forms import JSONField

# Create your models here.


class Machine(models.Model):
    name = models.CharField(max_length=50)
    ip = models.CharField(max_length=50)
    data = models.JSONField(blank=True, null=True)
    registry_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name+"---"+self.registry_date.strftime("%Y-%m-%d %H:%M:%S")
