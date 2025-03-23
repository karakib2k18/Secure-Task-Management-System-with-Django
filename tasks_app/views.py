from django.shortcuts import render, get_object_or_404, redirect
from .models import Task, Category
from .forms import TaskForm

def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()  # Save the task
            return redirect('task_list')  # Redirect to task list after creation
    else:
        form = TaskForm()

    return render(request, 'tasks_app/task_create.html', {'form': form})

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks_app/task_list.html', {'tasks': tasks})

def task_detail(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    return render(request, 'tasks_app/task_detail.html', {'task': task})

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'tasks_app/category_list.html', {'categories': categories})

def category_tasks(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    tasks = Task.objects.filter(category=category)
    return render(request, 'tasks_app/category_tasks.html', {'category': category, 'tasks': tasks})
