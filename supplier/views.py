from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import (
    View, CreateView, UpdateView, ListView
)
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from .models import Supplier
from .forms import SupplierForm
# Create your views here.


# Create 
class SupplierCreateView(SuccessMessageMixin, CreateView):                                 # createview class to add new stock, mixin used to display message
    model = Supplier                                                                       # setting 'Stock' model as model
    form_class = SupplierForm                                                              # setting 'StockForm' form as form
    template_name = "supplier/create.html"                                                 # 'edit_stock.html' used as the template
    success_url = '/supplier'                                                                 # redirects to 'inventory' page in the url after submitting the form
    success_message = "Supplier has been created successfully"                             # displays message when form is submitted

    def get_context_data(self, **kwargs):                                               # used to send additional context
        context = super().get_context_data(**kwargs)
        return context  
    

# Read
class SupplierListView(ListView):
    model = Supplier 
    template_name = 'supplier/read.html'
    context_object_name = 'suppliers'
    paginate_by = 10
        
# Update 
class SupplierUpdateView(SuccessMessageMixin, UpdateView):                                 # updateview class to edit stock, mixin used to display message
    model = Supplier                                                                       # setting 'Stock' model as model
    form_class = SupplierForm                                                              # setting 'StockForm' form as form
    template_name = "supplier/update.html"                                                 # 'edit_stock.html' used as the template
    success_url = '/supplier'                                                              # redirects to 'inventory' page in the url after submitting the form
    success_message = "Supplier details has been updated successfully"                             # displays message when form is submitted

    def get_context_data(self, **kwargs):                                               # used to send additional context
        context = super().get_context_data(**kwargs)
        return context
    
# Delete 
def supplier_delete(request, pk):
    get_supplier = get_object_or_404(Supplier, pk=pk)
    get_supplier.delete()
    messages.error(request, 'Supplier delete successfully')
    return redirect('supplier_read')