from django.contrib import admin

from .models import (Topic, Event, Technology, Project)


class SlugAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Topic)
admin.site.register(Event)
admin.site.register(Technology)
admin.site.register(Project)