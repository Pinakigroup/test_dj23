from django import forms
from django.forms import formset_factory
from .models import PurchasesItem, PurchasesBillDetails, PurchasesBill
from stock.models import Stock

class PurchasesForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'textinput form-control', 'pattern' : '[a-zA-Z\s]{1,50}', 'title' : 'Alphabets and Spaces only', 'required': 'true'})
        self.fields['phone'].widget.attrs.update({'class': 'textinput form-control', 'maxlength': '10', 'pattern' : '[0-9]{10}', 'title' : 'Numbers only', 'required': 'true'})
        self.fields['supplier'].widget.attrs.update({'class': 'textinput form-control'})
        
    class Meta:
        model = PurchasesBill
        fields = ['name', 'phone', 'address', 'email']
        widgets = {
            'address' : forms.Textarea(attrs = {'class' : 'textinput form-control', 'rows'  : '4'})
        }


# form used to render a single stock item form
class PurchasesItemForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['stock'].queryset = Stock.objects.filter(is_deleted=False)
        self.fields['stock'].widget.attrs.update({'class': 'textinput form-control setprice stock', 'required': 'true'})
        self.fields['quantity'].widget.attrs.update({'class': 'textinput form-control setprice quantity', 'min': '0', 'required': 'true'})
        self.fields['unit_price'].widget.attrs.update({'class': 'textinput form-control setprice price', 'min': '0', 'required': 'true'})
    class Meta:
        model = PurchasesItem
        fields = ['stock', 'quantity', 'unit_price']

# formset used to render multiple 'PurchaseItemForm'
PurchasesItemFormset = formset_factory(PurchasesItemForm, extra=1)

class PurchasesDetailsForm(forms.ModelForm):
    class Meta:
        model = PurchasesBillDetails
        fields = ['eway','veh', 'destination', 'po', 'cgst', 'sgst', 'igst', 'cess', 'tcs', 'total']