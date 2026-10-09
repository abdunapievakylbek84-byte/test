from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=255, verbose_name="CharField")
    description = models.TextField(blank=True, verbose_name="TextField")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="DateTimeField")
    completed = models.BooleanField(default=False, verbose_name="BooleanField")

    def __str__(self):
        return self.title
