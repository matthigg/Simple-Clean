from django.shortcuts import render

def about(request):
  context = {}
  return render(request, 'pages/about.html', context)

def contact(request):
  context = {}
  return render(request, 'pages/contact.html', context)

def index(request):
  context = {}
  return render(request, 'pages/index.html', context)

def reviews(request):
  context = {}
  return render(request, 'pages/reviews.html', context)

def services(request):
  context = {}
  return render(request, 'pages/services.html', context)