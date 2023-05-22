from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Person
from django.contrib import messages
from .forms import PersonForm

# def my_form_view(request):
#     form = MyForm()
#     if request.method == 'POST':
#         form = MyForm(request.POST)
#         if form.is_valid():
#             # Process the form data
#             # ...
#             form.save()
#             messages.success(request, 'Auto Populate created successfully')
#             return redirect('get_person_details')
        
#     context = {
#         'form': form
#     }
#     return render(request, 'auto_populate/my_form.html', context)

# def get_person_details(request):
#     person_id = request.GET.get('person_id')
#     try:
#         person = Person.objects.get(id=person_id)
#         response = {
#             'phone': person.phone,
#             'email': person.email,
#             'city': person.city
#         }
#         return JsonResponse(response)
#     except Person.DoesNotExist:
#         return JsonResponse({'error': 'Person not found.'})
    
    
from django.shortcuts import render
from django.http import JsonResponse
from .forms import EmployeeForm

def employee_form_view(request):
    form = EmployeeForm()
    return render(request, 'auto_populate/my_form.html', {'form': form})

def fetch_person_details(request):
    person_id = request.GET.get('person_id')
    person = Person.objects.filter(id=person_id).first()

    if person:
        data = {
            'phone': person.phone,
            'email': person.email,
            'city': person.city
        }
    else:
        data = {}

    return JsonResponse(data)



def create(request):
    form = PersonForm()
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Person created successfully')
            return redirect('create')
    context= {
        'form': form
    }
    return render(request, 'auto_populate/create.html', context)