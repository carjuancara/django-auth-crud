from django import forms 
from .models import Task 

# con esta clase cree facilmente un formulario de Task con los campos que yo le especifique
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task # <-- tabla que usare para tomar los datos
        fields = ['title', 'description', 'important'] #<-- estos son los campos que quiero que se muestre en el formulario
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control', 'placeholder':'title'}),
            'description':forms.Textarea(attrs={'class':'form-control', 'placeholder':'description'}),
            'important':forms.CheckboxInput(attrs={'class':'form-check-input text-center'})
        }