from django.urls import path
from .views import contact_submit

app_name = "contact"

urlpatterns = [
  path('submit/', contact_submit, name='submit'),
]