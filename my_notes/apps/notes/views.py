from django.shortcuts import render
from .models import Note
from .forms import NoteForm
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def notes_list (request):
    var = request.POST
    notes = Note.objects.all()
    context = {
        "var" : var,
        'notes': notes
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
