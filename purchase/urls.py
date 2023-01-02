from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('select_supplier/', views.SelectSupplierView.as_view(), name='select_supplier'),
    path('create/<pk>', views.PurchaseCreateView.as_view(), name='create'),  
    path('', views.PurchaseView.as_view(), name='purchases_list'),
    path("bill/<billno>", views.PurchaseBillView.as_view(), name="purchase_bill"),
    path('delete/<int:pk>/', views.PurchaseDeleteView.as_view(), name='purchase_delete'),
    # path('new/', views.StockCreateView.as_view(), name='new'),
    # path('<int:pk>/edit', views.StockUpdateView.as_view(), name='stock_update'),
    
    
    # path('create/', views.create, name="create"),
    # path('', views.product_read, name='product_read'),
    # path('<int:pk>/', views.product_update, name='product_update'),
    # path('delete/<int:pk>/', views.stock_delete, name='stock_delete'),   
]