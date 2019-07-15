from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from . import forms

import os
# import smtplib


# Create your views here.
def contact_submit(request):

  # Use information submitted via POST request to create an instance of a contact
  # form via the CreateContactForm() class, check that it is_valid(), and if so
  # then save it to the database and send a notification email.
  if request.method == "POST":
    form = forms.CreateContactForm(request.POST)
    if form.is_valid():
      form.save()
      
      send_mail(
        'Simple Clean Contact Form Submission',
        form.cleaned_data['message'],
        os.environ['CONTACT_FORM_ADMIN_EMAIL'],
        [os.environ['CONTACT_FORM_ADMIN_EMAIL']],
        fail_silently=False,
      )

      # Return 'success' message if form is valid
      messages.add_message(request, messages.INFO, 'Your message has been sent!')
      return redirect('contact')
    
    # Handle any potential errors with form submission
    else:
      form = forms.CreateContactForm()
      messages.add_message(request, messages.INFO, 'There was an error processing your request. Please call us at (123) 456-7890 or email us at email@email.com.')
    return render(request, 'contact', { 'form': form })