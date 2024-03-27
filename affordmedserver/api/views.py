from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Product

from .utils import fetch_products, sort_products, paginate_products
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


