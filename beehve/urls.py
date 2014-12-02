from django.conf import settings
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()

from honey.views import BuzzListView

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    (r'^accounts/', include('allauth.urls')),
    (r'^avatar/', include('avatar.urls')),
    (r'^select2/', include('select2.urls')),
    (r'^blog/', include('biblion.urls')),
    (r'^dashboard/', include('honey.urls')),
    (r'^dashboard/', include('workers.urls')),
    url("^$", 
        BuzzListView.as_view(template_name='homepage.html'), 
        name="homepage"),
    (r'', include('gnocchi.cms.urls')),
)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )
