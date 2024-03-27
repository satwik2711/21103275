import requests


def sort_products(products, sort_by):

    return sorted(products, key=lambda x: x.get(sort_by, 0), reverse=False)

def paginate_products(products, page, n):

    start = (page - 1) * n
    end = start + n
    return products[start:end]

def fetch_products(access_token, companyname, categoryname, top, min_price, max_price):

    url = f'http://20.244.56.144/test/companies/{companyname}/categories/{categoryname}/products?top={top}&minPrice={min_price}&maxPrice={max_price}'

    headers = {'Authorization': f'Bearer {access_token}'}
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        return []

