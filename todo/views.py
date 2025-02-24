from django.shortcuts import render, redirect, get_object_or_404                                
from .models import Task
from .forms import TaskForm

# Create your views here.

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'todo/task_list.html', {'tasks' : tasks}) # pass the tasks to template...


def task_create(request):
    if request.method == "POST":
        description = request.POST.get("description")  # Get task from input field
        if description:
            Task.objects.create(description = description)  # Save to DB
        return redirect('task_list')  # Refresh page
    return render(request, 'todo/task_form.html')
        

def task_update(request, pk):
    task = get_object_or_404(Task, pk = pk)
    
    if request.method == "POST":
        form = TaskForm(request.POST, instance = task)
        if form.is_valid():
            form.save()
            return redirect('task_list') 
    else:
        form = TaskForm(instance = task)
    
    return render(request, 'todo/task_form.html', {'form' : form})

def task_delete(request, pk):
    task = get_object_or_404(Task, pk = pk)
    if request.method == "POST":
        task.delete() # delete the task from the database
        return redirect("task_list")
    
    return render(request, 'todo/task_confirm_delete.html', {'task' : task})



def task_complete(request, pk):
    task = get_object_or_404(Task, pk = pk)
    task.completed = True 
    task.save()
    return redirect('task_list')
                        