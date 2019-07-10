from django.db import models

# Create your models here.
class ContactForm(models.Model):
  name = models.CharField(max_length=100)
  email = models.CharField(max_length=100)
  phone = models.CharField(max_length = 24, default=None, blank=True)
  message = models.TextField()