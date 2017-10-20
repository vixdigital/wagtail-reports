from django.shortcuts import redirect, render
from wagtail.wagtailcore.models import Page, PageRevision

def reports(request):

    def get_live_pages():
        live_pages = Page.objects.in_site(request.site).live()
        return live_pages

    def get_page_results():
        page_results = get_live_pages()
        order_by = request.GET.get('orderby')

        if order_by:
            page_results = page_results.order_by(order_by)
        else:
            # default to showing most stale content first
            page_results = page_results.order_by('last_published_at')

        return page_results

    return render(request, 'reports/dashboard.html', {
        'page_results': get_page_results
    })