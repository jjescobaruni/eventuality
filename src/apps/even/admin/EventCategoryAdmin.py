from django.contrib import admin
from apps.even.models.EventCategory import EventCategory

class EventCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'parent_category']
    ordering = ['name']

admin.site.register(EventCategory, EventCategoryAdmin)
