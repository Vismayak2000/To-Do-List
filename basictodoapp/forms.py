from django import forms

from basictodoapp.models import Task,User


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'completed']

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'password']