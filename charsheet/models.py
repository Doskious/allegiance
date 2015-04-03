from django.db import models
from django.utils import timezone
from cms.models.pluginmodel import CMSPlugin


class CharSheet(CMSPlugin):
    char_name = models.CharField(max_length=50, default='Stranger')

    def __unicode__(self):
        return u'{0}'.format(self.char_name)
