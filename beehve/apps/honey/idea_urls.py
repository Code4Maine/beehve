from django.conf.urls import url
from honey import views as honey_views

urlpatterns = [
    url(r'^ideas/add/',
        view=honey_views.ProjectIdeaCreateView.as_view(),
        name="projectidea-create"),
    url(r'^ideas/(?P<slug>[-\w]+)/edit/',
        view=honey_views.ProjectIdeaUpdateView.as_view(),
        name="projectidea-update"),
    url(r'^ideas.json',
        view=honey_views.ProjectIdeaListJSONView.as_view(),
        name="projectidea-list-json"),
    url(r'^ideas/(?P<slug>[-\w]+)/',
        view=honey_views.ProjectIdeaDetailView.as_view(),
        name="projectidea-detail"),
    url(r'^ideas/$',
        view=honey_views.ProjectIdeaListView.as_view(),
        name="projectidea-list")
]


    #url(r'^ideas.csv',
    #    view=honey_views.ProjectIdeaListCSVView.as_view(),
    #    name="projectidea-list-csv"),
