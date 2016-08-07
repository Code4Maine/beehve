from django.conf.urls import url
from honey import views as honey_views

urlpatterns = [
    url(r'^projects/add/',
        view=honey_views.ProjectCreateView.as_view(),
        name="project-create"),
    url(r'^projects/(?P<slug>[-\w]+)/edit/',
        view=honey_views.ProjectUpdateView.as_view(),
        name="project-update"),
    url(r'^projects/(?P<slug>[-\w]+)/join/',
        view=honey_views.ProjectJoinView.as_view(),
        name="project-join"),
    url(r'^projects/(?P<slug>[-\w]+)/leave/',
        view=honey_views.ProjectLeaveView.as_view(),
        name="project-leave"),
    url(r'^projects/(?P<slug>[-\w]+)/buzz/create/',
        view=honey_views.BuzzCreateView.as_view(),
        name="buzz-create"),
    url(r'^projects/(?P<project_slug>[-\w]+)/buzz/(?P<slug>[-\w]+)/',
        view=honey_views.BuzzDetailView.as_view(),
        name="buzz-detail"),
    url(r'^projects/(?P<project_slug>[-\w]+)/commit/(?P<slug>[-\w]+)/',
        view=honey_views.ProjectCommitDetailView.as_view(),
        name="commit-detail"),
    url(r'^projects/(?P<slug>[-\w]+)/link/create/',
        view=honey_views.LinkCreateView.as_view(),
        name="link-create"),
    url(r'^projects.json',
        view=honey_views.ProjectListJSONView.as_view(),
        name="project-list-json"),
    url(r'^projects/(?P<slug>[-\w]+)/',
        view=honey_views.ProjectDetailView.as_view(),
        name="project-detail"),
    url(r'^projects/$',
        view=honey_views.ProjectListView.as_view(),
        name="project-list")
]

#url(r'^projects.csv',
#    view=honey_views.ProjectListCSVView.as_view(),
#    name="project-list-csv"),

