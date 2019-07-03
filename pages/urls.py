from django.urls import path
from .views import about, contact, index, reviews, services

urlpatterns = [
  path('', index),
  path('about/', about),
  path('contact/', contact),
  path('reviews/', reviews),
  path('services/', services),
]