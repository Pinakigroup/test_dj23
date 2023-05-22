from django import forms
from django.forms import formset_factory
from .models import StoreBill, StoreItem, StoreBillDetails
from stock.models import Stock
from category.models import Category

# form used to get customer details
class StoreForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['supplier'].widget.attrs.update({'class': 'textinput form-control'})
        # self.fields['name'].widget.attrs.update({'class': 'textinput form-control', 'pattern' : '[a-zA-Z\s]{1,50}', 'title' : 'Alphabets and Spaces only', 'required': 'true'})
        # self.fields['phone'].widget.attrs.update({'class': 'textinput form-control', 'maxlength': '10', 'pattern' : '[0-9]{10}', 'title' : 'Numbers only', 'required': 'true'})
        # self.fields['email'].widget.attrs.update({'class': 'textinput form-control'})
        
    class Meta:
        model = StoreBill
        fields = ['supplier', 'buyer_name', 'report', 'report_no', 'report_date', 'po_no', 'lc', 'style_no', 'file_no', 'lot_no', 'fabric_detail', 'store_location', 'order_qty']
        widgets = {
            
            'buyer_name' : forms.TextInput(attrs = {'class' : 'textinput form-control'}),
            'report' : forms.Select(attrs = {'class' : 'textinput form-control'}),
            'report_no' : forms.TextInput(attrs = {'class' : 'textinput form-control'}),
            'report_date' : forms.TextInput(attrs = {'class' : 'textinput form-control', 'type': 'date'}),
            'po_no' : forms.TextInput(attrs = {'class' : 'textinput form-control'}),
            'lc' : forms.TextInput(attrs = {'class' : 'textinput form-control'}),
            'style_no' : forms.TextInput(attrs = {'class' : 'textinput form-control'}),
            'file_no' : forms.TextInput(attrs = {'class' : 'textinput form-control'}),
            'lot_no' : forms.TextInput(attrs = {'class' : 'textinput form-control'}),
            'order_qty' : forms.NumberInput(attrs = {'class' : 'textinput form-control'}),
            'fabric_detail' : forms.Textarea(attrs = {'class' : 'textinput form-control', 'rows'  : '4'}),
            'store_location' : forms.TextInput(attrs = {'class' : 'textinput form-control'}),
        }
        labels = {
            'company': 'Company',
            'buyer_name': 'Buyer Name',
            'report': 'Inv/DC',
            'report_no': 'Inv/DC No',
            'report_date': 'Inv/DC Date',
            'po_no': 'PO No',
            'lc': 'LC',
            'style_no': 'Style No',
            'file_no': 'File No',
            'lot_no': 'Lot No',
            'product_item': 'Product Name',
            'fabric_color': 'Fabric Color',
            'fabric_detail': 'Fabric Detail',
            'store_location': 'Location',
            'order_qty': 'Order Qty',
            'receive_qty': 'Receive Qty',
            'uom': 'UOM',
            'unit_price': 'Uprice',
        }


class StoreItemForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].queryset = Category.objects.filter(is_deleted=False)
        self.fields['stock'].queryset = Stock.objects.filter(is_deleted=False)
        
        self.fields['category'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['stock'].widget.attrs.update({'class': 'textinput form-control setprice stock'})
        self.fields['quantity'].widget.attrs.update({'class': 'textinput form-control setprice quantity', 'min': '1'})
        self.fields['unit_price'].widget.attrs.update({'class': 'textinput form-control setprice price', 'min': '1'})
        self.fields['uom'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['fabric_color'].widget.attrs.update({'class': 'textinput form-control'})
    class Meta:
        model = StoreItem
        fields = ['stock', 'category', 'quantity', 'unit_price', 'uom', 'fabric_color']
    
        # widgets = {           
        #     'category' : forms.Select(attrs = {'class' : 'textinput form-control'}),            
        #     'stock' : forms.Select(attrs = {'class' : 'textinput form-control'}),   
        #     'quantity' : forms.NumberInput(attrs = {'class' : 'textinput form-control'}),         
        #     'unit_price' : forms.NumberInput(attrs = {'class' : 'textinput form-control'}),         
        #     'uom' : forms.Select(attrs = {'class' : 'textinput form-control'}),         
        #     'fabric_color' : forms.TextInput(attrs = {'class' : 'textinput form-control'}),         
        # }


    # Dependent Dropdown 
                
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
            
            
            

# formset used to render multiple 'StoreItemForm'
StoreItemFormset = formset_factory(StoreItemForm, extra=1)


# form used to accept the other details for Store bill
class StoreDetailsForm(forms.ModelForm):
    class Meta:
        model = StoreBillDetails
        fields = ['eway','veh', 'destination', 'po', 'cgst', 'sgst', 'igst', 'cess', 'tcs', 'total']
        
        
class StockSearchForm2(forms.ModelForm):
    start_date = forms.DateTimeField(label="Your Name", widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}), required=True)
    end_date = forms.DateTimeField(label="Your Name", widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}), required=True)
    class Meta:
        model = StoreBill
        fields = ['start_date', 'end_date']
