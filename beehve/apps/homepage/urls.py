from django.conf.urls import patterns, url
from .views import (WorkerListJSONView, WorkerListView, WorkerDetailView,
                    WorkerUpdateView, WorkerProfileView)


# custom views
urlpatterns = patterns(
    '',
    url(r'^profile/edit/',
        view=WorkerUpdateView.as_view(),
        name="worker-update"),

    url(r'^profile/',
        view=WorkerProfileView.as_view(),
        name="profile-detail"),

    url(r'^workers.json',
        view=WorkerListJSONView.as_view(),
        name="worker-list-json"),

    #url(r'^workers.csv',
    #    view=WorkerListCSVView.as_view(),
    #    name="worker-list-csv"),

    url(r'^workers/(?P<slug>[-\w]+)/',
        view=WorkerDetailView.as_view(),
        name="worker-detail"),

    url(r'^workers/',
        view=WorkerListView.as_view(),
        name="worker-list"),
)
