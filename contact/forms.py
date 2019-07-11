from django.forms import ModelForm, TextInput, Textarea
from . import models

class CreateContactForm(ModelForm):
  class Meta:
    model = models.ContactForm
    fields = [
      'name',
      'email',
      'phone',
      'message',
    ]
    widgets = {
      'name': TextInput(attrs={'placeholder': 'name'}),
      'email': TextInput(attrs={'placeholder': 'email'}),
      'phone': TextInput(attrs={'placeholder': 'phone'}),
      'message': Textarea(attrs={'placeholder': 'message'}),
    }