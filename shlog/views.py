from django.shortcuts import render
from .models import JournalEntry, JournalSection, SectionGroup


def full_blog(request):
    shlog_posts = JournalEntry.objects.all()
    shlog_sections = JournalSection.objects.all()
    schlog_groups = SectionGroup.objects.all()
    return render(request, 'shlog.html', {"posts":shlog_posts, "sections": shlog_sections, "groups": schlog_groups}, content_type="text/html")
