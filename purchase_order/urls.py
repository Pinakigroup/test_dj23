from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('create/', views.PurchasesCreateView.as_view(), name='create'),
    path('', views.PurchasesView.as_view(), name='pur_read'),
    path("bill/<billno>", views.PurchasesBillView.as_view(), name="pur_bill"),
]