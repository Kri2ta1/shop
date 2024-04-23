from django.urls import path
from .views import *

urlpatterns = [
    path('', catalog, name='catalog'),
    path('order/', order, name='order'),
    path('product_detail/<int:product_id>/', product_detail, name='product_detail')
]
