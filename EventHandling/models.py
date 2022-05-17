from django.db import models

# Create your models here.
class EventHandling(models.Model):
    name = models.CharField(max_length=100) 
    organiser = models.CharField(max_length=50)       
    special_guest = models.CharField(max_length=80)
    date = models.DateTimeField(default=10) 
    venue = models.CharField(max_length=50)

    def __str__(self):
        return self.name