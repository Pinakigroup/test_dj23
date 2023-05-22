from django import forms

from store2.models import Store2
from stock.models import Stock


class Store2CreationForm(forms.ModelForm):
    class Meta:
        model = Store2
        fields = ['id', 'address', 'birth_date', 'category', 'stock']
        widgets = {           
            'address' : forms.TextInput(attrs = {'class' : 'textinput form-control'}),
            'birth_date' : forms.TextInput(attrs = {'class' : 'textinput form-control', 'type': 'date'}),
            'category' : forms.Select(attrs = {'class' : 'textinput form-control'}),            
            'stock' : forms.Select(attrs = {'class' : 'textinput form-control'}),            
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['stock'].queryset = Stock.objects.none()
        
        if 'category' in self.data:
            try:
                category_id = int(self.data.get('category'))
                self.fields['stock'].queryset = Stock.objects.filter(category_id=category_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty stock queryset
        elif self.instance.pk:
            self.fields['stock'].queryset = self.instance.category.stock_set.order_by('name')
                