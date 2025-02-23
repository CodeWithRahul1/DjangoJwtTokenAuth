from rest_framework import generics, permissions
from django.core.cache import cache
from .models import Product
from .serializers import ProductSerializer
from django.core.cache import cache  
from rest_framework.response import Response
from rest_framework.status import HTTP_503_SERVICE_UNAVAILABLE
import pybreaker


# Create a circuit breaker instance
db_circuit_breaker = pybreaker.CircuitBreaker(fail_max=3, reset_timeout=10)

class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]

    @db_circuit_breaker
    def get_queryset(self):
        try:
            products = Product.objects.all()
            cache.set("cached_products", products, timeout=300)  # Cache data for 5 minutes
            return products
        except Exception as e:
            # If circuit breaker trips, return cached data
            cached_data = cache.get("cached_products")
            if cached_data:
                return cached_data
            return Response({"error": "Service unavailable"}, status=HTTP_503_SERVICE_UNAVAILABLE)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        instance = serializer.save()
        cache.delete("product_list")  # Clear cache after update
        return instance

    def perform_destroy(self, instance):
        instance.delete()
        cache.delete("product_list")  # Clear cache after deletion
