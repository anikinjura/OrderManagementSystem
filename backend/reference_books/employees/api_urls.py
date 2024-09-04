# backend/reference_books/employees/api_urls.py

from django.urls import path
from . import api_views

app_name = 'api_employees'

urlpatterns = [
    path('', api_views.EmployeeListAPIView.as_view(), name='list'),
    path('<int:pk>/', api_views.EmployeeDetailAPIView.as_view(), name='detail'),
    path('create/', api_views.EmployeeCreateAPIView.as_view(), name='create'),
    path('<int:pk>/update/', api_views.EmployeeUpdateAPIView.as_view(), name='update'),
    path('<int:pk>/delete/', api_views.EmployeeDeleteAPIView.as_view(), name='delete'),
]
