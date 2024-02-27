from .models import Product

def get_all_products(info) -> list[str]:
    products = Product.objects.filter(stock_quantity__gt=0).order_by('-created_at')
    return products

def get_product(info, id: int):
    product = Product.objects.get(id=id)
    return product