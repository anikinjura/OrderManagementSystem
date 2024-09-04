# backend/reference_books/accounting_periods/api_views.py

from rest_framework import generics
from .models import AccountingPeriod
from .serializers import AccountingPeriodSerializer

class AccountingPeriodListAPIView(generics.ListCreateAPIView):
    queryset = AccountingPeriod.objects.all()
    serializer_class = AccountingPeriodSerializer

class AccountingPeriodDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AccountingPeriod.objects.all()
    serializer_class = AccountingPeriodSerializer
