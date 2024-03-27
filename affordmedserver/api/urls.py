from django.urls import path
from . import views

urlpatterns = [
    path('categories/<str:categoryname>/products/', views.product_list, name='product-list'),
    path('categories/<str:categoryname>/products/<str:productid>/', views.product_detail, name='product-detail'),
    path('register/', views.register, name='register'),
    path('get_auth_token/', views.get_auth_token, name='get_auth_token'),
    path('products/<str:companyname>/<str:categoryname>/', views.get_products, name='get_products'),
]
