from django.urls import path
from . import views

urlpatterns = [
    path('categories/<str:categoryname>/products/', views.product_list, name='product-list'),
    path('get_auth_token/', views.get_auth_token, name='get_auth_token'),
]
