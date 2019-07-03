from django.urls import path
from .views import contact, index, ourwork, reviews, services

urlpatterns = [
  path('', index),
  path('contact/', contact),
  path('ourwork/', ourwork),
  path('reviews/', reviews),
  path('services/', services),
]