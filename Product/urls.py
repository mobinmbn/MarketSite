from django.urls import path
from .views import *

urlpatterns = [
    path("product", product_view, name='product'),
    path("product/<pk>", product_single_view, name='single product'),
]
