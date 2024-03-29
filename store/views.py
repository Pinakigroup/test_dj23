from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from stock.models import Stock
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import StoreBill, StoreBillDetails, StoreItem
from .forms import StoreDetailsForm, StoreItemFormset, StoreForm, StoreItemForm, StockSearchForm2
from django.views.generic import (
    View, 
    ListView,
    DeleteView,
    UpdateView,
)

# Create your views here

class StoreCreateView(View):                                                      
    template_name = 'store/create.html'

    def get(self, request):
        form = StoreForm(request.GET or None)
        formset = StoreItemFormset(request.GET or None)                          # renders an empty formset
        stocks = Stock.objects.filter(is_deleted=False)
        context = {
            'form'      : form,
            'formset'   : formset,
            'stocks'    : stocks
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = StoreForm(request.POST)
        formset = StoreItemFormset(request.POST)                                 # recieves a post method for the formset
        if form.is_valid() and formset.is_valid():
            # saves bill
            billobj = form.save(commit=False)
            billobj.save()     
            # create bill details object
            # billdetailsobj = StoreBillDetails(billno=billobj)
            # billdetailsobj.save()
            for form in formset:                                                # for loop to save each individual form as its own object
                # false saves the item and links bill to the item
                billitem = form.save(commit=False)
                billitem.billno = billobj                                       # links the bill object to the items
                # gets the stock item
                stock = get_object_or_404(Stock, name=billitem.stock.name)  
                # calculates the total price
                billitem.totalprice = billitem.unit_price * billitem.quantity
                # updates quantity in stock db
                stock.quantity += billitem.quantity             

                # saves bill item and stock
                stock.save()
                billitem.save()
            messages.success(request, "Stores items have been registered successfully")
            return redirect('store_read')
        form = StoreForm(request.GET or None)
        formset = StoreItemForm(request.GET or None)
        context = {
            'form'      : form,
            'formset'   : formset,
        }
        return render(request, self.template_name, context)
    
# Class Base 
# class StoreView(ListView):
#     model = StoreBill 
#     template_name = 'store/read.html'
#     context_object_name = 'bills'
#     ordering = ['-time']
    
# Functions Base 
@method_decorator(login_required, name='dispatch')
def store_read(request):
    form = StockSearchForm2(request.POST or None)
    bills = StoreBill.objects.all()
    context = {
        'bills':bills,
        'form':form,
    }
    if request.method == 'POST':
        bills = StoreBill.objects.filter(
										date_created__range=[
																form['start_date'].value(),
																form['end_date'].value()
															]
										)
    context = {
        'bills':bills,
        'form':form,
    }
    return render(request, 'store/read.html', context)
    
    
    
class StoreBillView(View):
    model = StoreBill
    template_name = "bill/store_bill.html"
    
    def get(self, request, billno):
        context = {
            'bill'          : StoreBill.objects.get(billno=billno),
            'items'         : StoreItem.objects.filter(billno=billno),
        }
        return render(request, self.template_name, context)

    def post(self, request, billno):
        form = StoreDetailsForm(request.POST)
        if form.is_valid():
            billdetailsobj = StoreBillDetails.objects.get(billno=billno)
            
            billdetailsobj.eway = request.POST.get("eway")    
            billdetailsobj.veh = request.POST.get("veh")
            billdetailsobj.destination = request.POST.get("destination")
            billdetailsobj.po = request.POST.get("po")
            billdetailsobj.cgst = request.POST.get("cgst")
            billdetailsobj.sgst = request.POST.get("sgst")
            billdetailsobj.igst = request.POST.get("igst")
            billdetailsobj.cess = request.POST.get("cess")
            billdetailsobj.tcs = request.POST.get("tcs")
            billdetailsobj.total = request.POST.get("total")

            billdetailsobj.save()
            messages.success(request, "Bill details have been modified successfully")
        context = {
            'bill'          : StoreBill.objects.get(billno=billno),
            'items'         : StoreItem.objects.filter(billno=billno),
            'billdetails'   : StoreBillDetails.objects.get(billno=billno),
        }
        return render(request, self.template_name, context)
    
# Delete
# @login_required
# def product_delete(request, pk):
#     get_product = get_object_or_404(StoreBill, pk=pk)
#     get_product.delete()
#     messages.error(request, 'Product delete successfully')
#     return redirect('product_read')

class StoreDeleteView(SuccessMessageMixin, DeleteView):
    model = StoreBill
    template_name = "store/delete.html"
    success_url = '/store'
    
    def delete(self, *args, **kwargs):
        self.object = self.get_object()
        items = StoreItem.objects.filter(billno=self.object.billno)
        for item in items:
            stock = get_object_or_404(Stock, name=item.stock.name)
            if stock.is_deleted == False:
                stock.quantity -= item.quantity
                stock.save()
        messages.success(self.request, "Purchase bill has been deleted successfully")
        return super(StoreDeleteView, self).delete(*args, **kwargs)
    

# used to update a supplier's info
class StoreUpdateView(SuccessMessageMixin, UpdateView):
    model = StoreBill
    # form_class = SupplierForm
    success_url = '/store'
    success_message = "Store details has been updated successfully"
    template_name = "suppliers/edit_supplier.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Edit Supplier'
        context["savebtn"] = 'Save Changes'
        context["delbtn"] = 'Delete Supplier'
        return context
    

# AJAX
def load_stocks(request):
    country_id = request.GET.get('country_id')
    stocks = Stock.objects.filter(country_id=country_id).order_by('name')
    context = {
        'stocks': stocks         
        }
    return render(request, 'person/city_dropdown_list_options.html', context)