from django.db import models
from django.utils.translation import ugettext_lazy as _

from idios.models import ProfileBase

class Person(models.Model):
    """ A borrower that may not have an account. These can migrate to be real people"""
    name = models.CharField(_("name"), max_length=50, null=True, blank=True)

class Profile(Person, ProfileBase):
    about = models.TextField(_("about"), null=True, blank=True)
    location = models.CharField(_("location"), max_length=40, null=True, blank=True)
    website = models.URLField(_("website"), null=True, blank=True, verify_exists=False)
