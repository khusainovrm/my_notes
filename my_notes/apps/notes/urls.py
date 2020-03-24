from django.urls import path
from . import views


app_name = "notes"
urlpatterns = [
    path('', views.notes_list, name = "notes_list"),
    #path ('all/', views.note_all, name="note_all"),

]