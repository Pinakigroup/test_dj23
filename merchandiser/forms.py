from django import forms
from django.db import models
from django.forms import fields, widgets
from .models import Merchandiser


class MerchandiserForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'textinput form-control', 'pattern' : '[a-zA-Z\s]{1,50}', 'title' : 'Alphabets and Spaces only', 'required': 'true'})
        self.fields['phone'].widget.attrs.update({'class': 'textinput form-control', 'maxlength': '10', 'pattern' : '[0-9]{10}', 'title' : 'Numbers only', 'required': 'true'})
        self.fields['email'].widget.attrs.update({'class': 'textinput form-control'})
        
    class Meta:
        model = Merchandiser
        fields = ['id', 'office_id', 'name', 'phone', 'email', 'designation', 'access_area', 'joining_date']
        widgets = {
            'office_id' : forms.TextInput(attrs = {'class' : 'textinput form-control'}),
            'designation' : forms.TextInput(attrs = {'class' : 'textinput form-control'}),
            # 'address' : forms.Textarea(attrs = {'class' : 'textinput form-control', 'rows'  : '4'}),
            'access_area' : forms.TextInput(attrs = {'class' : 'textinput form-control'}),
            'joining_date' : forms.TextInput(attrs = {'class' : 'textinput form-control', 'type': 'date'}),
        }
        