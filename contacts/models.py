from django.db import models

from django.utils.timezone import now

class Contact(models.Model):
    listing_id = models.IntegerField()
    listing = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    message = models.TextField(blank=True)
    contact_date = models.DateTimeField(default=now, blank=True)
    user_id = models.IntegerField(blank=True)
    
    def __str__(self):
        return self.name