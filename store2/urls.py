from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('create/', views.store2_create_view, name="create"),
    path('', views.store2_read, name='store2_read'),
    # path('<int:pk>/', views.merchandiser_update, name='merchandiser_update'),
    # path('delete/<int:pk>/', views.merchandiser_delete, name='merchandiser_delete'),
    path('ajax/load-stocks/', views.load_stocks, name='ajax_load_stocks'), # AJAX
]