# backend/reference_books/urls.py

from django.urls import path, include

app_name = 'reference_books'

urlpatterns = [
    path('agents/', include('reference_books.agents.urls', namespace='agents')),
    path('pickup_points/', include('reference_books.pickup_points.urls', namespace='pickup_points')),
    path('accounting_periods/', include('reference_books.accounting_periods.urls', namespace='accounting_periods')),
    path('employees/', include('reference_books.employees.urls', namespace='employees')),
]
