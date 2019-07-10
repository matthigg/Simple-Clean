from django.shortcuts import render
from django.http import HttpResponse
from . import forms

# Create your views here.
def contact_submit(request):
  if request.method == "POST":
    form = forms.CreateContactForm(request.POST, request.FILES)
    if form.is_valid():
      return HttpResponse("<h1>Form is valid!</h1>")
      # returned_instance = form.save()
      # returned_instance = form.save(commit=False) # hesitate to commit
      # person_who_clicked_submit = request.user
    else:
      return HttpResponse("<h1>Nope!</h1>")