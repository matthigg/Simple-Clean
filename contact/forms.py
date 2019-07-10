from django import forms
from . import models

class CreateContactForm(forms.ModelForm):
  class Meta:
    model = models.ContactForm
    fields = [
      'name',
      'email',
      'phone',
      'message',
    ]