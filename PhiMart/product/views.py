from rest_framework.decorators import api_view
from rest_framework.response import Response
from product.models import Product

# Create your views here.

@api_view()
def view_specific_product(request, id):
    try:
        product = Product.objects.get(pk=id)
        product_dict = {
            'id': product.id,
            'name': product.name,
            'price': product.price,
        }
        return Response(product_dict)
    except Product.DoesNotExist:
        return Response({'message': 'Product dones not exists'})


@api_view()
def view_categories(request):
    return Response({'message': 'Categories'})