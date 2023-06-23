from django.forms import ModelForm
from .models import Task
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class TaskForm(ModelForm): #Form to add new Task with fields from Task model
    class Meta:

        model = Task
        fields = ['title', 'related_to'] #The fields that are shown in the form

class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'first_name', 'last_name', 'email'] 
        
