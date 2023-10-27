from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Cart, Wishlist
from .serializer import CartSerializer, WishlistSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_cart(request):
    cart = Cart.objects.get(user=request.user)
    serializer = CartSerializer(cart)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_wishlist(request):
    wishlist = Wishlist.objects.get(user=request.user)
    serializer = WishlistSerializer(wishlist)
    return Response(serializer.data, status=status.HTTP_200_OK)
