from django.contrib import admin
from .models import JournalEntry, JournalSection


admin.site.register(JournalEntry)
admin.site.register(JournalSection)