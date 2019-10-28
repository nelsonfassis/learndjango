from django.urls import path

from .views import (
    product_detail_view, 
    product_create_view, 
    product_edit_view, 
    product_delete_view, 
    product_list_view
)

app_name = "products"
urlpatterns = [
    path('product/<int:product_id>', product_detail_view, name='product'),
    path('create/', product_create_view, name='product_create'),
    path('edit/<int:product_id>/', product_edit_view, name='product_edit'),
    path('list/', product_list_view, name='product_list'),
    path('delete/<int:product_id>/', product_delete_view, name='product_delete'),
]
