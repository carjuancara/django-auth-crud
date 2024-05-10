from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse
from .forms import TaskForm
from .models import Task
from django.utils import timezone
from django.contrib.auth.decorators import login_required
# Create your views here.
# aqui creo las funciones que serviran de vista para mi projecto
# al ejecutar UserCreationForm me devolvera un formulario
    
def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'GET':
        form = UserCreationForm()  # Instancia del formulario para pasar al template
        return render(request, 'signup.html', {'form': form})
    else:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user =form.save()  # Esto crea el usuario y lo guarda en la base de datos
            login(request, user) # mantiene en sesion al usuario
            return redirect('tasks') # <--- redirecciona a la pagina de tasks
        else:
            # Si el formulario no es válido, vuelve a mostrar el formulario con los errores
            return render(request, 'signup.html', {'form': form})
@ login_required        
def tasks(request):
    task = Task.objects.filter(user=request.user, datecompleted__isnull=True) # <-- traemos solo las tareas del usuario logueado
    # y los que tengan la prop datecompleted con el subfijo __isnull=True, asi trae solo las que falten completar
    return render(request, 'tasks.html', { 'tasks':task})

@ login_required
def tasks_completed(request):
    task = Task.objects.filter(user=request.user, datecompleted__isnull=False).order_by('-datecompleted') # <-- traemos solo las tareas del usuario logueado
    # y los que tengan la prop datecompleted con el subfijo __isnull=True, asi trae solo las que falten completar
    return render(request, 'tasks.html', { 'tasks':task})

@ login_required
def task_detail(request, id):
    if request.method == 'GET':
        task = get_object_or_404(Task, pk=id, user=request.user)
        form = TaskForm(instance=task)
        return render(request, 'task_detail.html', { 'task':task, 'form':form})
    else:
       try:
            task = get_object_or_404(Task, pk=id, user=request.user)
            form = TaskForm(request.POST, instance=task)
            form.save()
            return redirect('tasks')
       except ValueError:
            return render(request, 'task_detail.html', { 'task':task_detail, 'form':form, 'error': 'Error actualizando la tarea'})

@ login_required
def complete_task(request, id):
    task =get_object_or_404(Task, pk=id, user=request.user)
   
    if request.method == 'POST':
        task.datecompleted = timezone.now()
        task.save()
        return redirect('tasks')

@ login_required
def delete_task(request, id):
    task =get_object_or_404(Task, pk=id, user=request.user)
   
    if request.method == 'POST':
        task.delete()
        return redirect('tasks')

@ login_required
def create_task(request):
    if request.method == 'GET':
        return render(request, 'create_task.html', { 'form': TaskForm})
    else:
        try:
            form = TaskForm(request.POST)
            new_task = form.save(commit=False)
            new_task.user=request.user
            new_task.save()
            return redirect('tasks')
        except:
            return render(request, 'create_task.html', { 'form': TaskForm, 'error':'por favor, verifica los datos'})

@ login_required
def signout(request):
    logout(request)
    return redirect('/')

def signin(request):
    if request.method == 'GET':
        form = AuthenticationForm()
        return render(request, 'signin.html', {'form': form})
    else:
        user = authenticate(request, username= request.POST['username'], password= request.POST['password'])
        print(user)
        if user is None:
            return render(request, 'signin.html', {'form': AuthenticationForm, 'error':'usernane or password incorrect'})
        else:
            login(request, user)
            return redirect('/tasks')
            

    
    
    