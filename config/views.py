from django.shortcuts import render
from contact import forms

def index(request):
  form = forms.CreateContactForm
  context = {
    'form': form,
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