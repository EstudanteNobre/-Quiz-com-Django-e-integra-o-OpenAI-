from django.db import models

class Task(models.Model):
    label = models.CharField(max_length=100)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.label