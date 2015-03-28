from django.shortcuts import render
from .models import JournalEntry, JournalSection


def full_blog(request):
    shlog_posts = JournalEntry.objects.all()
    shlog_sections = JournalSection.objects.all()
    return render(request, 'shlog.html', {"posts":shlog_posts, "sections": shlog_sections}, content_type="text/html")
