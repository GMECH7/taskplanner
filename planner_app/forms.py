from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import TaskCategory, TaskItem


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


class CategoryForm(forms.ModelForm):
    class Meta:
        model = TaskCategory
        fields = [
            "name",
            "description",
        ]

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)


class RegisterNewUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
