from django.db import models
from django.utils import timezone
from cms.models.pluginmodel import CMSPlugin


class Hello(CMSPlugin):
    guest_name = models.CharField(max_length=50, default='Guest')

    def __unicode__(self):
        return u'{0}'.format(self.guest_name)


class JournalEntry(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=60)
    subtext = models.CharField(max_length=42)
    context = models.CharField(max_length=128)
    section = models.CharField(max_length=128)
    journal_date = models.CharField(max_length=10)
    body = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __unicode__(self):
        return u'{0}'.format(self.name)

