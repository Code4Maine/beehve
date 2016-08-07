from django.conf import settings
from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^avatar/', include('avatar.urls')),
    url(r'^dashboard/', include('honey.urls')),
    url(r'^dashboard/', include('workers.urls')),
    url(r'', include('homepage.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
