from django.conf.urls import include, url
from django.core import urlresolvers
from django.conf import settings
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.utils.html import format_html, format_html_join
from wagtail.wagtailcore import hooks
from wagtail.wagtailadmin.menu import MenuItem
from django.core.urlresolvers import reverse

from . import urls
from . import views

@hooks.register('register_admin_urls')
def register_admin_urls():
    return [
        url(r'^reports/', include(urls)),
    ]

@hooks.register('register_admin_menu_item')
def register_reports_menu_item():
    return MenuItem(
        ('Reports'),
        urlresolvers.reverse('wagtailreports'),
        classnames='icon icon-wagtail',
        order=1000
    )
