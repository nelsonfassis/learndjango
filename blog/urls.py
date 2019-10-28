from django.urls import path
from .views import (
    ArticleListView
)

app_name = "blog"
urlpatterns = [
    path('', ArticleListView.as_view(), name='article_list'),
    # path('create/', product_create_view, name='product_create'),
    # path('edit/<int:product_id>/', product_edit_view, name='product_edit'),
    # path('list/', product_list_view, name='product_list'),
    # path('delete/<int:product_id>/', product_delete_view, name='product_delete'),
]
