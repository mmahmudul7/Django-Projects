from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, DestroyModelMixin
from order.models import Cart, CartItem
from order.serializers import CartSerializer, CartItemSerializer, AddCartItemSerializer


class CartViewSet(CreateModelMixin, RetrieveModelMixin, DestroyModelMixin, GenericViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class CartItemViewSet(ModelViewSet):
    serializer_class = CartItemSerializer

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return AddCartItemSerializer
        return CartItemSerializer
    
    # def get_serializer(self):
    #     return {'cart_id': self.kwargs['cart_pk']}

    def get_serializer(self, *args, **kwargs):
        kwargs.setdefault('context', self.get_serializer_context())
        kwargs['context']['cart_id'] = self.kwargs['cart_pk']
        return super().get_serializer(*args, **kwargs)

    def get_queryset(self):
        return CartItem.objects.filter(cart_id=self.kwargs['cart_pk'])