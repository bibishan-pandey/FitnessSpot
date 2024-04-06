from django.db import models


class BaseModel(models.Model):
    """
    Base model for all models in the application.
    """
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        abstract = True
        ordering = ['-created_at']
