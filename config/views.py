from django.shortcuts import render

def index(request):
  context = {}
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
  context = {}
  return render(request, 'contact.html', context)