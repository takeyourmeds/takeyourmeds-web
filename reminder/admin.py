from django.contrib import admin

from .models import Reminder


def dispatch_tasks(modeladmin, request, queryset):
    for reminder in queryset:
        reminder.dispatch_task()


@admin.register(Reminder)
class Reminder(admin.ModelAdmin):
    list_display = [
            'id',
            'cronstring',
            'message',
            'audiourl',
            'telnumber',
            'last_run',
        ]
    actions = [dispatch_tasks]
