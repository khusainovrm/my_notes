from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Note(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="my_notess")
    text = models.CharField(max_length=40)
    date_created = models.DateTimeField("Дата создания", auto_now_add=True)

    class Meta:
        ordering = ('-date_created',)

    def __str__(self):
        return self.text

class Goal(models.Model):
    note = models.ForeignKey(Note, on_delete=models.CASCADE)
    text = models.CharField(max_length=60)

    def __str__(self):
        return self.text