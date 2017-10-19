from django.shortcuts import redirect, render
from wagtail.wagtailcore.models import Page

def reports(request):
    live_pages = Page.objects.live()
    
    return render(request, 'reports/dashboard.html', {
        'pages': live_pages
    })