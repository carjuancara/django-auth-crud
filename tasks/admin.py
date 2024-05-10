from django.contrib import admin
from .models import Task # <-- para importar algo de la misma carpete anteponemos el (.) delante del nombre del archivo
# Register your models here.
admin.site.register(Task) # < --- aqui registro el modelo para que el panel de administracion me permita hacer CRUD sobre el modelo
