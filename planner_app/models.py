from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class TaskCategory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.name)


class TaskItemManager(models.Manager):
    def for_user(self, user):
        return super().get_queryset().filter(user=user)


class TaskItem(models.Model):
    STATUS_CHOICES = [
        ("completed", "Completed"),
        ("open", "Open"),
        ("cancelled", "Cancelled"),
        ("optional", "Optional"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(
        TaskCategory, related_name="tasks", on_delete=models.CASCADE
    )
    alternative_category = models.ForeignKey(
        TaskCategory,
        related_name="alternative_tasks",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="open")
    date_created = models.DateTimeField(auto_now_add=True)
    date_closed = models.DateTimeField(blank=True, null=True)

    objects = TaskItemManager()

    def __str__(self):
        return str(self.title)

    def close_task(self):
        self.status = "completed"
        self.date_closed = timezone.now()
        self.save()
