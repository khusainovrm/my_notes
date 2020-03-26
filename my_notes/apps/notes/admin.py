from django.contrib import admin
from .models import Note, Goal


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ['text', 'author', 'date_created']
    #raw_id_fields = ('author',)
    #prepopulated_fields = {'slug': ('title',)}

@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    list_display = ['note', 'text']

