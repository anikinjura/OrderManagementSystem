# backend/reference_books/accounting_periods/api_urls.py

from django.urls import path
from . import api_views

app_name = 'api_accounting_periods'

urlpatterns = [
    path('', api_views.AccountingPeriodListAPIView.as_view(), name='list'),
    path('<int:pk>/', api_views.AccountingPeriodDetailAPIView.as_view(), name='detail'),
    path('create/', api_views.AccountingPeriodCreateAPIView.as_view(), name='create'),
    path('<int:pk>/update/', api_views.AccountingPeriodUpdateAPIView.as_view(), name='update'),
    path('<int:pk>/delete/', api_views.AccountingPeriodDeleteAPIView.as_view(), name='delete'),
]
