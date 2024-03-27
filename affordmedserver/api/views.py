from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Product

from .utils import fetch_products, fetch_product_detail
import requests

from .models import AccessToken
from django.conf import settings



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def product_list(request, categoryname):
    sort_by = request.query_params.get('sort', 'rating')
    page = int(request.query_params.get('page', 1))
    n = int(request.query_params.get('n', 10))

    products = fetch_products(categoryname, sort_by)
    sorted_products = sort_products(products, sort_by)
    page_of_products = paginate_products(sorted_products, page, n)

    return Response(page_of_products)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def product_detail(request, categoryname, productid):
    product = fetch_product_detail(categoryname, productid)
    return Response(product)




# @api_view(['POST'])
# def register(request):
#     data = request.data
#     response = requests.post('http://20.244.56.144/test/register', json=data)
#     response_data = response.json()

#     if response.status_code == 200:
#         AccessToken.objects.create(
#             company_name=data.get('companyName'),
#             client_id=response_data['clientID'],
#             client_secret=response_data['clientSecret'],
#             access_token=''  
#         )
#     return Response(response_data, status=response.status_code)

@api_view(['GET'])
def get_auth_token(request):

    company_name = request.query_params.get('companyName')
    access_token_obj = AccessToken.objects.get(company_name=company_name)

    data = {
        'companyName': company_name,
        'clientID': access_token_obj.client_id,
        'clientSecret': access_token_obj.client_secret,
        'ownerName': request.query_params.get('ownerName'),
        'ownerEmail': request.query_params.get('ownerEmail'),
        'rollNo': request.query_params.get('rollNo'),
    }
    response = requests.post('http://20.244.56.144/test/auth', json=data)
    response_data = response.json()

    access_token_obj.access_token = response_data['access_token']
    access_token_obj.save()

    return Response(response_data)

@api_view(['GET'])
def get_products(request, companyname, categoryname):
    access_token_obj = AccessToken.objects.get(company_name=companyname)
    auth_token = access_token_obj.access_token

    top = request.query_params.get('top')
    min_price = request.query_params.get('minPrice')
    max_price = request.query_params.get('maxPrice')

    headers = {'Authorization': f'Bearer {auth_token}'}
    url = f'http://20.244.56.144/test/companies/{companyname}/categories/{categoryname}/products?top={top}&minPrice={min_price}&maxPrice={max_price}'

    response = requests.get(url, headers=headers)
    return Response(response.json())