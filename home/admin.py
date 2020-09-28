from django.contrib import admin
from .models import Pillars, VisionMissionAbout


class PillarsAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'active')
    list_filter = ('title', 'active')
    search_fields = ('title', 'content')


class VisionMissionAboutAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'active')
    list_filter = ('title', 'active')
    search_fields = ('title', 'content')


admin.site.register(VisionMissionAbout, VisionMissionAboutAdmin)
admin.site.register(Pillars, PillarsAdmin)
