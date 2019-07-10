from django.shortcuts import render
from django.http import HttpResponse
from . import forms

# Create your views here.
def contact_submit(request):
  if request.method == "POST":
    form = forms.CreateContactForm(request.POST, request.FILES)
    if form.is_valid():
      return HttpResponse("<h1>Form is valid!</h1>")
    else:
      return HttpResponse("<h1>Nope!</h1>")