from django.contrib import admin
from .models import Note, Goal

class NoteAdmin(admin.ModelAdmin):
    list_display = ['text', 'author']


class GoalAdmin(admin.ModelAdmin):
    list_display = ['note', 'text']


admin.site.register(Note, NoteAdmin)
admin.site.register(Goal, GoalAdmin)

