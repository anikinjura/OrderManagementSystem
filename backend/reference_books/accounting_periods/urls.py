# backend/reference_books/accounting_periods/urls.py

from django.urls import path
from . import views

app_name = 'accounting_periods'

urlpatterns = [
    path('', views.AccountingPeriodListView.as_view(), name='list'),
    path('<int:pk>/', views.AccountingPeriodDetailView.as_view(), name='detail'),
    path('create/', views.AccountingPeriodCreateView.as_view(), name='create'),
    path('<int:pk>/update/', views.AccountingPeriodUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', views.AccountingPeriodDeleteView.as_view(), name='delete'),
]
