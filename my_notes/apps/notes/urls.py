from django.urls import path
from . import views


app_name = "notes"
urlpatterns = [
    path('', views.notes_list, name = "notes_list"),
    path ('delete/<int:note_id>/', views.notedelete, name="note_delete"),
]

