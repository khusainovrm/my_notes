from django.shortcuts import render

# Create your views here.
def notes_list (request):
    return render (request, "notes/notes_list.html")