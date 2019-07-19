from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from . import forms

import os
import requests

# Create your views here.
def submit(request):

  # reCAPTCHA v3
  r = requests.post(
    'https://www.google.com/recaptcha/api/siteverify', 
    params={
      'response': request.POST["g-recaptcha-response"],
      'secret': os.environ["RECAPTCHA_SECRET_KEY"],
    }
  )

  # Return 'error' message if reCAPTCHA fails
  if r.json()['success'] == False:
      messages.add_message(request, messages.INFO, 'There was an error with your request. Please contact us at (123) 456-7890 or email us at email@email.com.')
      return redirect('contact')

  # Use information submitted via POST request to create an instance of a contact
  # form via the CreateContactForm() class, check that it is_valid(), and if so
  # then save it to the database and send a notification email.
  if request.method == "POST":
    form = forms.CreateContactForm(request.POST)

    # Save form submission to database
    if form.is_valid():
      form.save()
      
      # Send email notification
      send_mail(
        'Simple Clean Contact Form Submission',
        form.cleaned_data['message'],
        os.environ['CONTACT_FORM_ADMIN_EMAIL'],
        [os.environ['CONTACT_FORM_ADMIN_EMAIL']],
        fail_silently=False,
      )

      # Return 'success' message if form is valid
      messages.add_message(request, messages.SUCCESS, 'Your message has been sent!')
      return redirect('thanks')
    
    # Handle any potential errors with form submission
    else:
      context = {
        'form': form,
      }
      return render(request, 'contact.html', context)