from django.db import models
from nannies.models import Nanny
from django.utils import timezone


class CommentManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted_at=None)


class Comment(models.Model):
    nanny = models.ForeignKey(
        Nanny,
        on_delete=models.CASCADE,
    )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True)

    objects = CommentManager()

    def delete(self):
        self.deleted_at = timezone.now()
        self.save()
