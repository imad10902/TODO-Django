from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    host = models.ForeignKey(User, on_delete=models.CASCADE, null=True) #A User can have many Tasks
    title = models.CharField(null=True, blank=False, max_length=25)
    related_to = models.CharField(null=False, blank=False, max_length=25)
    updated = models.DateTimeField(auto_now=True) #whenever user updates something about this model, date is recorded
    created = models.DateTimeField(auto_now_add=True) # records date of creation og entry of this model table

    class Meta: 
        ordering = ['-updated', 'created']

    def __str__(self):
        return self.title
