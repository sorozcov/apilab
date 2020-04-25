from django.db import models


class Event(models.Model):
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    notes = models.CharField(max_length=200)
    baby = models.ForeignKey(
        'babies.Baby',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    
    def __str__(self):
        return self.name
