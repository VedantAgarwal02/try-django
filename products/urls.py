from django.urls import path
from .views import *

app_name = "products"

urlpatterns = [
    path('create/', create_product),
    path('raw_create/', create_simple_product),
    path('<int:id>/', dynamic_product_view, name='product-details'),
    path('<int:id>/delete/', delete_product_view, name='product-delete'),
    path('', get_products, name='product-list'),
]