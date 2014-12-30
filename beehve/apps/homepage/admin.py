from django.contrib import admin

from .models import Partner, Initiative, Brigade


admin.site.register(Brigade)
admin.site.register(Partner)
admin.site.register(Initiative)
