# views.py
from rest_framework import generics
from .models import Product
from .serializer import ProductSerializer
import base64
from django.http import HttpResponse

def get_image_data_url(image_path):
    try:
        with open(image_path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode()
        return f"data:image/png;base64,{encoded_string}"
    except Exception as e:
        print(f"Error loading image: {e}")
        return None

from django.db.models import Q

class ProductListView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.all()

        # Filter by gender
        gender = self.request.query_params.get('gender', None)
        if gender is not None:
            queryset = queryset.filter(gender__name=gender)

        # Search by name
        search_query = self.request.query_params.get('search', None)
        if search_query is not None:
            queryset = queryset.filter(Q(name__icontains=search_query) | Q(description__icontains=search_query))

        # Order by price
        order_by = self.request.query_params.get('order_by', None)
        if order_by == 'price':
            queryset = queryset.order_by('price')
        elif order_by == 'price_desc':
            queryset = queryset.order_by('-price')

        return queryset


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

  