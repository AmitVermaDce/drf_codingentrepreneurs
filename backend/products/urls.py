from django.urls import path
from .views import *

urlpatterns = [    
    path("", product_list_create_view, name="create_view"),
    # path("", product_list_view, name="list_view"),
    # path("", product_mixin_view, name="list_view"),
    path("<int:pk>/", product_detail_view, name="detail_view"),
    path("<int:pk>/update/", product_update_view, name="update_view"),
    path("<int:pk>/delete/", product_destroy_view, name="delete_view"),      
] 
