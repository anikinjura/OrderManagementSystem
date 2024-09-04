# backend/reference_books/pickup_points/api_views.py

from rest_framework import generics
from .models import PickupPoint
from .serializers import PickupPointSerializer

class PickupPointListAPIView(generics.ListCreateAPIView):
    queryset = PickupPoint.objects.all()
    serializer_class = PickupPointSerializer

class PickupPointDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PickupPoint.objects.all()
    serializer_class = PickupPointSerializer
