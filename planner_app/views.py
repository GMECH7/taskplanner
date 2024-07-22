from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import TaskItem, TaskCategory
from .forms import TaskForm, CategoryForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def home(request):
    context = {}
    return render(request, "planner_app/home.html", context)


@login_required
def task(request):
    """This is the view of the created tasks"""
    tasks = TaskItem.objects.filter(user=request.user)  # Filter tasks by logged-in user

    sort_by_task_category = request.GET.get("sort_by_task_category")
    if sort_by_task_category == "category":
        tasks = tasks.order_by("-category")  # Sort tasks alphabetically by category

    context = {
        "tasks": tasks,
    }
    return render(request, "planner_app/task_list.html", context)


@login_required
def task_detail(request, pk):
    task = get_object_or_404(TaskItem, pk=pk)
    return render(request, "planner_app/task_detail.html", {"task": task})


@login_required
def task_create(request):
    """task create form"""
    if request.method == "POST":
        form = TaskForm(request.user, request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            # This ensures that the task is associated with the user who created it
            task.user = request.user
            # This commits the task instance to the database, saving the new task along with the associated user
            task.save()
            return redirect("task_detail", pk=task.pk)
    else:
        form = TaskForm(request.user)

    return render(request, "planner_app/task_form.html", {"form": form})


@login_required
def task_edit(request, pk):
    """task editing form"""
    task = get_object_or_404(TaskItem, pk=pk)
    if request.method == "POST":
        form = TaskForm(request.user, request.POST, instance=task)
        if form.is_valid():
            task = form.save()
            return redirect("task_detail", pk=task.pk)
    else:
        form = TaskForm(request.user, instance=task)
    return render(request, "planner_app/task_form.html", {"form": form})


@login_required
def task_status_update(request, pk):
    """Update task's status inside the table. No view rendering"""
    task = get_object_or_404(TaskItem, pk=pk, user=request.user)
    if request.method == "POST":
        new_status = request.POST.get("status")
        if new_status in dict(TaskItem.STATUS_CHOICES):
            task.status = new_status
            task.save()
    return redirect("task")


@login_required
def category(request):
    """This is the view of the created categories"""
    # Filter categories by logged-in user
    categories = TaskCategory.objects.filter(user=request.user)

    context = {
        "categories": categories,
    }
    return render(request, "planner_app/category_list.html", context)


@login_required
def category_detail(request, pk):
    """ """
    category = get_object_or_404(TaskCategory, pk=pk)
    return render(request, "planner_app/category_detail.html", {"category": category})


@login_required
def category_create(request):
    """category create form"""
    if request.method == "POST":
        form = CategoryForm(request.user, request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            # This ensures that the task is associated with the user who created it
            category.user = request.user
            # This commits the task instance to the database, saving the new task along with the associated user
            category.save()
            return redirect("category_detail", pk=category.pk)
    else:
        form = CategoryForm(request.user)

    return render(request, "planner_app/category_form.html", {"form": form})


@login_required
def category_edit(request, pk):
    """category editing form"""
    category = get_object_or_404(TaskCategory, pk=pk)
    if request.method == "POST":
        form = CategoryForm(request.user, request.POST, instance=category)
        if form.is_valid():
            category = form.save()
            return redirect("category_detail", pk=category.pk)
    else:
        form = CategoryForm(request.user, instance=category)
    return render(request, "planner_app/category_form.html", {"form": form})


def custom_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("task")
    else:
        form = AuthenticationForm()

    return render(request, "planner_app/login.html", {"form": form})


def custom_logout(request):
    logout(request)
    return redirect("login")
