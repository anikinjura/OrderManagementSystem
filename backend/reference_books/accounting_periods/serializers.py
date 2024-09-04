# backend/reference_books/accounting_periods/serializers.py

from rest_framework import serializers
from .models import AccountingPeriod

class AccountingPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountingPeriod
        fields = '__all__'
