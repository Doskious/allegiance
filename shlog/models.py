from django.db import models
from django.utils import timezone
from cms.models.pluginmodel import CMSPlugin


class Hello(CMSPlugin):
    guest_name = models.CharField(max_length=50, default='Stranger')

    def __unicode__(self):
        return u'{0}'.format(self.guest_name)


class SectionGroup(models.Model):
    group_name = models.CharField(max_length=128)

    def __unicode__(self):
        return u'{0}'.format(self.group_name)


class JournalSection(models.Model):
    journal_section = models.CharField(max_length=128)
    section_group = models.ForeignKey('SectionGroup')

    def __unicode__(self):
        return u'{0}'.format(self.journal_section)


class JournalEntry(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=60)
    subtext = models.CharField(max_length=42, default="", blank=True)
    context = models.CharField(max_length=128, default="Ship's Log: The Allegiance", blank=True)
    section = models.ForeignKey('JournalSection')
    journal_date = models.CharField(max_length=10, default="4714/MM/DD")
    body = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __unicode__(self):
        return u'{0}'.format(self.title)

