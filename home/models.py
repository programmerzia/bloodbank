from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=200, blank=True)
    email = models.CharField(max_length=50,blank=True)
    subject = models.CharField(max_length=255,blank=True)
    message = models.TextField(blank=True)

    def __str__(self):
        return self.name