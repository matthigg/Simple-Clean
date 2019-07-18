from django.db import models

# Create your models here.
class ContactForm(models.Model):
  class Meta:
    verbose_name_plural = "Contact Form Submissions"
  name = models.CharField(max_length=254)
  email = models.EmailField(max_length=254)
  phone = models.CharField(max_length = 24, default=None, blank=True)
  message = models.TextField()