from django import forms
from . import models

class CreateContactForm(forms.ModelForm):
  class Meta:
    model = models.Contact
    fields = [
      'name',
      'email',
      'phone',
      'message',
    ]