from django.conf.urls import include, url
from honey import views as honey_views


# custom views
urlpatterns = [
    url(r'^', include('honey.project_urls')),
    url(r'^', include('honey.idea_urls')),
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
        view=honey_views.DashboardView.as_view(),
        name="dashboard",),
]
