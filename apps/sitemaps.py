from django.contrib.sitemaps import Sitemap
from contact_form.models import ContactForm

class PostSitemap(Sitemap):
  def items(self):
    return ContactForm.objects.all()