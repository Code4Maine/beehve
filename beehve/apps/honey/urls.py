from django.conf.urls import patterns, url
from .views import (ProjectListView, ProjectDetailView, ProjectCreateView, 
                    ProjectUpdateView, ProjectListJSONView, ProjectJoinView,
                    ProjectLeaveView, EventListView, #ProjectListCSVView,
                    TechnologyDetailView, TechnologyListView, TopicDetailView,
                    TopicListView, EventDetailView)


# custom views
urlpatterns = patterns(
    '',
    url(r'^projects/add/',
        view=ProjectCreateView.as_view(),
        name="project-create"),

    url(r'^projects/(?P<slug>[-\w]+)/edit/',
        view=ProjectUpdateView.as_view(),
        name="project-update"),

    url(r'^projects/(?P<slug>[-\w]+)/join/',
        view=ProjectJoinView.as_view(),
        name="project-join"),

    url(r'^projects/(?P<slug>[-\w]+)/leave/',
        view=ProjectLeaveView.as_view(),
        name="project-leave"),

    url(r'^projects.json',
        view=ProjectListJSONView.as_view(),
        name="project-list-json"),

    url(r'^projects/(?P<slug>[-\w]+)/',
        view=ProjectDetailView.as_view(),
        name="project-detail"),
    #url(r'^projects.csv',
    #    view=ProjectListCSVView.as_view(),
    #    name="project-list-csv"),

    url(r'^projects/',
        view=ProjectListView.as_view(),
        name="project-list"),

    url(r'^events/',
        view=EventListView.as_view(),
        name="event-list"),

    url(r'^events/(?P<slug>[-\w]+)/',
        view=EventDetailView.as_view(),
        name="event-detail"),

    url(r'^topic/',
        view=TopicListView.as_view(),
        name="topic-list"),

    url(r'^topic/(?P<slug>[-\w]+)/',
        view=TopicDetailView.as_view(),
        name="topic-detail"),

    url(r'^technology/',
        view=TechnologyListView.as_view(),
        name="technology-list"),

    url(r'^technology/(?P<slug>[-\w]+)/',
        view=TechnologyDetailView.as_view(),
        name="technology-detail")
)
