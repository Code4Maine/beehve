from django.contrib import admin

from .models import Buzz, Topic, Event, Technology, Project, ProjectCommit, Link


class SlugAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Link)
admin.site.register(Topic)
admin.site.register(Event)
admin.site.register(Technology)
admin.site.register(Project)
admin.site.register(ProjectCommit)
admin.site.register(Buzz)
