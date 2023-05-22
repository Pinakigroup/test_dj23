from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Store2
from stock.models import Stock
from .forms import Store2CreationForm

# Create your views here.


def store2_create_view(request):
    form = Store2CreationForm()
    if request.method == 'POST':
        form = Store2CreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('store2_read')
        
    context = {
        'form': form         
        }
    return render(request, 'store2/create.html', context)

# Read 
# @allowed_users(allowed_roles=['admin', 'merchandiser'])
# @login_required
def store2_read(request):
    store2_data = Store2.objects.all().order_by('-id')
    context = {
        'store2_data': store2_data
    }  
    return render(request, 'store2/read.html', context)



# AJAX
def load_stocks(request):
    category_id = request.GET.get('category_id')
    stocks = Stock.objects.filter(category_id=category_id).all()
    context = {
        'stocks': stocks
        }
    return render(request, 'store2/store2_dropdown_list_options.html', context)
    # return JsonResponse(list(stocks.values('id', 'name')), safe=False)