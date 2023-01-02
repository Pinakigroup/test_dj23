from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.SupplierListView.as_view(), name='supplier_read'),
    path('new/', views.SupplierCreateView.as_view(), name='new'),
    path('<int:pk>/edit', views.SupplierUpdateView.as_view(), name='supplier_update'),
    path('delete/<int:pk>/', views.supplier_delete, name='supplier_delete'),   
]