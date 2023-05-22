from django import forms
from .models import Employee, Person
from django.db import models
from django.forms import fields, Widget

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        self.fields['person'].queryset = Person.objects.all()


class PersonForm(forms.ModelForm):
    name = forms.CharField(label='Person Name', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Person Name'}), required=True, error_messages={'required':'Must Enter a Correct Name'})
    class Meta:
        model = Person
        fields = '__all__'
        widgets = {
            'phone' : forms.TextInput(attrs = {'class' : 'textinput form-control'}),
            'email' : forms.EmailInput(attrs = {'class' : 'textinput form-control'}),
            'city' : forms.TextInput(attrs = {'class' : 'textinput form-control'}),
        }