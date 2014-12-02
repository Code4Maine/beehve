from django.conf.urls import patterns, url
from honey import views as honey_views


# custom views
urlpatterns = patterns(
    '',
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

    #url(r'^projects.csv',
    #    view=honey_views.ProjectListCSVView.as_view(),
    #    name="project-list-csv"),

    url(r'^projects/$',
        view=honey_views.ProjectListView.as_view(),
        name="project-list"),

    url(r'^events/add/',
        view=honey_views.EventCreateView.as_view(),
        name="event-create"),

    url(r'^events/(?P<slug>[-\w]+)/',
        view=honey_views.EventDetailView.as_view(),
        name="event-detail"),

    url(r'^events/$',
        view=honey_views.EventListView.as_view(),
        name="event-list"),

    url(r'^topic/add/',
        view=honey_views.TopicCreateView.as_view(),
        name="topic-create"),

    url(r'^topic/(?P<slug>[-\w]+)/',
        view=honey_views.TopicDetailView.as_view(),
        name="topic-detail"),

    url(r'^topic/$',
        view=honey_views.TopicListView.as_view(),
        name="topic-list"),

    url(r'^technology/add/',
        view=honey_views.TechnologyCreateView.as_view(),
        name="technology-create"),

    url(r'^technology/(?P<slug>[-\w]+)/',
        view=honey_views.TechnologyDetailView.as_view(),
        name="technology-detail"),

    url(r'^technology/$',
        view=honey_views.TechnologyListView.as_view(),
        name="technology-list"),

    url(r'^$',
        view=honey_views.BuzzListView.as_view(
        template_name = 'honey/dashboard.html'),
        name="homepage",),
)
