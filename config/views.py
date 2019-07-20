from django.shortcuts import render
# from contact import forms
from apps.contact_form import forms

import os

def index(request):
  form = forms.CreateContactForm
  context = {
    'form': form,
    'phone_number': os.environ['PHONE_NUMBER'],
  }
  return render(request, 'index.html', context)

def services(request):
  context = {}
  return render(request, 'services.html', context)

def ourwork(request):
  context = {}
  return render(request, 'ourwork.html', context)

def reviews(request):
  context = {}
  return render(request, 'reviews.html', context)

def contact(request):
  form = forms.CreateContactForm
  context = {
    'form': form,
  }
  return render(request, 'contact.html', context)

def thanks(request):
  return render(request, 'thanks.html')