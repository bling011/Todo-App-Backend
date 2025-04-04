from django.db import models
from django.utils import timezone

class Todo(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)  # Allow blank descriptions
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)  # Add timestamp
    updated_at = models.DateTimeField(auto_now=True)         # Auto update timestamp

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']  # Newest first
