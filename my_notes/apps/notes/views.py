from django.shortcuts import render, redirect
from .models import Note
from .forms import NoteForm
from django.contrib.auth.models import User

# Create your views here.
def notes_list (request):
    notes = Note.objects.all()
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            new_note = form.save(commit=False)
            new_note.author = request.user
            new_note.save()
            return redirect("notes:notes_list")
    else:
        form = NoteForm()

    context = {
        'notes': notes,
        'form': form,
    }
    return render (request, "notes/notes_list.html", context)

def note_all (request):
    form = NoteForm(request.Post)
    if form.is_valid():
        form.save()
        form.NoteForm()
    context = {
        "form" : form
    }
    return render (request, "notes/note_all.html", context)
