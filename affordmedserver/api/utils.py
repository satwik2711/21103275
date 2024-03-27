def sort_products(products, sort_by):

    return sorted(products, key=lambda x: x.get(sort_by, 0), reverse=False)

def paginate_products(products, page, n):

    start = (page - 1) * n
    end = start + n
    return products[start:end]

