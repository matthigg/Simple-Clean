from django.shortcuts import render
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
  context = {
    'phone_number': os.environ['PHONE_NUMBER'],
  }
  return render(request, 'services.html', context)

def ourwork(request):
  context = {
    'phone_number': os.environ['PHONE_NUMBER'],
  }
  return render(request, 'ourwork.html', context)

def reviews(request):
  context = {
    'phone_number': os.environ['PHONE_NUMBER'],
  }
  return render(request, 'reviews.html', context)

def contact(request):
  form = forms.CreateContactForm
  context = {
    'form': form,
    'phone_number': os.environ['PHONE_NUMBER'],
  }
  return render(request, 'contact.html', context)

def thanks(request):
  context = {
    'phone_number': os.environ['PHONE_NUMBER'],
  }
  return render(request, 'thanks.html', context)