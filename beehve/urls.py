from django.conf import settings
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    (r'^accounts/', include('allauth.urls')),
    (r'^avatar/', include('avatar.urls')),
    (r'^select2/', include('select2.urls')),
    (r'^', include('workers.urls')),
    (r'^', include('honey.urls')),
    url("^$", 
        TemplateView.as_view(template_name='homepage.html'), 
        name="homepage")
)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )
