from django.contrib import admin

from .models import Reminder, ReminderTime


class ReminderTimesInline(admin.TabularInline):
    model = ReminderTime

def dispatch_tasks(modeladmin, request, queryset):
    for reminder in queryset:
        reminder.dispatch_task()


@admin.register(Reminder)
class Reminder(admin.ModelAdmin):
    inlines = [ReminderTimesInline, ]
    list_display = [
        'id',
        'message',
        'audiourl',
        'telnumber',
    ]
    actions = [dispatch_tasks]
