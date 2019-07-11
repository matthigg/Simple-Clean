from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import forms

from django.contrib import messages

# Create your views here.
def contact_submit(request):

  # Use information submitted via POST request to create an instance of a contact
  # form via the CreateContactForm() class, check that it is_valid(), and if so
  # then save it to the database.
  if request.method == "POST":
    form = forms.CreateContactForm(request.POST)
    if form.is_valid():
      form.save()

      # Return 'success' message if form is valid
      messages.add_message(request, messages.INFO, 'Your message has been sent!')
      return redirect('contact')
    
    # Handle any potential errors with form submission
    else:
      form = forms.CreateContactForm()
    return render(request, 'contact', { 'form': form })