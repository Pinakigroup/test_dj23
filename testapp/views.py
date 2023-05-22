from django.shortcuts import render, get_object_or_404
from .forms import MyForm
from .models import MyModel

# Create your views here.

def show_data(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            id = form.cleaned_data['id']
            my_data = get_object_or_404(MyModel, id=id)
            return render(request, 'testapp/create.html', {'form': form, 'my_data': my_data})
    else:
        form = MyForm()
    return render(request, 'testapp/create.html', {'form': form})