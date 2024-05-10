# DJANGO CRUD

Este es un projecto de django en el cual hare **Login, Register, Rutas protegidas y más!**

## APPLICATION TASKS

```python
# creo una app de tasks, crea la carpeta **tasks** con archivos
python manage.py startapp tasks
```

```python
# djangocrud/settings.py
# ahora para que django reconozca la app que creamos haremos lo siguiente

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
# en esta lista tenemos las app, por defecto y la que  nosotros creamos, en este caso deberemos agregar la que acabamos de crear, entonces quedaria asi
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tasks' # la app que nosotros acabamos de crear
]

```

## CREANDO FORMULARIO DE SIGNUP

```python
# tasks/views.py

# importamos modulo que crea el formulario signup
from django.contrib.auth.forms import UserCreationForm

# creamos una funcion que servira de vista
def helloworld(request): 
    return render(request, 'signup.html', { # para este ej. cree un archivo signup.html
        'form': UserCreationForm # y para q django me cree el form auto, paso un diccionario con una prop y como valor
        # el metodo que hace esto UserCreationForm y al refrescar mi app ya podremos ver los cambios
    })

```

## REGISTRANDO UN USUARIO
```python
# creamos una vista para validar los datos del nuevo usuario
# con userCreationForm de Djando
def signup(request):
    if request.method == 'GET':
        form = UserCreationForm()  # Instancia del formulario para pasar al template
        return render(request, 'signup.html', {'form': form})
    else:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Esto crea el usuario y lo guarda en la base de datos
            return HttpResponse('Usuario creado satisfactoriamente!')
        else:
            # Si el formulario no es válido, vuelve a mostrar el formulario con los errores
            return render(request, 'signup.html', {'form': form})

```


```python
# en el archivo de urls.py creamos una ruta para el login
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('signup/', signup, name='signup') # <-- aqui registramos la nueva url
]
```

## LOGIN Y LISTA DE TAREAS
despues de hacer login el usuario se mantendra la sesion, para ello haremos lo siguiente

```python
# tasks/views.py
def signup(request):
    if request.method == 'GET':
        form = UserCreationForm()  # Instancia del formulario para pasar al template
        return render(request, 'signup.html', {'form': form})
    else:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user =form.save()  # Esto crea el usuario y lo guarda en la base de datos
            login(request, user) # <--- mantiene en sesion al usuario
            return redirect('tasks') # <--- redirecciona a la pagina de tasks
        else:
            # Si el formulario no es válido, vuelve a mostrar el formulario con los errores
            return render(request, 'signup.html', {'form': form})
        
def tasks(request):
    return render(request, 'tasks.html')
```

## TASK MODEL

```python
# aqui creo el modelo de TASK

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    creted  = models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateTimeField(null=True)
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
     
    def __str__(self): # <-- esto permite que al usarlo como string muestra la info que se retorna
        return f'{self.title} by {self.user}' 
```


## LISTAR TASKS


## PROTEGER LAS RUTAS
