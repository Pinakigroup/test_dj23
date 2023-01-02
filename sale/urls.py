from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('create/', views.SaleCreateView.as_view(), name='create'),
    path('', views.SaleView.as_view(), name='sale_read'),
    path("bill/<billno>", views.SaleBillView.as_view(), name="sale_bill"),
]