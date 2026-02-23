"""trydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from pages.views import home_view, about_view, contact_view
from products.views import (
    get_product, 
    create_product, 
    create_simple_product, 
    create_raw_product, 
    dynamic_product_view, 
    delete_product_view,
    get_products
)
# from products.urls import url_paths

urlpatterns = [
    path('', home_view, name='home'),
    path('about/', about_view, name='about'),
    path('contact/', contact_view, name='contact'),
    # path('product/', get_product, name='product-static-details'),
    # path('products/create/', create_product),
    # path('products/raw_create/', create_simple_product),
    # path('products/<int:id>/', dynamic_product_view, name='product-details'),
    # path('products/<int:id>/delete/', delete_product_view, name='product-delete'),
    # path('products/', get_products, name='product-list'),
    path('products/', include('products.urls')),
    path('blogs/', include('blogs.urls')),
    path('admin/', admin.site.urls),
]
