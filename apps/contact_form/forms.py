from django.forms import ModelForm, TextInput, Textarea
from . import models

# This is a hack to get rid of the defalt label_suffix=":"
# https://www.caktusgroup.com/blog/2018/06/18/make-all-your-django-forms-better/
class BaseForm(ModelForm):
  def __init__(self, *args, **kwargs):
    kwargs.setdefault('label_suffix', '')  
    super(BaseForm, self).__init__(*args, **kwargs)
ModelForm = BaseForm

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