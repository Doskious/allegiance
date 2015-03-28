from django.contrib import admin
from .models import JournalEntry, JournalSection, SectionGroup


admin.site.register(JournalEntry)
admin.site.register(JournalSection)
admin.site.register(SectionGroup)
