from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('create/', views.StoreCreateView.as_view(), name='create'),
    # path('', views.StoreView.as_view(), name='store_read'),
    path('', views.store_read, name='store_read'),
    path("bill/<billno>", views.StoreBillView.as_view(), name="store_bill"),
    path('delete/<int:pk>/', views.StoreDeleteView.as_view(), name='store_delete'),
    path('ajax/load-stocks/', views.load_stocks, name='ajax_load_stocks'), # AJAX 
]