from django.urls import path
from .views import show_data

urlpatterns = [
    path('show-data/', show_data, name='show_data'),
    # Add more URL patterns as needed
]