from django.shortcuts import render, redirect, get_object_or_404
from.models import Task
from .forms import TaskForm

def home(request):
    tasks = Task.objects.all()
    completed_tasks = 0
    total_tasks = len(tasks)
    remaining_tasks = 0
    pct = 0
    
    #Contando quab=ntas tarefas existem
    for task in tasks:
        if task.done == True:
            completed_tasks += 1

    #Contar quantas tarefas ainda falta
    remaning_task = total_tasks - completed_tasks
    
    #Calculando porcentagem
    if total_tasks > 0:
        pct = int((completed_tasks / total_tasks)*100)
        
    return render(
        request,
        'tarefas/home.html',
          {
              'tasks' : tasks,
              'total' : total_tasks,
              'completed' : completed_tasks,
              'remaning' : remaining_tasks,
              'pct' : pct
            
          })
    
def add(request):
    form = TaskForm(request.POST)
    if form.is_valid():
        form.save()
    return redirect('home')

def toggle(reqwuest, id):
    task = get_object_or_404(Task, id=id)
    
    if task.done == True:
        task.done = False
    else:
        task.done = True
        
    task.save()
    return redirect('home')

def delete(request, id):
    task = get_object_or_404(Task, id=id)
    task.delete()
    return redirect('home')