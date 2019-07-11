from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import forms

from django.contrib import messages

# Create your views here.
def contact_submit(request):
  if request.method == "POST":
    form = forms.CreateContactForm(request.POST)
    if form.is_valid():
      # returned_instance = form.save()
      # returned_instance = form.save(commit=False) # hesitate to commit
      # person_who_clicked_submit = request.user
      messages.add_message(request, messages.INFO, 'Your message has been sent!')
      return redirect('contact')
    
    # Handle error with form submission
    else:
      form = forms.CreateContactForm()
    return render(request, 'contact', { 'form': form })