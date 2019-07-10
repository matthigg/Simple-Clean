from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def contact_submit(request):
  return HttpResponse("<h1>Success!</h1>")