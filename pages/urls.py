from django.urls import path
from .views import contact, index, ourwork, reviews, services

urlpatterns = [
  path('',          index,    name='index'),
  path('contact/',  contact,  name='contact'),
  path('ourwork/',  ourwork,  name='ourwork'),
  path('reviews/',  reviews,  name='reviews'),
  path('services/', services, name='services'),
]