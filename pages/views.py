from django.shortcuts import render

def about(request):
  return render(request, 'pages/about.html')

def contact(request):
  return render(request, 'pages/contact.html')

def index(request):
  return render(request, 'pages/index.html')

def reviews(request):
  return render(request, 'pages/reviews.html')

def services(request):
  return render(request, 'pages/services.html')