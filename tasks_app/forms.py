from django import forms
from .models import Task, Category

class TaskForm(forms.ModelForm):
    due_date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'dd/mm/yyyy',
                'type': 'date'  # This gives you a date picker in modern browsers
            }
        ),
        input_formats=['%Y-%m-%d']  # Format expected from HTML5 date input
    )

    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'status', 'priority', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'priority': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }
