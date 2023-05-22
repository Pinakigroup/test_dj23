from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('person/', views.create, name="create"),
    path('create/', views.employee_form_view, name="employee_form_view"),
    path('', views.fetch_person_details, name='fetch_person_details'),
    # path('<int:pk>/', views.category_update, name='category_update'),
    # path('delete/<int:pk>/', views.category_delete, name='category_delete'),   
]