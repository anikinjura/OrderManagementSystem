# backend/reference_books/api_urls.py

from django.urls import path, include

app_name = 'api_reference_books'

urlpatterns = [
    path('agents/', include('reference_books.agents.api_urls', namespace='api_agents')),
    path('pickup_points/', include('reference_books.pickup_points.api_urls', namespace='api_pickup_points')),
    path('accounting_periods/', include('reference_books.accounting_periods.api_urls', namespace='api_accounting_periods')),
    path('employees/', include('reference_books.employees.api_urls', namespace='api_employees')),
]
