from django.db import models

# Create your models here.
class Note(models.Model):
    author = models.CharField(max_length=20)
    text = models.CharField(max_length=40)

    def __str__(self):
        return self.text

class Goal(models.Model):
    note = models.ForeignKey(Note, on_delete=models.CASCADE)
    text = models.CharField(max_length=60)

    def __str__(self):
        return self.text