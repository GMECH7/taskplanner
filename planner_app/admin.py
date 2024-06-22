from django.contrib import admin
from .models import TaskCategory, TaskItem

# Register your models here.
admin.site.register(TaskCategory)
admin.site.register(TaskItem)
