from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.conf.urls import url
from .views import (WorkerListJSONView, WorkerListView, WorkerDetailView,
                    WorkerUpdateView, WorkerProfileView, PositionListView,
                    PositionDetailView)
from .models import Worker

urlpatterns = [
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

    url(r'^positions/(?P<slug>[-\w]+)/',
        view=PositionDetailView.as_view(),
        name="position-detail"),

    url(r'^positions/',
        view=PositionListView.as_view(),
        name="position-list"),
]

def get_or_create_worker(sender, instance, **kwargs):
    Worker.objects.get_or_create(user=instance)


post_save.connect(get_or_create_worker, sender=get_user_model(), dispatch_uid='get_or_create_worker')
get_user_model().worker = property(lambda u: Worker.objects.get_or_create(user=u)[0])
