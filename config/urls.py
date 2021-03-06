"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from .views import contact, index, ourwork, reviews, services, thanks

from django.contrib.sitemaps.views import sitemap
from .sitemaps import StaticViewSitemap

sitemaps = {
  'static': StaticViewSitemap,
}

urlpatterns = [
    path('admin/',    admin.site.urls),
    path('',          include('apps.contact_form.urls', namespace='contact-form')),
    path('',          index,    name='index'),
    path('contact/',  contact,  name='contact'),
    path('ourwork/',  ourwork,  name='ourwork'),
    path('reviews/',  reviews,  name='reviews'),
    path('services/', services, name='services'),
    path('thanks/',   thanks,   name='thanks'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]
