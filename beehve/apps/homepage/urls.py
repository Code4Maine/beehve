from django.conf.urls import url
from homepage import views as homepage_views


urlpatterns = [
    url(r'^initiatives.json',
        view=homepage_views.InitiativeListJSONView.as_view(),
        name="iniative-list-json"),

    url(r'^initiatives/(?P<slug>[-\w]+)/',
        view=homepage_views.InitiativeDetailView.as_view(),
        name="initiative-detail"),

    url(r'^initiatives/',
        view=homepage_views.InitiativeListView.as_view(),
        name="initiative-list"),

    #url(r'^partners.json',
    #    view=homepage_views.PartnerListJSONView.as_view(),
    #    name="partner-list-json"),

    url(r'^partners/(?P<slug>[-\w]+)/',
        view=homepage_views.PartnerDetailView.as_view(),
        name="partner-detail"),

    url(r'^partners/',
        view=homepage_views.PartnerListView.as_view(),
        name="partner-list"),

    url("^$", 
        view=homepage_views.HomepageView.as_view(), 
        name="homepage"),
]
