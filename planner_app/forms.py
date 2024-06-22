from django import forms
from .models import TaskItem, TaskCategory


class TaskForm(forms.ModelForm):
    class Meta:
        model = TaskItem
        fields = [
            "title",
            "description",
            "category",
            "alternative_category",
            "status",
            "date_closed",
        ]

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["category"].queryset = TaskCategory.objects.filter(user=user)
        self.fields["alternative_category"].queryset = TaskCategory.objects.filter(
            user=user
        )
