from django.shortcuts import render, redirect, get_object_or_404
from stock.models import Stock
from django.contrib import messages
from .models import FabricRequisitionBill, FabricRequisitionBillDetails, FabricRequisitionItem
from .forms import FabricRDetailsForm, FabricRItemFormset, FabricRForm, FabricRItemForm
from django.views.generic import (
    View, 
    ListView,
)

# Create your views here

class FabricRequiCreateView(View):                                                      
    template_name = 'fabric_requisition/create.html'

    def get(self, request):
        form = FabricRForm(request.GET or None)
        formset = FabricRItemFormset(request.GET or None)                          # renders an empty formset
        stocks = Stock.objects.filter(is_deleted=False)
        context = {
            'form'      : form,
            'formset'   : formset,
            'stocks'    : stocks
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = FabricRForm(request.POST)
        formset = FabricRItemFormset(request.POST)                                 # recieves a post method for the formset
        if form.is_valid() and formset.is_valid():
            # saves bill
            billobj = form.save(commit=False)
            billobj.save()     
            # create bill details object
            # billdetailsobj = FabricRequisitionBillDetails(billno=billobj)
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
                stock.quantity -= billitem.quantity             

                # saves bill item and stock
                stock.save()
                billitem.save()
            messages.success(request, "Fabric Requisition items have been registered successfully")
            return redirect('fabricr_read')
        form = FabricRForm(request.GET or None)
        formset = FabricRItemForm(request.GET or None)
        context = {
            'form'      : form,
            'formset'   : formset,
        }
        return render(request, self.template_name, context)
    
class FabricRequiView(ListView):
    model = FabricRequisitionBill 
    template_name = 'fabric_requisition/read.html'
    context_object_name = 'bills'
    ordering = ['-time']
    
class FabricRequiBillView(View):
    model = FabricRequisitionBill
    template_name = "bill/fr_bill.html"
    
    def get(self, request, billno):
        context = {
            'bill'          : FabricRequisitionBill.objects.get(billno=billno),
            'items'         : FabricRequisitionItem.objects.filter(billno=billno),
        }
        return render(request, self.template_name, context)

    def post(self, request, billno):
        form = FabricRDetailsForm(request.POST)
        if form.is_valid():
            billdetailsobj = FabricRequisitionBillDetails.objects.get(billno=billno)
            
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
            'bill'          : FabricRequisitionBill.objects.get(billno=billno),
            'items'         : FabricRequisitionItem.objects.filter(billno=billno),
            'billdetails'   : FabricRequisitionBillDetails.objects.get(billno=billno),
        }
        return render(request, self.template_name, context)